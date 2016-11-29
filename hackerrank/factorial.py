def factorial(n, index, max):
  if index == max:
    return n

  n = n * index
  index = index + 1
  return factorial(n, index, max)
    

print(factorial(1, 1, 5))
