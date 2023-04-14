import os
def mb(bytes):
    mb=bytes/(1024*1024)
    return round(mb,2)
def uso(bytes,total):
    percent=(bytes/total)*100
    return round(percent,2)
users={}
with open("users.txt", "r") as arquivo:
    for linha in arquivo :
        user=linha[:15].strip()
        utilizado=int(linha[15:].strip())
        users[user]=utilizado
total=sum(users.values())
with open("relatorio.txt","w") as arquivo:
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo.write("------------------------------------------------------------------------\n")
    arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
n_user=1
for user, espaco in sorted(users.item(), key=lambda item:item[1], reverse=true):
    espaco_mb=mb(espaco)
    percentual_uso=uso(espaco,total)
    arquivo.write(f"{n_user:<5}{user:<15}{espaco_mb:>15} MB{percentual_uso:>15}%\n")
    n_user += 1
espaco_total_mb = mb(total)
espaco_medio_mb = mb(total / len(users))
arquivo.write(f"\nEspaço total ocupado: {espaco_total_mb} MB\n")
arquivo.write(f"Espaço médio ocupado: {espaco_medio_mb} MB\n")
