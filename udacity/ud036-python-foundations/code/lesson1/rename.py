import os, sys

path = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else 'img'
chars_to_strip = sys.argv[2] if len(sys.argv) > 2 else "0123456789"
files = os.listdir(path)

def strip(s):
    return ''.join([c for c in s if not c in chars_to_strip])

os.chdir(path)

for f in files:
    os.rename(f, strip(f))