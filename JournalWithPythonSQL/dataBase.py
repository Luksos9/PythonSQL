entries = []


def add_entry(entry_content, entry_date):
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date: ")

    entries.append({"content": entry_content, "date": entry_date})

def get_entries():
    return entries

