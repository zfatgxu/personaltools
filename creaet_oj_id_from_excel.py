import  pandas  as pd
import string,random
df=pd.read_excel('D:/chrome下载/excels/181.xls')
#data=df.head()#默认读取前5行的数据
#print("获取到所有的值:\n{0}".format(data))#格式化输出
#data=df.ix[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
#print("读取指定行的数据：\n{0}".format(data))
#print("输出值\n",df['学号'].values)
part1=df['班级'].values.tolist()
part2=df['学号'].values.tolist()
part3=df['姓名'].values.tolist()
# print(str(part1[0])+"_"+str(part2[0])+"_"+str(part3[0]))
# //print(len(part1))
for i in range(len(part1)):
    j=8
    id=[]
    goal = ''.join(str(i) for i in random.sample(range(0,9),j)) #''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
    print(str(part1[i]) + "_" + str(part2[i]) + "_" + str(part3[i])+","+goal+",test@test.com")

# print(s)
# print(type(part1))
#for c in range(part1):


