import sys

filepath1 = sys.argv[1]
filepath2 = sys.argv[2]
resultPath = sys.argv[3]

try:
    with open(f'./{filepath1}') as file:
        file_data1 = file.read()
except FileNotFoundError:
    print("File2 does not exist")

try:
    with open(f'./{filepath2}') as file:
        file_data2 = file.read()
except FileNotFoundError:
    print("File2 does not exist")

if file_data1 and file_data2:
    try:
        with open(f'./{resultPath}','a') as file:
            file.writelines(file_data1)
            file.write("\n")
            file.writelines(file_data2)
    except FileExistsError:
        print("File already exists")
