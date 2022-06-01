import os
import json


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


files = os.listdir('completions/')
data = list()
for file in files:
    completion = open_file('completions/%s' % file).replace('================================','').strip()
    story = open_file('stories/%s' % file)
    info = {'prompt': story + '\n\n PROFESSIONAL FEEDBACK: ', 'completion': ' ' + completion}
    data.append(info)


with open('creative_writing_coach.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')