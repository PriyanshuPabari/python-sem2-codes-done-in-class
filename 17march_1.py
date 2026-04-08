search_name = "aarav"
with open("student_records.txt","r") as f1:
    print(type(f1))
    found=False
    for i in f1:
        if search_name in i:
            print(search_name)
            found=True
    if not found:
                print("not found")