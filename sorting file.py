import os

path = input("path: ")
file_type = []

x = 1
for files_list in os.listdir(path):
    x += 1


for n in range(0 ,x):
    for file_list in os.listdir(path):
        if "." in file_list:
            for files in os.listdir(path):
                for i in files:
                    if "." in i:
                        if not files.split(".")[-1] in file_type:
                            file_type.append(files.split(".")[-1])
                            print(file_type)
            for j in file_type:
                try:
                    os.mkdir(path + "\\" + j)
                except OSError:
                    print("Failed to create folder " + j)
                else:
                    print("Create folder " + j + " complete")

            try:
                for file in os.listdir(path):
                    for x in file:
                        if "." in x:
                            if file.split(".")[-1] in file_type:
                                os.replace(path + "\\" + file, path + "\\" + file.split(".")[-1] + "\\" + file)
            except Exception:
                print(Exception)