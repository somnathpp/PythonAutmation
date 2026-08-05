import math
num=int(input('Enter a number for square root : '))
p=10    # global variable
def square_root(num):
    nun3=6    # local variable
    if num ==0  or num == 1:
        return num
    else:
        return math.sqrt(num)
print(f'Square root of given number { num } :',square_root(num))
def sum(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
def pow(num1,num2):
    return num1**num2
sums=lambda a,b: a+b
print(f'Sum of a ,b',sums(6,8))
# local variable ---- > inside the function body  global variable ------> outside the function body