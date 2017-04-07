planet_list = ["Mercury", "Mars"]

new_planets = ["Jupiter", "Saturn"]
for planet in new_planets:
	planet_list.append(planet)
# print(planet_list)

planet_list.extend(['Uranus','Neptune'])
# print(planet_list)

planet_list.insert(1, 'Earth')
planet_list.insert(1, 'Venus')
planet_list.append('Pluto')
# print(planet_list)

rocky_planets = planet_list[0:4]
# print(rocky_planets)

del planet_list[-1]
# print(planet_list)

spacecraft_and_planets = [
('Ford','Mercury'),
('Chevy','Venus'),
('Honda','Earth'),
('Tesla','Mars'),
('Porsche','Jupiter'),
('Nissan','Saturn'),
('Buick','Uranus'),
('Chrysler','Neptune'),
('Tesla','Pluto')]

for k,v in spacecraft_and_planets:
	print("{} has visited {}".format(k,v))