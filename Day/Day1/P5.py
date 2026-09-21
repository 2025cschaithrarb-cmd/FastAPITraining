#Concept of Decorators in Python feature that 
#lets u modify a function using @ symbol
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()