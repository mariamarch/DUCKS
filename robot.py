utk_bot = 55/3
import math
class Road:
    def _init_(self,x1,y1,seg):
        self.b_cord = x1,y1

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
    def cord_next(self,sign):
        self.sign = sign
        if sign == '+':
            self.next_x = self.base_x
            self.next_y = self.base_y + self.wid
        elif sign == '-':
            self.next_x = self.base_x
            self.next_y = self.base_y - self.wid
        return (self.next_x, self.next_y,self.sign)
    
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
    def cord_next(self,sign):
        self.sign = sign
        if sign == '+':
            self.next_x = self.base_x+self.wid
            self.next_y = self.base_y
        elif sign == '-':
            self.next_x = self.base_x-self.wid
            self.next_y = self.base_y
        return (self.next_x, self.next_y,self.sign)

class circle_road_right_down:
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
    def cord_next(self,sign):
        self.sign='+'
        self.next_x=self.base_x+self.r1
        self.next_y=self.base_y+self.r1
        return(self.next_x,self.next_y,self.sign)

class circle_road_right_upper:
    def _init_(self,cord_b):
        self.base_x, self.base_y, self.r1, self.r2 = cord_b
        self.len = math.pi / 2 * (self.r1 + self.r2) / 2
    def is_in_phragment(self,x,y):
        ro = ((self.base_x - x) ** 2 + (self.base_y - y) ** 2)
        ro = math.sqrt(ro)
        sin = (self.base_x-x) / ro
        angle = math.asin(sin)
        if math.pi/2<=angle<=math.pi and self.r1<=ro<=self.r2:
            return True
        else:
            return False
    def dlina(self):
        return self.len
    def cord_next(self,sign):
        self.sign = '-'
        self.next_x = self.base_x + self.r1
        self.next_y = self.base_y - self.r1
        return (self.next_x, self.next_y, self.sign)



class circle_road_left_upper:
    def _init_(self,cord_b):
        self.base_x, self.base_y, self.r1, self.r2 = cord_b
        self.len = math.pi / 2 * (self.r1 + self.r2) / 2
    def is_in_phragment(self,x,y):
        ro = ((self.base_x - x) ** 2 + (self.base_y - y) ** 2)
        ro = math.sqrt(ro)
        sin = (self.base_x-x) / ro
        angle = math.asin(sin)
        if math.pi<=angle<=math.pi*3/2 and self.r1<=ro<=self.r2:
            return True
        else:
            return False
    def dlina(self):
        return self.len
    def cord_next(self,sign):
        self.sign = '+'
        self.next_x = self.base_x - self.r1
        self.next_y = self.base_y - self.r1
        return (self.next_x, self.next_y,self.sign)

class circle_road_left_down:
    def _init_(self,cord_b):
        self.base_x, self.base_y, self.r1, self.r2 = cord_b
        self.len = math.pi / 2 * (self.r1 + self.r2) / 2
    def is_in_phragment(self,x,y):
        ro = ((self.base_x - x) ** 2 + (self.base_y - y) ** 2)
        ro = math.sqrt(ro)
        sin = (self.base_x-x) / ro
        angle = math.asin(sin)
        if math.pi*3/2<=angle<=math.pi*2 and self.r1<=ro<=self.r2:
            return True
        else:
            return False
    def dlina(self):
        return self.len
    def cord_next(self,sign):
        self.sign = '+'
        self.next_x = self.base_x + self.r1
        self.next_y = self.base_y - self.r1
        return (self.next_x, self.next_y,self.sign)



rr1 = Road()
rr2 = Road()
rr1.road1 = rr2
rr2.road1 = rr1


#rr1 = Road()
#rr2 = Road()
#rr1.road1 = rr2
#rr2.road1 = rr1


