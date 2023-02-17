# Chapter : 1 - item : 1 - Rabbit & Turtle & Fly

# #    เริ่มต้นกระต่ายวิ่งอยู่หน้าเต่าเป็นระยะ d เมตร กระต่ายวิ่งด้วยความเร็วคงที่ Vr เมตรต่อวินาที และเต่าวิ่งด้วยความเร็วคงที่ Vt เมตรต่อวินาที ซึ่งนิทานเรื่องนี้เต่าจะวิ่งเร็วกว่ากระต่ายเสมอ แมลงวันตัวหนึ่งอยู่บนหัวเต่าบินด้วยควมเร็วคงที่ Vf เมตรต่อวินาที เมื่อแมลงวันบินไปจนถึงกระต่ายแล้วมันก็จะบินย้อนกลับไปหาเต่าด้วยความเร็วเท่าเดิม แมลงวันจะบินกลับไปกลับมาระหว่างกระต่ายและเต่าจนกว่าเต่าจะวิ่งมาทันกระต่ายพอดี (เต่าจะต้องวิ่งมาทันกระต่ายเพราะเต่าวิ่งด้วยความเร็วมากกว่ากระต่าย) 

# #     จงเขียนโปรแกรมเพื่อหาว่าแมลงวันจะบินได้เป็นระยะทางทั้งสิ้นกี่เมตร เต่าจึงจะวิ่งทันกระต่ายพอดี ในข้อนี้ให้ถือว่าทั้งกระต่ายและเต่า และ แมลงวันเคลื่อนที่โดยไม่มีความเร่งเสมอ

# # ข้อมูลนำเข้า

# # บรรทัดเดียว จำนวนเต็มบวก d Vr Vt และ Vf ตามลำดับห่างกันด้วยเว้นวรรคหนึ่งช่อง โดยตัวเลขทุกตัวเลขทุกตัวจะไม่เกิน 5000 และ Vt > Vr และแมลงวันบินด้วยความเร็วสูงกว่าเต่าและกระต่ายเสมอ

# # ข้อมูลส่งออก

# # บรรทัดเดียว ระยะทางของแมลงวันที่บินได้ทั้งหมด โดยให้ตอบเป็นทศนิยม 2 ตำแหน่ง

# # *** ห้ามใช้ For / While Loop ***



# # Hint : S = VT

print("*** Rabbit & Turtle ***")
d,vr,vt,vf = input('Enter Input : ').split()
a = int(vf)/(int(vt)-int(vr))*int(d)
print('%.2f' %a)
