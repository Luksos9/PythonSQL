import database

welcome = "Welcome to Your Diary App!"

menu = """----menu----

Select:
1) To add a new log entry
2) To view your entries
3) To delete entry
4) To Exit 
----
Your choice: """

database.create_table()


def close_connection():
    """Closes connection"""
    database.close_conn()


def add_new_log():
    """Asks user to add new entry"""
    entry = input("Your entry: ")
    entry_date = input("Enter today's date (dd-mm-yyyy): ")
    while len(entry_date) != 10:  # It could be more precise
        print("Invalid date!")
    database.add_entry(entry, entry_date)
    print("Entry was successfully added!")


def view_all_entries():
    """Views all entries in database"""
    entries = database.view_entries()
    for entry in entries:
        print("Entry({}), Date: {}\n".format(entry[0], entry[1]),
              "'{}'\n".format(entry[2]))


def delete_entry_by_id():
    """Asks user to enter entry id to delete entry (Entry id can be found by viewing entries) """
    entry_number = input("Enter entry id: ")
    database.delete_entry(entry_number)
    print("Entry was successfully deleted!")


# Main loop asking user to enter number to take corresponding action
while (user_input := input(menu)) != "4":

    if user_input == '1':
        add_new_log()
    elif user_input == '2':
        view_all_entries()
    elif user_input == '3':
        delete_entry_by_id()
    else:
        print("Wrong input. Please select a number between 1-4.")

close_connection()
