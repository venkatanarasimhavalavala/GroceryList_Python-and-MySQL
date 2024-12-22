import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Narsi@1117",
    database="grocery_db"
)

cursor = db.cursor()

def adding():
    item = input("Enter the item you want to add: ").lower()
    query = "INSERT INTO groceries (item_name) VALUES (%s)"
    cursor.execute(query, (item,))
    db.commit()
    return f"{item}, has been added to the list"

def removing():
    item = input("Enter the item you want to remove: ").lower()
    query = "SELECT * FROM groceries WHERE item_name = %s"
    cursor.execute(query, (item,))
    result = cursor.fetchone()
    if result is None:
        return f"{item} is not in the list"
    else:
        query = "DELETE FROM groceries WHERE item_name = %s"
        cursor.execute(query, (item,))
        db.commit()
        return f"{item}, has been removed from the list"

def viewing():
    query = "SELECT item_name FROM groceries"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("Your list is:")
        for row in results:
            print(row[0])
    else:
        print("Your list is empty")

def quit_program():
    cursor.close()
    db.close()
    return "Goodbye"

while True:
    print("\n\nSelect the options you want")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addlist = adding()
        print(addlist)
    elif choice == 2:
        remove = removing()
        print(remove)
    elif choice == 3:
        viewing()
    elif choice == 4:
        print(quit_program())
        break
    else:
        print("Invalid choice, please try again.")
