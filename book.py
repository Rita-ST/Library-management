

class Book:
    def __init__(self,title,author,contributors,edition,date,number_of_pages,copies=1):
        self.bookTitle=title
        self.author=author
        self.contributor=self.contributor
        self.edition=edition
        self.date=date
        self.numpages=number_of_pages
        self.number_of_copies=copies

    def info(self):
        return f"{self.bookTitle} ,{self.date} by {self.author}"
    def available(self) -> bool:
        return self.number_of_copies >0
    def borrow_copy(self) -> bool:
        if self.available():
            self.number_of_copies-=1
            return True 
        else:
            return False
    def return_copy(self) -> None:
        self.number_of_copies +=1
        
