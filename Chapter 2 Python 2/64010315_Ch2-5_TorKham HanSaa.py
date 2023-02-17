# Chapter : 2 - item : 5 - ต่อคำหรรษา

# # ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
# # 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# # จะไม่สามารถพูดว่า “Apple” ได้อีก


# # 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# # ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# # แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


# # 3. Ignore Case Sensitive


# # โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# # - P < word > จะเป็นการต่อคำ
# # - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# # - X เป็นการระบุว่าจบการทำงาน


# # โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุดคือ

class TorKham:
    def __init__(self) -> None:
        self.wordlst = []
    def next(self,word):
        if self.wordlst == []:
            self.wordlst.append(word)
            print('\''+str(word)+'\' ->',self.wordlst)
        else:
            if self.wordlst[len(self.wordlst)-1][-1].casefold()==word[1].casefold() and self.wordlst[len(self.wordlst)-1][-2].casefold()==word[0].casefold():
                self.wordlst.append(word)
                print('\''+str(word)+'\' ->',self.wordlst)
            else:
                print('\''+str(word)+'\' -> game over')
    def restart(self):
        self.wordlst = []
        print("game restarted")
        
print("*** TorKham HanSaa ***")
x = list(map(str,input("Enter Input : ").split(",")))
TorKham = TorKham()

for i in x:
    word = i.split()
    if word[0] == 'P':
        TorKham.next(word[1])
    elif word[0] == 'R':
        TorKham.restart()
    elif word[0] == 'X':
        exit()
    else:
        print('\''+' '.join(word)+'\' is Invalid Input !!!')
        break


        