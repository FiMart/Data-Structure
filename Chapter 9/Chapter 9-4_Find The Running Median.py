# # เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

# # ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# l = [e for e in input("Enter Input :" ).split()]
# if l[0] == 'EX':
#     Ans == "xxx"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
#     l=list(map(int, l))
#     #code here
    
# ***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

# พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

# - bubble sort

# - straight selection sort

# - insertion sort

# - shell sort

# - merge sort

# - quick sort

# - minHeap and maxHeap

# พิมพ์คำตอบลงในช่อง Ans = "xxx"

# ***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***

def bubbleSort(l:list) -> list:
    if len(l) <= 1:
        return l
    if len(l) == 2:
        return l if l[0] < l[1] else [l[1], l[0]]
    x,y = l[0], l[1]
    bs = l[2:]
    array = []
    if x < y:
        array = [x] + bubbleSort([y] + bs)
    else:
        array = [y] + bubbleSort([x] + bs)
    return bubbleSort(array[:-1]) + array[-1:]

def meDian(l:list) -> float:
    l = bubbleSort(l)
    index = int(len(l)/2)
    if len(l) % 2 != 0:
        return l[index]
    return (l[index]+l[index-1])/2

def run_list(l:list) -> None:
    for i in range(1,len(l)+1):
        print(f"list = {l[:i]} : median = {meDian(l[:i]):.1f}")

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "bubble sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+ Ans)
else:
    l = list(map(int,l))
    run_list(l)