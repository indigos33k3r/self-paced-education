import json
import hashlib

class Contact():
    """Stores a contact and their name, email address, and phone number."""
    
    def __init__(self, name, phone, email):
        self.hash_name = hashlib.sha256(name).hexdigest()
        self.name = name
        self.phone = phone
        self.email = email
        
    def json(self):
        info = {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
        return json.dumps(info, indent=4)
    
    def get_hash_name(self):
        return self.hash_name
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def set_name(self, name):
        self.hash_name = hashlib.sha256(name).hexdigest()
        self.name = name
        
    def set_phone(self, phone):
        self.phone = phone
        
    def set_email(self, email):
        self.email = email