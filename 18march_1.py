try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    output=a/b
except ZeroDivisionError:
    print("Error Occured")
except ValueError:
    print("Invalid input")
finally:
    print("code executed successfully")