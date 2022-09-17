import os
for root, dirs, files in os.walk(".", topdown=True):
    print(root)
    for name in files:
        path = os.path.join(root, name) 
        print(path)

        if os.path.splitext(name)[-1][1:] == "txt":
            tname = os.path.splitext(name)[0]
            file_new_path = os.path.join(root, tname + ".md") 
            os.rename(path, file_new_path)
            TFile = open(file_new_path, 'r', encoding='utf-8') # 打开文件(只读)
            conntent = TFile.readlines() # 按行读取
            TFile.close()
            for i in range(0, len(conntent)):
                conntent[i] = conntent[i].strip('\n') 
                conntent[i] = conntent[i] + "  \n"

            TFile = open(file_new_path, 'w', encoding='utf-8')
            TFile.writelines(conntent)
            TFile.close()
            print(file_new_path)
    for name in dirs:
        print(os.path.join(root, name))