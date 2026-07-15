import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sb
plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows
plt.rcParams['axes.unicode_minus'] = False
# data = np.random.randint(10,20,size = 20)
# fig,axs = plt.subplots()
# axs.plot(data,color='green')
# axs.set_title('random_output')
# axs.set_xlabel('times')
# axs.set_ylabel('output')
# plt.tight_layout()
# plt.show()
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
df = pd.read_csv('titanic.csv',index_col='PassengerId')
# print(df)
#这是条形图
axes[0].set_title("魔方石佬母了")
data_1 = df["Survived"]
data_2 = df['Sex']
sb.barplot(x = data_2,y=data_1,ax=axes[0])
#热力图
numeric_df = df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']]
data_3 = numeric_df.corr()  # 这就是一个二维矩阵
axes[1].set_title('a heat plot')
sb.heatmap(data = data_3,annot=True,ax=axes[1])
plt.show()
#散点图
# sb.scatterplot()