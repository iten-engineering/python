
names = ["Lea", "Anna", "Sam"]
ages  = [12, None, 18]
vips  = [True, False, False]

infos = [ 
    {"age":12, "city":"Bern"}, 
    {"age":None, "city":"Luzern"}, 
    {"age":18, "city":"Lausanne"}, 
]


for name, age, vip in zip(names, ages, vips):
    print(name, age, vip)

for t in zip(names, ages, vips):
    print(t)    


for name, info in zip(names, infos):
    print(name)
    print(info)