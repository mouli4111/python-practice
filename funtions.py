# def average(a=9, b=1):
    # print("The average is", (a+b)/2)
# 
# 
# average(4, 6)
# average(b=9)
# 
# average(b=9, a=21)

# def name(fname, mname, lname):
    # print("hello,", fname, mname, lname)
# 
# name("Amy", "Agarwal", "Jian")    
# 
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))

average(5, 6, 4, 1)
