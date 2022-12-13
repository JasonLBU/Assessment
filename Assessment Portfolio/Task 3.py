import random

try:
    StudentFile = open("Student.txt", "r")
    FileLines = StudentFile.readlines()
    List_Email = []

    for i in range(len(FileLines)):
        FourDigit = random.randint(1000, 9999)
        ID = FileLines[i].split(" ")[0]
        Forename = (FileLines[i].split(" ")[1]).replace(",", "").lower()
        Surname = FileLines[i].split(", ", 2)[1]
        initials = '.'.join(word[0].lower() for word in Surname.split())
        Student_Email = initials + '.' + Forename + str(FourDigit) + "@poppleton.ac.uk"
        print(Student_Email)
        List_Email.append(Student_Email)

    with open("Email.txt", "w") as File:
        for Emails in List_Email:
            File.writelines(f"{ID} {Emails}\n")

except IOError:
    print("Could not read file.")