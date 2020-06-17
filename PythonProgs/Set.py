s = set()
# print(type(s))
#
# l = [1,2,3,4,5,6]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(2)
s.remove(2)
print(s)
s1 = s.union({1,2,3})
s2 = s.intersection({1,2,3,4,5})
s3 = {4,6}
s4 = s.isdisjoint(s3)

print(s,s1,s2)
print(len(s))
print(max(s))
print(min(s))
print(s4)


