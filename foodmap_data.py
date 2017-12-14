import random
import datetime


food = ["Pizza", "Ice Cream", "Subs", "Doughnuts", "Coffee", "Fruit/Veggies"]
building = ["George Eastman Hall", "Campus Center", "Student Alumni Union", "Liberal Arts Hall", "James E. Booth Hall", "Frank E. Gannett Hall", "Thomas Gosnell Hall", "James E. Gleason Hall", "Lewis P. Ross Hall", "Max Lowenthal Hall", "Orange Hall", "Monroe Hall", "Engineering Hall", "Gordon Field House and Activities Center", "Grace Watson Hall", "Sustainability Institute", "Golisano Hall"]

lat_min = 43.08086111
lat_max = 43.08813889
lng_min =  -77.66583333
lng_max = -77.68500000
coordinates = (random.uniform(lat_min, lat_max), random.uniform(lng_min, lng_max))

data = []
index = 0

for f in food:
    data.append({"food" : random.choice(food), "building" : random.choice(building), "time" : datetime.datetime.now(), "coordinates" : coordinates})

f = open("fooddata.json", "w")
f.write(str(data))
f.close()