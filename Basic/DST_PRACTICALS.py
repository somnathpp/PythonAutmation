# Write a Python program to print all even numbers between 1 to 100 using while loop.
# n=int(input('Enter number for factorial'))
# orig=n
# fact=1
# while n>=1:
#     fact=fact*n
#     n=n-1
# print(f"Factorial of number {orig} is :",fact)
#fibonaci series
a=0
b=1
n=int(input('Enter a number: '))
while a<n:
    print(a,end=" ")
    a,b=b,a+b
