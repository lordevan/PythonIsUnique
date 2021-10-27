import hashlib
import sqlite3
conectar = ""

class Login():
    def __init__(self, caminho):
        self.Db = caminho
        self.conectar = ''
        self.cursor = ''

    def Hash(self, dados):
        sha224 = hashlib.sha224()
        dados = dados.encode()
        sha224.update(dados)
        return sha224.hexdigest()

    def Conectar(self):
        try:
            self.conectar = sqlite3.connect(self.Db)
            self.cursor = self.conectar.cursor()
            return 1
        except Exception as erro:
            return [0, str(erro)]
    
    def Criar_Base_De_Dados(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS"LoginUsers" (
                "Id"	INTEGER,
                "Usuario"	TEXT NOT NULL,
                "Senha"	TEXT NOT NULL,
                PRIMARY KEY("Id" AUTOINCREMENT)
            );''')
            return 1
        except Exception as erro:
            return [0, str(erro)]
    
    def Adicionar_Usuario(self, dados):
        try:
            dados_protegidos = [None]
            dados_protegidos.append(self.Hash(dados[0]))
            dados_protegidos.append(self.Hash(dados[1]))
            linhas = self.cursor.execute("SELECT Usuario, Senha FROM LoginUsers WHERE Usuario = ? and Senha = ?", [dados_protegidos[1], dados_protegidos[2]])
            if(linhas.fetchall() == []):
                self.cursor.execute('''INSERT INTO LoginUsers(Id, Usuario, Senha)
                    VALUES(?, ?, ?)
                ''', dados_protegidos)
                self.conectar.commit()
                return 1
            else:
                return 0
        except Exception as erro:
            return [0, str(erro)]

    def Atualiza_User(self, dados):
        try:
            dados_protegidos = []
            dados_protegidos.append(self.Hash(dados[0]))
            dados_protegidos.append(self.Hash(dados[1]))
            dados_protegidos.append(self.Hash(dados[2]))
            dados_protegidos.append(self.Hash(dados[3]))
            linhas = self.cursor.execute("SELECT Usuario, Senha FROM LoginUsers WHERE Usuario = ? and Senha = ?", [dados_protegidos[2], dados_protegidos[3]])
            if(linhas.fetchall() != []):
                self.cursor.execute("UPDATE LoginUsers SET Usuario = ?, Senha = ? WHERE Usuario = ? and Senha = ?", [dados_protegidos[0], dados_protegidos[1], dados_protegidos[2], dados_protegidos[3]])
                self.conectar.commit()
                return 1
            else: 
                return 0
        except Exception as erro:
            return [0, str(erro)]
        
    def Remover_Usuario(self, dados):
        try:
            dados_protegidos = []
            dados_protegidos.append(self.Hash(dados[0]))
            dados_protegidos.append(self.Hash(dados[1]))
            linhas = self.cursor.execute("SELECT Usuario, Senha FROM LoginUsers WHERE Usuario = ? and Senha = ?", [dados_protegidos[0], dados_protegidos[1]])
            if(linhas.fetchall() != []):
                self.cursor.execute("DELETE FROM LoginUsers WHERE Usuario = ? and Senha = ?", dados_protegidos)
                self.conectar.commit()
                return 1
            else:
                return 0
        except Exception as erro:
            return[0, str(erro)]
    
    def Consulta(self, dados):
        try:
            dados_protegidos = []
            dados_protegidos.append(self.Hash(dados[0]))
            dados_protegidos.append(self.Hash(dados[1]))
            linhas = self.cursor.execute("SELECT Usuario, Senha FROM LoginUsers WHERE Usuario = ? and Senha = ?", [dados_protegidos[0], dados_protegidos[1]])
            if(linhas.fetchall() != []):
                return 1
            else:
                return 0
        except Exception as erro:
            print([0, str(erro)])