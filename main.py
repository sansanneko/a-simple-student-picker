import random
import datetime
now = datetime.datetime.now()
# init
# Author Li RH
#导入3班和6班的学生
class03= open('Sample_space_03.txt','r',encoding='utf-8')
class06= open('Sample_space_06.txt','r',encoding='utf-8')
Students_03 = list(class03.readlines())
Students_06 = list(class06.readlines())
class03.close()
class06.close()
selected = []
newadd = []
class06names= list(open('Class06_names.txt','r',encoding='utf-8'))
class03names= list(open('Class03_names.txt','r',encoding='utf-8'))
def pickc03():
    if len(Students_03) == 0 :
        print('3班已经没有人可以抽取了。')
        input('press any key to exit ')
    elif len (Students_03)<= 4:
        _chosen = []
        _picked = []
        for i in Students_03:
            _chosen.append(i)
        _picked = _chosen
        for i in _chosen:
            Students_03.remove(i)
        clear(3)
        print("3班已全部抽取完毕，再见")

    else:
        _picked = []
        for i in range(4):
            _chosen = (random.choice(Students_03))
            _picked.append(_chosen)
            Students_03.remove(_chosen)
        clear(3)

    s03= open('Selected_03.txt', 'a+')
    _tempload = s03.readlines()

    newadd.append(now.strftime("%Y-%m-%d %H:%M:%S"+ ' Lucky students: \n'))
    for i in _tempload:
        newadd.append(i)
    for i in _picked:
        newadd.append(i)
    for j in newadd:
        s03.write(j)
    s03.write('\n')
    return _picked

def pickc06():
    if len(Students_06) == 0 :
        print('6班已经没有人可以抽取了。')
        input('press any key to exit ')
    elif len (Students_06)<= 4:
        _chosen = []
        _picked = []
        for i in Students_06:
            _chosen.append(i)
        _picked = _chosen
        for i in _chosen:
            Students_06.remove(i)
        clear(6)
        print("6班已全部抽取完毕，再见")

    else:
        _picked = []
        for i in range(4):
            _chosen = (random.choice(Students_06))
            _picked.append(_chosen)
            Students_06.remove(_chosen)
        clear(6)

    s06 = open('Selected_06.txt', 'a+')
    s06.write(now.strftime("%Y-%m-%d %H:%M:%S" + ' Lucky students: \n'))
    for i in _picked:
        s06.write(i)
    s06.write('\n')
    s06.close()
    return  _picked

def clear(x):
    if x == 3:
        c12 = open('Sample_space_12.txt','w+')
        for i in Students_03:
            c12.write(i)
    if x == 6:
        c01 = open('Sample_space_06.txt','w+')
        for i in Students_06:
            c01.write(i)



def pickacg(x):
    if x == 3:
        selected = list(pickc03())
        print(f'3班抽出的学生为：')
        for i in selected:
            print(f'{i} {class03names[int(i[2:4])-1]}')
            #print(f'{i[2:4]}')
            #print(class03names[int(i[2:4])-1])
        print(f'3班还有{len(Students_03)}位学生没有抽到，具体可以看文件目录下的Sample_space_03查看。')
    if x == 6:
        selected = list(pickc06())
        print('6班抽出的学生为：')
        for i in selected:
            print(f'{i} {class06names[int(i[2:4])-1]}')
        print(f'6班还有{len(Students_06)}位学生没有抽到，具体可以看文件目录下的Sample_space_06查看。')

print("************************************************************************")
print('欢迎使用学生抽取小程序，作者：匿名')
a = input('请输入要抽取的班级，例如要抽6班的学生6班就输入6，然后按下回车键，如果想重置的话，可以点击文件目录下的Reset Students.exe来重置。>>  ')
pickacg(int(a))
print(f'学生已抽好，抽到的学生已保存在目录下的selected_{a}文件。')
print("************************************************************************")
input('按Enter(回车)键来退出。 ')


#加入功能：通过学号查询姓名，显示剩余未抽取到的学生