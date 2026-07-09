def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


# tuple return

def return_tuple():
    return (1,2,3,4)

a,b,c,d=return_tuple()
print(a,b,c,d)


# arbitary arguments  *args and **kwargs

# *args used for positional arguments

def arb_fun(greeting,*args):
    for i in args:
        print(greeting,i)
        
arb_fun("Hello","Parag","Rohan")

def total_calc(*numbers):
    total=0
    for i in numbers:
        total+=i
    return total

total1=total_calc(2,4,5,6)
print(total1)
total2=total_calc(2,4,5,5,6,88,65,4,6)
print(total2)


# Finding the maximum value:

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


# **kwargs

def kwargs_fun(**detail):
    print("name=",detail["name"])
    print("age=",detail["age"])
    print("tu full details le=",detail)

kwargs_fun(name="Parag",age=18,loc="Delhi") 

# use of kwargs with dict
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")   