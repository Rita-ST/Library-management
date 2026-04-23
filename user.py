
    
class User:
    def __init__(self,name,email,user_id):
        self.name=name
        self.email=email
        self.user_id=user_id
        self.borrowed_books=[]


    def description(self):
        print(f"Hi {self.name}")

    def borrowed_books(self,book):
        self.borrowed_books.append(book)

    def return_book(self,book):
        self.borrowed_books.remove(book)
    def total_book(self):
        return len(self.borrowed_books)
    
user1=User("Rita Gadlela","londiwegadlela@gmail.com","1122")

print(user1.total_book())        
