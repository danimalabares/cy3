def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

#print(len(list(powerset([1,2,3,4, 5, 6,7,8]))))

Delta8=list(powerset([1,2,3,4,5,6,7,8]))#The power set of {1,...,8}
poly1=[[1,2,4,5],[1,2,3,4],[1,2,3,7],[1,3,4,5],[1,3,5,6],[1,2,6,7],[1,3,6,7],[2,3,6,7],[2,3,4,5],[2,3,5,8],[1,2,5,8],[1,2,6,8],[1,5,6,8],[2,5,6,8]]

#Now lets put the whole polytope in a list: it must contain all the subsets of elements in poly1
pol=[]
print(pol)
for element in poly1:
    for element2 in list(powerset(element)):
                pol.append(element2)

#Now lets compute the complement of the polytope in the power set of {1,...,8}
compl=[]
for element in Delta8:
    if element not in pol:
        compl.append(element)

#print(compl)

#Now let's produce a nice output to put it in other programs

# Generate the list of strings for GAP
#result_strings = ['*'.join(f'r.{num}' for num in sublist) for sublist in compl]

# Generate the list of strings for gfan
result_strings = ['*'.join(f'x{num}' for num in sublist) for sublist in compl]

# Print the formatted output for GAP
'''
print("monomials := [")
for monomial in result_strings:
            print(f'    {monomial.replace("*", " * ")},')
print("];")
'''

#Pring the formatted output for gfan
print("{")
for monomial in result_strings:
    print(f'    {monomial.replace("*", "")},')
print("}")

print(len(result_strings))
