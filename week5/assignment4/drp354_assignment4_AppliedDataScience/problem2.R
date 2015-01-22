##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 4                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
##############################################

require("foreign")
require("stargazer")
require("markovchain")


######################################################################
## 2a:
######################################################################
union <- read.dta("C:/Users/dimas_000/Dropbox/fall-2014-NYU/Applied-Data-Science/week5/assignment4/union_pred.dta")
union <- union[order(union$idcode, union$year),]
View(union)

#to make matrix indexing easier, change non-union to 1 and union to 2
for (n in 1:(nrow(union))) {
  union$prior_union[n] <- union$prior_union[n]+1
  union$union[n] <- union$union[n]+1
}

#probability matrix
p_union = matrix( 
  nrow=2,              # number of rows 
  ncol=2,              # number of columns
  0,
  byrow = TRUE)        # fill matrix by rows 
dimnames(p_union) = list( 
  c("0", "1"), # row names 
  c("0", "1")) # column names 

#calculate the summation table
for (n in 1:(nrow(union))) {
  p_union[union$prior_union[n], union$union[n]]<- p_union[union$prior_union[n], union$union[n]]+1
}
# summation table
cat("\n\nSummation table:\n")
print(p_union)

#calculate the probability
for (nn in 1:2) {
  p_union[nn, ] <- (p_union[nn, ] / sum(p_union[nn, ]))
}
# Average table
cat("\n\nAs percentage:\n")
print(p_union)

#create a two-by-two matrix of Markov transition probabilities based on these results
#using markov chain library
unionState <- c("0","1")
byRow <- TRUE
unionMatrix <- matrix(data = c(p_union[1,1],p_union[1,2],p_union[2,1],p_union[2,2]),
                      byrow = byRow, 
                      nrow = 2,
                      dimnames = list(unionState, unionState))
markovUnion <- new("markovchain", 
               states = unionState,  
               transitionMatrix = unionMatrix, 
               name = "Union")
print(markovUnion)
rm(union)

######################################################################
## 2b:
######################################################################
union<- read.dta("C:/Users/dimas_000/Dropbox/fall-2014-NYU/Applied-Data-Science/week5/assignment4/union_pred.dta")
union<- union[order(union$idcode, union$year),]
union.logit <- glm(union ~ age+grade+smsa+south+black+year+prior_union, data = union, family = "binomial")  
summary(union.logit)
stargazer(union.logit, title="Regression Results for logit", type="text")


######################################################################
## 2c:
######################################################################
union_pred <- union
#assigns null
for (n in 1:(nrow(union_pred))){
  union_pred$prior_union[n] <- 0
}
#assign the predicted values to union
union_pred$pred_01 <- predict(union.logit, newdata = union_pred, type = "response")  
union_pred$pred_00 <- 1-union_pred$pred_01
head(union_pred$pred_01)
head(union_pred$pred_00)

######################################################################
## 2d:
######################################################################
#assigns 1
for (n in 1:(nrow(union))){
  union_pred$prior_union[n] <- 1
}
#assign the predicted values to union
union_pred$pred_11 <- predict(union.logit, newdata = union_pred, type = "response")  
union_pred$pred_10 <- 1-union_pred$pred_11
head(union_pred$pred_11)
head(union_pred$pred_10)


######################################################################
## 2e:
######################################################################
#markov matrix transition probabilities
p_transition = matrix( 
  nrow=2,              # number of rows 
  ncol=2,              # number of columns
  0,                   # initial value
  byrow = TRUE)        # fill matrix by rows 
dimnames(p_transition) = list( 
  c("0", "1"), # row names 
  c("0", "1")) # column names 

#assign mean value of pred_00 ~ pred_11
p_transition[1,1] <- mean(union_pred$pred_00)
p_transition[1,2] <- mean(union_pred$pred_01)
p_transition[2,1] <- mean(union_pred$pred_10)
p_transition[2,2] <- mean(union_pred$pred_11)
print(p_transition)


######################################################################
## 2f:
######################################################################
#create a two-by-two matrix of Markov transition probabilities based on these results
#using markov chain library
unionState <- c("0","1")
byRow <- TRUE
unionMatrixTrans <- matrix(data = c(p_transition[1,1],p_transition[1,2],p_transition[2,1],p_transition[2,2]),
                           byrow = byRow, 
                           nrow = 2,
                           dimnames = list(unionState, unionState))
markovUnionTrans <- new("markovchain",
                        states = unionState,
                        transitionMatrix = unionMatrixTrans,
                        name = "Union-prediction")
print(markovUnionTrans)
initial <- matrix(data = c(1,0,0,1), 
                            nrow = 2,
                            dimnames = list(unionState, unionState))

#n-step
n_step <- c(2,5,10,25,100000)
for (n in n_step) {  ##  possible steps (2,5,10,20).
  cat("\n\nMarkov transition matrix when step = ",n,"\n")
  ResultMatrixPrediction = initial * (markovUnionTrans^n)
  print(ResultMatrixPrediction)
}

