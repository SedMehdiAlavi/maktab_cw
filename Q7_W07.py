class Library :
    def __init__(self , book : list , quantity : int ) :
        self.book = book
        self.quantity = quantity

    def __len__(self):
        return len(self.book)

    def __add__(self, other):
        return Library(self.book + other.book, self.quantity + other.quantity)

    def __str__(self):
        c = 1
        for book in self.book:
            print(f"{c} : {book}")
            c += 1
        return f"Book : {self.book} Quantity: {self.quantity}\n"


    def __del__(self):
        print("Deleted library")

book11 = Library(["atomic habits2" ,"reality2" ] ,3)
# book22 = Library([] , 4)
print(book11)
# print(sum())
