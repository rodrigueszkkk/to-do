lista = { #criar um dicionrio de lista de tarefas
    'id': '1',
    'titulo': 'Fazer essa lista',
    'concluida': False
}

tarefas = [] #criar a lista onde ficara armazenada

proximo_id = 1 #somador

def adicionar_tarefa(titulo, descricao=''): ## deixa descricao como opcional
    global proximo_id #puxa a variavel de fora quando global
    nova_tarefa = {
        'id': proximo_id,
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(nova_tarefa) #add na lista
    proximo_id += 1 #aumentar o contador

    print(f'Tarefa adicionada: {titulo}')
    


def listar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada')
    else:
        print("\n--- SUAS TAREFAS ---")
        for task in tarefas: #para cada task em tarefa, printa a task
            print(f'ID: {task['id']}')
            print(f'Titulo: {task['titulo']}')
            if task['descricao']:
                print(f'Descrição: {task['descricao']}')
            if task['concluida'] == True:
                print('Status: Concluida')
            else:
                print('Status: Pendente')
            print('--------------------\n')


def marcar_tarefa_concluida(id_tarefa):
    encontrada = False #reseta o valor

    for task in tarefas:                
        if task['id'] == id_tarefa: # == comparaçao verifica se id q está é o mesmo fornecido
            task['concluida'] = True # = atribuição
            print(f'Tarefa: {task['titulo']}, (ID: {task['id']})  foi concluida')
            encontrada = True #redefine a função
            break #quebra o loop

    if not encontrada:
        print(f'ERROR: Tarefa com ID {task['id']} não encontrada.')
                

def remover_tarefa(id_tarefa):
    encontrada = False

    for task in tarefas:
        if task['id'] == id_tarefa:
            print(f'Tarefa: {task['titulo']} (ID {task['id']}) removida com suceso')
            tarefas.remove(task)
            encontrada = True
            break
    
    if not encontrada:
         print(f'Tarefa com ID {id_tarefa} não encontrada')

def exibir_menu():
    print('''
            --- MENU DA TO-DO LIST ---
            1. Adicionar Tarefa
            2. Listar Tarefas
            3. Marcar Tarefa como Concluída
            4. Remover Tarefa
            5. Sair
            --------------------------
          ''')

def main():
    while True:
        exibir_menu()
        opcao = int(input('Digite a opcao desejada'))
        if opcao == 1:
            adicionar_tarefa(titulo=str, descricao='')
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            marcar_tarefa_concluida(id_tarefa=int)
        elif opcao == 4:
            remover_tarefa(id_tarefa=int)
        elif opcao == 5:
            print('Saindo')
        else :
            print('Opcao invalidada')
            



adicionar_tarefa('Estudar Python', 'Revisar listas e dicionários')
adicionar_tarefa('Fazer compras', 'Comprar frutas e verduras')
adicionar_tarefa('pagar contar')

print("\n--- Marcando tarefas ---")
marcar_tarefa_concluida(1) # Tente marcar a primeira tarefa
marcar_tarefa_concluida(99) # Tente marcar uma tarefa que não existe

print("\n--- Removendo tarefas ---")
remover_tarefa(2) # Tente remover a tarefa com ID 2
remover_tarefa(99) # Tente remover uma tarefa que não existe

print("\n--- Lista de tarefas após marcar ---")

listar_tarefas()
