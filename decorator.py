# def my_decorator(func):
#     def wrapper():
#         print("HELLO ")
#         func()
#         print("OREWA D LUFFY")
#     return wrapper
# @my_decorator
# def greet():
#     print("iam")
# greet()
from logging import exception


# Create a function place_order(item)
#     Write a decorator that prints:
#     * “Function started” before execution
#     * “Function ended” after execution

# def my_decorator(func):
#     def wrapper(item):
#         print("Before started")
#         func(item)
#         print("After started")
#     return wrapper
# @my_decorator
# def place_order(item):
#     print(f"order placed is {item}")
# place_order('laptop')
# Create a function greet(name) Write a decorator that adds:
# * “Welcome!” before
# * “Have a nice day!” after
# def my_decorator(func):
#     def wrapper(name):
#         print("Welcome!")
#         func(name)
#         print("Have a nice day!")
#     return wrapper
# @my_decorator
# def greet(name):
#     print(f"My Name is{name}")
# greet("KHADRI")
# Create a function transfer_money()
#     Write a decorator that prints:
#     * “Transaction started”
#     * “Transaction successful” / “Transaction failed”
# def transfer_decorator(func):
#     def wrapper():
#         print("Transaction started")
#     try:
#         func()
#         print("Transaction Successful")
#     except:
#         print("Transaction failed")
# @transfer_decorator
# def transfer_money():
#     print("Money transferred")
#     raise Exception("Insufficent balance")
# Create a function start_system() Write a decorator that prints: * “System starting…” before execution * “System started successfully” after execution
# def system_decorator(func):
#     def wrapper():
#         print("Systen Starting....")
#         func()
#         print("System Started Successfully")
#     return wrapper
# @system_decorator
# def start_system():
#     print("System is  running")
# start_system()
# Create a function get_message() that returns "hello user". Write a decorator using @ syntax that converts the output to uppercase.
# def upper_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# @upper_decorator
# def upper():
#     return ("hello khadri")
# print(upper())
# # Create a function get_number() that returns 10 Use a decorator to return double the value.
# def number_decorator(func):
#     def wrapper():
#         return func() * 2
#     return wrapper
# @number_decorator
# def get_number():
#     return 10
# print(get_number())
# Create a function add(a, b) Use a decorator to print:
#     * “Calculating sum…”
#     * “Calculation done”
# def add_decorator(func):
#     def wrapper(a,b):
#         print("Caluculating Sum...")
#         result = func(a,b)
#         print("caluculating done")
#         return result
#     return wrapper
# @add_decorator
# def add(a,b):
#     return a + b
# print(add(5,5))

# def price_decorator(func):
#     def wrapper(price):
#         print("Apply discount")
#         result = func(price)
#         print("Discount applied")
#         return result
#     return wrapper
# @price_decorator
# def apply_discount(price):
#     return price * 0.90
# print(apply_discount(100))

def verif_user(func):
    def wrapper(*args,**kwargs):
        print("user verified")
        func(*args,**kwargs)
    return wrapper
def user_verified(func):
    def wrapper(*args,**kwargs):
        print("Transaction logged")
        func(*args,**kwargs)
    return wrapper
#they are 2 methods:
#1
# @verif_user
# @user_verified
# def check_balance():
#     print("balance displayed")
# check_balance()
#2
def check_balance():
    print("Balance displayed")
check_balance=user_verified(verif_user(check_balance))
check_balance()
