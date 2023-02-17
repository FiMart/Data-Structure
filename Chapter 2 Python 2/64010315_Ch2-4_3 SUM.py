# Chapter : 2 - item : 4 - 3 SUM

# # จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

array = [int(n) for n in input('Enter Your List : ').split(' ')]
if len(array) > 3:
    lst = []
    for a in range(len(array)):
        for b in range(len(array)):
            for c in range(len(array)):
                if array[a] + array[b] + array[c] == 0 and array[a] <= array[b] and array[b] <= array[c] and a != b != c:
                    lst.append([array[a], array[b], array[c]])
    for i in range(len(lst) - 1, 0, -1):
        if lst[0] == lst[i]:
            lst.remove(lst[i])
    print(lst)

else:
    print('Array Input Length Must More Than ' + str(len(array)))

