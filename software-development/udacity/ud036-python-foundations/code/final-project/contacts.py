from contact import Contact
from logger import Logger
import sys
import os
import hashlib
import json

logger = Logger()
db_file = 'contacts.json'

# -------------
# database api
# -------------

def init_db():
    """Initialize an empty database, wiping out an existing one if necessary."""
    data = json.dumps({}, indent=4)
    with open(db_file, 'w') as f:
        f.write(data)
        
def get_db():
    """Read database from a file and load into a dictionary."""
    with open(db_file) as f:
        db = json.load(f)
    return db

def write_db(db):
    """Write the contacts dictionary to a file."""
    with open(db_file, 'w') as f:
        json.dump(db, f, indent=4)

def add_contact(contact):
    """Writes a contact to the file, checking if that contact exists or not first."""
    db = get_db()
    
    if contact.get_hash_name() not in db:
        db[contact.get_hash_name()] = json.loads(contact.json())
        write_db(db)
    else:
        sys.exit(logger.fail('fatal: contact already exists'))

def edit_contact(contact):
    """Edit a contact in the database, if they exist."""
    db = get_db()
    
    if contact.get_hash_name() in db:
        db[contact.get_hash_name()] = json.loads(contact.json())
        write_db(db)
    else:
        sys.exit(logger.fail('fatal: contact does not exist'))
        
def list_contact(name):
    """List a contact's information, if they exist in the database."""
    db = get_db()
    name = hashlib.sha256(name).hexdigest()
    
    if name in db:
        info = db[name]
        print logger.ok("""
        Contact Information:
            Name: %s
            Phone Number: %s
            Email Address: %s
        """ % (info['name'], info['phone'], info['email']))
    else:
        sys.exit(logger.fail('fatal: contact does not exist'))
        
def del_contact(contact):
    """Deletes a contact from the dictionary if it exists."""
    db = get_db()
    
    if contact.get_hash_name() in db:
        db.pop(contact.get_hash_name())
        write_db(db)
        sys.exit(logger.ok('success: contact ' + '"%s"' % contact.get_name() + ' deleted'))
    else:
        sys.exit(logger.fail('fatal: contact does not exist'))
        
# -------------
# cli
# -------------
        
def check_name(flag):
    start = sys.argv.index(flag)
    name = sys.argv[start + 1] + " " + sys.argv[start + 2] if len(sys.argv) > 3 else sys.argv[start + 1]
    return name
    
def check_input():
    if '-a' in sys.argv:
        try:
            name = check_name('-a')
            phone = raw_input('phone number: ')
            email = raw_input('email address: ')
            person = Contact(name, phone, email)
            add_contact(person)
            list_contact(name)
        except IndexError:
            sys.exit(logger.fail('fatal: not enough arguments'))
        except IOError:
            sys.exit(logger.fail('fatal: contacts database not found'))
    elif '-e' in sys.argv:
        try:
            name = check_name('-e')
            phone = raw_input('phone number: ')
            email = raw_input('email address: ')
            person = Contact(name, phone, email)
            edit_contact(person)
            list_contact(name)
        except IndexError:
            sys.exit(logger.fail('fatal: not enough arguments'))
        except IOError:
            sys.exit(logger.fail('fatal: contacts database not found'))
    elif '-d' in sys.argv:
        try:
            name = check_name('-d')
            person = Contact(name, '', '')
            del_contact(person)
        except IndexError:
            sys.exit(logger.fail('fatal: not enough arguments'))
        except IOError:
            sys.exit(logger.fail('fatal: contacts database not found'))
    elif '-i' in sys.argv:
        init_db()
        sys.exit(logger.ok('success: database created in contacts.json'))
    elif '-l' in sys.argv:
        try:
            name = check_name('-l')
            list_contact(name)
        except IndexError:
            sys.exit(logger.fail('fatal: not enough arguments'))
        except IOError:
            sys.exit(logger.fail('fatal: contacts database not found'))
    else:
        sys.exit(logger.warn("""
        usage:
            -i : initialize database / clear existing one
            -a <name> : add contact to database
            -l <name> : list contact information
            -d <name> : remove contact from database
        """))
        
check_input()