from peewee import Model,SqliteDatabase, CharField, BooleanField
import os 

banco = os.path.abspath(os.path.join(os.path.dirname(__file__), "tarefas.sqlite"))

db = SqliteDatabase(banco)

class Tarefa(Model):
    titulo = CharField()
    completo = BooleanField()

    class Meta:
        database = db



    @classmethod
    def criar (cls, titulo, completo):
        try:
            nova_tarefa = cls.create(titulo=titulo, completo=completo)
            return nova_tarefa
        except Exception as e:
            print(f"Erro ao criar tarefa: {e}")

    @classmethod
    def buscar_todos(cls):
        return cls.select()      
    

    @classmethod
    def buscar_por_titulo(cls, titulo):
        return cls.get(cls.titulo == titulo)
    
    def atualizar(self, completo):
        self.completo = completo
        self.save()

    def deletar (self):
        self.delete_instance()
        

    if __name__ == "__main__":
        db.connect()
        db.create_tables([Tarefa])


    nova_tarefa = Tarefa.criar("Faer compras", False)

    for tarefa in Tarefa.buscar_todos():
        print(tarefa.titulo, tarefa.completo)

    if not Tarefa.buscar_todos().exsits():
        print("Sem tarefas")


    tarefa_para_deletar = Tarefa.buscar_por_titulos("Fazer compras")
    tarefa_para_deletar.deletar()        
    for tarefa in Tarefa.buscar_todos():
        print(tarefa.titulo, tarefa.completo)
    if not Tarefa.buscar_todos().exists():
        print("Sem tarefas")    