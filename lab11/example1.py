class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  def get_radius(self):
    return self.radius
  def set_radius(self,radius):
    self.radius = radius
  def get_height(self):
    return self.height
  def set_height(self,height):
    self.height = height
  def base_area(self,radius):
    base_area = 3.14 * self.radius ** 2
  def surface_area(self,radius,height):
    surface_area =2* 3,14 * self.radius* self.height

    
cylinder = Cylinder(radius = 15, height = 20) 

print(cylinder.get_radius())