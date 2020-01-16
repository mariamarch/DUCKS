utk_bot = 55/3
import math


class Road:
    def __init__(self,x1,y1,seg,sign):
        self.b_cord = x1,y1
        self.R1=None
        self.R2=None
        coordinates = self.b_cord
        x, y = coordinates
        x_s, y_s = (x, y)
        sign = sign
        sequence = seg
        self.segments = list()
        # segmentum
        for segmentum in sequence:
            if segmentum == 'v':
                curr_segm = Vert_road((x_s, y_s))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
            if segmentum == 'h':
                curr_segm = Horizontal_road((x_s, y_s))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
            if segmentum[:-1] == 'turnrd':
                if segmentum[-1] == 'm':
                    r1 = 0
                    r2 = 1.5
                elif segmentum[-1] == 'b':
                    r1 = 1.5
                    r2 = 3
                curr_segm = circle_road_right_down((x_s, y_s, r1, r2))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
            if segmentum[:-1] == 'turnru':
                if segmentum[-1] == 'm':
                    r1 = 0
                    r2 = 1.5
                else:
                    r1 = 1.5
                    r2 = 3
                curr_segm = circle_road_right_upper((x_s, y_s, r1, r2))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
            if segmentum[:-1] == 'turnld':
                if segmentum[-1] == 'm':
                    r1 = 0
                    r2 = 1.5
                else:
                    r1 = 1.5
                    r2 = 3
                curr_segm = circle_road_left_down((x_s, y_s, r1, r2))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
            if segmentum[:-1] == 'turnlu':
                if segmentum[-1] == 'm':
                    r1 = 0
                    r2 = 1.5
                else:
                    r1 = 1.5
                    r2 = 3
                curr_segm = circle_road_left_upper((x_s, y_s, r1, r2))
                self.segments.append(curr_segm)
                x_s, y_s, sign = curr_segm.cord_next(sign)
    def is_on_road(self,x,y):
        is_on_road_v = False
        for segmentum in self.sequence:
            if segmentum.is_in_phragment(x,y):
                is_on_road_v = True
        return is_on_road_v

class Vert_road:
    def __init__(self,cord_b):
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
    def __init__(self,cord_b):
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
    def __init__(self,cord_b):
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
    def __init__(self,cord_b):
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
    def __init__(self,cord_b):
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
    def __init__(self,cord_b):
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


segm = ['v','turnldb','h','h','h','turnrdb','v']
R1 = Road(0*utk_bot,6*utk_bot,segm,'-')
segm = ['v','turnldm','h','h','h','turnrdm','v']
r1 = Road(1.5*utk_bot,6*utk_bot,segm,'-')
segm = ['v','turnrub','h']
R2 = Road(9*utk_bot,15*utk_bot,segm,'+')
segm = ['v','turnrum','h']
r2 = Road(9*utk_bot,13.5*utk_bot,segm,'+')
segm = ['h']
R3 = Road(9*utk_bot,9*utk_bot,segm,'+')
r3 = Road(9*utk_bot,7.5*utk_bot,segm,'+')
segm = ['v','turnlub','h']
R4 = Road(0*utk_bot,9*utk_bot,segm,'+')
segm = ['v','turnlum','h']
r4 = Road(1.5*utk_bot,9*utk_bot,segm,'+')
segm = ['v']
R5 = Road(6*utk_bot,12*utk_bot,segm,'-')
r5 = Road(7.5*utk_bot,12*utk_bot,segm,'-')
segm = ['h']
R6 = Road(3*utk_bot,9*utk_bot,segm,'+')
r6 = Road(3*utk_bot,7.5*utk_bot,segm,'+')
R1.Road1 = R2
R1.Road2 = R3
R2.Road1 = R4
R2.Road2 = R5
R3.Road1 = r5
R3.Road2 = R6
R4.Road1 = R1
R4.Road2 = r6
R5.Road1 = R6
R5.Road2 = r3
R6.Road1 = r4
R6.Road2 = R1
r1.Road1 = r6
r1.Road2 = r4
r2.Road1 = R3
r2.Road2 = r1
r3.Road1 = r1
r3.Road2 = R2
r4.Road1 = R5
r4.Road2 = r2
r5.Road1 = r2
r5.Road2 = R4
r6.Road1 = r3
r6.Road2 = r5

print(r2.segments)



#rr1 = Road()
#rr2 = Road()
#rr1.road1 = rr2
#rr2.road1 = rr1


