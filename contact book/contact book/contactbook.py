class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contacts(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{contact.name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for index, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[index]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contacts(keyword)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contacts found.")

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number (press Enter to skip): ").strip()
            new_email = input("Enter new email (press Enter to skip): ").strip()
            new_address = input("Enter new address (press Enter to skip): ").strip()
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
