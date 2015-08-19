import webbrowser as wb
import time as t
import sys

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
interval = int(sys.argv[1]) if len(sys.argv) > 1 and is_int(sys.argv[1]) else 300
url = sys.argv[2] if len(sys.argv) > 2 else 'http://xkcd.com/'

for i in range(0,5):
    t.sleep(interval)
    print t.asctime()
    wb.open(url)