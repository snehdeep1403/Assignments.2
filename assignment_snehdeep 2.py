############ Assignment for Today ######################
# Create student class as module
# Define functions -- add student, read student, delete student -- store in JSON file
# create new class - school student , inherit student -- school name, get school details()
# create new class - colledge studet, inherit student - colledge name, stream, location, get colledge details, get strength(), get location()


# Importing student module because we have to use student class of the module


import Student as s  


t= s.Student()
t1=s.school_student()
t2=s.college_student()

while 1:  
    a = int(input("1.For operations\n2.For get school deatils\n3.For college deatils\n4.For School Strength\n"))
    if a == 1:
        b = int(input("1. For Add data\n 2. To retrieve data\n 3. or delete data\n"))
        if b == 1:
            t.add_data()
        elif b == 2:
            t.display()
        elif b == 3:
            t.delete_record()
        else:
            print("invalid option\n")
    elif a==2:
        s_id = int(input("Enter student id\n"))
        t1.get_school_details(s_id)
    elif a==3:
        n=str(input("Enter College name"))
        t2.get_college_details(n)
    elif opt ==4:
        t1.strength()
    
    else:
        print("Invalid Option\n")