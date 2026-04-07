a = 10
b = 20
c = a + b

print("The sum of a and b is:", c)
def greet(name):
    return f"Hello, {name}!"        
name = "Alice"
greeting = greet(name)      
print(greeting)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    


number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)