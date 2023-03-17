import os

os.chdir('Users\Asus-New\Desktop')
path = os.path.abspath('pp2-id')


for folder, subfolder, file in os.walk(path):
    print(folder)


def geb():
    yield