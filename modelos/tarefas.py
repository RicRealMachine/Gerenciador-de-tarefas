class Tarefa():
    tarefas=[]
   
    def __init__(self, titulo, categoria ,equipe, data_entrega):
        self._titulo = titulo
        self._categoria = categoria
        self._equipe = equipe
        self._data_entrega = data_entrega

    def __str__(self):
        return self._titulo, self._categoria, self._equipe, self._data_entrega