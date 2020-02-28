
Customers = ['Chansa','Chan','Nosiku','Walter']
points = [200,500,800,900]

platinum = []

for point in zip(Customers,points):
    platinum.append("{},{}".format(*point))
    

print(platinum)





x_coord = [23, 53, 2, -12, 95, 103, 14, -5]

labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]



points = []


for point in zip(labels, x_coord):
    points.append("{}: {}".format(*point))

for point in points:
    print(point)


        
        
