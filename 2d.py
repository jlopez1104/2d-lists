#working with 2d lists
#list within a list(2D list)
grades = [[45,37,54],
[62,58,59],
[49,47,60],
[78,83,62]]

print(grades[0])
print(grades[0][1])
print(grades)
#using keys for row

grades2 = {'susan':[45,37,54],
'peter':[62,58,59],
'mark':[49,47,60],
'andy':[78,83,62]}
print(grades2['mark'])
print(grades2['mark'][0])
#more
grades3={'susan':{'ma':45,'en':37,'fr':54},
'peter':{'ma':62,'en':58,'fr':59},
'mark':{'ma':49,'en':47,'fr':60},
'andy':{'ma':78,'en'83,'fr':62}}

print(grades3['peter']["ma'"])