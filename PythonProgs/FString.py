# F String

import math

me = "Parin"
a1 = 3
# a = "This is %s" %(me,a1)
# a = "This is {1} {0}"
# a.format(me, a1)
# print(a)

a = f"this is {me} {a1} {4*65} {math.cos(65)}" # f means fast string
print(a)