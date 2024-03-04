import json
import os

employee_data = {'count': 0, 'employee_list': []}

def clear():
    os.system("clear")

def save_file():
    with open('employee_data.json', 'w') as file:
        json.dump(employee_data, file, indent=4)

def load_file():
    global employee_data
    if os.path.exists('employee_data.json'):
        with open('employee_data.json', 'r+') as file:
            employee_data = json.load(file)
            print(f"Data fetched from 'employee_data.json'")

def add_employee():
    global employee_data
    i_d = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    phone_number = input("Enter Employee Phone Number: ")
    experience = int(input("Enter Employee Experience: "))
    grade = input("Enter Employee Grade: ")

    employee_data["count"] += 1
    employee_data['employee_list'].append({'ID': i_d, 'Name': name, 'Age': age, 'Phone Number': phone_number, 'Experience': experience, 'Grade': grade})
    
    save_file()
    clear()
    print(f"Employee {name} With ID Number {i_d} Added Successfully")

def get_employee():
    global employee_data
    search_input = input("Enter Employee ID To See The Data: ")
    if os.path.exists('employee_data.json'):
        with open('employee_data.json', 'r') as file:
            try:
                employee_data = json.load(file)
            except json.JSONDecodeError:
                print("Error decoding JSON data")
                return

            found = False
            for employee in employee_data['employee_list']:
                if employee['ID'] == int(search_input):
                    clear()
                    print(f"Employee Data With ID Number {search_input} Fetched Successfully")
                    for key, value in employee.items():
                        print(f"{key}: {value}")
                    found = True
                    break

            if not found:
                print(f"Employee with ID {search_input} not found.")
    else:
        print("File does not exist.")

def update_employee():
    global employee_data
    clear()
    id_no = int(input('Enter the ID to update: '))
    for employee in employee_data['employee_list']:
        if employee['ID'] == id_no:
            new_name = input('Enter new name: ')
            new_age = int(input('Enter new age: '))
            new_number = input('Enter new number: ')
            new_experience = int(input('Enter new experience: '))
            new_grade = input('Enter new grade: ')

            employee['Name'] = new_name
            employee['Age'] = new_age
            employee['Phone Number'] = new_number
            employee['Experience'] = new_experience
            employee['Grade'] = new_grade

            save_file()
            print(f'Employee with ID Number {id_no} data updated successfully.')
            break
    else:
        print(f"Employee with ID Number {id_no} not found.")

def delete_employee():
    global employee_data
    clear()
    id_no = int(input('Enter the ID to remove: '))
    for employee in employee_data['employee_list']:
        if employee['ID'] == id_no:
            employee_data['employee_list'].remove(employee)
            employee_data['count'] -= 1
            save_file()
            print(f"Employee with ID Number {id_no} deleted successfully.")
            break
    else:
        print(f"Employee with ID Number {id_no} not found.")

def display_employee_data():
    global employee_data
    print("\nEmployee Data:\n")
    for employee in employee_data['employee_list']:
        print(f"Employee ID: {employee['ID']}")
        for key, value in employee.items():
            if key != 'ID':
                print(f"{key}: {value}")
        print("\n")

def main():
    clear()
    load_file()
    while True:
        print("\n___Employee Management System___\n")
        print("1. Add Employee")
        print("2. Get Employee Data")
        print("3. Update Employee Data")
        print("4. Delete Employee Data")
        print("5. Display Employee Data")
        print("6. Exit Management System")

        user_input = int(input("Select the option: "))

        if user_input == 1:
            add_employee()
        elif user_input == 2:
            get_employee()
        elif user_input == 3:
            update_employee()
        elif user_input == 4:
            delete_employee()
        elif user_input == 5:
            display_employee_data()
        elif user_input == 6:
            save_file()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
