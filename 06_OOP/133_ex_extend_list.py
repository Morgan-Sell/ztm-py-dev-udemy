# Exercise: Extending List

# SuperList() inherits from list object.

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
super_list1.append('m')
super_list1.append(3)

print(super_list1)
print(len(super_list1))
print(super_list1[1])
print(issubclass(SuperList, list))