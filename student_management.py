# Program  for adding new record, searching and deleting in list in Python

studentList =[]
print("********  The  program for maintaing list of students ************")
print("1. Enter new student: ")
print("2. View student list: ")
print("3. Search  student: ")
print("4. Delete  student: ")


choice = True
addFlag = True
searchFlag = True

def viewstudent(studentList):
  
    addFlag = True
    while addFlag == True:
      if len(studentList) == 0:
       print("List is empty ")
       addFlag = False
      else:
       print("Student list as follows....")
       print(studentList)
       addFlag = False


def addstudent(studentList):
    addFlag = True
    while addFlag == True:
     name = input("Enter new student: ") 
     if name in studentList:
       print("Name already exist")
       addFlag = False
     else:studentList.append(name)
     print(studentList)
     print("Sorted List........")
     print(sorted(studentList))

     more = input('Do you want to enter more students :y/n  ')
     if more.lower() == 'y':
       print("ok")
       addFlag = True
     else:
       print("Go to next option.")  
       addFlag = False

def search(studentList):
  
    addFlag = True
    while addFlag == True:
      if len(studentList) == 0:
       print("Nothing to search")
       addFlag = False
      else:
        name = input("Enter student name to search : ")
        for i in range(len(studentList)):
         if name == studentList[i]:
          print("Student name in list: ",name) 
          break
         elif i == (len(studentList) - 1): 
          print("Name is not in list:",name)


      more = input('Do you want to search more students :y/n  ')
      if more.lower() == 'y':
       print("ok")
       addFlag = True
      else:
       print("Go to next option.")  
       addFlag = False

def delete(studentList):
  
    addFlag = True
    while addFlag == True:
     if len(studentList) == 0:
       print("Nothing to delete")
       addFlag = False
     else:
      name = input("Enter student name to delete : ") 
      studentList.remove(name)
      print("***student list",studentList)
      more = input('Do you want to delete more students :y/n  ')
      if more.lower() == 'y':
       print("ok")
       addFlag = True
      else:
       print("Go to next option.")  
       addFlag = False

while choice == True:

   option = int(input('Enter options:'))
   if option == 1: 
    addstudent(studentList)
    choice = True
 
   elif option == 2: 
    viewstudent(studentList)
    choice = True

   elif option == 3: 
    search(studentList)
    choice = True

   elif option == 4: 
   
    delete(studentList)
    choice = True

   elif option == option > 4 :
    print("Exit thank you!!")
    choice = False   




