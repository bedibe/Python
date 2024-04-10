from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo


#criação de instância de pessoa
pessoa1 = Pessoa(cpf=134345678912, nome="Junin", nascimento=date(2001, 5, 30), oculos=True)

# Criando uma instância de Marca
marca1 = Marca(id=1, nome="Chevrolet", sigla="CHT")

#Criando uma instacia para o veiculo
veiculo1 = Veiculo(placa="BDB586", cor="Azul Marinho", propietario=[Pessoa], marca=[Marca])