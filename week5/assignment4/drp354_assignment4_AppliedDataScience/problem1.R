##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 4                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

######################################################################
## 1a:
######################################################################
A = matrix( 
     c(0.5, 0.5, 0, 
       0.25, 0.5, 0.25, 
       0, 0.5, 0.5),      # the data elements 
     nrow=3,              # number of rows 
     ncol=3,              # number of columns 
     byrow = TRUE)        # fill matrix by rows 

dimnames(A) = list( 
  c("A", "B","C"), # row names 
  c("A", "B","C")) # column names 


#Markov transition function
IterateTransition<-function(step,matrix){
  A_temp=matrix
  for (n in 1:step) {  ##  possible steps (2,5,10,20).
    A_temp=A_temp%*%matrix
    }
  return(A_temp)
}

#n-step
n_step <- c(2,5,10,25)
for (n in n_step) {  ##  possible steps (2,5,10,20).
  cat("\n\nMarkov transition matrix when step = ",n,"\n")
  #print(n)
  ResultMatrix=IterateTransition(n,A)
  print(ResultMatrix)
}

rm(ResultMatrix)
#rm(list = ls())

######################################################################
## 1b:
######################################################################
A = matrix( 
  c(1,0,0,
    0.25, 0.5, 0.25, 
    0,0,1), # the data elements 
  nrow=3,              # number of rows 
  ncol=3,              # number of columns 
  byrow = TRUE)        # fill matrix by rows 

dimnames(A) = list( 
  c("A", "B","C"), # row names 
  c("A", "B","C")) # column names 


#n-step
n_step <- c(2,5,10,25,1000,100000)
for (n in n_step) {  ##  possible steps (2,5,10,20).
  cat("\n\nMarkov transition matrix when step = ",n,"\n")
  #print(n)
  ResultMatrix=IterateTransition(n,A)
  print(ResultMatrix)
}

rm(ResultMatrix)
#rm(list = ls())

######################################################################
## 1c:
######################################################################
A = matrix( 
  c(1,0,0,0,0,
    0.25,0.5,0.25,0,0,
    0,0.25,0.5,0.25,0,
    0,0,0.25,0.5,0.25,
    0,0,0,0.5,0.5
    ),                 # the data elements 
  nrow=5,              # number of rows 
  ncol=5,              # number of columns 
  byrow = TRUE)        # fill matrix by rows 

dimnames(A) = list( 
  c("A", "B","C","D","E"), # row names 
  c("A", "B","C","D","E")) # column names 


#n-step
n_step <- c(2,5,10,25,1000,10000000)
for (n in n_step) {  ##  possible steps (2,5,10,20).
  cat("\n\nMarkov transition matrix when step = ",n,"\n")
  ResultMatrix=IterateTransition(n,A)
  print(ResultMatrix)
}

rm(ResultMatrix)
#rm(list = ls())


