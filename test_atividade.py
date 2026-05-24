from atividade import login
from atividade import cadastro
from atividade import carrinho_adicionar, carrinho_remover, carrinho_alterar_quantidade, carrinho_total
from atividade import biblioteca_adicionar_livro, biblioteca_emprestar, biblioteca_devolver
from atividade import agenda
from atividade import senha_rec_enviar, senha_rec_validar
from atividade import notas
from atividade import almoxarifado_entrada, almoxarifado_saida, almoxarifado_saldo
from atividade import banco_criar_conta, banco
from atividade import matricula_criar_turma, matricula
import pytest


def test_login_sucesso():
    assert login("Nicolas", "0511") == "Login realizado com sucesso"

def test_login_senha_incorreta():
    assert login("Nicolas", "errada") == "Senha incorreta"

def test_login_usuario_inexistente():
    assert login("Vinicios", "1234") == "Usuário não cadastrado"

def test_login_campos_vazios():
    assert login("", "") == "Algum campo obrigatório está vazio"

def test_login_usuario_vazio():
    assert login("", "0511") == "Algum campo obrigatório está vazio"

def test_login_senha_vazia():
    assert login("Nicolas", "") == "Algum campo obrigatório está vazio"


def test_cadastro_sucesso():
    assert cadastro("Nicolas", "12345678901", "nicolas@gmail.com", "41999999999") == "Cadastro realizado com sucesso"

def test_cadastro_nome_vazio():
    assert cadastro("", "12345678901", "nicolas@gmail.com", "41999999999") == "Nome obrigatório"

def test_cadastro_cpf_invalido():
    assert cadastro("Nicolas", "123", "nicolas@gmail.com", "41999999999") == "CPF inválido"

def test_cadastro_cpf_vazio():
    assert cadastro("Nicolas", "", "nicolas@gmail.com", "41999999999") == "CPF inválido"

def test_cadastro_email_invalido():
    assert cadastro("Nicolas", "12345678901", "nicolasgmail.com", "41999999999") == "E-mail inválido"

def test_cadastro_telefone_vazio():
    assert cadastro("Nicolas", "12345678901", "nicolas@gmail.com", "") == "Campo telefone está em branco"


def test_carrinho_adicionar_produto():
    c = {}
    carrinho_adicionar(c, "Caneta", 2.50)
    assert carrinho_total(c) == 2.50

def test_carrinho_adicionar_dois_produtos():
    c = {}
    carrinho_adicionar(c, "Caneta", 2.50)
    carrinho_adicionar(c, "Caderno", 15.00)
    assert carrinho_total(c) == 17.50

def test_carrinho_remover_produto():
    c = {}
    carrinho_adicionar(c, "Caneta", 2.50)
    carrinho_remover(c, "Caneta")
    assert carrinho_total(c) == 0.0

def test_carrinho_remover_produto_inexistente():
    c = {}
    assert carrinho_remover(c, "Borracha") == "Produto não encontrado"

def test_carrinho_alterar_quantidade():
    c = {}
    carrinho_adicionar(c, "Caneta", 2.50)
    carrinho_alterar_quantidade(c, "Caneta", 3)
    assert carrinho_total(c) == 7.50

def test_carrinho_alterar_quantidade_invalida():
    c = {}
    carrinho_adicionar(c, "Caneta", 2.50)
    assert carrinho_alterar_quantidade(c, "Caneta", 0) == "Quantidade inválida"

def test_carrinho_total_vazio():
    c = {}
    assert carrinho_total(c) == 0.0


def test_biblioteca_emprestimo_sucesso():
    acervo = {}
    emprestimos = {}
    biblioteca_adicionar_livro(acervo, "Dom Casmurro", 2)
    assert biblioteca_emprestar(acervo, emprestimos, "Nicolas", "Dom Casmurro") == "Empréstimo realizado com sucesso"

def test_biblioteca_livro_indisponivel():
    acervo = {}
    emprestimos = {}
    biblioteca_adicionar_livro(acervo, "Dom Casmurro", 0)
    assert biblioteca_emprestar(acervo, emprestimos, "Nicolas", "Dom Casmurro") == "Livro indisponível"

