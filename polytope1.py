def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

#print(len(list(powerset([1,2,3,4, 5, 6,7,8]))))

Delta8=list(powerset([1,2,3,4,5,6,7,8]))
poly1=[[1,2,4,5],[1,2,3,4],[1,2,3,7],[1,3,4,5],[1,3,5,6],[1,2,6,7],[1,3,6,7],[2,3,6,7],[2,3,4,5],[2,3,5,8],[1,2,5,8],[1,2,6,8],[1,5,6,8],[2,5,6,8]]

compl=[]
for element in Delta8:
    if element not in poly1:
        compl.append(element)

print(compl)
