from atividade import login
from atividade import cadastrar_cliente
from atividade import carrinho
from atividade import biblioteca
from atividade import agenda
from atividade import recuperacao_senha
from atividade import calcular_media
from atividade import almoxarifado
from atividade import conta_banco
from atividade import matricula
import pytest

def test_login_sucesso():
    assert login("Nicolas", "0511") == "Login realizado com sucesso"

def test_senha_incorreta():
    assert login("Nicolas", "errada") == "Senha incorreta"

def test_usuario_inexistente():
    assert login("Vinicios", "1234") == "Usuário não cadastrado"

def test_campos_vazios():
    assert login("", "") == "Algum campo obrigatório está vazio"


def test_cadastro_sucesso():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "41999999999") == "Cadastro realizado com sucesso"

def test_nome_vazio():
    assert cadastrar_cliente("", "12345678901", "teste@gmail.com", "41999999999") == "Nome obrigatório"

def test_cpf_invalido():
    assert cadastrar_cliente("Nicolas", "123", "teste@gmail.com", "41999999999") == "CPF inválido"

def test_email_invalido():
    assert cadastrar_cliente("Nicolas", "12345678901", "testegmail.com", "41999999999") == "E-mail inválido"

def test_telefone_vazio():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "") == "Campo telefone está em branco"

def test_login_sucesso():
    assert login("Nicolas", "0511") == "Login realizado com sucesso"

def test_login_senha_incorreta():
    assert login("Nicolas", "errada") == "Senha incorreta"

def test_login_usuario_inexistente():
    assert login("Vinicios", "1234") == "Usuário não cadastrado"

def test_login_campos_vazios():
    assert login("", "") == "Algum campo obrigatório está vazio"


def test_cadastro_sucesso():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "41999999999") == "Cadastro realizado com sucesso"

def test_cadastro_nome_vazio():
    assert cadastrar_cliente("", "12345678901", "teste@gmail.com", "41999999999") == "Nome obrigatório"

def test_cadastro_cpf_invalido():
    assert cadastrar_cliente("Nicolas", "123", "teste@gmail.com", "41999999999") == "CPF inválido"

def test_cadastro_email_invalido():
    assert cadastrar_cliente("Nicolas", "12345678901", "testegmail.com", "41999999999") == "E-mail inválido"

def test_cadastro_telefone_vazio():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "") == "Campo telefone está em branco"


def test_carrinho_adicionar_produto():
    c = carrinho()
    c.adicionar("Caneta", 2.50)
    assert c.total() == 2.50

def test_carrinho_adicionar_dois_produtos():
    c = carrinho()
    c.adicionar("Caneta", 2.50)
    c.adicionar("Caderno", 15.00)
    assert c.total() == 17.50

def test_carrinho_remover_produto():
    c = carrinho()
    c.adicionar("Caneta", 2.50)
    c.remover("Caneta")
    assert c.total() == 0.0

def test_carrinho_remover_produto_inexistente():
    c = carrinho()
    assert c.remover("Borracha") == "Produto não encontrado"

def test_carrinho_alterar_quantidade():
    c = carrinho()
    c.adicionar("Caneta", 2.50)
    c.alterar_quantidade("Caneta", 3)
    assert c.total() == 7.50

def test_carrinho_alterar_quantidade_invalida():
    c = carrinho()
    c.adicionar("Caneta", 2.50)
    assert c.alterar_quantidade("Caneta", 0) == "Quantidade inválida"

def test_carrinho_total_vazio():
    c = carrinho()
    assert c.total() == 0.0


# ============================================================
# QUESTÃO 4 - Biblioteca
# ============================================================
def test_biblioteca_emprestimo_sucesso():
    b = biblioteca()
    b.adicionar_livro("Dom Casmurro", 2)
    assert b.emprestar("Carlos", "Dom Casmurro") == "Empréstimo realizado com sucesso"

def test_biblioteca_livro_indisponivel():
    b = biblioteca()
    b.adicionar_livro("Dom Casmurro", 0)
    assert b.emprestar("Carlos", "Dom Casmurro") == "Livro indisponível"

def test_biblioteca_limite_emprestimos():
    b = biblioteca()
    for i in range(3):
        b.adicionar_livro(f"Livro {i}", 1)
        b.emprestar("Carlos", f"Livro {i}")
    b.adicionar_livro("Livro Extra", 1)
    assert b.emprestar("Carlos", "Livro Extra") == "Limite de empréstimos atingido"

def test_biblioteca_devolucao_sucesso():
    b = biblioteca()
    b.adicionar_livro("Dom Casmurro", 1)
    b.emprestar("Carlos", "Dom Casmurro")
    assert b.devolver("Carlos", "Dom Casmurro") == "Devolução realizada com sucesso"

def test_biblioteca_estoque_atualiza_apos_emprestimo():
    b = biblioteca()
    b.adicionar_livro("Dom Casmurro", 2)
    b.emprestar("Carlos", "Dom Casmurro")
    assert b.acervo["Dom Casmurro"] == 1


# ============================================================
# QUESTÃO 5 - Agenda
# ============================================================
def test_agenda_cadastro_sucesso():
    a = agenda()
    assert a.cadastrar("25/12/2025", "10:00", "Reunião") == "Compromisso cadastrado com sucesso"

def test_agenda_data_invalida():
    a = agenda()
    assert a.cadastrar("32/13/2025", "10:00", "Reunião") == "Data inválida"

def test_agenda_horario_invalido():
    a = agenda()
    assert a.cadastrar("25/12/2025", "25:99", "Reunião") == "Horário inválido"

def test_agenda_horario_duplicado():
    a = agenda()
    a.cadastrar("25/12/2025", "10:00", "Reunião")
    assert a.cadastrar("25/12/2025", "10:00", "Outra reunião") == "Já existe um compromisso nesse horário"

