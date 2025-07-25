import json

all_student={

}

class Student:
    def __init__(self,name,classes,subject):
        self.name=name.capitalize()
        all_student[self.name]=self
        self.classes=classes
        self.subject=subject
        self.b=self.subject.split(",")
        self.c=[sub for sub in self.b]
        self.marks={}
        for i in self.c:
            self.marks[i]=[]

    def add_grade(self,i,grad):
        if (i not in self.marks):
            self.marks[i]=[grad]
        else:
            self.marks[i].append(grad)
    
    def show(self):
        self.all=0
        self.size=0
        for v in self.marks.values():
            self.all+=sum(v)
            self.size+=len(v)
        if(self.size==0):
            return f'Name: {self.name}, Class: {self.classes}, All Subjects: {",".join(self.marks.keys())}, All Marks: N/A, GPA: N/A'
        else:
            return f'Name:{self.name}, Class:{self.classes}, All Subjects:{",".join(self.marks.keys())}, All Marks:{self.marks}, GPA:{self.all/self.size}'
    def save_file(self):
        with open ("Students.txt","a") as file:
            file.write(self.name+"\n")
            for k,v in self.marks.items():
                gr=[str(b) for b in v]
                file.write(f'\t{k}:{",".join(gr)}\n')

    def save_json(self):
        a={
            self.name:{
                "class":self.classes,
                "marks":self.marks
            }
        }
        with open (f"students/{self.name}.json","w") as files:
            json.dump(a,files,indent=4)
            files.write("\n")
                
        
student_1=Student("JJ","9","math,biology,chemistry")
student_2=Student("Kiara","8","history,PE,art")

# student_1.add_grade("PE",11)
# print(student_2.show())
# student_2.save_file()
# student_1.save_json()
# print(student_1.show())
# student_2.save_json()


while True:
    name=input("Enter name an existing student (or 'exit'): ").capitalize()
    if(name.lower()=="exit"):
        print("Goodbye!")
        break
    elif(name not in all_student):
        print("This student is not in our school")
    else:
        while True:
            st=all_student[name]
            choose=input("Select operation:\n1-Add a grade to the student \n2-Show information about all students \n3-Save data in file (TXT) \n4-Save from JSON \n5-Exit\n\t")
            if(choose=="1"):
                sub=input("What subject in the mark for? ")
                mark=int(input("What grade? "))
                st.add_grade(sub,mark)
            elif(choose=="2"):
                print(st.show())
            elif(choose=="3"):
                st.save_file()
            elif(choose=="4"):
                st.save_json()
            elif(choose=="5"):
                print("Bye")
                break
            