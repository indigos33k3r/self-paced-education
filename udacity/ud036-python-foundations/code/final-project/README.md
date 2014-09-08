###Project Idea

Create a database of contacts, and a command-line interface for adding, editing, and removing them from the database.

Since this is an OOP class, two classes are used:

1. contact.Contact: the blueprint for an actual contact w/ name, phone number, and email address
2. logger.Logger: class for logging messages to console with color coding

Several external modules are used as well, including:

1. json
2. sys
3. os
4. hashlib

---

###Database

Contacts are stored in a JSON file of this format:

    {
        "contacts": {
            "1a389272506332876e524310cd9f1dd481a5cc895a643f9132cf82746f5d3393": {
                "name": "Joe Jones"
                "phone": "000-000-0000"
                "email": "joe@example.com"
            },
            "1e4bd2e2d2c42b971708c8014c6ca5fc6ceb798dab406f458b1e6789a8a7a748": {
                "name": "Shannon Jones",
                "phone": "111-111-1111",
                "email": "shannon@example.com"
            }
        }
    }
    
There are a few things of note:

1. The inner dictionaries containing each contact's name is an object with a name that is a SHA-256 hash of each name.
    * For example, "Shannon Jones" hashes to "1e4bd2e2d2c42b971708c8014c6ca5fc6ceb798dab406f458b1e6789a8a7a748".
2. Each contact has a name, phone number, and email address.

###CLI

The command-line interface can be run using Python 2.7 by typing this command:

    python contacts.py [-a -d -e -l -i] [name]
    
* `-a`: Add a contact; if they already exist, quit and notify user.
* `-e`: Edit a contact; if they don't exist, quit and notify user.
* `-d`: Delete a contact; if they don't exist, quit and notify user.
* `-l`: List a contact's information; if they don't exist, quit and notify user.
* `-i`: Create the contacts.json file, or wipe existing file.

Here is an example for each option:

* `-a`: `$ python contacts.py -a Joe Jones`
* `-e`: `$ python contacts.py -e Joe Jones`
* `-d`: `$ python contacts.py -d Joe Jones`
* `-l`: `$ python contacts.py -l Joe Jones`
* `-i`: `$ python contacts.py -i`
        
###Other Information

Contact info is stored in `contacts.json`.