# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True, end="\n")
print(False and True and True, end="\n")
print(True or False or False, end="\n")
print(False and False and False, end="\n")
print(True or True or True, end="\n")
print(False or False or False, end="\n")
print(not True and True, end="\n")
print(False and False, end="\n")
print(not False and False, end="\n")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #usar parenteses
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
