a = []
b = a
# a and b are same names for same object

print(id(a), id(b), sep="\n")


a = 7894
b = 7894
# same name for same values for optimization
print(id(a), id(b), sep="\n")

a = 7895
# id of a now changes
print(id(a), id(b), sep="\n")