import os


def checker(fname):
    if os.path.exists(f'{fname}.txt'):
        return True

    print('No such file')
    return False


def opener(fname, form='r'):
    try:
        file = open(fname + '.txt', form)
        return file
    except:
        return 'I cant open file'


def take_some_new_text():
    text = input('Input some text')
    return text


def createFile(fname):
    file = opener(fname, form='w')
    file.close()


def readFile(fname):
    if checker(fname):
        file = opener(fname, form='r')
        print(file.read())


def appendFile(fname):
    if checker(fname):
        file = opener(fname, form='a+')
        print(file.read())
        file.write(take_some_new_text())


def overwriteFile(fname):
    if checker(fname):
        file = opener(fname, form='w')
        file.write(take_some_new_text())


def removeFile(fname):
    if checker(fname):
        os.remove(f'{fname}.txt')


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
try:
    option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))
except ValueError:
    print('НУЖНО ВВОДИТЬ ЧИСЛА')

file_name = input('Please enter a file name (no extension, .txt will be added automatically):')
print(file_name)

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')