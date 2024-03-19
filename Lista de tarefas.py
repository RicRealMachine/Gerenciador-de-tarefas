#Lista de tarefas
from modelos.tarefas import Tarefa


lista_de_tarefas = []


def menu() :
  
   print(25*'*') 
   print('1- Incluir nova tarefa')
   print('2- Ver lista de tarefas')
   print('3- Excluir tarefa')
   print('4- Sair')
   print(25*'*') 
   


def adicionar_tarefa():
   print('Qual tarefa deseja adicionar?')
   titulo = input('adicione o titulo da tarefa:  ')
   categoria = input(f'qual a categoria de {titulo}: ')
   equipe = input('Equipe responsavel pela tarefa: ')
   data_entrega = input('prazo de entrega: ')
   tarefa_adicionada = Tarefa(titulo, categoria, equipe, data_entrega)
   lista_de_tarefas.append(tarefa_adicionada)
   main()
  


def exibir_lista():
   print('Tarefa'.ljust(25) + 'Categoria'.ljust(25) + 'Equipe'.ljust(25) +'Data de entrega')
   for tarefa in lista_de_tarefas:
       print(f'\n{tarefa._titulo}'.ljust(25) + f'{tarefa._categoria}'.ljust(25) + f'{tarefa._equipe}'.ljust(25) + f'{tarefa._data_entrega}')
   input('pressione qualquer tecla para continuar')
   main()


def escolhas_menu():
   opcao_do_menu = 0
   opcao_do_menu = int(input('\n selecione a opção desejada: '))
   if opcao_do_menu == 1:
      adicionar_tarefa()

   elif opcao_do_menu == 2:
      exibir_lista()



def main():
   menu()
   escolhas_menu()

if __name__ == '__main__':
    main()   
   
