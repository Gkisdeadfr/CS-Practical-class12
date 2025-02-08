import csv
import os

"""
Write a menu driven program implementing user defined functions to perform different functions on CSV file "student" such as:
1) Write all records in one single file.
2) Display the contents of the CSV file.
"""
def write_records_to_file(filename, records):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)
    print(f"Records written to {filename}")

def display_csv_contents(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exist.")
        return

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    records = [
        ['Name', 'Age', 'Grade'],
        ['Alice', '14', '8'],
        ['Bob', '15', '9'],
        ['Charlie', '13', '7']
    ]
    filename = 'student.csv'

    while True:
        print("\nMenu:")
        print("1. Write all records to file")
        print("2. Display the contents of the CSV file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            write_records_to_file(filename, records)
        elif choice == '2':
            display_csv_contents(filename)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()
    
    
    
    
"""
def display_menu():
    print("Menu:")
    print("1. Display all records")
    print("2. Add a new record")
    print("3. Search for a record")
    print("4. Delete a record")
    print("5. Exit")

def display_records(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def add_record(filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")
        writer.writerow([name, age, grade])
        print("Record added successfully.")

def search_record(filename):
    search_name = input("Enter name to search: ")
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_name:
                print("Record found:", row)
                return
        print("Record not found.")

def delete_record(filename):
    temp_filename = 'temp.csv'
    delete_name = input("Enter name to delete: ")
    with open(filename, mode='r', newline='') as file, open(temp_filename, mode='w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)
        deleted = False
        for row in reader:
            if row[0] != delete_name:
                writer.writerow(row)
            else:
                deleted = True
        if deleted:
            print("Record deleted successfully.")
        else:
            print("Record not found.")
    os.replace(temp_filename, filename)

def main():
    filename = 'student.csv'
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            display_records(filename)
        elif choice == '2':
            add_record(filename)
        elif choice == '3':
            search_record(filename)
        elif choice == '4':
            delete_record(filename)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
"""