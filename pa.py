empty_list=[]
empty_list.append("apple")
empty_list.append("banana")
print(empty_list)

empty_list.remove("banana")
print(empty_list)

for fruit in (empty_list):
    print(empty_list)


for index, fruit in enumerate(empty_list):
    print(f"Item position: {index} and value: {fruit}")