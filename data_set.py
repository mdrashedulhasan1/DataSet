file = open('C:\\Users\DOLPHIN\Desktop\data_set.txt','r')
employee=[]
for data_set in file:
    # print(data_set)
    x=data_set.split()
    employee.append(x)
    # print(employee)
salary={}
job={}
for all_employee in employee:
    key=all_employee[0]
    value=all_employee[1]
    value2=all_employee[2]
    salary[key]=value
    job[key]=value2
x=input('Enter the employee name: ')
output_file= open('C:\\Users\DOLPHIN\Desktop\output_set.txt','w')
if x in salary:
    output_file.write("Salary for "+x+":"+salary[x]+'\n') 
    output_file.write("Job for "+x+":"+job[x]) 
else:
    print("Not Found")
