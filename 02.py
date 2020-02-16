# Find the sum of the even numbers in the Fibonacci sequence
# considering the terms whose values are less than 4,000,000
prev = 1
prev2 = 0
fibo = 0
sum = 0

while fibo < 4000000:

  # Compute Fibonacci sequence`
  fibo = prev + prev2
  prev2 = prev
  prev = fibo

  # Sum even terms
  if fibo % 2 == 0:
    sum = sum + fibo

print("Sum is %d." % sum)
