##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 4                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3                                  #
##############################################

######################################################################
## 3a:
######################################################################
set.seed(1234567)  ## Set the random number seed to ensure the same draws.
x1 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
x2 <- rnorm(1000, mean=0, sd=(sqrt(2)))  
x3 <- rnorm(1000, mean=0, sd=2)

#plot X1
plot(1:(length(x1)),
     x1, 
     #pch=16, 
     type="l",
     main="Gaussian White noise N(0,1)", 
     col="darkblue", 
     ylab="1,000 draws from N(0,1)",
     xlab="index (0:1000)", 
     xlim=c(0,1000), ylim=c(-6,6))

#plot X2
plot(1:(length(x2)),
     x2, 
     #pch=16, 
     type="l",
     main="Gaussian White noise N(0,2)", 
     col="darkblue", 
     xlab="index (0:1000)", 
     ylab="1,000 draws from N(0,2)", 
     xlim=c(0,1000), ylim=c(-6,6))

#plot X3
plot(1:(length(x3)),
     x3, 
     #pch=16, 
     type="l",
     main="Gaussian White noise N(0,4)", 
     col="darkblue", 
     ylab="1,000 draws from N(0,4)",
     xlab="index (0:1000)", 
     xlim=c(0,1000), ylim=c(-6,6))


#histogram
hist(x1, 
     breaks=50, 
     col="darkblue", 
     main="Gaussian white noise of x1", 
     freq=F, 
     xlab="")

hist(x2, 
     breaks=50, 
     col="darkblue", 
     main="Gaussian white noise of x2", 
     freq=F, 
     xlab="")

hist(x3, 
     breaks=50, 
     col="darkblue", 
     main="Gaussian white noise of x3", 
     freq=F, 
     xlab="")

######################################################################
## 3b:
######################################################################
X1 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
X2 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
linear.model <- lm(X2 ~ X1)
beta <- linear.model$coefficients[2]
summary(linear.model)

######################################################################
## 3c:
######################################################################

beta <- rep(0,1000)  ## Creates a real-valued vector of zeros of 1 by 1000
set.seed(9212014)

for(i in 1:1000) {
  X1 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  X2 <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  linear.model <- lm(X2 ~ X1)
  beta[i] <- linear.model$coefficients[2]
  }

hist(beta, 
     breaks=50, 
     col="darkblue", 
     main="Histogram of Slope Coefficients", 
     freq=F, 
     xlab="")  ## Histogram for distribution of betas

