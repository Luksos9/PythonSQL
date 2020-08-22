from dataBase import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming Journal!"

def prompt_new_entry():
    """Prompt user to add new entry"""
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)

def view_entries(entries):
    """Display entry information"""
    for entry in entries:
        print(f"{entry[1]}\n{entry[0]}\n\n")


print(welcome)
create_table()

while (user_input := input(menu)) != "3":  # That is new Python 3.8 feature, so i dont have to put user_input
    if user_input == '1':                  # before and after the loop: user_input = input(menu)
        prompt_new_entry()

    elif user_input == '2':
        view_entries(get_entries())

    else:
        print('Invalid option, please try again!')
