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