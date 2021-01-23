def overlap(L1,L2):      #checking if there is an interaction between two lines, L1 and L2
    if L1[0] == L2[0] and L1[1] == L2[1] or L1[0] == L2[1] and L2[0] == L1[1]:  # check if lines are identical
        return True
    elif L1[0] == L2[0] or L1[0] == L2[1] or L1[1] == L2[0] or L1[1] == L2[1]:  #checking the interaction on start\end points
        return True
    elif L1[0]< L2[0] and L2[0] < L1[1] :
        return True
    elif L2[0] < L1[0] and L2[0] > L1[1]:
        return True
    elif L2[1] > L1[0] and L2[1] < L1[1] :
        return True
    elif L2[1]>L1[1] and L2[1]<L1[0] :
        return True
    elif L1[0] and L1[1] > L2[0] & L1[1] and L1[0] <L2[1] :       # line 1 is a part of line 2
        return True
    else:
        return False


x=[]
y=[]

def get_values_and_keys(d):
    for key, value in d.items():
        x.append(key)
        y.append(value)

inputs = {
  'A': (3,6),
  'B': (1,8),
  'C': (15,11),
  'D': (6,9),
    'F':(-1,8)
}
get_values_and_keys(inputs)


s=[]
i = 0
j = 0
while j< len(y):
    w = []

    if j != i:
        overlap(y[i],y[j])
        if overlap(y[i],y[j]) is True:
            w.append(x[i])
            w.append(x[j])
            a=tuple(w)
            s.append(a)
    j=j+1
    if j==len(y)-1:
        break
while i< len(y):
    m = []
    if i != j:
        overlap(y[i],y[j])
        if overlap(y[i],y[j]) is True:
            m.append(x[i])
            m.append(x[j])
            a=tuple(m)
            s.append(a)
        i = i + 1
        if i == len(y) - 1:
            break







#print(w)
print(s)






