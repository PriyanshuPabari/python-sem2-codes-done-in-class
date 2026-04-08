def sum(*num):
    total = 0
    for i in num:
        total = total + i
    return total

def add(*num):
    total = sum(*num)
    print("The sum is", total)

add(1, 2, 3)
add(10, 20, 30, 40)
