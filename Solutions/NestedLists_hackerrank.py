l.clear()
for i in range(int(input())):  ## Taking inputs to a nested list.
    name = input()
    score = float(input())
    l1=[name,score]
    l.append(l1)               ## l is the nested list where [name,score] are stored.
l2=[]     
lf=[]
lw=[]
for j in l:                   ## Extracting all elements into one list from the nested list.
    for k in j:
        l2.append(k)
##print(l2)

for i in range(0,len(l2)):    ##Extracting names and marks into individual lists.
    ##print(i)
    if i%2 != 0:
        lf.append(l2[i])      ## scores are stored in lf  
    else:
        lw.append(l2[i])      ## names are stored in lw 

print(lf)
print(lw)

## Finding second lowest score in list lf

# lowest=min(lf[0],lf[1])
# lowest2 = max(lf[0],lf[1])
# for item in lf:
#     if item < lowest:
#         lowest2 = lowest
#         lowest = item
#     elif lowest2 > item and item > lowest:
#         lowest2 = item
# print(lowest2)

# or
lf.sort()
for i in range(0,len(lf)-1):
    if lf[i]==lf[i+1]:
        lowest2=lf[i+1]

## Finding corresponding name for second lowest score.
lop=[]
for i in range(0,len(lf)):
    if lf[i] == lowest2:
        lop.append(lw[i])
lop.sort()
for i in lop:
    print(i)
  
    
    
