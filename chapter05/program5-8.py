# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# Calculate the area of a triangle given its vertices
import math

def get_vertex():
    x = float(input("    Please enter x: "))
    y = float(input("    Please enter y: "))
    return x,y

def get_triangle():
    print("First vertex")
    x1,y1 = get_vertex()
    print("Second vertex")
    x2,y2 = get_vertex()
    print("Third vertex")
    x3,y3 = get_vertex() 
    return x1, y1, x2, y2, x3, y3
    
def side_length(x1,y1,x2,y2):
    '''return length of a side (Euclidean distance)'''
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
def calculate_area(x1,y1,x2,y2,x3,y3):
    '''return area using Heron's forumula'''
    a = side_length(x1,y1,x2,y2)
    b = side_length(x2,y2,x3,y3)
    c = side_length(x3,y3,x1,y1)
    s = (1/2)*(a + b + c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
x1, y1, x2, y2, x3, y3 = get_triangle()
area = calculate_area(x1,y1,x2,y2,x3,y3)
print("Area is",area)

    
    
    
