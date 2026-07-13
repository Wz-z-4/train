class people:
    def __init__(self,n,a,g,na):
        self.name = n
        self.gender = g
        self.__age = a
        self.nation = na
    def __str__(self):
        return f"my name is {self.name},my gender is {self.gender},I'm from {self.nation}"
    def age_change(self):
        new_age =self.__age + 2
        print(f"my age is {new_age}")
    def __eq__(self,other):
        return(self.__age == other.__age)
# people("zz",19,"大一","CN")
# people.age_change(19)  尝试用外部输入来赋值
e = 1
while e<3:
    n,a,g,na = input().split(',')
    a = int(a)
    p=people(n,a,g,na)
    print(p)
    p.age_change()
    if e ==1:
        p1 = p
    else :
        p2 = p
    e+=1
print(p1 == p2)






    
