from datetime import datetime

def login(usuario, senha):
    usuarios = {
        "Nicolas": "0511",
    }

    if not usuario or not senha:
        return "Algum campo obrigatório está vazio"

    if usuario not in usuarios:
        return "Usuário não cadastrado"

    if usuarios[usuario] != senha:
        return "Senha incorreta"

    return "Login realizado com sucesso"

def cadastrar_cliente(nome, cpf, email, telefone):

    if not nome:
        return "Nome obrigatório"

    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido"

    if "@" not in email:
        return "E-mail inválido"

    if not telefone:
        return "Campo telefone está em branco"

    return "Cadastro realizado com sucesso"

class carrinho:
    def __init__(self):
        self.itens = {}  

    def adicionar(self, produto, preco, quantidade=1):
        if quantidade <= 0:
            return "Quantidade inválida"
        if produto in self.itens:
            self.itens[produto]["quantidade"] += quantidade
        else:
            self.itens[produto] = {"preco": preco, "quantidade": quantidade}
        return "Produto adicionado"

    def remover(self, produto):
        if produto not in self.itens:
            return "Produto não encontrado"
        del self.itens[produto]
        return "Produto removido"

    def alterar_quantidade(self, produto, nova_quantidade):
        if produto not in self.itens:
            return "Produto não encontrado"
        if nova_quantidade <= 0:
            return "Quantidade inválida"
        self.itens[produto]["quantidade"] = nova_quantidade
        return "Quantidade atualizada"

    def total(self):
        return sum(item["preco"] * item["quantidade"] for item in self.itens.values())


class biblioteca:
    LIMITE_EMPRESTIMOS = 3

    def __init__(self):
        self.acervo = {}
        self.emprestimos = {}

    def adicionar_livro(self, titulo, quantidade):
        self.acervo[titulo] = quantidade

    def emprestar(self, aluno, titulo):
        if titulo not in self.acervo or self.acervo[titulo] == 0:
            return "Livro indisponível"
        emprestados = self.emprestimos.get(aluno, [])
        if len(emprestados) >= self.LIMITE_EMPRESTIMOS:
            return "Limite de empréstimos atingido"
        self.acervo[titulo] -= 1
        self.emprestimos.setdefault(aluno, []).append(titulo)
        return "Empréstimo realizado com sucesso"

    def devolver(self, aluno, titulo):
        if aluno not in self.emprestimos or titulo not in self.emprestimos[aluno]:
            return "Empréstimo não encontrado"
        self.emprestimos[aluno].remove(titulo)
        self.acervo[titulo] += 1
        return "Devolução realizada com sucesso"

class agenda:
    def __init__(self):
        self.compromissos = {}

    def cadastrar(self, data_str, horario_str, descricao):
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            return "Data inválida"

        try:
            horario = datetime.strptime(horario_str, "%H:%M")
        except ValueError:
            return "Horário inválido"

        chave = (data_str, horario_str)
        if chave in self.compromissos:
            return "Já existe um compromisso nesse horário"

        self.compromissos[chave] = descricao
        return "Compromisso cadastrado com sucesso"


import time

class recuperacao_senha:
    VALIDADE_SEGUNDOS = 300

    def __init__(self):
        self.codigos = {}

    def enviar_codigo(self, email, codigo):
        if "@" not in email:
            return "E-mail inválido"
        self.codigos[email] = {"codigo": codigo, "timestamp": time.time()}
        return "Código enviado com sucesso"

    def validar_codigo(self, email, codigo_informado, tempo_atual=None):
        if email not in self.codigos:
            return "Nenhum código enviado para este e-mail"
        registro = self.codigos[email]
        agora = tempo_atual if tempo_atual is not None else time.time()
        if agora - registro["timestamp"] > self.VALIDADE_SEGUNDOS:
            return "Código expirado"
        if registro["codigo"] != codigo_informado:
            return "Código inválido"
        return "Código válido"


def calcular_media(notas):
    if not notas:
        return "Nenhuma nota informada"
    for nota in notas:
        if nota is None:
            return "Campo de nota não preenchido"
        if nota < 0 or nota > 10:
            return "Nota fora do intervalo permitido"
    media = sum(notas) / len(notas)
    return round(media, 2)


class almoxarifado:
    def __init__(self):
        self.estoque = {}

    def entrada(self, produto, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida"
        self.estoque[produto] = self.estoque.get(produto, 0) + quantidade
        return "Entrada registrada"

    def saida(self, produto, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida"
        disponivel = self.estoque.get(produto, 0)
        if quantidade > disponivel:
            return "Quantidade insuficiente em estoque"
        self.estoque[produto] = disponivel - quantidade
        return "Saída registrada"

    def saldo(self, produto):
        return self.estoque.get(produto, 0)


class conta_banco:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def transferir(self, destino, valor):
        if destino is self:
            return "Transferência para a mesma conta não permitida"
        if valor <= 0:
            return "Valor inválido para transferência"
        if valor > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= valor
        destino.saldo += valor
        return "Transferência realizada com sucesso"

class matricula:
    def __init__(self):
        self.turmas = {}

    def criar_turma(self, turma_id, curso, vagas):
        self.turmas[turma_id] = {"curso": curso, "vagas": vagas, "alunos": []}

    def matricular(self, aluno, turma_id):
        if turma_id not in self.turmas:
            return "Turma não encontrada"
        turma = self.turmas[turma_id]
        if aluno in turma["alunos"]:
            return "Aluno já matriculado nesta turma"
        if len(turma["alunos"]) >= turma["vagas"]:
            return "Turma lotada"
        turma["alunos"].append(aluno)
        return "Matrícula realizada com sucesso"
