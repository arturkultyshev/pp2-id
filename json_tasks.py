import json

with open('data.json', 'r') as file:
    a = json.load(file)

for key in a:
    if 'title' in key:
        print('hello')
    else:
        print(key, a[key])


f = {
    'artur': 18,
    'misha': 20,
    'sergey': 45
}
with open('data2.json', 'w') as file2:
    json.dump(f, file2)
