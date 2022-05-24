import os


files = os.listdir('stories/')
for file in files:
    with open('stories/%s' % file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    if "I am a bot" in content:
        os.remove('stories/%s' % file)