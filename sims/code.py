from vectors import Point, Vector


eps = 1e-6
delta = 1e-2

def distance(a,b):
	return (a-b).magnitude()


laser = Point(0,0,0)
camera = Point(0,0,0)

pointLit = Point(5,5,0)
pointSeen = Point(5,5,0)

obj1 = Point(10,0,0)

print(distance(pointSeen,obj1))
