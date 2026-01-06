import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(student, f, indent=4)

student = load_data()
def add_student():
        
        #basic details
        std = (input("Enter the class of a student :"))
        name = input("Enter full name :")
        roll_n = (input("Roll No.: "))
        if std in student and roll_n in student[std]:
            print("This Roll No. is already Exists.")
            return None
        ad_id = input("Admission ID :")
        gender = input("Gender :")
        dob = input("Date of birth(for ex.,01/01/2000) :")
        
        #contact details
        phone_no = input("Contact number of student/parents :")
        if not phone_no.isdigit() or len(phone_no) != 10:
            print("Enter Valid 10 digit Number")
            return
        adr = input("Enter Correspondance adress :")
        email = input("Enter email :")
        if not (email.endswith("@gmail.com") or email.endswith("@outlook.com") or email.endswith(".org")):
            print("Enter Valid Email") 
            return
        
        #Academic details
        n = int(input("Enter no. of subjects :"))
        marks = []
        for _ in range(n):
            m_sub = int(input(f"Enter marks of sub{_} :"))
            if not 0 <= m_sub <= 100:
                print("Marks must be between 0 and 100")
                return
            marks.append(m_sub)
        total_m = 100*n
        per = round((sum(marks)/total_m) *100,2)
        if 90<= per <= 100 :
            grade = "Distinction"
        elif 80<= per < 90 :
            grade = "Grade A"
        elif 50<= per < 80 :
            grade = "Grade B"
        elif 35 <= per < 50 :
            grade = "Grade C"
        elif 0 <= per < 35 :
            grade = "Fail"
        else :
            print("Invalid Marks")
            return
        
        #Add all information in the students dictionary
        if std not in student:
             student[std] = {}

        student[std][roll_n] ={
                "Basic Details" : {
                    "Admission Id" : ad_id,
                    "Name" : name,
                    "Standard" : std,
                    "Date Of Birth" : dob,
                    "Gender" : gender
                },
                "Contact Details" : {
                    "Phone No.:" : phone_no,
                    "Address" : adr,
                    "Email Id" : email
                },
                "Academic Details" : {
                    "Marks" : marks,
                    "Percentage" : per,
                    "Grade" : grade
                }
            }
        
        save_data()
        print("Student Added Successfully!!")   
        print(student)

#to view or search the student 
def search_student():
        std = (input("Enter the class of the student :"))
        roll_no = (input("Enter student's roll number :"))
        if std in student and roll_no in student[std]:
             print(student[std][roll_no])
        else:
             print("Student not found")

def update_student():
     std = (input("Enter the class of the student :"))
     roll = (input("Enter Roll Number :"))
     if std in student and roll in student[std]:
        print("1.Name  2.Admission Id  3.Date Of Birth  4.Phone NO  5.Address  6.Email Id ")
        ch = int(input("What do you want to update:"))
        if ch == 1:
            student[std][roll]["Basic Details"]["Name"]=input("Enter new Name :")
        elif ch == 2:
            student[std][roll]["Basic Details"]["Admission Id"]=input("Enter Corre ted ID :")
        elif ch == 3:
            student[std][roll]["Basic Details"]["Date Of Birth"]=input("Enter new DOB :")
        elif ch == 4:
            student[std][roll]["Contact Details"]["Phone No.:"]=input("Enter a new phone number :")
        elif ch == 5:
            student[std][roll]["Contact Details"]["Address"]=input("Enter new Adress :")
        elif ch == 6:
            student[std][roll]["Contact Details"]["Email Id"]=input("Enter new email ID :")
        else:
            print("Please Enter A Valid Choice Code")
        save_data()
        print("Student Updated Successfully")
        print(student)
     else:
          print("Student Not Found")

def delete_student() :
     std = (input("Enter the class of the student :"))
     roll = (input("Enter Roll Number :"))
     if std in student and roll in student[std]:
        del student[std][roll]
        save_data()
        print("Student Deleted Successfully")
        print(student)
     else:
         print("Student Not Found")


while True:
    print("1.Add new student\n" \
        "2.Search Student\n"
        "3.Update student\n"
        "4.Delete Student\n"
        "5.Exit"
        )
    choice = int(input("What do you want to do??\n"))
    if choice == 1 :
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")

          



          












