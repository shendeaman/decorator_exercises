def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def floorDivide(x,y):
  return x//y

def decoratorFunc(func,x,y):
  return func(x,y)

op1 = decoratorFunc(floorDivide,10,3)
print(f"op1 : {op1}")
