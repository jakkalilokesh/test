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

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True