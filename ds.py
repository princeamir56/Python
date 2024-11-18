#l = [(1,"Vide"),(2,"Vide"),(40,"Vide")]

l = []

for i  in range(40):  #  range(40) -> 0..39 or  range(1,41) -> 1..40
    l.append((i+1,"Vide"))
print(l)

#Question 1 : 
def add_spectator(nom):
    i = 0 
    while i<40 and l[i][1]!="Vide":
        i+=1
    if i==40: 
        print("Toutes les places sont reservées")
    else : 
        element = list(l[i])
        element.pop()
        element.append(nom)
        l[i] = tuple(element)

#Question 2 :
def print_list():
    for i in range(40):
        if l[i][1]=="Vide":
            print("La place numero ",l[i][0]," est libre") # 0 -> numero de place , 1 -> nom de personne
        else :
            print("numero place : ",l[i][0])
            print("nom spectateur :",l[i][1])

#Question 3 : 

def find_spectator(nom):
    i = 0
    while i<40 and l[i][1]!=nom:
        i+=1 
    if i==40:
        print(nom,"n'existe pas!")
    else :
        print(nom," il est dans la place numero ",l[i][0])

#Question 4:

def delete_spectator(nom): 
    i = 0
    while i<40 and l[i][1]!=nom:
        i+=1 
    if i==40:
        print(nom,"n'existe pas!")
    else :
        element = list(l[i])
        element.pop()
        element.append("Vide")
        l[i] = tuple(element)
#Question 5 : 

def menu():
    for i in range(10):
        nom = input("nom = ")
        add_spectator(nom)
    
    print_list()
    nom2 = input("donner un nom à trouver: ")
    find_spectator(nom2)
    nom3 = input("donner un nom à supprimer: ")    
    delete_spectator(nom3)
    print_list()

menu()

    



