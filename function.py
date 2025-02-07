def greet():
    print("hi,good morning")
    print("hello buddy")

greet()


def add(a, b):
    sum = a + b 
    mul = a * b 
    div = a / b 
    subs = a - b
    print(sum, mul, div, subs)

add(5,5)
# different types to pass argument 
# def add(a=10, b=10):
# def mul(a, b=10):
# def sum(a, b):
def average(*number):
  print(type(number))
  sum = 0
  for i in number:
     sum = sum + i
  print(sum//len(number))

average(5,8,15)    

def average (*number):
    sum = 0
    for i in number:
       sum = sum + i 
    return sum/len(number)

c = average(5,12,14,10)
print(c)