file = open("input.txt")
content = file.read()

current_floor, position = 0,0

#comment for git push

for char in content:
    position+=1
    if char == "(":
        current_floor+=1
    elif char == ")":
        current_floor-=1
    if current_floor == -1:
        break

print(position)
