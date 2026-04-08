with open("marks.txt","r") as f1:
    total=0
    count=0
    for i in f1:
        total+=int(i)
        count+=1
    print("Average marks:",total/count)
with open("marks.txt","a") as f2:
    marks=int(input("Enter marks to add: "))
    f2.write(str(marks) + "\n")