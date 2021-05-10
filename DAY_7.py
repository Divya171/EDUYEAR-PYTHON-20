#Day 7:

"""
Take the details of user: name, email
You are going to assign the user_id, courses

Show the menu:
  1. All courses
    - show all courses
    - user will pick one course
    - you add that course to user profile
  2. My courses
    - show enrolled courses
  3. Edit my profile 
    - take input for new name & new email 
    - update user dictionary
  0. Exit

"""
Data = []
courses = ['Python', 'Java', 'Compiler Design', 'React JS', 'Finearts', 'Machine learning', 'Ruby', 'Database managemnet systems', 'Swift programming', 'Flutter framework', 'Oracle SQL', 'Artificial Intelligence']

name = input('Enter your name')
email = input('Enter your email id')
user = {'user_id': 101,'name': name,'email': email,'courses': []}

#print(user)

print('List of courses')
for i in range(len(courses)):
  print('{}. {}'.format(i+1, courses[i]))

while True:
  print('choose your option')
  print('1. Edit my profile')
  print('2. exit')
  print('3. Add new course')
  
  option = eval(input())
  
  if option == 1:
    name = input('Enter your name')
    email = input('Enter your email id')
    user['name']=name
    user['email']=email
    print(user)
    Data.append(user)

  elif option == 2:
    break

  elif option == 3:

    choice = eval(input('pick a course of your choice or enter 0 to quit:'))

  if choice ==1:
    user["courses"].append("Python")
    #print(user)

  elif choice ==2:
    user["courses"].append("Java")

  elif choice ==3:
    user["courses"].append("Compiler Design")

  elif choice ==4:
    user["courses"].append("React JS")

  elif choice ==5:
    user["courses"].append("Finearts")

  elif choice ==6:
    user["courses"].append("Machine learning")

  elif choice ==7:
    user["courses"].append("Ruby")

  elif choice ==8:
    user["courses"].append("Database managemnet systems")

  elif choice ==9:
    user["courses"].append("Swift programming")

  elif choice == 10:
    user["courses"].append(" Flutter framework")
  
  elif choice == 11:
    user["courses"].append("Oracle SQL")
  
  elif choice == 12:
    user["courses"].append("Artificial Intelligence")
  elif choice == 0:
    break

  else:
    print("Invalid choice, try again")

print(user)
Data.append(user)  
print(Data)






