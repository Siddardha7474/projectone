library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "Title": title,
        "Author": author
    }

    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available.\n")
        return

    print("\n===== Library Books =====")

    for book_id, details in library.items():
        print(f"Book ID : {book_id}")
        print(f"Title   : {details['Title']}")
        print(f"Author  : {details['Author']}")
        print("------------------------")

def search_book():
    book_id = input("Enter Book ID to search: ")

    if book_id in library:
        details = library[book_id]

        print("\nBook Found")
        print(f"Title  : {details['Title']}")
        print(f"Author : {details['Author']}\n")

    else:
        print("Book not found.\n")

def delete_book():
    book_id = input("Enter Book ID to delete: ")

    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!\n")

    else:
        print("Book not found.\n")

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.\n")