import json
import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Initialize the library as an empty list
library = []

# Load library data from file if it exists
def load_library():
    global library
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = json.load(file)

# Save library data to file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

# Add a book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book from the library
def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print("Book removed successfully!")

# Search for a book by title or author
def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search term: ").lower()
    
    results = []
    if choice == "1":
        results = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if query in book["author"].lower()]
    
    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read_status"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books in the library
def display_all_books():
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read_status"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display library statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("Total books: 0")
        print("Percentage read: 0%")
        return
    
    read_books = sum(1 for book in library if book["read_status"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main menu
def main_menu():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    load_library()
    main_menu()