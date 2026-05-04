print("Hello World")

name = "John"
name2 = "John"
num = 25
balance = 159.258
flag = True

print(id(name))
print(id(name2))

print(type(name))
print(type(num))
print(type(balance))
print(type(flag))

print("Using range")
for i in range(5):
    print(i)



print("Using for loop")
items = [1,2,3,4,5,6,7,8]
for item in items:
    print(item)
    

def greet(name="Guest", age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet()
greet("Alice", 30)
greet(25)