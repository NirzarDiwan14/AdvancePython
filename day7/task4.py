class EmailValidator:
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email
    
print(EmailValidator.is_valid("Nirzar@gmail.com"))
print(EmailValidator.is_valid("Nirzargmailcom"))
