## 1.
## a.
list <- c(.5,.5,0,.25,.5,.25,0,.5,.5)  ## The elements of the Markov transition matrix
TP <- matrix(list, 3, 3, byrow=T)  ## invoke R's matrix and make sure it is done by row rather than by column
TP  ## Confirm matrix

TP2 <- TP %*% TP ## Two-step ahead is just the square using proper matrix multiplication
TP2

TP5 <- TP2 %*% TP2 %*% TP ## Five-step ahead
TP5

TP10 <- TP5 %*% TP5 ## 10-step ahead
TP10

TP25 <- TP10 %*% TP10 %*% TP5 ## 25-step ahead
TP25 ## This is effectively the limiting distribution.

## b.
list <- c(1,0,0,.25,.5,.25,0,0,1)  ## The elements of the Markov transition matrix
TP <- matrix(list, 3, 3, byrow=T)  ## invoke R's matrix and make sure it is done by row rather than by column
TP  ## Confirm matrix

TP2 <- TP %*% TP ## Two-step ahead is just the square using proper matrix multiplication
TP2

TP5 <- TP2 %*% TP2 %*% TP ## Five-step ahead
TP5

TP10 <- TP5 %*% TP5 ## 10-step ahead
TP10

TP25 <- TP10 %*% TP10 %*% TP5 ## 25-step ahead
TP25 ## In the limit, the rat winds up in Room A half the time and Room C half the time, which makes sense.

## c.
## Problem is straightforward by combining a. and b.
listA <- c(1,0,0,0,0) ## The elements of the Markov transition matrix for Room A
listB <- c(.25,.5,.25,0,0) ## The elements of the Markov transition matrix for Room B
listC <- c(0,.25,.5,.25,0) ## The elements of the Markov transition matrix for Room C
listD <- c(0,0,.25,.5,.25) ## The elements of the Markov transition matrix for Room D
listE <- c(0,0,0,.5,.5)  ## The elements of the Markov transition matrix for Room E
TP <- matrix(listA, 1, 5, byrow=T)
TP <- rbind(TP, listB)
TP <- rbind(TP, listC)
TP <- rbind(TP, listD)
TP <- rbind(TP, listE)
TP <- matrix(TP, 5, 5)  ## Bind everything together and ensure it's a matrix.
TP

TP2 <- TP %*% TP ## Two-step ahead is just the square using proper matrix multiplication
TP2

TP5 <- TP2 %*% TP2 %*% TP ## Five-step ahead
TP5

TP10 <- TP5 %*% TP5 ## 10-step ahead
TP10

TP25 <- TP10 %*% TP10 %*% TP5 ## 25-step ahead
TP25 ## Not enough iteration, so keep trying.

TP100 <- TP25 %*% TP25 %*% TP25 %*% TP25
TP100 ## Almost there.

TP200 <- TP100 %*% TP100
TP200 ## Almost there.

TP500 <- TP100 %*% TP100 %*% TP100 %*% TP100 %*% TP100
TP500 ## Close enough.  The results are clear.
## With one absorbing state and a positive probability that the rat enters the absorbing state from any room,
## it will ultimately be absorbed.  Therefore, start the rat in any room, and it will ultimately be absorbed
## in Room A.  Again this is a powerful result.  A system with a single absorbing state, in which there is
## a non-zero probability of entering, will ultimately absorb the rat in finite time regardless of where the
## rat commences its journey.  

## 2.
library(foreign)  ## Convenient library for reading in data stored in different formats
library(stargazer)  ## Convenient library to express regression results in R
library(car)  ## Convenient library for variable transformation in R

## a. 
union <- read.dta("E:\\Big Data\\GX 5004\\union_pred.dta")

table(union$prior_union, union$union)  ## This reproduces the table in class
100*prop.table(table(union$prior_union, union$union), 1)  ## Command in R to express table as row percentages

## b.
union.logit <- glm(union ~ age+grade+smsa+south+black+year+prior_union, data = union, family = "binomial")  
## R's logit command is invoked with generalized linear models
stargazer(union.logit, title="Logit Using Prior Union Status", type="text")

## c.
union$prior_union <- recode(union$prior_union, "1=0; 0=0")  ## Simulation as if prior union status was 0 for all.
union$pred.01 <- predict(union.logit, newdata = union, type = "response")  
## R's predict command, which predicts the likelihood of being in a union today as if prior union status 
## was always zero.  That is, this is the likelihood of transition into a union given not in a union.
union$pred.00 <- 1-union$pred.01
## Obviously, one minus the probability of a transition is equal to the probability of no transition.

## d.
union$prior_union <- recode(union$prior_union, "0=1; 1=1")  ## Simulation as if prior union status was 1 for all.
union$pred.11 <- predict(union.logit, newdata = union, type = "response")  
## R's predict command, which predicts the likelihood of being in a union today as if prior union status 
## was always one.  That is, this is the likelihood of remaining in a union .
union$pred.10 <- 1-union$pred.11
## Obviously, one minus the probability of no transition is equal to the probability of transition.

## e.
print(c(100*mean(union$pred.00), 100*mean(union$pred.01)), digits=4)
print(c(100*mean(union$pred.10), 100*mean(union$pred.11)), digits=4)

## f.
list <- c(mean(union$pred.00),mean(union$pred.01),mean(union$pred.10),mean(union$pred.11))  ## The elements of the Markov transition matrix
TP <- matrix(list, 2, 2, byrow=T)  ## invoke R's matrix and make sure it is done by row rather than by column
TP  ## Confirm matrix

TP2 <- TP %*% TP ## Two-step ahead is just the square using proper matrix multiplication
TP2

TP5 <- TP2 %*% TP2 %*% TP ## Five-step ahead
TP5

TP10 <- TP5 %*% TP5 ## 10-step ahead
TP10

TP25 <- TP10 %*% TP10 %*% TP5 ## 25-step ahead
TP25 ## Looks like convergence has been achieved.
TP25[1,]
## Simulation shows non-union rate among women of 78.3% and union rate of 21.7%.
## In truth, current unionization rates among women is approximately 11%, nearly 10 points lower than predicted.
## See http://www.bls.gov/news.release/union2.t01.htm
## Again, we have done what amounts to out-of-sample prediction.

## 3.
## a.  
set.seed(51093)  ## Set the random number seed to ensure same sequence
x <- rnorm(1000, mean=0, sd=1)
plot.ts(x, col="darkblue", ylim=c(-6,6))

x <- rnorm(1000, mean=0, sd=sqrt(2))
plot.ts(x, col="darkblue", ylim=c(-6,6))

x <- rnorm(1000, mean=0, sd=sqrt(4))
plot.ts(x, col="darkblue", ylim=c(-6,6))

## b.
set.seed(10203040)  ## Set the random number seed to ensure same sequence
x1 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
x2 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
summary(lm(x1 ~ x2))


## c.
set.seed(182647)  ## Set the random number seed to ensure same sequence
betas <- rep(0,1000)  ## Creates a real-valued vector of zeros of 1 by 1000

for(i in 1:1000) {
  x1 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  x2 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  linear.model <- lm(x1 ~ x2)
  betas[i] <- linear.model$coefficients[2]
}

hist(betas, breaks=50, col="darkblue", main="Monte Carlo Simulation", freq=F, xlab="")  ## Histogram 
mean(betas)
sd(betas)

