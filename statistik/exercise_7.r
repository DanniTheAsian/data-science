euler <- function(f, t0,y0, h, n, verbose = TRUE) {
  t <- numeric(n + 1);
  y <- numeric(n + 1)
  t[1] <- t0; y[1]<y0
  
  if(verbose) cat(sprintf("j  t_j        y_j\n0  %-9.5f %-9.5f\n", t[1], y[1]))
  
  for (j in 1:n) {
    m <- f(t0, y0)
    y1 <- y0 + h * m
    t1 <- t0 + h
    if (verbose) cat(sprintf("%-2d %-9.5f %-9.5f\n", j, t1, y1))
    t0 <- t1; 
    y0 <- y1
    
    t[j + 1] <- t0; y[j + 1] <- y0
  }
  data.frame(t = t, y = y)
}

f <- function(t, y) y              # dy/dt = y
sol <- euler(f, t0 = 0, y0 = 1, h = 0.1, n = 50, verbose = FALSE)

# Sand løsning
sol$y_true <- exp(sol$t)
sol$error  <- sol$y - sol$y_true

# Vis de første rækker
head(sol)

# Plot numerisk vs sand løsning
plot(sol$t, sol$y, type = "l", lwd = 2, xlab = "t", ylab = "y",
     main = "Euler vs. e^t (h = 0.1)")
lines(sol$t, sol$y_true, lty = 2)
legend("topleft", c("Euler", "Sand: e^t"), lty = c(1,2), lwd = c(2,1), bty = "n")

# Max absolut fejl
max(abs(sol$error))
