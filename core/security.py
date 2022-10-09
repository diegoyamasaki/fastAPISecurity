from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verficar se a senha está correta, comparado
    a senha em texto puro, informado pelo usuario, e o hash da
    senha que estará salvo no banco de dados durante a criação
    da conta.
    """

    return CRIPTO.verify(senha, hash_senha)
