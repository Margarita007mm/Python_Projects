pets={

    }
All={

    }
b=0
c=["a","u","o","i","e"]
while True:
    # Pytaty imya korystuvacha ta kilkist' tvarynok, далі зілежно від кількості ми питаємо інформацію про кожну тваринку
    name=input("Enter your name: ")
    ammount_of_pets=int(input("Enter the number of pets: "))
    a=[]
    for i in range(ammount_of_pets):
        name_pets=input("Enter your pet's name: ")
        a.append(name_pets)
        pets[name_pets]={

        }
        type_pets=input("Enter type of pet: ")
        age_pets=int(input("Enter your pet's age: "))
        pets[name_pets]["Type"]=type_pets
        pets[name_pets]["Age"]=age_pets
    # print(pets)
    All[name]={

    }
    All[name]["Ammount"]=ammount_of_pets
    All[name]["Pet's name"]=a
    print(All)
    choose=input("Would you like to add information about 1 more pet owner? ")
    b+=1
    if(choose.lower()=="no"):
        break

name_owner=list(All.keys())
name_pet=pets.keys()

with open("Pet_Owner_Manager\pets_info.txt","w") as file:
    for names in name_owner:
        file.write(f"{names} has {All[names]['Ammount']} pet")

        if(All[names]["Ammount"]>1):
            file.write("s, their names are ")
        else:
            file.write(", its name is ")
        
        file.write(", ".join(All[names]["Pet's name"])+"\n")

        for names_pet in All[names]["Pet's name"]:
            file.write(f"\t{names_pet} is ")
            if(pets[names_pet]["Type"][0] in c):
                file.write("an ")
            else:
                file.write("a ")
            if(names==name_owner[-1] and names_pet==All[names]["Pet's name"][-1]):
                file.write(f"{pets[names_pet]['Type']}, {pets[names_pet]['Age']} years old.")
            else:
                file.write(f"{pets[names_pet]['Type']}, {pets[names_pet]['Age']} years old.\n")