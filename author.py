class Author:
    def __init__(self,name,nationality,data_of_birth):
        self.name=name
        self.nationality=nationality
        self.date_of_birth=date_of_birth
        self.nationality=nationality
    def add_book(self,book):
        self.book_writtten.append(book)

    def bio(self,award):
        print(f"{self.name} is a {self.nationality} author born on {self.date_of_birth} ,with {self.award} awards . ")



