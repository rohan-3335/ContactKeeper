import json


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump([vars(contact) for contact in contacts], file, indent=4)


def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def delete_contact():
    name = input("Enter the name to remove: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")


def search_contact():
    name = input("Enter the name of the user to search: ")
    for contact in contacts:
       if contact["name"] == name:
            print(contact)
            
            return

    print("Contact not found!")


def display_contacts():
    for contact in contacts:
        print(contact)


def main():
    global contacts
    contacts = load_contacts()

    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
