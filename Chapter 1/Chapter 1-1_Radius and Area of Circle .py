# เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล #

import math

def area(radius):
    return math.pi * (radius**2)

radius = float(input("r="))
print("Area=" + str(area(radius)))
