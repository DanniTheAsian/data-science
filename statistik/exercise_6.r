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


# Simpson's Rule Exercise:
simpson <- function(f, a, b, n) {
  if (n %% 2 == 1) {
    return("n must be even for Simpson's rule")
  }
  # Define operators:
  delta_x <- (b - a) / n          # Bin width for division of the area of integration
  x <- seq(a, b, by = delta_x)    # Create an array of function inputs
  y <- f(x)                       # Create an array of function outputs
  
  # Apply Simpson's Rule:
  S <- (y[1] + y[n + 1] +
          4 * sum(y[seq(2, n, by = 2)]) +
          2 * sum(y[seq(3, n - 1, by = 2)]))* delta_x / 3  # First and last value + seq of terms multiplied by 2 and 4 respectly.
  
  return(S)              # Multiply by a third of the bin width and return the value
}


# Trapezoidal Rule for comparison, another numerical approximation
trapezoid <- function(f, a, b, n) {
  h <- (b - a) / n                   # Bin width
  x <- seq(a, b, by = h)             # Sequence of function input
  y <- f(x)                          # Sequence of function output    
  T <- (y[1] + y[n + 1] + 2 * sum(y[2:n])) # Trapezoidal rule
  return(T * h / 2) 
}

# Test with sin(x) from 0 to pi
f <- sin
a <- 0
b <- pi
n <- 10   # must be even

simpson_result <- simpson(f, a, b, n)
trapezoid_result <- Trapezoid(f, a, b, n)
exact_result <- 2  # integral of sin(x) from 0 to pi is 2

cat("Simpson's Rule Result:", simpson_result, "\n")
cat("Trapezoidal Rule Result:", trapezoid_result, "\n")
cat("Exact Result:", exact_result, "\n")


# Sum of squares exercise
sum_dif <- function(n){
  sum_of_squares <- 0                       # Define a variable to work with
  for (i in 1:n){
    sum_of_squares <- sum_of_squares + i^2  # Add the square of all numbers from 1 ot n
  }
  square_of_sum <- ((n*(n+1))/2)^2          # Square the (Gauss closed form) sum of all numbers up to n
  print(square_of_sum)                      # Print values of the teo sums
  print(sum_of_squares)
  return(square_of_sum - sum_of_squares)    # Return the difference of the two sums.
}

sum_dif(100)


sum_num <- function(n){
  result <- 0                 # Define variable to work with
  if (n < 0){                                   
    return("Only positive values allowed!")  # Check for legal input
  }
  for (i in 1:n){                            # Loop through numbers up to n
    if (i %% 5 == 0){                        # Add if 5 is a factor
      result <- result + i
    }
    else if (i %% 3 == 0){                   # Add if 3 is a factor
      result <- result + i
    }
  }
  return(result)                             # Return result
}