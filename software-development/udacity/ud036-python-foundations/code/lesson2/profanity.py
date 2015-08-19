import os, urllib

def read_text(path_to_file):
    quotes = open(path_to_file)
    return quotes.read()

def check_profanity(text_to_check):
    url = 'http://www.wdyl.com/profanity?q=' + text_to_check
    connection = urllib.urlopen(url)
    response = connection.read()
    connection.close()
    return True if 'true' in response else False

files = ['files/' + f for f in os.listdir('files')]

for f in files:
    text = read_text(f)
    has_swears = check_profanity(text)
    if has_swears:
        print "File: " + f + " contains profanity!"