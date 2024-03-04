def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("User")
print(greet())  #Hello, User!
