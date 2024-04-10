import os
import sqlite3
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):          
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Err ao conectar ao banco de dados: {e}")


    def criar_tabelas(self):
        self.criar_tabelas_pessoa()
        self.criar_tabelas_marca()
        self.criar_tabelas_veiculo()   

    def criar_tabelas_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa (
                        cpf INTERGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        nascimento DATE,
                        oculos BOOLEAN
                    )"""
                ) 
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro criar tabela Pessoa: {e}")   

        def criar_tabelas_marca(self):
            if self.conn:
             try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca (
                        id INTERGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sigla TEXT
                    )"""
                ) 
                self.conn.commit()
             except sqlite3.Error as e:
                print(f"Erro criar tabela Marca: {e}")   

        def criar_tabelas_veiculo(self):
            if self.conn:
             try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo (
                        placa TEXT PRIMARY KEY,
                        cor TEXT NOT NULL,
                        cpf_proprietario INTEGER,
                        id_marca INTEGER,
                        FOREIGN KEY(cpf_proprietario) REFERENCES Pessoa(cpf),
                        FOREIGN KEY(id_marca) REFERENCES Marcar(id)
                    )"""
                ) 
                self.conn.commit()
             except sqlite3.Error as e:
                print(f"Erro criar tabela Veiculo: {e}")      

        def inserir_pessoa(self, pessoa: Pessoa):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute("INSERT INTO Pessoa VALUES (?, ?, ?, ?)",
                     (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos),)
                    self.conn.commit()
                except sqlite3.Error as e:
                     print(f"Erro ao inserir pessoa:{e}")        


        def inserir_marca(self, marca: Marca):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute("INSERT INTO Marca VALUES (?, ?, ?)") 
                    (marca.id, marca.nome, marca.sigla)    
                    self.conn.commit()         
                except sqlite3.Error as e:
                    print(f"Erro ao inserir marca:{e} ")

        def inserir_veiculo(self, veiculo: Veiculo):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute(
                        "INSERT INTO Veiculo VALUES (?, ?, ?, ?)",
                        (
                            veiculo.placa,
                            veiculo.cor,
                            veiculo.propietario.cpf,
                            veiculo.marca.id,
                        ),
                    )
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao inserir veiculo: {e}")

        def atualizar_pessoa(self, pessoa):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute(
                        "UPDATE Pessoa SET nome=?, nascimento=?, oculos=? WHERE cpf=?",
                        (pessoa.nome, pessoa.nascimento, pessoa.oculos, pessoa.cpf),
                    )
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao atualizar pessoa: {e}")
        def atualizar_veiculo(self, veiculo):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute(
                        "UPDATE Veiculo SET cor=?, cpf_proprietario=?, id_marca=? WHERE placa=?",
                        (
                            veiculo.cor,
                            veiculo.propietario.cpf,
                            veiculo.marca.id,
                            veiculo.placa
                        ),
                    )
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao atualizar veiculo: {e}")

        def atualizar_marca(self, marca):
            if self.conn:
                try:
                    cursor = self.conn.cursor()
                    cursor.execute(
                        "UPDATE Marca SET id=?, nome=?, sigla=? WHERE modelo=?",
                        (
                            marca.id,
                            marca.nome,
                            marca.sigla,
                            marca.modelo,
                        ),
                    )                                
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao atualizar marca {e}")    