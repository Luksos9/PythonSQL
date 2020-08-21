from dataBase import add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming Journal!"


print(welcome)

while (user_input := input(menu)) != "3":  # That is new Python 3.8 feature, so i dont have to put user_input
    if user_input == '1':                  # before and after the loop: user_input = input(menu)
        entry_content = input("What have you learned today?")
        entry_date = input("Enter the date: ")

        add_entry(entry_content, entry_date)
    elif user_input == '2':
        entries = get_entries()

        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")

    else:
        print('Invalid option, please try again!')
