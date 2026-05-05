marks = [3, 5, 6, "mouli", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
print(marks[-3])
print(marks[len(marks)-3])

print(marks[5-3])
print(marks[2])

if 7 in marks:
    print("yes")
else:
    print("no")    

print(marks[:])
print(marks[1:4])
print(marks[1:4:2])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "goat", "cow", "doneky"]
print(animals[0:6])
print(animals[:7])
           
name = ["milo", "sarah", "bruno", "anastasia", "rosa"]
namesWith_o = [item for item in name if "o" in item]
print(namesWith_o)