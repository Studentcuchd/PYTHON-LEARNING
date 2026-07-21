from collections import OrderedDict
dict_order=OrderedDict()

dict_order["val1"]=5
dict_order["val2"]=6
dict_order["val3"]=1

print(dict_order)


print("\n Moving items \n")

dict_order.move_to_end("val1")

dict_order.move_to_end("val2",last=False)

print(dict_order)

dict_order.popitem()
print(dict_order)