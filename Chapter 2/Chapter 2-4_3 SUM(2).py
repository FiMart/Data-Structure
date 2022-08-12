# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป*** #

array = [int(x) for x in input("Enter Your List : ").split()]

def findThreeSum(number):
        if len(number) < 3:
            return []

        ansArray = []
        number.sort()
        for currentIndex in range(0, len(number)-2):
            if number[currentIndex] > 0:
                continue
                
            if number[currentIndex] == number[currentIndex-1] and currentIndex > 0:
                continue
                
            ptr_first = currentIndex+1
            ptr_second = len(number)-1
            
            while ptr_first < ptr_second:
                sum = number[currentIndex] + number[ptr_first] + number[ptr_second]
                
                if sum == 5:
                    ansArray.append([number[currentIndex], number[ptr_first], number[ptr_second]])        
                if sum <= 5:
                    ptr_first += 1
                    while number[ptr_first] == number[ptr_first-1] and ptr_first < ptr_second:
                        ptr_first += 1
                else:
                    ptr_second -= 1
        return ansArray
    
if(len(findThreeSum(array))==0):
    print("Array Input Length Must More Than " + str(len(array)))
else:
    print(findThreeSum(array))