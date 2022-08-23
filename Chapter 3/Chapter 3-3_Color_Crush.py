# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

    # โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย



# class Stack:

    # def __init__(self):

    # def push(self, value):

    # def pop(self):

    # def size(self):

    # def isEmpty(self):



# inp = input('Enter Input : ').split()

# S = Stack()

### Enter Your Code Here ###

# print(S.size())

### Enter Your Code Here ###

class Stack:
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop(len(self.items)-1)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
inp = input('Enter Input : ').split()
S = Stack()
c = ''
counter = 0
combo_counter = 0

for items in inp:
    S.push(items)
    if items == c:
        counter += 1
    else:
        c = items
        counter = 1
    if counter == 3:
        counter = 0
        S.pop()
        S.pop()
        S.pop()
        combo_counter += 1
        if S.size() > 1:
            if S.items[-2] == S.items[-1]:
                c = S.items[-1]
                counter = 2
            else:
                c = S.items[-1]
                counter = 1
        elif S.size() == 1:
            c = S.items[-1]
            counter = 1
            
print(S.size())

if S.size() == 0:
    print('Empty', end='')
else:
    for items in range (S.size()-1, -1, -1):
        print(S.items[items], end='')
if combo_counter > 1:
    print('\nCombo : ' + str(combo_counter) +' ! ! !')
