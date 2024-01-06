
def AddSamplespace():
    #样本空间：6班
    class_06 = open('Sample_space_06.txt','w+')
    class_06_all = open('class06_allori.txt','r')
    class06_num = list(class_06_all.readlines())
    for i in class06_num:
        #formatted_number = f'06{i:02}'  # 使用 f-string 格式化数字，并确保至少两位数
        class_06.write(i)
    class_06.close()
    #样本空间:3班
    class_03 = open('Sample_space_03.txt', 'w+')
    class_03_all = open('class03_allori.txt', 'r')
    class03_num = list(class_03_all.readlines())
    for i in class03_num:
        #formatted_number = f'03{i:02}'  # 使用 f-string 格式化数字，并确保至少两位数
        class_03.write(i)
    class_03.close()
def resetSelected():
    s01 = open('Selected_06.txt','w+')
    s02 = open('Selected_03.txt','w+')
    s01.close()
    s02.close()

AddSamplespace()
resetSelected()
input('已重置完毕，按Enter键来退出。 ')
