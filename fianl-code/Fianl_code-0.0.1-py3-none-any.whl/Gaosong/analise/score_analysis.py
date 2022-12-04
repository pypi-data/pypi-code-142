import pandas as pd
import matplotlib.pyplot as plt

#对学生成绩单和信息进行整合以及数据分析

# 定义分数等级划分原则
def get_datas(df, col):
    level_1 = len(df[df[col] >= 90]) #df[df[col]]选择col列成绩大于90的行的数量
    level_2 = len(df[(df[col] < 90) & (df[col] >= 80)])
    level_3 = len(df[(df[col] < 80) & (df[col] >= 70)])
    level_4 = len(df[(df[col] < 70) & (df[col] >= 60)])
    level_5 = len(df[df[col] < 60])
    return level_1, level_2, level_3, level_4, level_5


# 两个表格合并
d_1 = pd.read_excel("学生基本信息表.xlsx", skiprows=1) #读取并跳过第一行
d_2 = pd.read_excel("期末考试成绩表.xlsx", skiprows=1) #读取并跳过第一行
d_3 = pd.merge(d_1, d_2) #合并
d_3 = d_3.sort_values(by=["总分", "英语"], ascending=False) #按照总分由高向低，总分相同看英语
d_3.to_excel("学生期末考试成绩排名表.xlsx")

# 各科成绩分布
results = []
subjects = ["语文", "数学", "英语"]
labels = ["优秀", "良好", "中等", "及格", "不及格"]

# 调用函数并向函数内输入表格和科目，返回对应等级人数
for subject in subjects: #提取学科
    results.append(get_datas(d_3, subject)) #将学科对应分数段人数追加到列表
print(results)
print('-'*50)

plt.figure(figsize=(12, 5))  #创建一个新图
plt.suptitle("学生各科成绩分布图") #定义标题

# 提取每科的数据
for index, data in enumerate(results):
    print(index,data)
    
# 打印图表
    plt.subplot(1, 3, index + 1) #行、列、对子图进行编号
    plt.title(subjects[index] + "成绩分布") #设置标题
    #设置图表样式：
    plt.pie(data, labels=labels, autopct='%.1f%%', shadow=True, labeldistance=1.2,
            explode=(0.1, 0, 0, 0, 0), colors=['m', 'c', 'y', 'r', 'g'])
    plt.savefig("饼状图")

