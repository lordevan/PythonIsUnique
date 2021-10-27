from login import Login

LOGIN = Login("./Banco/banco.db") # Local aonde o Bd vai ser criado!
LOGIN.Conectar() # Estabelece a conexão
LOGIN.Criar_Base_De_Dados() # Cria a tabela!


opcoes = {
    0 : LOGIN.Consulta,
    1 : LOGIN.Adicionar_Usuario,
    2 : LOGIN.Atualiza_User,
    3 : LOGIN.Remover_Usuario
}

def Start():
    print("Bem vindo, para entrar no sistema, precisa logar!\n")
    print("[0] - Login\n")
    print("[1] - Registrar\n")
    print("[2] - Atualizar\n")
    print("[3] - Remover\n")
    escolha = int(input(">> "))
    if(escolha == 0):
        usuario = input("Digite seu usuario > ")
        senha = input("Digite sua senha > ")
        resposta = opcoes[0]([usuario, senha])
        if resposta != 0 : print("Bem vindo ao sistema")
        else : print("Algo está incorreto!")
    
    if(escolha == 1):
        usuario = input("Digite seu usuario > ")
        senha = input("Digite sua nova senha > ")
        resposta = opcoes[1]([usuario, senha])
        if resposta != 0 : print("Usuario foi registrado!")
        else : print("Não foi possivel realizar seu cadastro no sistema")
    
    if(escolha == 2):
        usuario = input("Digite seu usuario > ")
        senha = input("Digite sua senha > ")
        usuario_novo = input("Digite seu novo usuario > ")
        senha_novo = input("Digite sua senha > ")
        resposta = opcoes[2]([usuario_novo, senha_novo, usuario, senha])
        if resposta != 0 : print("Usuario foi Atualizado!")
        else : print("Não foi possivel realizar seu update no sistema")

    if(escolha == 3):
        usuario = input("Digite seu usuario > ")
        senha = input("Digite sua senha > ")
        resposta = opcoes[3]([usuario, senha])
        if resposta != 0 : print("Usuario foi Removido!")
        else : print("Não foi possivel realizar sua remoção no sistema")

Start()
