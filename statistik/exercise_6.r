#1

collatz <- function(n) {
  steps <- 0
  sequence <- c(n) 
  while(n != 1) {
    if(n %% 2 == 0 ){
      n <- n / 2
    }
    else {
      n <- 3 * n + 1
    }
    sequence <- c(sequence, n)
    steps <- steps + 1
  }
  cat("Sequence", sequence, "\n")
  cat("Steps", steps, "\n")
  
  return(list(sequence = sequence, steps = steps))
}

collatz(523)

#2 Simpson

simpson <- function(f,a,b,n) {
  if (n %% 2 != 0) {
    deltaX <- (b-a)/n
  
  }
}