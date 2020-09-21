from pessoa_class import Pessoa
from pessoa_class import Aluno
from pessoa_class import Professor
from pessoa_class import Responsavel
from pessoa_class import Coordenador
from pessoa_class import Diretor

pessoa = Pessoa(18, "Ricardo", 74, 174, 000.000.000-00)
pessoa.saber_idade()
pessoa.saber_nome()
pessoa.saber_cpf()

aluno = Aluno(21, "Antonio", 92, 180, 111.111.111-11, 1)
aluno.saber_disciplina()
aluno.saber_matricula()

professor = Professor(23, "Matheus", 76, 164, 222.222.222-33, "Matemática")
professor.dar_aula
professor.saber_disciplina_ministrada

responsavel = Responsavel(33, "Clodoaldo", 66, 170, 333.333.333-55, "Igor")
responsavel.verificar()
responsavel.saber_responsavel()

coordenador = Coordenador(45, "Anelucia", 55, 162, 000.012.123-97, "GTI")
coordenador.coordenar()
coordenador.saber_curso_cordenado()


diretor = Diretor(50, "Joelson", 32, 170, 666.654.68-95, "FACET")
diretor.gerir()
diretor.saber_escola()