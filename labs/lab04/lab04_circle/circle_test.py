from circle import Circle

def test_small():
	c = Circle(3)
	assert(round(c.circumference(), 1) == 18.8)
	assert(round(c.area(), 1) == 28.3)

def test_big():
	c = Circle(18)
	assert(round(c.circumference(), 1) == 113.1)
	assert(round(c.area(), 1) == 1017.9)

def test_float():
	c = Circle(3.14)
	assert(round(c.circumference(), 1) == 19.7)
	assert(round(c.area(), 1) == 31.0)