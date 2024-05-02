saldo = 200
saque = 200
cheque_especial = -500
saldo_cheque_especial = saldo + cheque_especial
print(saldo_cheque_especial)
valores_a_receber =+ (-1)*(saldo_cheque_especial)
print(valores_a_receber)

saldo += 200 #saldo = saldo + 200
print(saldo, end="\n")
saldo -= 200 #saldo = saldo - 200
print(saldo, end="\n")
saldo /= 200 #saldo = saldo / 200
print(saldo, end="\n")
saldo //= 200 #saldo = saldo / 200
print(saldo, end="\n")
saldo %= 200
print(saldo, end="\n")
saldo **=200
print(saldo, end="\n")

print(saldo == saque) #igual a, retorno bool(True and False)
print(saldo != saque) #diferente de 
print(saldo > saque) #maior
print(saldo >= saque) #maior or igual
print(saldo < saque) # menor
print(saldo <= saque) #menor or igual
print(saldo < valores_a_receber)
print(saldo)
print(valores_a_receber,end="$R")
