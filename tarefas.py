tarefas = []

def add_tarefa(nome, descricao, prioridade, categoria, concluido):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluido': concluido
    }
    tarefas.append(tarefa)

def criar_tarefa():
    nome=input("Nome da Tarefa: ")
    descricao=input("Descrição da tarefa: ")
    prioridade=int(input("Nível de prioridade de 1-10: "))
    categoria=input("Categoria: ")
    concluido=input("Concluido? sim/não: ").strip().lower() == 'sim'
   
    add_tarefa(nome, descricao, prioridade, categoria, concluido)

def lista_tarefas():
    if not tarefas:
        print("Não há tarefas")
        return
    
    print('\nTodas as tarefas: ')
    for index, tarefa in enumerate(tarefas, start=1):
        concluido = "Concluida" if tarefa['concluido'] else "Pendente"
        print(f"\nTarefa {index}: ")
        print(f"Nome: {tarefa['nome']}")
        print(f"Status: {concluido}")

   
 
def opcoes ():
    while True:
        print('\nOpções')
        print('1- Nova Tarefa')
        print('2- Lista De Tarefas')
        print('3- Sair')
       
        escolhido=input('Escolha uma opção: \n')
       
        if escolhido == '1':
            criar_tarefa()
        elif escolhido == '2':
            lista_tarefas()
        elif escolhido == '3':
            break
        else:
            print('Opção invalida')
           
if __name__ == "__main__":
    opcoes()