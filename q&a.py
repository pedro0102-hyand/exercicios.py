questions=[
    {
       'Question': 'What is the result of 8+5?',
       'Options': ['12','13','7'],
       'Answer': '13',
    },
    { 
        'Question': 'How much do you have received?',
        'Options': ['30', '300', '3400'],
        'Answer': '3400',
    },
    {
        'Question':'How old is your dog?',
        'Options': ['7','3', '4'],
        'Answer': '4',
    },
]
acertos=0
for question in questions:
    print('Question:', question['Question'])
    print()
option = question['Option']
for i, option in enumerate(option):
        print(f'{i})', option)
print()
choose=input('Choose an option:')
certo=False
choose_int= None
n_options=len(option)
if choose.isdigit():
      choose_int=int(choose)
if choose_int is not None:
      if choose_int>=0 and choose_int<n_options:
            if option[choose_int]==question['Answer']:
                  certo=True
print()
if certo:
      acertos+=1
      print('Acertou')
else:
      print('Errou')
print()
print('Voce acertou', acertos)
print('de',len(questions),'questions.')
