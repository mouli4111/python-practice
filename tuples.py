tup = (1,)
print(type(tup))

tup = (2, 4, 2, 6, 7, 8, 9, "harry", "mouli")
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[3])
print(tup[2])

tup1 = (1, 2, 3, 4, 5, 6, 7)
tup2 = ("red", "blue", "green")
print(tup1)
print(tup2)

details = ('abhijeet', 18, 9.8, "eteyge")
print(details)

country = ('spain', 'italy', 'india', 'england', 'germany')
if 'germany' in country:
    print("germany is a country")
else:
    print("germany is not a country")  

animal = ("cat", "dog", "camel", "horse", "donkey", "cow", "bat", "pig", "goat")
print(animal[3:7])
print(animal[-7:-3])      

animal = ("cat", "dog", "camel", "horse", "donkey", "cow", "bat", "pig", "goat")
print(animal[::8])
print(animal[1:4:8])
print(animal[-1:-2:-9])

T=tuple(input("Enter vlaue"))
print(T) 

T =(40,50,60,80,100)
n=len(T)
for i in range(n):
    print(T[i])

T=(40,50,60,80,100)
print(min(T))
print(max(T))
print(T.index(80))

            
