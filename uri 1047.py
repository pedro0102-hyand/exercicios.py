h_inicial,h_final,m_inicial,m_final=map(int,input().split())
total=(h_final*60 +m_final)-(h_inicial*60 +m_inicial)
if total<0:
    total+=24*60
horas=total//60
minutos=total%60
print(f"O jogo durou {horas} horas e {minutos} minutos")
