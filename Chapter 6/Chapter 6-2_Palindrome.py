# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

def palindrome(a):
    if len(a) < 1:
        return 1
    else:
        if a[0] == a[-1]:
            return palindrome(a[1:-1])
        else:
            return 0
        
s = str(input("Enter Input : "))

if(palindrome(s) == 1):
    print("'{}' is palindrome".format(s))
else:
    print("'{}' is not palindrome".format(s))