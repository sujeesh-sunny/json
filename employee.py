import json
import os

employee_data = {'count':0,'emp_list':[]}

def clear():
    os.system('clear')

def save_file():
    with open('em.json','w+')as file:
        json.dump(employee_data,file,indent=4)
    print(f"added successfully")
    
def load_file():
    global employee_data
    if os.path.exists('em.json'):
        with open('em.json','r+')as file:
            employee_data = json.load(file)
            print(f"data fetched from {'em.json'}")

    
    

def add_employee():
    clear()
    id_no = int(input('enter ID No: '))
    name = input('Enter the name: ')
    age = int(input('enter age: '))
    number = int(input('enter number: '))
    experience = int(input('Enter experience: '))
    grade = input('enter grade: ')
    
    employee_data['count'] += 1
    employee_data['emp_list'].append({'id_no':id_no,'name':name,'age':age,'number':number,'experience':experience,'grade':grade})
    
    
    
def display_data():
    clear()
    for employ in employee_data['emp_list']:
        for key,values in employ.items():
            print(f"{key}:{values}")
            
        print('Fetched successfully')
        
def delete_data():
    clear()
    id_no = int(input('Enter the ID to remove: '))
    for i in employee_data['emp_list']:
        if i['id_no'] == id_no:
            employee_data['emp_list'].remove(i)
            employee_data['count'] -= 1
            print(f"{id_no} deleted")
            save_file()
            break
        else:
            print(f"{id_no} not found")
            
def update_data():
    clear()
    id_no = int(input('Enter the ID to update: '))
    new_name = input('Enter new name: ')
    new_age = int(input('Enter new age: '))
    new_number = int(input('Enter new number: '))
    new_experience = int(input('enter experience: '))
    new_grade = input('Enter new grade: ')
    for i in employee_data['emp_list']:
        if i['id_no'] == id_no:
            i['name'] = new_name
            i['age'] = new_age
            i['number'] = new_number
            i['experience'] = new_experience
            i['grade'] = new_grade
            print('Updated')
            save_file()
            break
        else:
            print(f"{id_no} not found")
    
            



    

def main():
    clear()
    load_file()
    while True:
        print('1.Add employ data')
        print('2.display data')
        print('3.delete')
        print('4.update')
        print('5.save')
        print('6.Quit')
        
        
        choice = int(input('enter the choice: '))
        if choice == 1:
            add_employee()
        elif choice == 2:
            display_data()
        elif choice == 3:
            delete_data()
        elif choice == 4:
            update_data()
        elif choice == 5:
             save_file()
        elif choice == 6:
            break
        else:
            None
if __name__ == "_main_":
    main()