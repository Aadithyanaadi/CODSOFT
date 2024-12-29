import json

CONTACT_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added!")

def view_contacts(contacts):
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.")

def update_contact(contacts):
    search_contact(contacts)
    name_to_update = input("Enter the name of the contact to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print("Enter new details (leave blank to keep current):")
            contact['name'] = input(f"Name [{contact['name']}]: ") or contact['name']
            contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
            save_contacts(contacts)
            print("Contact updated!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_contact(contacts)
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