def test_biblioteca_limite_emprestimos():
    acervo = {}
    emprestimos = {}
    for i in range(3):
        biblioteca_adicionar_livro(acervo, f"Livro {i}", 1)
        biblioteca_emprestar(acervo, emprestimos, "Nicolas", f"Livro {i}")
    biblioteca_adicionar_livro(acervo, "Livro Extra", 1)
    assert biblioteca_emprestar(acervo, emprestimos, "Nicolas", "Livro Extra") == "Limite de empréstimos atingido"

def test_biblioteca_devolucao_sucesso():
    acervo = {}
    emprestimos = {}
    biblioteca_adicionar_livro(acervo, "Dom Casmurro", 1)
    biblioteca_emprestar(acervo, emprestimos, "Nicolas", "Dom Casmurro")
    assert biblioteca_devolver(acervo, emprestimos, "Nicolas", "Dom Casmurro") == "Devolução realizada com sucesso"

def test_biblioteca_estoque_atualiza_apos_emprestimo():
    acervo = {}
    emprestimos = {}
    biblioteca_adicionar_livro(acervo, "Dom Casmurro", 2)
    biblioteca_emprestar(acervo, emprestimos, "Nicolas", "Dom Casmurro")
    assert acervo["Dom Casmurro"] == 1


def test_agenda_cadastro_sucesso():
    compromissos = {}
    assert agenda(compromissos, "25/12/2025", "10:00", "Reunião") == "Compromisso cadastrado com sucesso"

def test_agenda_data_invalida():
    compromissos = {}
    assert agenda(compromissos, "32/13/2025", "10:00", "Reunião") == "Data inválida"

def test_agenda_horario_invalido():
    compromissos = {}
    assert agenda(compromissos, "25/12/2025", "25:99", "Reunião") == "Horário inválido"

def test_agenda_horario_duplicado():
    compromissos = {}
    agenda(compromissos, "25/12/2025", "10:00", "Reunião")
    assert agenda(compromissos, "25/12/2025", "10:00", "Outra reunião") == "Já existe um compromisso nesse horário"

def test_agenda_mesmo_horario_dia_diferente():
    compromissos = {}
    agenda(compromissos, "25/12/2025", "10:00", "Reunião")
    assert agenda(compromissos, "26/12/2025", "10:00", "Consulta") == "Compromisso cadastrado com sucesso"


def test_senha_rec_envio_sucesso():
    codigos = {}
    assert senha_rec_enviar(codigos, "nicolas@gmail.com", "123456") == "Código enviado com sucesso"

def test_senha_rec_email_invalido():
    codigos = {}
    assert senha_rec_enviar(codigos, "nicolasgmail.com", "123456") == "E-mail inválido"

def test_senha_rec_codigo_valido():
    codigos = {}
    senha_rec_enviar(codigos, "nicolas@gmail.com", "123456")
    assert senha_rec_validar(codigos, "nicolas@gmail.com", "123456") == "Código válido"

def test_senha_rec_codigo_invalido():
    codigos = {}
    senha_rec_enviar(codigos, "nicolas@gmail.com", "123456")
    assert senha_rec_validar(codigos, "nicolas@gmail.com", "000000") == "Código inválido"

def test_senha_rec_codigo_expirado():
    codigos = {}
    senha_rec_enviar(codigos, "nicolas@gmail.com", "123456")
    tempo_futuro = codigos["nicolas@gmail.com"]["timestamp"] + 360
    assert senha_rec_validar(codigos, "nicolas@gmail.com", "123456", tempo_atual=tempo_futuro) == "Código expirado"


def test_notas_media_normal():
    assert notas([7.0, 8.0, 6.0, 9.0]) == 7.5

def test_notas_maximas():
    assert notas([10.0, 10.0, 10.0]) == 10.0

def test_notas_minimas():
    assert notas([0.0, 0.0, 0.0]) == 0.0

def test_notas_campo_nao_preenchido():
    assert notas([7.0, None, 8.0]) == "Campo de nota não preenchido"

