## Use Quandl to obtain market data
library(Quandl)
library(neuralnet)

start_date <- "1980-01-01"
end_date <- "2014-10-09"
tbill.3 <- Quandl("FRED/DTB3", trim_start=start_date, trim_end=end_date)
tbill.6 <- Quandl("FRED/DTB6", trim_start=start_date, trim_end=end_date)
tbond.10 <- Quandl("FRED/DGS10", trim_start=start_date, trim_end=end_date)

## Plot the time series
plot(tbill.3, pch=16, col="darkblue", type="l", ylim=c(0,17), ylab="%")
plot(tbill.6, pch=16, col="darkblue", type="l", ylim=c(0,17), ylab="%")
plot(tbond.10, pch=16, col="darkblue", type="l", ylim=c(0,17), ylab="%")

data <- merge(tbill.3, tbill.6, by="Date")
data <- merge(data, tbond.10, by="Date")

rm(tbill.3, tbill.6, tbond.10)

names <- c("Date", "tbill.3", "tbill.6", "tbond.10")
colnames(data) <- names

m <- dim(data)[1] ## Measure the length of the file to split into separate training and actual datasets

## Randomly sample one-third of the dataset for training purposes
set.seed(10142014) ## Set the random number generator to ensure I get the same sample
val <- sample(1:m, size = round(m/3), replace = FALSE, prob = rep(1/m, m)) 
data.train <- data[val,] ## Assign training dataset
data.test <- data[-val,] ## Assign test dataset
tbond.10 <- data.test[, 4]  ## Cleave off 10 year from test data for prediction error calculation
tbills <- data.test[, 2:3]  ## Cleave off 3 and 6 months from test data to pass through neural net.

set.seed(1066)
ann.1 <- neuralnet(tbond.10~tbill.6 + tbill.3, data=data.train, 
                   threshold=0.5, lifesign="full", hidden=5, rep=1, linear.output=TRUE, stepmax=1000000,
                   err.fct="sse", act.fct="logistic")             
## Estimate the neural network with 5 hidden layers.  Minimize SSE with logistic activation function.

plot(ann.1, rep="best")

ann.results <- compute(ann.1, tbills) ## Run the 3 and 6 month test data through the ANN to get a prediction for the 10 year rate.

error <- (ann.results$net.result - tbond.10)*100  ## Calculate the prediction error in basis points.

plot(error, type="l", col="darkblue", ylim=c(-700,700), ylab="Error (Basis Points)")  

## Neural network estimation is slow.  It may be the algorithm or the machine on which the algorithm is running (or both).
## It would be interesting to run this on a "fast" machine.
## As for the results, in the early period of the sample, basically 1980's through the mid 1990's, 
## the ANN consistently underpredicts the long-term rate, ## and by a large amount.  See conclusions from class slides.