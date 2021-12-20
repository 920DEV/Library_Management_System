# COLLEGE LIBRARY.

class Library:
    def __init__(self, list_of_books):  # taking constructor
        self.Books=list_of_books        # here we create an instance attribute
    # Displaying the books Library have.
    def display_books(self):
        print("Books Present in the Library are: ")
        for index,book_list in enumerate(self.Books):        # by using the enumerate function we can display the serial no of the books
            print(f"{index+1})",book_list)

     # showing  the name of hte book we borrow, and if the book is not showing it will show else and return false.       

    def borrow(self, Book_name):
        if Book_name in self.Books:
            print(f"The Name of the book issued to you is '{Book_name}'. Return it before 30 days. Otherwise extra fine will be charged,")
            self.Books.remove(Book_name)
            return True
        else:
            print("Sorry this Book is already issued to someone else. Please Take any other Book or wait till the book is returned.") 
            return False

    # When the book is returned.
    def Return_Book(self,Book_name):
        self.Books.append(Book_name)
        
        print(f"Thanks for returning this book '{Name}'. ")

# A student can request the book he wants from the library.
# and student also wants to return the book to the library.
class Student:
    def requestBook(self):
        self.book=input(f"Enter the name of the book you want {Name} : ")
        return self.book
    def returnBook(self):
        self.book=input(f"Enter the name of the book you want to return {Name}: ")
        return self.book


if __name__=="__main__":
    # Now creating a object "college_library" 
    college_Library=Library(["computer science","maths","icit","django","Rich dad poor dad", "Rd sharma"]) # Mentioning the list of the books in the class library.
    college_Library.display_books()
    student=Student()

# Now we creating the loop so     
    while(True):
        Name=input("Enter your name: ")

        welcome='''======Welcome to the college library=====
        Please Choose an Option:
        1. To list the all avilable books 
        2. Request a book
        3. Return a book
        4. Exit form the library.
        '''
        print(welcome)

        a=int(input(f"Enter Your options {Name}:"))
        if a==1:
            college_Library.display_books()

        elif a==2:
            college_Library.borrow(student.requestBook())

        elif a==3:
            college_Library.Return_Book(student.returnBook())
        elif a==4:
            print(f"Thanks {Name} for using this library management system! \n Have a good day.")
            exit()
        else:
            print("Invalid Opitons")
            