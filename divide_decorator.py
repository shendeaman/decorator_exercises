def smartDivide(func):
  def inner(x,y):
    print("I'll be dividing {x} by {y}.")
    if y==0:
      return
    else:
      return func(x,y)
  return inner

def divide(x,y):
  return x/y
