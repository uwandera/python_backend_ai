from datetime import datetime, timedelta, date

tipo_carro = "p"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 59
data_atual = datetime.now()

if tipo_carro == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")
elif tipo_carro == "m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")



print(date.today() - timedelta(days=1) )

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())