from homeworks.distance import Distance

d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(500, "cm")


print(d1)
print(d2)
print(d3)

print(d1 + d2)
print(d1 + d3)

print(d2 - d1)
print(d1 - d2)

print(d1 == Distance(1000, "cm"))
print(d1 < d2)

print(d1.convert("km"))