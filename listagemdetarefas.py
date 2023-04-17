import os
def listagem(tarefas):
    if not tarefas:
        print("Sem tarefas")
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
def desfazer(tarefas, tarefas_ref):
    print()
    if not tarefas:
        print('Sem tarefas para desfazer')
        return
    tarefa=tarefas.pop()
    print(f'{tarefas=} removida da lista.')
    tarefas_ref.append(tarefa)
    print()
def ref(tarefas,tarefas_ref):
    print()
    if not tarefas_ref:
        print('Sem tarefas')
        return
    tarefa=tarefas_ref.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
def add(tarefa,tarefas):
    tarefa=tarefa.strip()
    if not tarefa:
        print('Cade a merda da tarefa cacete ?')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
tarefas=[]
tarefas_ref=[]
while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa=='listagem':
        listagem(tarefas)
        continue
    elif tarefas=='desfazer':
        desfazer(tarefas,tarefas_ref)
        listagem(tarefas)
        continue
    elif tarefa=='ref':
        ref(tarefas,tarefas_ref)
        listagem(tarefas)
        continue
    elif tarefa=='clear':
        os.system('clear')
        continue
    else:
        add(tarefa,tarefas)
        listagem(tarefas)
        continue

