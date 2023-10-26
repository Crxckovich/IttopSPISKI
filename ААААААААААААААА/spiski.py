import os
folder = os.getcwd() + "\data\\"
walk = os.walk(folder)
var = []
for line in walk:
    print(line)

files = line[2]

print(len(files))













