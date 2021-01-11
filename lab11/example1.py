class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  def getradius(self):
    return self._radius
  def getheight(self):
    return self._height
cylinder = Cylinder(15,20) 
def calculator(r,radius,height):
  base_area = 3.14*cylinder.getradius()**2
  surface_area =2*3,14*cylinder.getradius()*cylinder.getheight()
  print(base_area,surface_area)

calculator(r,radius,height)