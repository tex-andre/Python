import datetime

agora = datetime.datetime.now()
print(agora.year)
print(agora.month)
print(agora.day)

print(agora.strftime("%A"))

x = datetime.datetime(2121, 6, 27)
print(x)
print(x.strftime("%B"))