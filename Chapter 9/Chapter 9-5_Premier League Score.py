# สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# [ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

# ตัวอย่าง

# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68

def premierleagueScore(data):
    tab = []
    for team in data:
        tmp = []
        team = team.split(',')
        score = int(team[1]) * 3 + int(team[3])
        gd = int(team[4]) - int(team[5])
        tmp += [team[0],score,gd]
        tab.append(tmp)
    for i in range(1,len(tab)):
        tmp = tab[i]
        for k in range(i,-1,-1):
            if tmp[1] > tab[k - 1][1] and k > 0:
                tab[k] = tab[k - 1]
            elif tmp[1] == tab[k - 1][1] and k > 0:
                if tmp[2] > tab[k - 1][2]:
                    tab[k] = tab[k - 1]
                else:
                    tab[k] = tmp
                    break
            else:
                tab[k] = tmp
                break
    return tab

inp = input('Enter Input : ').split('/')
premierleagueScore = premierleagueScore(inp)
print('== results ==')
for data in premierleagueScore:
    print(f"['{data[0]}', " + "{'points': " + f"{data[1]}" + "}, {" + f"'gd': {data[2]}" + "}]")
