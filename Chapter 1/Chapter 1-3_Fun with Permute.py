# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด #

import math
Answer = []

def n(l):
    P = l.copy()
    Answer.append(P)
    Q = l.copy()
    for j in range(0, len(l)-1):
        q = Q[j]
        Q[j] = Q[j+1]
        Q[j+1] = q
        C = Q.copy()
        Answer.append(C)
        
def set(l):
    temp = l.copy()
    n(temp)
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            q = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = q
            n(temp)
            
        q = temp[1]
        temp[1] = temp[len(l)-1]
        temp[len(l)-1] = q
        if i != len(l)-2:
            n(temp)
            
print("*** Fun with permute ***")
i = [int(j) for j in input("input : ").split(",")]
print(f'Original Cofllection:  {i}')
xx = i[::-1]
set(xx)
print(f'Collection of distinct numbers:\n {Answer}')