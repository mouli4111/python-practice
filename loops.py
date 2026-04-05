product = {
    "TV" : 250000,
    "telephone" : 3000,
    "phone" : 4000
}
for item, price in product.items():
    if price > 500:
        print(item, ":", price)

# find all odd numbers from 1 to 50 using for loop
for i in range(1, 51, 1):
    print(i)

# PRINT TABLE OF 5 
for i in range(1, 11):
    print("5 x", i,"=", 5 * i)

# print the table of 7

for i in range( 1 ,10):
    print("6 x",  i, "=", 6 * i)

name = 'mouli'
for i in name:
    print(i)
if(i == "u"):
    print ("this is something special") 

color = ["red", 'yellow', 'green', 'blue']
for color in color:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k)        

for k in range(1, 8):
    print(k+1)

for k in range(1, 12, 2):
    print(k)    

for i in range(2, 45, 1):
    print(i + 4)
