import json

with open("身份证前六位对应的省市区.json", "r", encoding='UTF-8') as file:
    data = json.load(file)
    six = input("请输入身份证前6位：")
    for i in data.keys():
        if i.__contains__(six[0:2] + "0000"):
            for j in data[i].keys():
                if j.__contains__(six[0:4] + "00"):
                    for k, v in (data[i][j]).items():
                        if v == six:
                            print(i.split(":")[0] + j.split(":")[0] + k)
                            break
                    break
            break