def test_agenda_mesmo_horario_dia_diferente():
    a = agenda()
    a.cadastrar("25/12/2025", "10:00", "Reunião")
    assert a.cadastrar("26/12/2025", "10:00", "Consulta") == "Compromisso cadastrado com sucesso"


# ============================================================
# QUESTÃO 6 - Recuperação de senha
# ============================================================
def test_recuperacao_envio_sucesso():
    r = recuperacao_senha()
    assert r.enviar_codigo("user@email.com", "123456") == "Código enviado com sucesso"

def test_recuperacao_email_invalido():
    r = recuperacao_senha()
    assert r.enviar_codigo("emailinvalido", "123456") == "E-mail inválido"

def test_recuperacao_codigo_valido():
    r = recuperacao_senha()
    r.enviar_codigo("user@email.com", "123456")
    assert r.validar_codigo("user@email.com", "123456") == "Código válido"

def test_recuperacao_codigo_invalido():
    r = recuperacao_senha()
    r.enviar_codigo("user@email.com", "123456")
    assert r.validar_codigo("user@email.com", "000000") == "Código inválido"

def test_recuperacao_codigo_expirado():
    import time
    r = recuperacao_senha()
    r.enviar_codigo("user@email.com", "123456")
    # Simula passar 6 minutos
    tempo_futuro = time.time() + 360
    assert r.validar_codigo("user@email.com", "123456", tempo_atual=tempo_futuro) == "Código expirado"


# ============================================================
# QUESTÃO 7 - Notas escolares
# ============================================================
def test_media_notas_normais():
    assert calcular_media([7.0, 8.0, 6.0, 9.0]) == 7.5

def test_media_notas_maximas():
    assert calcular_media([10.0, 10.0, 10.0]) == 10.0

def test_media_notas_minimas():
    assert calcular_media([0.0, 0.0, 0.0]) == 0.0

def test_media_campo_nao_preenchido():
    assert calcular_media([7.0, None, 8.0]) == "Campo de nota não preenchido"

def test_media_sem_notas():
    assert calcular_media([]) == "Nenhuma nota informada"

def test_media_nota_fora_do_intervalo():
    assert calcular_media([7.0, 11.0]) == "Nota fora do intervalo permitido"


# ============================================================
# QUESTÃO 8 - Almoxarifado
# ============================================================
def test_almoxarifado_entrada():
    a = almoxarifado()
    a.entrada("Papel A4", 100)
    assert a.saldo("Papel A4") == 100

def test_almoxarifado_saida():
    a = almoxarifado()
    a.entrada("Papel A4", 100)
    a.saida("Papel A4", 30)
    assert a.saldo("Papel A4") == 70

def test_almoxarifado_saida_insuficiente():
    a = almoxarifado()
    a.entrada("Papel A4", 10)
    assert a.saida("Papel A4", 50) == "Quantidade insuficiente em estoque"

def test_almoxarifado_entrada_invalida():
    a = almoxarifado()
    assert a.entrada("Papel A4", 0) == "Quantidade inválida"

def test_almoxarifado_saida_invalida():
    a = almoxarifado()
    a.entrada("Papel A4", 10)
    assert a.saida("Papel A4", -5) == "Quantidade inválida"

def test_almoxarifado_estoque_zerado():
    a = almoxarifado()
    assert a.saldo("Produto X") == 0


# ============================================================
# QUESTÃO 9 - Transferência bancária
# ============================================================
def test_transferencia_sucesso():
    c1 = conta_banco("Ana", 500)
    c2 = conta_banco("Bruno", 100)
    assert c1.transferir(c2, 200) == "Transferência realizada com sucesso"
    assert c1.saldo == 300
    assert c2.saldo == 300

def test_transferencia_saldo_insuficiente():
    c1 = conta_banco("Ana", 50)
    c2 = conta_banco("Bruno", 100)
    assert c1.transferir(c2, 200) == "Saldo insuficiente"

def test_transferencia_valor_negativo():
    c1 = conta_banco("Ana", 500)
    c2 = conta_banco("Bruno", 100)
    assert c1.transferir(c2, -100) == "Valor inválido para transferência"

def test_transferencia_valor_zero():
    c1 = conta_banco("Ana", 500)
    c2 = conta_banco("Bruno", 100)
    assert c1.transferir(c2, 0) == "Valor inválido para transferência"

def test_transferencia_mesma_conta():
    c1 = conta_banco("Ana", 500)
    assert c1.transferir(c1, 100) == "Transferência para a mesma conta não permitida"


# ============================================================
# QUESTÃO 10 - Matrícula escolar
# ============================================================
def test_matricula_sucesso():
    s = matricula()
    s.criar_turma("T1", "Informática", 30)
    assert s.matricular("Nicolas", "T1") == "Matrícula realizada com sucesso"

def test_matricula_turma_lotada():
    s = matricula()
    s.criar_turma("T1", "Informática", 1)
    s.matricular("Nicolas", "T1")
    assert s.matricular("Carlos", "T1") == "Turma lotada"

def test_matricula_turma_inexistente():
    s = matricula()
    assert s.matricular("Nicolas", "T99") == "Turma não encontrada"

def test_matricula_aluno_ja_matriculado():
    s = matricula()
    s.criar_turma("T1", "Informática", 30)
    s.matricular("Nicolas", "T1")
    assert s.matricular("Nicolas", "T1") == "Aluno já matriculado nesta turma"

def test_matricula_multiplas_vagas():
    s = matricula()
    s.criar_turma("T1", "Informática", 2)
    s.matricular("Nicolas", "T1")
    assert s.matricular("Carlos", "T1") == "Matrícula realizada com sucesso"
