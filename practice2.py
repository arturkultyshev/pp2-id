import os

path = os.path.abspath(input())

size = 0
msize = 0
mfile = ''

for folder, subfolder, files in os.walk(path):
    print(folder, subfolder, files)
    for file in files:
        size = os.stat(os.path.join(folder, file)).st_size

        if size > msize:
            msize = size
            mfile = os.path.join(folder, file)

print(f'The largest file is: {mfile}')
print(f'Size: {msize} bytes')
