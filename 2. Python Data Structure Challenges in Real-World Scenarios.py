
## 2. Python Data Structure Challenges in Real-World Scenarios

## Checking if the book is exists in the library ###

def add_book(library, book):
    if book in library:
        return "The book is already in the library."
    else:
        library.append(book) 
        return "Book added successfully."
    
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

### Adding a new book ###

new_book = ("The Child", "Fiona Barton")
print(add_book(library, new_book))

### Add a duplicate book ###

duplicate_book = ("1984", "George Orwell")
print(add_book(library, duplicate_book))

print(library)
