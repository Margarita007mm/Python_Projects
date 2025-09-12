from datetime import datetime
import json
now = datetime.now()
class Vault:
    def __init__(self):
        None


    def encrypt(self,txt,key:int):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_ua = 'абвгґдеєжзийіїйклмнопрстуфхцчшщьюя'
        encrypt_txt = ""

        # Encrypt english
        for char in txt.lower():
            if(char in alphabet):
                index = alphabet.index(char)
                new_index = (index + key) % len(alphabet)
                encrypt_txt += alphabet[new_index]
            elif(char in alphabet_ua):
                index = alphabet_ua.index(char)
                new_index = (index + key) % len(alphabet_ua)
                encrypt_txt += alphabet_ua[new_index]
            else:
                encrypt_txt += char



        return encrypt_txt.capitalize()
    
    def decrypt(self,txt,key:int):
        return self.encrypt(txt,-key)


    def add(self,title,text,shift):
        note = {
            "title":title,
            "cipher":"ceasar",
            "shift":shift,
            "created":str(now),
            "content":self.encrypt(text,shift)
        }
        try:
            with open("Note.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            data = {}


        new_key = str(len(data) + 1)
        data[new_key] = note


        with open("Note.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=2,ensure_ascii=False)
            
             


    # title_date = [[title, date], [title_2, date_2], [title, date]]


    def list(self):
        title_date = []
        with open("Note.json", "r", encoding="utf-8") as file:
            dt = json.load(file)
            for key in dt.keys():
                d = dt[key]
                title_date.append([d["title"],d["created"]])

        return title_date



    def read(self,title,shift):
        text = ""
        with open("Note.json", "r", encoding="utf-8") as file:
            data_1 = json.load(file)
            for key in data_1.keys():
                d = data_1[key]
                if(d["title"]==title):
                    text=d["content"]
                    break
        return self.decrypt(text,shift)


    def search(self,substr):
        
        t = ""
        with open("Note.json", "r", encoding="utf-8") as file:
            data_2 = json.load(file)
            for key in data_2.keys():
                d_2 = data_2[key]
                if(substr==self.decrypt(d_2["content"],d_2["shift"])):
                    t = d_2["title"]
                    break
        if(not t==""):
            print(t)
        else:
            print("Sorry, we don't have this")
        

    def mn(self):
        while True:
            menu = input("Choose the function (add/list/read/search) or exit: ")
            if(menu=="add".lower()):

                print(self.add())
            elif(menu=="list".lower()):
                print(self.list())
            elif(menu=="read".lower()):

                print(self.read())
            elif(menu=="search".lower()):
                
                print(self.search())

abc = Vault()
abc.mn()


text_Iv = "In that pleasant district of merry England which is watered by the river Don, there extended in ancient times a large forest, covering the greater part of the beautiful hills and valleys between Sheffield and Doncaster. The remains of this extensive wood are still to be seen at the noble seats of Wentworth, of Warncliffe Park, and around Rotherham. Here haunted of yore the fabulous Dragon of Wantley; here were fought many of the most desperate battles during the Civil Wars of the Roses; and here also flourished in ancient times those bands of gallant outlaws whose deeds have been rendered so popular in English song."
abc.add("Ivanhoe",text_Iv,25)

text_Iv2 = "The passage was gloomy, narrow, and winding, so that they proceeded with caution; and the farther they advanced, the more the air became damp and oppressive. It seemed as if the whole ruin trembled with the gusts of wind that found their way through chinks in the dilapidated masonry."
abc.add("Ivanhoe_2", text_Iv2, 30)

text_Iv3 = "Він ішов повільно, споглядаючи довкола себе. Ліс був густий і темний, лише зрідка сонячні промені пробивалися крізь гілля. Чути було лише шелест листя та крик птахів, що зривалися у небо."
abc.add("Ivanhoe_UA", text_Iv3, 27) 

text_Iv4 = "The knight, clad in armor that bore many a token of former strife, raised his visor and looked upon the crowd with calm yet piercing eyes. A murmur ran through the assembly, for they recognized in him one long absent and thought to be lost."
abc.add("Ivanhoe_3", text_Iv4, 35)

text_Iv5 = "Стародавні хроніки розповідають про мужніх воїнів і забутих королів, чиї імена досі живуть у піснях народу. І хоч минуло багато віків, та пам'ять про них ніколи не згасне серед зелених пагорбів Англії."
abc.add("Ivanhoe_UA2", text_Iv5, 22)


print(abc.list())
print(abc.read("Ivanhoe_2",30))
abc.search("The as gloomy, narrow, and winding, so that they proceeded with caution; and the farther they advanced, the more the air became damp and oppressive. it seemed as if the whole ruin trembled with the gusts of wind that found their way through chinks in the dilapidated masonry.")