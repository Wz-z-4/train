import pandas as pd
a = pd.DataFrame({
    'a':[1,2,3],
    'b':[4,6,5]
})

a.set_index((i for i in range(1,4)),inplace =  True)
print(a.T)
