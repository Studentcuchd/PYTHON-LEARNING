dict1_outside={
    "Parag":10,
    "rolf":12
}
def see_det(dict_inside,find):
    print("inside fun 1",id(dict_inside))

    dict_inside[find]=0

    print("inside fun dict_inside=",id(dict_inside["Parag"]))

    print("Inside fun 2",id(dict_inside))


print("before fun call",id(dict1_outside["Parag"]))

see_det(dict1_outside,"Parag")

print("after fun call",id(dict1_outside["Parag"]))

print(id(dict1_outside))



print("\n")
# More example
print("----------------------iadd and add----------")
print("\n")

primes=[2,3,5]
print("Id of prime list=",id(primes))
primes+=[7,11]
print("Id of prime list using iadd=",id(primes))
print(primes)

primes=primes+[7,11]
print("Id of prime list using add=",id(primes))
print(primes)