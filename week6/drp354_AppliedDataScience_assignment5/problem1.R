##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 5                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

require(stargazer) 

######################################################################
## 1a:
######################################################################

set.seed(182647)  ## Set the random number seed to ensure same sequence
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
ro <- 0.5
y <- rep(0,1000)
y[1] = e[1]

#iteration
for(t in 2:1000) y[t] <- ro*y[t-1]+e[t]

x <- rep(0,1000)
x <- 1:1000 # index

#plot 
plot(x,
     y, 
     #pch=16, 
     type="l",
     main="y estimate over time", 
     col="darkblue", 
     ylab="y over time",
     xlab="index (1:1000)", 
     xlim=c(0,1000), ylim=c(-6,6))

model_linear <- lm(y[2:1000] ~ y[1:999])
summary(model_linear)
stargazer(model_linear, title="Linear regression results", type="text", ci.level=0.95, ci=TRUE)

######################################################################
## 1b:
######################################################################
set.seed(182647)  ## Set the random number seed to ensure same sequence
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
ro <- (-0.5)
y <- rep(0,1000)
y[1] = e[1]

#iteration
for(t in 2:1000) y[t] <- ro*y[t-1]+e[t]

x <- rep(0,1000)
x <- 1:1000 # index

#plot 
plot(x,
     y, 
     #pch=16, 
     type="l",
     main="y estimate over time", 
     col="darkblue", 
     ylab="y over time",
     xlab="index (1:1000)", 
     xlim=c(0,1000), ylim=c(-6,6))

model_linear <- lm(y[2:1000] ~ y[1:999])
summary(model_linear)
stargazer(model_linear, title="Linear regression results", type="text", ci.level=0.95, ci=TRUE)


######################################################################
## 1c:
######################################################################
set.seed(182647)  ## Set the random number seed to ensure same sequence
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
ro <- (1)
y <- rep(0,1000)
y[1] = e[1]

#iteration
for(t in 2:1000) y[t] <- ro*y[t-1]+e[t]

x <- rep(0,1000)
x <- 1:1000 # index

#plot 
plot(x,
     y, 
     #pch=16, 
     type="l",
     main="y estimate over time", 
     col="darkblue", 
     ylab="y over time",
     xlab="index (1:1000)")

model_linear <- lm(y[2:1000] ~ y[1:999])
summary(model_linear)
stargazer(model_linear, title="Linear regression results", type="text", ci.level=0.95, ci=TRUE)
