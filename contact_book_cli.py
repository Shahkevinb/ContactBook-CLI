 
# SAMPLE README.MD
# 📇 Contact Book CLI (Python Project)

# A simple command-line Python app to manage your personal contacts.

# ## 🔧 Features:
# - Add Contact
# - View All Contacts
# - Search by Name
# - Delete by Name
# - Save to JSON file

# ## 🛠️ Technologies Used:
# - Python
# - File Handling
# - JSON

# ## 📦 How to Run:
# ```bash
# python contact_book.py



# Ek simple Python program jo contacts (name, phone, email) ko add, search, delete, aur view karta hai — command line (terminal) me.


print("PROJECT NAME: Contact Book CLI (Command Line Interface App)")

# step:1 create the manu (cli)
# Step 2: Add Contact Feature

contacts = []       # Global list to store all contacts

def add_contact():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Number: ")
    email = input("Enter Your Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email":email
    }

    contacts.append(contact)
    print(" Contact Added Successfully..!")

# Step 3: View All Contacts

def view_all_contacts():
    if len(contacts) == 0:
        print(" ❌ No Contacts Found.")
    else:
        print("\n All Saved Contacts:")
        for index, contact in enumerate(contacts, start=1):
             print(f"\nContact {index}")
             print(f"Name  : {contact['name']}")
             print(f"Phone : {contact['phone']}")
             print(f"Email : {contact['email']}")

# Step 4: Search Contact by Name

def search_contact():
    search_name = input("Enter Name To Search: ").lower()
    found = False

    for contact in contacts:
        if contact['name'].lower() == search_name:
            print("\n🔍 Contact Found:")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
            found = True
            break

    if not found:
        print("❌ Contact not found.")

#  Step 5: Delete Contact by Name

def delete_contact():
    delete_name = input("Enter Name To Delete: ").lower()
    found = False

    for contact in contacts:
        if contact['name'].lower() == delete_name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            found = True
            break

    if not found:
        print("❌ Contact not found.")

def show_menu():
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_all_contacts()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print(" ❌ Invalid choice. Please enter a number between 1 and 5.")


