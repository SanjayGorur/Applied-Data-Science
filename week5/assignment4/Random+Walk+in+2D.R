
## Random Walk in 2D

start <- 30  ## Set the starting value for the Cartesian plane to be used.  It is (-start, start) in 2D.
## If you increase this to, say, 100 you will get an image that looks like the diffusion of milk in coffee (for example)

plot(-start:start,-start:start, type="n", xlab="",ylab="", main="Druken Sailor on a Mountain Top (2D Random Walk)")
x <- y<- 0  ## Start the drunken sailor at point (0, 0)
points(0, 0, pch=16, col="purple")  ## Drop a purple dot at the origin.

for (i in 1:100000) {  ##  Allow the sailor to take 100,000 possible steps.
  xi <- sample(c(1,0,-1),1)  ## In each period, 1/3 chance of moving left, 1/3 chance of moving right, 1/3 chance of not moving left or right
  yi <- sample(c(1,0,-1),1)  ## Movement in y dimension, with same probabilities.
  lines(c(x,x+xi), c(y,y+yi), col="blue")  ## Follow his movement
  x <- x+xi  ## Update location in both dimensions
  y <- y+yi
  if (abs(x)>start | abs(y)>start) {  ## Check to see if he's fallen on the mountain top
    points(x, y, pch=16, col="red")  ## If so record location with a red dot
    break
  }
}
"Fell off the edge at point"  ## Print the location of his demise if he fell off the mountain top
print(x)
print(y)
"after step" 
print(i)