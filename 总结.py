import matplotlib.pyplot as plt
import numpy as np
import  seaborn as sb
import pandas as pd
from pathlib import Path
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv(Path('titanic.csv'),index_col='PassengerId')
print(df.isna().sum())  #先找出各项的缺失值，然后跟据不同的需求改变策略
#进行分析。
fig, axes = plt.subplots(2, 2, figsize=(14, 6))
fig.suptitle('analysis about Titanic')
 #幸存者与舱位等级关系，用直方图表示
axes[0,0].set_title('幸存者与仓位')
a = df.dropna(subset = ['Sex'])
# a['survived rate'] = a.groupby('Pclass')['Survived'].mean()  这里是ai提出的建议，但是实际发现展示效果不好所以弃用
sb.barplot(y=a['Survived'], x=a['Pclass'], ax=axes[0,0],hue = a['Sex'])
axes[0,0].set_xlabel('舱位等级')
axes[0,0].set_ylabel('存活')
#------------------------------------------
#接下来是年龄与兄弟姐妹配偶、父母子女的热力图
axes[0,1].set_title('热力图-regarding parents and sis,bro')
b = df.dropna(subset=['Age'])
data_heatmap =b[['Age', 'SibSp', 'Parch']].corr()
sb.heatmap(data = data_heatmap,annot = True,ax = axes[0,1])
#------------------------------------------
#折线图，关于年龄、兄弟姐妹、性别
sb.stripplot(x=b['SibSp'],y=b['Age'],hue=b['Sex'],ax = axes[1,0])
#跟据ai，因为是离散数据所以会出现裙带阴影
#------------------------------------------
#舱位等级、票价、幸存的散点图，以性别为标识
axes[1,1].set_title('年龄与票价散点图')
sb.scatterplot(x=b['Age'], y=b['Fare'], hue=b['Sex'], ax=axes[1,1])
axes[1,1].set_xlim(0, 50)      # X轴：年龄范围
axes[1,1].set_ylim(0, 300)     # Y轴：票价范围
plt.tight_layout()
plt.show()

#-------------------------------------------
#关于港口的分析 是否可以分析港口和舱位等级的关系
fig,axes = plt.subplots(figsize = (10,6))
df.dropna(subset=['Embarked'],inplace = True)
#使用直方图来分析
sb.barplot(x = df['Embarked'],y = df['Pclass'])
axes.set_xlabel('港口')
axes.set_ylabel("舱位等级")
axes.set_title('舱口等级与港口')
plt.tight_layout()
plt.show()

