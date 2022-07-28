f=open('dataset_3363_3.txt','r') # cчитываем файл
line=f.readline().lower()
s = {}
while line:
    line=line.split()    
    i1=0
    i2=''
    q=0
    t=[]
    min1=0
    for i in line: # вводим слова в словарь
        if i not in s: # проверяем есть ли слово в словаре,если есть,то добавляю 1 
            s[i]=1
        else:
            s[i]+=1
    for values in s.values(): # находим максимальное число повторений
        if values>i1:
            i1=values
    for keys , values in s.items():
        if values==i1:
            min1=keys
for keys , values in s.items(): # если слова встречаются одинаковое кол-во,
    if values==i1:              # то находим  лексикографически первое 
        if min1>keys:
            min1=keys
print(min1,i1)
line=f.readline().lower()
f.close()