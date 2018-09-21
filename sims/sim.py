import numpy as np

class Point():
	coords = np.array([0,0])

	def set(self, a,b):
		self.coords = np.array([a,b])

	def __sub__(self, otherPoint):
		x = self.coords[0]-otherPoint.coords[0]
		y = self.coords[1]-otherPoint.coords[1]
		p = Point()
		p.set(x,y)
		return p

	def __add__(self, otherPoint):
		x = self.coords[0]+otherPoint.coords[0]
		y = self.coords[1]+otherPoint.coords[1]
		p = Point()
		p.set(x,y)
		return p

	def getCoords(self):
		return self.coords

	def setCoords(self, coords):
		self.coords = coords


class Segment():
	start = Point()
	end = Point()

	def setStart(self, a,b):
		self.start.set(a,b)

	def setEnd(self, a,b):
		self.end.set(a,b)

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

def distance(a,b):
	return np.sqrt(np.sum(np.square((a-b).getCoords())))


laser = Point()
camera = Point()

pointLit = Point()
pointLit.set(5,5)

pointSeen = pointLit

obj1 = Point()
obj1.set(10,0)


obj2 = Segment()
obj2.setStart(9,5)
obj2.setEnd(11,5)



# print(distance(pointLit,obj1))
print(distance(laser,obj1))


eps = 1e-6

delta = 1e-2

p = obj2.getStart()

diff = obj2.getEnd()-obj2.getStart()


print(obj2.getStart().getCoords())
print(obj2.getEnd().getCoords())
print(diff.getCoords())
i=0


def movePoint(point, delta, vec):
	coords = vec.getCoords()
	coords = delta*coords
	p = Point()
	p.setCoords(coords)
	return point+p

print("done 1")
while distance(p,obj2.getEnd()) > eps:
	print(i,distance(p,pointSeen))
	i=i+1

	p = movePoint(p,delta,diff)