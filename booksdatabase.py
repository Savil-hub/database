import sqlite3

# Connect to the database or create it if it doesn't exist
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()

print('Database Created!')

# Create the ebookstore table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebookstore (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        author VARCHAR,
        qty INTEGER
    );
''')

db.commit()
print('Table Created')

# Function to insert data into the ebookstore table
def insert_data(id, title, author, qty):
    cursor.execute('''
        INSERT INTO ebookstore(id, title, author, qty)
        VALUES(?,?,?,?)
    ''', (id, title, author, qty))
    db.commit()
    print("Data successfully added!")

# Function to view all books in the ebookstore
def view_all_books():
    cursor.execute('SELECT * FROM ebookstore')
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

# Function to enter a new book
def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter book quantity: "))
    insert_data(id, title, author, quantity)

# Function to update book information
def update_book():
    id = int(input("Enter book ID to update: "))
    title = input("Enter updated title: ")
    author = input("Enter updated author: ")
    quantity = int(input("Enter updated quantity: "))
    
    cursor.execute('''
        UPDATE ebookstore
        SET title=?, author=?, qty=?
        WHERE id=?
    ''', (title, author, quantity, id))
    db.commit()
    print("Book updated.")

# Function to delete a book
def delete_book():
    id = int(input("Enter book ID to delete: "))
    
    cursor.execute('DELETE FROM ebookstore WHERE id=?', (id,))
    db.commit()
    print("Book deleted.")

# Function to search for a specific book
def search_books():
    search_term = input("Enter book title or author to search: ")
    
    cursor.execute('''
        SELECT * FROM ebookstore
        WHERE title LIKE ? OR author LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%'))
    
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No books found.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Enter new book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("5. View all books")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        enter_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        view_all_books()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")