# 1. Library Management System 📚

# Create class:

# Library

# Methods:

# addBook()
# showBooks()
# totalBooks

class Library:
    def __init__(self,book1,book2,book3,book4):
        self.book1=book1
        self.book2=book2
        self.book3=book3
        self.book4=book4

    def totalBooks(self,book1,book2,book3,book4):
        total=book1+book2+book3+book4
        print("Total Books",total)

library=Library("The tale of two cities","The little Prince","The Alchemist","Harry Potter")

print("Books-1",library.book1)
print("Books-2",library.book2)
print("Books-3",library.book3)
print("Books-4",library.book4)

library.totalBooks("The tale of two cities","The little Prince","The Alchemist","Harry Potter")

        
        