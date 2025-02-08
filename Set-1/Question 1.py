#Write a menu based program to add, delete and display the record of hostel using list as stacks data structure in python. Record should contain the fields: Hostel number, Total Students and Total Rooms.

#Add Record
def add_record():
    hostel_number = int(input("Enter Hostel Number: "))
    total_students = int(input("Enter Total Students: "))
    total_rooms = int(input("Enter Total Rooms: "))
    record = [hostel_number, total_students, total_rooms]
    stack.append(record)
    print("Record Added Successfully")

#Delete Record
def delete_record():
    if len(stack) == 0:
        print("No Record Found")
    else:
        record = stack.pop()
        print("Record Deleted Successfully")
        
#Display Record
def display_record():
    if len(stack) == 0:
        print("No Record Found")
    else:
        for record in stack:
            print("Hostel Number: ", record[0])
            print("Total Students: ", record[1])
            print("Total Rooms: ", record[2])
            print()

stack = []
while True:
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Display Record")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        display_record()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
    print()
