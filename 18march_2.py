age = int(input("Enter age: "))
if age<18:
    print("You are a minor.")
    raise NameError("Age must be 18 or above.")