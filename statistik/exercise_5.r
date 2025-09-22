#1

quadrant <- function(x, y) {
  if ( x > 0 & y > 0) {
    return ("quadrant I");
  }
  else if (x < 0 & y > 0) {
    return("quadrant II");
  }
  else if (x < 0 & y < 0) {
    return("quadrant III")
  }
  else if (x > 0 & y < 0) {
    return("quadrant IV")
  }
}

quadrant(3,5)

#2

bmi <- function(weight, height) {
  if (height > 10) {
    height <- height / 100
  }
  
  result <- weight / (height^2)
  
  category <- if (result < 18.5) {
    "underweight"
  } else if (result <= 24.9) {
    "healthy"
  } else if (result <= 29.9) {
    "overweight"
  } else if (result <= 34.9) {
    "obese"
  } else if (result <= 39.9) {
    "severely obese"
  } else {
    "morbidly obese"
  }
  
  message <- switch(category,
                    underweight = "Underweight",
                    healthy = "Healthy weight",
                    overweight = "Overweight",
                    obese = "Obese",
                    severely_obese  = "Severely obese",
                    morbidly_obese  = "Morbidly obese"
  )
  
  return(paste("Your result:", result, "-", message))
}


bmi(60, 1.70)

#3 - fakultet 

facto <- function(n) {
  if (n < 0){
    stop("Factorial er ikke for negative tal")
  }
  
  result <- 1
  for (i in 1:n){
    result <- result * i
  }
  return (result)
}

facto(5)
factorial(5)

#4 - summen

sum <- function(n){
  result <- 0
  for (i in 1:n){
    result <- result + i  
  }
  return (result)
}

sum(10)



