Student_Data = {"NAME":"",
                "AGE":None,
                "GENDER":"",
                "ADRESS":"",
                "EMAIL":"",
                "PHONE":"",
                "CLUB_MEMBER":""}
process = True
while process:
    CommandLine = input("> ").lower().strip()
    if CommandLine == "student -assign -name":
        Name_Student = input("Assign Name for Student: ")
        Student_Data["NAME"] = Name_Student
        print(Student_Data)
    elif CommandLine == "student -assign -age":
        Age_Student = int(input(f"Assign Age for {Student_Data['NAME']}: "))
        Student_Data["AGE"] = int(Age_Student)
        print(Student_Data)
    elif CommandLine == "student -assign -gender":
        Student_Gender = input(f"Assign gender for {Student_Data['NAME']}:").strip().lower()
        if Student_Gender != "male" and Student_Gender != "female":
            print(f"The Gender {Student_Gender} Doesnt Exist!")
        else:
            Student_Data["GENDER"] = Student_Gender
            print(Student_Data)
    elif CommandLine == "student -assign -adress":
        Student_Adress = input(f"Assign adress For {Student_Data['NAME']}: ")
        Student_Data["ADRESS"] = Student_Adress
        print(Student_Data)
    elif CommandLine == "student -assign -email":
        Student_Email = input(f"Assign Email for {Student_Data['NAME']}: ")
        if "@" not in Student_Email:
            print("Email invalid or non Existent!")
        else:
            Student_Data["EMAIL"] = Student_Email
            print(Student_Data)
    elif CommandLine == "student -assign -phone":
        Student_Phone = input(f"Assign {Student_Data['NAME']}'s Number:")
        Student_Data["PHONE"] = Student_Phone
        print(Student_Data)
    elif CommandLine == "student -assign -club member":
        Student_Club_Member = input(f"{Student_Data['NAME']} is a Club Member in: ")
        Student_Data["CLUB_MEMBER"] = Student_Club_Member
        print(Student_Data)
    elif CommandLine == "mode -clearall":
        Student_Data.clear()
        Warn = input("This wont Be recoverable! are you sure?: ")
        if Warn == "yes":
            Student_Data.clear()
            print("Data Deleted.")
        else:
            print("Deletion Cancelled.")