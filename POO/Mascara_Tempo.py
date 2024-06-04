from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"
print(data_hora_atual.strftime(mascara_ptbr)) #formatação de datetime

print() #conversão de string para datahora
data_convertida_en = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida_en) #lembrando que se não houver as informações necessarias para conversão, o erro de tipo acontece