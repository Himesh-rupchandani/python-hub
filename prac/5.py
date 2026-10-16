name = {
    "maths" : 100,
    "physics" : 56,
    "dc" : 63,
    "ala" : 85,
    "qla" : 96
}

marks = 0
for i in name.values():
    marks += i

print(marks)
print(marks/5)
print((marks/500)*100)