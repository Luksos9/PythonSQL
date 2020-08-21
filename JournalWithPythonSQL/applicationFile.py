menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming Journal!"


print(welcome)

while (user_input := input(menu)) != "3":  # That is new Python 3.8 feature, so i dont have to put user_input
    if user_input == '1':                  # before and after the loop: user_input = input(menu)
        print("Adding...")
    elif user_input == '2':
        print('Viewing...')
    else:
        print('Invalid option, please try again!')
