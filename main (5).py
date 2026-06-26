# Contact Book Program

contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts.append([name, phone, email])
        print("Contact saved")

    elif ch == "2":
        if contacts == []:
            print("No contacts")
        else:
            for c in contacts:
                print("Name:", c[0], "| Phone:", c[1], "| Email:", c[2])

    elif ch == "3":
        s = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c[0] == s:
                print("Found:", c)
                found = True
        if found == False:
            print("Not found")

    elif ch == "4":
        d = input("Enter name to delete: ")
        for c in contacts:
            if c[0] == d:
                contacts.remove(c)
                print("Deleted")
                break
        else:
            print("Name not found")

    elif ch == "5":
        print("Closing program")
        break

    else:
        print("Invalid choice")