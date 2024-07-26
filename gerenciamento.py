tasks = []


def add_task(tasks, name_task):
    task = {"tarefa": name_task,
            "complete": False}
    tasks.append(task)
    print(f"Tarefa {name_task} foi adicionada com sucesso!")
    return

def see_task(tasks):
    print("\n Lista de tasks: ")
    for indice, tarefa in enumerate(tasks, start=1):
        status = "X" if tarefa["complete"] else " "
        name_task = tarefa ["tarefa"]
        print(f"{indice}. [{status}] {name_task}")
    return

def update_task():
    pass

def update_name_task(tasks, indice_task, new_name_task):
    indice_task_ajustado = int(indice_task) - 1
    if indice_task_ajustado >= 0 and indice_task_ajustado < len(tasks):
        tasks[indice_task_ajustado] ["tarefa"] = new_name_task
        print(f"Tarefa {indice_task} atualizado para {new_name_task}")
    else:
        print("indice inválido")
    return

def complete_task(tasks, indice_task):
    indice_task_ajustado = int(indice_task) - 1
    tasks [indice_task_ajustado] ["complete"] = True
    print(f"task {indice_task} marcada como completada")
    return

def task_complete(tasks):
    for tarefa in tasks:
        if tarefa ["complete"]:
            tasks.remove(tarefa)
    print("Tarefas completadas foram deletadas!!")   
    return

def menu():
    print("-------------------Menu-------------------")
    print("1. Adicionar task\n" +
    "2. Ver task\n" +
    "3. Atualizar task\n" +
    "4. Completar tasks\n"+
    "5. Deletar tasks completadadas\n" +
    "6. Sair\n")
    return

while True:

    menu()

    choice = int(input("Qual item vc deseja?\n"))    

    match choice:
        case 1:
            name_task = input("Digite o nome da atividade: ")
            add_task(tasks, name_task)
        case 2:
            see_task(tasks)
        case 3:
            see_task(tasks)
            indice_task = input("Digite o número da task que deseja atualizar: ")
            new_name_task = input("Digite o novo nome da task: ")
            update_name_task(tasks, indice_task, new_name_task)
        case 4:
            see_task(tasks)
            indice_task = input("Digite o número da tarefa que deseja completar: ")
            complete_task(tasks, indice_task)
        case 5:
            task_complete(tasks)
            see_task(tasks)

        case 6:
            break
    
print("\nProg finalizado")






