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

class Suppliers(Contact):

    def order(self, order):

        print("If this were a real system we would send"
              "'{}' order to '{}'".format(order, self.name))
        
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

