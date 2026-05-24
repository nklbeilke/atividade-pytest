from datetime import datetime
import time

LIMITE_EMPRESTIMOS = 3
VALIDADE_SEGUNDOS = 300

#1 - Login

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

#2 - Cadastro

def cadastro(nome, cpf, email, telefone):
    if not nome:
        return "Nome obrigatório"

    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido"

    if "@" not in email:
        return "E-mail inválido"

    if not telefone:
        return "Campo telefone está em branco"

    return "Cadastro realizado com sucesso"

#3 - Carrinho

def carrinho_adicionar(carrinho, produto, preco, quantidade=1):
    if quantidade <= 0:
        return "Quantidade inválida"
    if produto in carrinho:
        carrinho[produto]["quantidade"] += quantidade
    else:
        carrinho[produto] = {"preco": preco, "quantidade": quantidade}
    return "Produto adicionado"

def carrinho_remover(carrinho, produto):
    if produto not in carrinho:
        return "Produto não encontrado"
    del carrinho[produto]
    return "Produto removido"

def carrinho_alterar_quantidade(carrinho, produto, nova_quantidade):
    if produto not in carrinho:
        return "Produto não encontrado"
    if nova_quantidade <= 0:
        return "Quantidade inválida"
    carrinho[produto]["quantidade"] = nova_quantidade
    return "Quantidade atualizada"

def carrinho_total(carrinho):
    return sum(item["preco"] * item["quantidade"] for item in carrinho.values())

#4 - Biblioteca

def biblioteca_adicionar_livro(acervo, titulo, quantidade):
    acervo[titulo] = quantidade

def biblioteca_emprestar(acervo, emprestimos, aluno, titulo):
    if titulo not in acervo or acervo[titulo] == 0:
        return "Livro indisponível"
    emprestados = emprestimos.get(aluno, [])
    if len(emprestados) >= LIMITE_EMPRESTIMOS:
        return "Limite de empréstimos atingido"
    acervo[titulo] -= 1
    if aluno not in emprestimos:
        emprestimos[aluno] = []
    emprestimos[aluno].append(titulo)
    return "Empréstimo realizado com sucesso"

def biblioteca_devolver(acervo, emprestimos, aluno, titulo):
    if aluno not in emprestimos or titulo not in emprestimos[aluno]:
        return "Empréstimo não encontrado"
    emprestimos[aluno].remove(titulo)
    acervo[titulo] += 1
    return "Devolução realizada com sucesso"

#5 - Agenda

def agenda(compromissos, data, horario, descricao):
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return "Data inválida"

    try:
        datetime.strptime(horario, "%H:%M")
    except ValueError:
        return "Horário inválido"

    chave = (data, horario)
    if chave in compromissos:
        return "Já existe um compromisso nesse horário"

    compromissos[chave] = descricao
    return "Compromisso cadastrado com sucesso"

#6 - Senha Rec.

def senha_rec_enviar(codigos, email, codigo):
    if "@" not in email:
        return "E-mail inválido"
    codigos[email] = {"codigo": codigo, "timestamp": time.time()}
    return "Código enviado com sucesso"

def senha_rec_validar(codigos, email, codigo_informado, tempo_atual=None):
    if email not in codigos:
        return "Nenhum código enviado para este e-mail"
    registro = codigos[email]
    agora = tempo_atual if tempo_atual is not None else time.time()
    if agora - registro["timestamp"] > VALIDADE_SEGUNDOS:
        return "Código expirado"
    if registro["codigo"] != codigo_informado:
        return "Código inválido"
    return "Código válido"

#7 - Calcular media

def notas(lista_notas):
    if not lista_notas:
        return "Nenhuma nota informada"
    for nota in lista_notas:
        if nota is None:
            return "Campo de nota não preenchido"
        if nota < 0 or nota > 10:
            return "Nota fora do intervalo permitido"
    media = sum(lista_notas) / len(lista_notas)
    return round(media, 2)

#8 - Almoxarifado

def almoxarifado_entrada(estoque, produto, quantidade):
    if quantidade <= 0:
        return "Quantidade inválida"
    estoque[produto] = estoque.get(produto, 0) + quantidade
    return "Entrada registrada"

def almoxarifado_saida(estoque, produto, quantidade):
    if quantidade <= 0:
        return "Quantidade inválida"
    disponivel = estoque.get(produto, 0)
    if quantidade > disponivel:
        return "Quantidade insuficiente em estoque"
    estoque[produto] = disponivel - quantidade
    return "Saída registrada"

def almoxarifado_saldo(estoque, produto):
    return estoque.get(produto, 0)

#9 - Banco

def banco_criar_conta(contas, titular, saldo=0):
    contas[titular] = saldo

def banco(contas, origem, destino, valor):
    if origem == destino:
        return "Transferência para a mesma conta não permitida"
    if valor <= 0:
        return "Valor inválido para transferência"
    if contas[origem] < valor:
        return "Saldo insuficiente"
    contas[origem] -= valor
    contas[destino] += valor
    return "Transferência realizada com sucesso"

#10 - Matricula

def matricula_criar_turma(turmas, turma_id, curso, vagas):
    turmas[turma_id] = {"curso": curso, "vagas": vagas, "alunos": []}

def matricula(turmas, aluno, turma_id):
    if turma_id not in turmas:
        return "Turma não encontrada"
    turma = turmas[turma_id]
    if aluno in turma["alunos"]:
        return "Aluno já matriculado nesta turma"
    if len(turma["alunos"]) >= turma["vagas"]:
        return "Turma lotada"
    turma["alunos"].append(aluno)
    return "Matrícula realizada com sucesso"
