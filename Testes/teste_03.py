import pytest

def validar_email(email):
    """Valida se um email tem formato válido"""
    return (isinstance(email, str) and 
            "@" in email and 
            "." in email.split("@")[-1] and
            len(email.split("@")[0]) > 0)

def validar_senha(senha):
    """Valida se a senha tem:
    - Pelo menos 8 caracteres
    - 1 letra maiúscula
    - 1 número
    """
    if not isinstance(senha, str) or len(senha) < 8:
        return False
    return any(c.isupper() for c in senha) and any(c.isdigit() for c in senha)

# Testes para email
def test_email_valido():
    assert validar_email("teste@exemplo.com") is True
    assert validar_email("nome.sobrenome@dominio.com.br") is True

def test_email_invalido():
    assert validar_email("semarroba.com") is False
    assert validar_email("@semusuario.com") is False
    assert validar_email("") is False
    assert validar_email(None) is False

# Testes para senha
def test_senha_valida():
    assert validar_senha("Senha123") is True
    assert validar_senha("A1b2C3d4") is True

def test_senha_invalida():
    assert validar_senha("senhafraca") is False
    assert validar_senha("12345678") is False
    assert validar_senha("") is False
    assert validar_senha(None) is False
