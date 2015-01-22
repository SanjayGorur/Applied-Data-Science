Y <- c(2,6,4,6,8,2,0,5,5,6)
X <- c(1,4,3,6,2,8,6,4,1,9)

  plot(X,Y,
       pch = 15,
       col = "darkblue",
       main = "X vs Y",
       xlab = "X",
       ylab = "Y")

plot(Y,X,
     pch = 15,
     col = "darkblue",
     main = "Y vs X",
     xlab = "Y",
     ylab = "X")


mean_Y = mean(Y, na.rm = FALSE)
mean_X = mean(X, na.rm = FALSE)
mean_Y
mean_X

var_Y = var(Y, na.rm = FALSE)
var_X = var(X, na.rm = FALSE)
var_Y
var_X

sd_Y = sd(Y, na.rm = FALSE)
sd_X = sd(X, na.rm = FALSE)
sd_Y
sd_X

cov_YX = cov(Y, X)
cov_YX

cor_YX = cor(Y, X)
cor_YX

lm.yr = lm(Y ~ X)  
summary(lm.yr)
plot(lm.yr)
abline(lm.yr)



rm(lm.yr)

rm(list=ls(all=TRUE))