class Book :
    def __init__(self, title = None , author = None , pages = int):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"The book {self.title} written by {self.author} with pages {self.pages}"

    def __add__(self, other):
       # if isinstance(other):
        return Book(self.title + other.title , self.author + other.author , self.pages + other.pages)



    def __del__(self):
        print("Deleted book")

book1 = Book("atomic habits" , "james clear" , 331)
book2 = Book("reality" , "hans resling" , 300)
print(book1)
print(book2)
result = book1 + book2
print(result)
