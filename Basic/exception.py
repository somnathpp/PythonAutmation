# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print(f"Result: {result}")  # Runs only if no exception occurs
# finally:
#     print("Execution completed.")
#Catching Multiple Exceptions in One Block
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error occurred: {e}")
# else:
#     print(f"Result: {result}")
# finally:
#     print("Finally statement: ")
#  Raising Exceptions Manually

# def withdraw(amount):
#     if amount < 0:
#         raise ValueError("Amount cannot be negative.")
#     print(f"Withdrew {amount} successfully.")
# try:
#     withdraw(-500)
# except ValueError as e:
#     print(f"Exception: {e}")
# id input! Please enter a valid integer. :")
n1=int(input('Enter the Dividend  number n1  :'))
# n2=int(input('Enter the Diviser  number n2  : '))
try:
    n2='a'
    n3=n1/n2
    print('Division of n1/n2 & quotient :',n3)
# except Exception as e:
#     # print(e)
#     print('Division Error :', e)
except ZeroDivisionError as e:
    print(e)

except Exception as e:
    print(e)
    # print('division by zero')