def test_notas_lista_vazia():
    assert notas([]) == "Nenhuma nota informada"

def test_notas_fora_do_intervalo():
    assert notas([7.0, 11.0]) == "Nota fora do intervalo permitido"


def test_almoxarifado_entrada():
    estoque = {}
    almoxarifado_entrada(estoque, "Papel A4", 100)
    assert almoxarifado_saldo(estoque, "Papel A4") == 100

def test_almoxarifado_saida():
    estoque = {}
    almoxarifado_entrada(estoque, "Papel A4", 100)
    almoxarifado_saida(estoque, "Papel A4", 30)
    assert almoxarifado_saldo(estoque, "Papel A4") == 70

def test_almoxarifado_saida_insuficiente():
    estoque = {}
    almoxarifado_entrada(estoque, "Papel A4", 10)
    assert almoxarifado_saida(estoque, "Papel A4", 50) == "Quantidade insuficiente em estoque"

def test_almoxarifado_entrada_invalida():
    estoque = {}
    assert almoxarifado_entrada(estoque, "Papel A4", 0) == "Quantidade inválida"

def test_almoxarifado_saida_invalida():
    estoque = {}
    almoxarifado_entrada(estoque, "Papel A4", 10)
    assert almoxarifado_saida(estoque, "Papel A4", -5) == "Quantidade inválida"

def test_almoxarifado_estoque_zerado():
    estoque = {}
    assert almoxarifado_saldo(estoque, "Produto X") == 0


def test_banco_transferencia_sucesso():
    contas = {}
    banco_criar_conta(contas, "Nicolas", 500)
    banco_criar_conta(contas, "Bruno", 100)
    assert banco(contas, "Nicolas", "Bruno", 200) == "Transferência realizada com sucesso"
    assert contas["Nicolas"] == 300
    assert contas["Bruno"] == 300

def test_banco_saldo_insuficiente():
    contas = {}
    banco_criar_conta(contas, "Nicolas", 50)
    banco_criar_conta(contas, "Bruno", 100)
    assert banco(contas, "Nicolas", "Bruno", 200) == "Saldo insuficiente"

def test_banco_valor_negativo():
    contas = {}
    banco_criar_conta(contas, "Nicolas", 500)
    banco_criar_conta(contas, "Bruno", 100)
    assert banco(contas, "Nicolas", "Bruno", -100) == "Valor inválido para transferência"

def test_banco_valor_zero():
    contas = {}
    banco_criar_conta(contas, "Nicolas", 500)
    banco_criar_conta(contas, "Bruno", 100)
    assert banco(contas, "Nicolas", "Bruno", 0) == "Valor inválido para transferência"

def test_banco_mesma_conta():
    contas = {}
    banco_criar_conta(contas, "Nicolas", 500)
    assert banco(contas, "Nicolas", "Nicolas", 100) == "Transferência para a mesma conta não permitida"


def test_matricula_sucesso():
    turmas = {}
    matricula_criar_turma(turmas, "T1", "Informática", 30)
    assert matricula(turmas, "Nicolas", "T1") == "Matrícula realizada com sucesso"

def test_matricula_turma_lotada():
    turmas = {}
    matricula_criar_turma(turmas, "T1", "Informática", 1)
    matricula(turmas, "Nicolas", "T1")
    assert matricula(turmas, "Vinicios", "T1") == "Turma lotada"


def test_matricula_turma_inexistente():
    turmas = {}
    assert matricula(turmas, "Nicolas", "T00") == "Turma não encontrada"

def test_matricula_aluno_ja_matriculado():
    turmas = {}
    matricula_criar_turma(turmas, "T1", "Informática", 30)
    matricula(turmas, "Nicolas", "T1")
    assert matricula(turmas, "Nicolas", "T1") == "Aluno já matriculado nesta turma"

def test_matricula_multiplas_vagas():
    turmas = {}
    matricula_criar_turma(turmas, "T1", "Informática", 2)
    matricula(turmas, "Nicolas", "T1")
    assert matricula(turmas, "Bruno", "T1") == "Matrícula realizada com sucesso"