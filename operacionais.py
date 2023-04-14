options=["Windows","Unix","Linux", "Netware", "Mac", "Other"]
votes=[0,0,0,0,0,0]
total_votes=0
while True:
    vote=int(input("Type a vote:"))
    if vote==0:
        break
    elif vote<1 or vote>6:
        print("Try once again")
    else:
        votes[vote-1]+=1
        total_votes+=1
print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")
for i in range(len(options)):
    percent=votes[i]/total_votes*100
    print(f"{options[i]:<24}{votes[i]:<8}{percent:>5.0f}%")
    
print("-------------------     -----   ---")
print(f"Total                    {total_votes:<8}")
mais_votado = options[votes.index(max(votes))]
percentual_mais_votado = max(votes)/total_votes * 100
print(f"\nO Sistema Operacional mais votado foi o {mais_votado}, com {max(votes)} votos, correspondendo a {percentual_mais_votado:.0f}% dos votos.")
