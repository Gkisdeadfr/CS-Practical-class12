"""
Write a menu driven program to perform read and write operations using a text file called "student.txt" containing School Roll number, Name, Address using three separate functions as given below:
1)Student_record(filename) - Entering Student data
2)Student _readdata(filename) - Displaying Student data
3)Student_search(filename) - Searching Student data
"""

def Student_record(filename):
    with open(filename, 'a') as file:
        roll_number = input("Enter School Roll Number: ")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        file.write(f"{roll_number},{name},{address}\n")
    print("Record added successfully.")

def Student_readdata(filename):
    try:
        with open(filename, 'r') as file:
            print("School Roll Number, Name, Address")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please add some records first.")

def Student_search(filename):
    roll_number = input("Enter School Roll Number to search: ")
    found = False
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith(roll_number + ','):
                    print("Record found: ", line.strip())
                    found = True
                    break
        if not found:
            print("Record not found.")
    except FileNotFoundError:
        print("File not found. Please add some records first.")

def menu():
    filename = "student.txt"
    while True:
        print("\nMenu:")
        print("1. Enter Student Data")
        print("2. Display Student Data")
        print("3. Search Student Data")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Student_record(filename)
        elif choice == '2':
            Student_readdata(filename)
        elif choice == '3':
            Student_search(filename)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

menu()
