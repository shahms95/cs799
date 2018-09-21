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

	def setStartPoint(self, a):
		self.start = a

	def setEndPoint(self, a):
		self.end = a

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

def distance(a,b):
	return np.sqrt(np.sum(np.square((a-b).getCoords())))


def movePoint(point, delta, vec):
	coords = vec.getCoords()
	coords = delta*coords
	p = Point()
	p.setCoords(coords)
	return point+p

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
# print(distance(laser,obj1))


eps = 1e-6

delta = 1e-2

p = obj2.getStart()

diff = obj2.getEnd()-obj2.getStart()


# print(obj2.getStart().getCoords())
# print(obj2.getEnd().getCoords())
# print(diff.getCoords())


time=0

count = 2
wallPoints = np.asarray([Point() for x in xrange(count*count)])

counter = -((count**2)/2)

# init point coordinates of wallpoints being observed
for point in wallPoints:
	# point.set(counter/count, counter%count)
	point.set(counter, 10)
	print(counter, point.getCoords())
	counter = counter + 1

# while distance(p,obj2.getEnd()) > eps:
# 	print(time,distance(p,pointSeen))
# 	time=time+1

# 	p = movePoint(p,delta,diff)

totalTime=3
deltaTime=1

obj = Segment()
obj.setStart(8,5)
obj.setEnd(9,5)

speed = Point()
speed.set(0,0)

def moveSegment(obj,speed):
	obj.setStartPoint(obj.getStart() + speed)
	obj.setEndPoint(obj.getEnd() + speed)

delta= 0.1

# outer loop (time) is only useful for moving objects
for time in range(0,totalTime,deltaTime):
	print("time",time)
	# scanning the wall, one raster point at an instant
	for wp in wallPoints:
		print("wp",wp.getCoords())
		pLit  = wp
		pSeen = wp
		p = obj.getStart()
		diff = obj.getEnd()-obj.getStart()
		while distance(p,obj.getEnd()) > eps:
			print("hidden point observed", p.getCoords())
			print("peak in time intensity curve at ", distance(pSeen,p))
			p = movePoint(p,delta,diff)	
	moveSegment(obj,speed)