library(neuralnet)

## XOR neural net in R
XOR <- c(0,1,1,0)
xor.data <- data.frame(expand.grid(c(0,1), c(0,1)), XOR)
xor.data ## this is what XOR looks like

set.seed(7491016)
print(net.xor <- neuralnet(XOR~Var1+Var2, xor.data, 
                           threshold=0.01, lifesign="full", hidden=1, rep=1, algorithm="backprop", learningrate=2,
                           err.fct="sse", act.fct="logistic", linear.output=FALSE))
## Fit a model with one hidden neuron and backpropagation.  Minimize SSE with logistic activation function.

prediction(net.xor)
plot(net.xor, rep="best")

print(net.xor <- neuralnet(XOR~Var1+Var2, xor.data, 
                           threshold=0.01, lifesign="full", hidden=5, rep=10, algorithm="backprop", learningrate=2,
                           err.fct="sse", act.fct="logistic", linear.output=FALSE))
## Increase to five hidden neurons with 10 different random starts.  

prediction(net.xor)
plot(net.xor, rep="best")


## AND / OR neural net in R

AND <- c(rep(0,7),1)
OR <- c(0,rep(1,7))
binary.data <- data.frame(expand.grid(c(0,1), c(0,1), c(0,1)), AND, OR)
binary.data  ## This is what AND OR looks like.  AND is value 1 when all inputs are 1.  OR is value 1 when at least one input is value 1.

set.seed(2562562)
print(net <- neuralnet(AND+OR~Var1+Var2+Var3, binary.data,  
                       threshold=0.01, lifesign="full", hidden=1, rep=1, algorithm="backprop", learningrate=2,
                       err.fct="sse", act.fct="logistic", linear.output=FALSE))
## Fit a model with one hidden neuron and backpropagation.  Minimize SSE with logistic activation function.

prediction(net)
plot(net, rep="best")

print(net <- neuralnet(AND+OR~Var1+Var2+Var3, binary.data,  
                       threshold=0.01, lifesign="full", hidden=5, rep=10, algorithm="backprop", learningrate=2,
                       err.fct="sse", act.fct="logistic", linear.output=FALSE))
## Increase to five hidden neurons with 10 different random starts.  

prediction(net)
plot(net, rep="best")