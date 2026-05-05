Question = [ 
    {"q": "what is the capital of india", "options": ["A:Delhi", "B:Gujrat", "C:Lucknow", "D:mumbai"], "ans": "A"},

    {"q": "who is the prime minister of inida", "options": ["A:narendra modi", "B:draupati murmur", "C:govind sarani", "D:mouli srivastava"], "ans": "A"},
    {"q": "what is 2+2", "options": ["A:3", "B:2", "C:4", "D:6"], "ans": "4"},
    
    {"q": "which animal has hump", "options": ["A:elephant", "B:Camel", "C:rabbit", "D:COW"], "ans": "Camel"}]
for item in Question:
    print(item["q"])
    for opt in item["options"]:
        print(opt)
    user = input("Enter your answer:")
    
    if user == item["ans"]:
        print("7 CARORE!, SAHI JAWAB")
    else:
        print("TERI MAA KA BHOSDA FAAAHHHHHH!")
        break
         
