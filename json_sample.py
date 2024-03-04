import json
import os

employee_data = {'count':0,"employee_list":[]}

def add_data () :
    name = input("Enter your name here: ")
    age = int(input("Enter your age here: "))
    employee_data["count"] +=1
    employee_data["employee_list"].append({'name':name,'age':age})
    
    with open ('employee.json','w') as file :
        json.dump(employee_data,file,indent=4)
        
    print("added successfully")    
        
    
    
def get_data () :
    global employee_data
    search_input = input("Enter the name to search: ")
    if os.path.exists('employee.json') :
        with open ('employee.json','r') as file :
            employee_data = json.load(file)
        for employee in employee_data ["employee_list"]:
            if employee['name'] == search_input :
                for key,value in employee.items() :
                    print(f" {key} {value}")
                
            
        

def main ():
    while True :
        inputs = int(input("Enter your choice: "))
        
        if inputs == 1 :
            add_data()
            
        
        elif inputs == 2 :
            get_data()
            
        elif inputs == 3 :
            break      

        else :
            None 
            
            
if __name__ == '__main__' :
     main ()         