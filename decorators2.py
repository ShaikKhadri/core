us=0
username="luffy"
password="luffy@1234"
def login(username,password):
    global us
    if username=="luffy" and password=="luffy@1234":
        us=us+1
        print("login sucessfull")
        return True
    else:
        print("invalid username or password")
        return False
for i in range(3):
    user=input("enter the username")
    pwd=input("enter the password")
    if login(user,pwd):
        break
else:
    print("Account is locked")

# Decorators Questions create functions add(a, b), subtract(a, b) and multiply(a, b).
# Create a function calculate(operation, a, b) that accepts a function reference and performs the selected operation.
# Use lambda functions to perform:
# Square of a number
# Cube of a number
# Double of a number Add a decorator log_operation that prints "Operation started" before execution and "Operation completed" after execution.

def log_operation(func):
    def wrapper(*args):
        print("Operation started")
        res=func(*args)
        print("Operation completed")
        return res
    return wrapper
@log_operation
def add(a,b):
    return a+b
@log_operation
def sub(a,b):
    return a-b
@log_operation
def mul(a,b):
    return a*b

def calculate(op,a,b):
    return op(a,b)

square=lambda x:x**2
cube=lambda x:x**3
double=lambda x:x*2

print("Addition:",calculate(add,10,5))
print("Subtraction:",calculate(sub,10,5))
print("Multiplication:",calculate(mul,5,10))

print("square:",square(2))
print("cube:",cube(3))
print("double:",double(5))

