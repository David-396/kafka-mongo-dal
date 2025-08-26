import json

with open (r'producer\data\interesting_category_dict.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

    for k,v in d.items():
        print(k)

print('----------------------------------')
with open (r'producer\data\newsgroups_not_interesting.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

