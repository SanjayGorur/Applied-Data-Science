##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 5                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
##############################################

require(stargazer) 

######################################################################
## 2a:
######################################################################

set.seed(182647)  ## Set the random number seed to ensure same sequence
ro <- (1)
#walk 1
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
walk1 <- rep(0,1000)
walk1[1] = e[1]
for(t in 2:1000) walk1[t] <- ro*walk1[t-1]+e[t]

#walk 2
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
ro <- (1)
walk2 <- rep(0,1000)
walk2[1] = e[1]
for(t in 2:1000) walk2[t] <- ro*walk2[t-1]+e[t]


#plot 
plot(walk1,
     walk2, 
     #pch=16, 
     type="l",
     main="Walk1 VS walk2", 
     col="darkblue", 
     ylab="walk2",
     xlab="walk1")

model_linear <- lm(walk2 ~ walk1)
summary(model_linear)
stargazer(model_linear, title="Linear regression results", type="text", ci.level=0.95, ci=TRUE)

######################################################################
## 2b:
######################################################################
set.seed(182647)  ## Set the random number seed to ensure same sequence
betas <- rep(0,1000)  ## Creates a real-valued vector of zeros of 1 by 1000
ro <- (1)

for(i in 1:1000) {
  #walk 1
  e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  walk1 <- rep(0,1000)
  walk1[1] = e[1]
  for(t in 2:1000) walk1[t] <- ro*walk1[t-1]+e[t]
  
  #walk 2
  e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  ro <- (1)
  walk2 <- rep(0,1000)
  walk2[1] = e[1]
  for(t in 2:1000) walk2[t] <- ro*walk2[t-1]+e[t]
  
  linear.model <- lm(walk2 ~ walk1)
  betas[i] <- linear.model$coefficients[2]
}

hist(betas, breaks=50, col="darkblue", main="Monte Carlo Simulation", freq=F, xlab="")  ## Histogram 
mean(betas)
sd(betas)