# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# ให้เขียน Recursive หาค่า Min ของ Input

def min(array, number):
    if len(array) == 0:
        return number
    
    if number > array[0]:
        number = array[0]
    array.pop(0)
    
    return min(array, number)

L = list(map(int, input("Enter Input : ").split()))
print("Min : " + str(min(L, L[0])))
        