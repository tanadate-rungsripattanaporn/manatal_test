from random import choice
box=[i for i in range(1,51)] #50 balls
pick=[]
for _ in range(10):
    select=choice(box)
    box.remove(select)
    pick.append(select)
pick.sort()
print('all picked balls is',pick,'total=',len(pick))
print('all left balls in box',box,'total=',len(box))