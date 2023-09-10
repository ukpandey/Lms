class Library:
    def __init__(self, listOFBooks):
        self.books = listOFBooks

    def displayAvailableBooks(self):
        print("Books Present in the Library are: ")
        for i in self.books:
            print("\t*", i)
    def borrowBook(self,bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print("You have been issued ",bookName,". Please return this book within 30 days.")
            return True
        else:
            print("This book has already been issued!!!")
            return False
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Book has been returned!!")


class Student:
    listofStudents=[]
    def register(self,index,Name,Password):
        self.name=Name
        self.passWord=Password
        self.index=index
        l=[self.index,self.name,self.passWord]
        self.listofStudents.append(l)
        
    def checkUser(self,Name,Password,id):
        temp=[]
        for item in self.listofStudents:
            temp.append(item)
            # print(temp[0][1],temp[0][2])
            if temp[0][1]==Name and temp[0][2]==Password and temp[0][0]==id:
                return True
            else:
                temp.clear()
        return False

def menu():
    print("*********************************************************************************************")
    print("\t\t\t\t\tMENU")
    print("*********************************************************************************************")
    print("1.View Available Books")
    print("*********************************************************************************************")
    print("2.Borrow a Book")
    print("*********************************************************************************************")
    print("3.Return a Book")
    print("*********************************************************************************************")
    print("4.View Account")
    print("*********************************************************************************************")
    print("5.Exit")
    print("*********************************************************************************************")

centralLibrary = Library(
["Berserk", "One Piece", "Bleach", "Naruto", "Jujutsu Kaisen", "Vagabond", "Demon Slayer", "Attack on titan","Dr. Stone","Solo Leveling"])
# centralLibrary.displayAvailableBooks()
s=Student()
id=0
notFound=True
# s.register(0,"Ujjwal","ABC")
# # print(s.listofStudents)
# s.register(1,"Ujjwal","ABC")
# s.register(2,"jjwal","ABC")
# s.register(3,"jwal","ABC")
# s.register(4,"wal","ABC")
# print(s.listofStudents)
# print(len(s.listofStudents))

while True:
        print("Are You a Registered User (y/n)?")
        check=input()
        if check=='y':
            print("Enter id: ",end="")
            global tempId
            tempId=int(input())
            print("Enter Name: ",end="")
            name=input()
            print("Enter Password: ",end="")
            pwd=input()
            if s.checkUser(name,pwd,tempId):
                menu()
            else:
                print("User not found")
                notFound=False
        else:
            print("User not found!!!\n Do you want to register (y/n)?")
            check=input()
            if check=='y':
                print("Enter Name: ",end="")
                name=input()
                print("Enter Password: ",end="")
                pwd=input()
                print("You have been given an unique id ",id)
                s.register(id,name,pwd)
                tempId=id
                id+=1
                print(name," registered successfully")
                menu()
            else:
                break
        print("Do you want to continue (y/n)?")
        c=input()
        if c=='y' and notFound==True:
            while True: 
                print("Enter your choice from the menu: ")
                yourChoice=int(input())
                if yourChoice==1:
                    centralLibrary.displayAvailableBooks()
                elif yourChoice==2:
                    if len(s.listofStudents[tempId])<5:
                        print("Select the book: ",end="")
                        bName=input()
                        if centralLibrary.borrowBook(bName):
                            s.listofStudents[tempId].append(bName)
                    else:
                        print("You already have two books. You cannot issue another book")
                elif yourChoice==3:
                    print("Enter the book you want to return")
                    bname=input()
                    if bname in s.listofStudents[tempId]:
                        centralLibrary.returnBook(bname)
                        s.listofStudents[tempId].remove(bname)
                    else:
                        print("Book Not Found!!!")
                elif yourChoice==4:
                    print(s.listofStudents[tempId])
                elif yourChoice==5:
                    break
                else:
                    print("Please Enter valid option!!!")
        else:
            break
                        


# this is my library management system using oops


            
# menu()