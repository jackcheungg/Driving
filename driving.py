country = input('请问你是哪国人： ')
age = input('请输入你的年龄: ')
age = int(age)
if country == '中国':
    if age >= 18:
        print('可以开车')
    else:
        print('还不能考驾照')
elif country == '美国':
    if age >= 16:
        print('可以开车')
    else:
        print('还不能考驾照·')
else:
    print('只能输入中国或美国')