
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
# we get TRUE because is list sublist of SuperList - yes, so its TRUE!
print(issubclass(SuperList, list))
