## Contact 1.0
# class Contact():

#     all_contacts = []

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)

class ContactList(list):

    def search(self, name):

        matching_contacts = []

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        
        return matching_contacts
    
# Contact 1.1
class Contact():

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
# Conta

class Suppliers(Contact):

    def order(self, order):

        print("If this were a real system we would send"
              "'{}' order to '{}'".format(order, self.name))
        
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
print([c.name for c in Contact.all_contacts.search('John')])
print()

c1 = Contact("Alice", "alice@example.com")
f1 = Friend("Bob", "bob@example.com", "123-456-7890")

print(Contact.all_contacts)
print()
print(Contact.all_contacts[4].phone)  