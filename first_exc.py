def outer(x):
  def innner(y):
    return x+y
  return inner

innerFunc = outer(5)
output = innerFunc(6)
print(f"output : {output}")
