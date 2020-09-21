class Pessoa():

    def __init__(self, idade, nome, peso, altura, cpf):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.cpf = cpf

        def andar(self):
            print("{} está andando ".format(self.nome))

        def saber_idade(self):
            print("A idade é {}".format(self.idade))

        def saber_nome(self):
            print("A pessoa se chama {}".format(self.nome))

        def saber_cpf(self):
            print("O CPF é {}".format(self.cpf))

class Aluno(Pessoa):

    def __init__(self, idade, nome, peso, altura, cpf, disciplina, n_matricula):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.disciplina = disciplina
        self.cpf = cpf
        self.n_matricula = n_matricula

        def estudar(self):
            print("O aluno {} está estudando {}!".format(self.nome, self.disciplina))

        def saber_disciplina(self):
            print("A disciplina é {}".format(self.disciplina))

        def saber_matricula(self):
            print("A matricula do aluno {} é {} ".format(self.nome, self.n_matricula))

class Responsavel(Pessoa):

    def __init__(self, idade, nome, peso, altura, cpf, responsavel_por):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.responsavel_por = responsavel_por

    def verificar(self):
        print("{} está responsavel por verificar as ações do(a) jovem {}".format(self.nome, self.responsavel_por))

    def saber_responsavel(self):
        print("{} é responsavel por {}".format(self.nome, self.responsavel_por))

class Professor(Pessoa):

    def __init__(self, idade, nome, peso, altura, cpf, disciplina_que_ensina):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.cpf = cpf
        self.disciplina_que_ensina = disciplina_que_ensina

    def dar_aula(self):
        print("O professor {} esta dando a aula de {} nesse momento!".format(self.nome, self.disciplica_que_ensina))

    def saber_disciplina_ministrada(self):
        print("A disciplina que esse professor ministra é {}".format(self.disciplica_que_ensina))

class Coordenador(Pessoa):

    def __init__(self, idade, nome, peso, altura, cpf, curso_coordenado):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.cpf = cpf
        self.curso_coordenado = curso_coordenado

    def coordenar(self):
        print("O Coordenador {}, está gerindo o curso de {}".format(self.curso_coordenado))

    def saber_curso_cordenado(self):
        print("O curso coordenado é {}".format(self.curso_coordenado))

class Diretor(Pessoa):

    def __init__(self, idade, nome, peso, altura, cpf, escola_que_coordena):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.cpf = cpf
        self.escola_que_coordena = escola_que_coordena

    def gerir(self):
        print("O diretor {}, está gerindo esta a escola {}".format(self.nome, self.escola_que_coordena))

    def saber_escola(self):
        print("A escola que esta sendo regida é {} ".format(self.escola_que_coordena))
