# Find shortest line
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

lines = data.split('\n')
shortest_line = lines[0]
for line in lines:
    if len(line) < len(shortest_line):
        shortest_line = line

print(f"Shortest line in the file: {shortest_line}")
