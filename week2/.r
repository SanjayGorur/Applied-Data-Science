X <- c(6,7,8,8,7)
Y <- c(3,7,2,7,7)

plot(Y ~ X,
     pch = 11,
     col = "darkblue",
     main = "X vs Y",
     xlab = "X",
     ylab = "Y")


rm(list=ls(all=TRUE))