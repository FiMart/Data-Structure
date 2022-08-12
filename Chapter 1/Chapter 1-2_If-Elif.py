# โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

		# Speed (km/h)		ระดับพายุ
			# 0-51.99			Breeze
			# 52.00-55.99		Depression
			# 56.00-101.99	    Tropical Storm
			# 102.00-208.99	    Typhoon
			# >= 209			Super Typhoon

# โดยแสดงผลตามตัวอย่างการแสดงผล

print(" *** Wind classification *** ")
speed = input("Enter wind speed (km/h) : ")

if float(speed) > 0 and float(speed) <= 51.99:
    print("Wind classification is Breeze.")
elif float(speed) >= 52.00 and float(speed) <= 55.99:
    print("Wind classification is Depression.")
elif float(speed) >= 56.00 and float(speed) <= 101.99:
    print("Wind classification is Tropical Storm.")
elif float(speed) >= 102.00 and float(speed) <= 208.99:
    print("Wind classification is Typhoon.")
elif float(speed) >= 209.00:
    print("Wind classification is Super Typhoon.")