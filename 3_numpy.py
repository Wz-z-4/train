import numpy as np
# a = np.array([1,2,3])
# print(a)
# b = np.random.default_rng(42).random((3,2)) 
# print(b)
# a = np.ones((3, 4))
# b = np.array([1, 2, 3, 4])
# print(a + b )
# rr = np.arange(24).reshape(2, 3, 4)
# print(rr) 
# arr = np.arange(12)
# arr.reshape(3, 4)
# print(arr)          # 变成 3×4
# b = arr.reshape(3, -1)
# print(b)             # -1 = 自动推导 → (3, 4)
# c = arr.reshape(2, 3, 2)       # 变成 2×3×2 三维
# print(c)   
# arr.ravel()                # 展平（view，快）
# arr.flatten()              # 展平（copy，安全）

# a = np.arange(6).reshape(2, 3)
# a.T                        # 转置 → (3, 2)
# a.transpose(1, 0)    
# a = np.arange(12)
# c = a.reshape(3,-1)
# b = np.hsplit(c,2)
# # print(a)
# print(b)
# # print(c)


#现在进行独立的尝试rng = np.random.default_rng(42)
# data = rng.normal(50, 15, (1000, 5))

# # 随机插入一些 NaN
# mask = rng.random(data.shape) < 0.05
# data[mask] = np.nan

# # 你的任务：
# # 1. 统计每列 NaN 数量
# # 2. 用每列的均值填充 NaN
# # 3. 找出所有列的值都在 2σ 以内的行（去掉异常行）
# # 4. 对清洗后的数据统计每列的 mean, std, min, 25%, 50%, 75%, max

rng = np.random.default_rng(42)
data = rng.normal(50,15,(1000,5))
mask = rng.random(data.shape) < 0.05
data[mask] = np.nan
a,b,c,d,e = np.hsplit(data,5)
b = b.reshape(-1)
print(b,type(b))   
e = b.copy()              #这里重新拿出一个e承接b的数组

b_nan =np.isnan(b).sum()  #求出nan的个数

b[np.isnan(b)] = 0        #将nan修改为0

ave = np.sum(b)/(1000-b_nan) #因为b之前存在nan会造成误差所以不用mean()方法
print(b_nan ,ave)
b = b[b!=0]
b_max = b.max()            #最大值
b_min = b.min()               #最小值
b_std = b.std()             #标准差
e = e[~np.isnan(e)]
b_25 = np.percentile(e,25)   #1/4位数
b_50 = np.percentile(e,50)      #中位数
b_75 = np.percentile(e,75)      #3/4位数
#应该可以在剔除b为0后使用mean方法？
#接下来剔除可疑项
b_ok = b[(b>=ave - 2*b_std)&(b<= ave + 2*b_std)]
print(b_ok)



    

