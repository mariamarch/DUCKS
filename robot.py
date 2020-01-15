utk_bot = 55/3
import math
class Road:
    def _init_(self,x1,y1,seg):
        self.b_cord = x1,y1
        self.len =1
        self.wid =2

class Vert_road:
    def _init_(self,cord_b):
        self.base_x, self.base_y = cord_b
        self.len = 1.5 * utk_bot
        self.wid = 3 * utk_bot
    def is_in_phragment(self,x,y):
        if self.base_x<=x<=self.base_x+self.len and self.base_y<=y<=self.base_y+self.wid:
            return True
        else:
            return False
    def dlina(self):
        return self.wid

class Horizontal_road:
    def _init_(self,cord_b):
        self.base_x, self.base_y = cord_b
        self.len = 1.5 * utk_bot
        self.wid = 3 * utk_bot
    def is_in_phragment(self,x,y):
        if self.base_x<=x<=self.base_x+self.len and self.base_y<=y<=self.base_y+self.wid:
            return True
        else:
            return False
    def dlina(self):
        return self.len

class sqrt_road_right_down:
    def _init_(self,cord_b):
        self.base_x, self.base_y, self.r1, self.r2 = cord_b
        self.len = math.pi / 2 * (self.r1 + self.r2) / 2
    def is_in_phragment(self,x,y):
        ro = ((self.base_x - x) ** 2 + (self.base_y - y) ** 2)
        ro = math.sqrt(ro)
        sin = (self.base_x-x) / ro
        angle = math.asin(sin)
        if 0<=angle<=math.pi/2 and self.r1<=ro<=self.r2:
            return True
        else:
            return False
    def dlina(self):
        return self.len

class sqrt_road_right_upper:
    def _init_(self,cord_b):
        self.base_x, self.base_y, self.r1, self.r2 = cord_b
        self.len = math.pi / 2 * (self.r1 + self.r2) / 2
    def is_in_phragment(self,x,y):
        ro = ((self.base_x - x) ** 2 + (self.base_y - y) ** 2)
        ro = math.sqrt(ro)
        sin = (self.base_x-x) / ro
        angle = math.asin(sin)
        if 0<=angle<=math.pi/2 and self.r1<=ro<=self.r2:
            return True
        else:
            return False
    def dlina(self):
        return self.len


class RoadSector:
    def _init_(self):
        pass
    def is_in_fragment(self, x, y):
        pass
    def length(self):
        pass

rr1 = Road()
rr2 = Road()
rr1.road1 = rr2
rr2.road1 = rr1


#rr1 = Road()
#rr2 = Road()
#rr1.road1 = rr2
#rr2.road1 = rr1


