#  q08_top2_scores.py

def menu():
    print("(1) Insert scores")
    print("(2) Display highest two scores")


scorelist = {}

def insert():

    scorelist[int(input("Enter the score: "))]= input("Enter student's name: ")

def display():
    highest1 = 0
    highest2 = 0
    for key in scorelist.keys():
        if key >= highest1:
            highest1 = key
    name1 = scorelist[highest1]
    print(name1)
            
    for key in scorelist.keys():
        if highest1 > key >= highest2:
            highest2 = key
    name2 = scorelist[highest2]
    print(name2)
    
option = ""

while option != 0:
    menu()
    option = input("Enter option: ")
    if option == '1':
        insert()
    if option == '2':
        display()
        
