setA={1,2,3,4,5}
setB={3,4,5,6,7}

a_butnot_b=setA.difference(setB)
print(a_butnot_b)

b_butnot_a=setB.difference(setA)
print(b_butnot_a)

symmetric_difference=setA.symmetric_difference(setB)
print(symmetric_difference)

# intersection
intersection_sets=setA.intersection(setB)
print(intersection_sets)


# union
union_sets=setA.union(setB)
print(union_sets)
