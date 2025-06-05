# Instala o conector do MySQL para Python
# !pip install mysql-connector-python

# Importa o módulo necessário para conectar com o banco de dados MySQL
import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",     # Endereço do servidor (localhost = seu próprio computador)
        user="root",          # Nome de usuário do MySQL
        password="",  # Senha do MySQL (deixe em branco se não tiver)
        database="biblioteca" # Nome do banco de dados que será usado
    )

# Função para criar a tabela de livros, caso ela ainda não exista
def criar_tabela():
    conexao = conectar()        # Conecta ao banco
    cursor = conexao.cursor()   # Cria um cursor para executar comandos SQL
    cursor.execute('''          # Executa o comando SQL para criar a tabela
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,  # ID automático e chave primária
            titulo VARCHAR(255) NOT NULL,       # Título do livro (obrigatório)
            autor VARCHAR(255) NOT NULL,        # Autor do livro (obrigatório)
            ano INT NOT NULL                    # Ano de publicação (obrigatório)
        )
    ''')
    conexao.commit()     # Salva as alterações no banco
    conexao.close()      # Fecha a conexão com o banco

# Classe que representa um livro individual
class Livro:
    def __init__(self, id=None, titulo='', autor='', ano=0):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    # Representação do livro como string (texto), útil para exibir
    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano})"

# Classe principal que gerencia a biblioteca e os livros no banco de dados
class Biblioteca:
    def __init__(self):
        self.conexao = conectar()             # Conecta ao banco
        self.cursor = self.conexao.cursor()   # Cria o cursor para comandos SQL
        criar_tabela()                        # Garante que a tabela exista

    # Adiciona um novo livro ao banco de dados
    def adicionar_livro(self, titulo, autor, ano):
        self.cursor.execute('''
            INSERT INTO livros (titulo, autor, ano)
            VALUES (%s, %s, %s)
        ''', (titulo, autor, ano))           # Passa os dados como parâmetros
        self.conexao.commit()                # Salva no banco
        print(f"Livro '{titulo}' adicionado com sucesso!")

    # Lista todos os livros cadastrados
    def listar_livros(self):
        self.cursor.execute('SELECT * FROM livros')   # Busca todos os livros
        livros = self.cursor.fetchall()               # Pega os resultados
        if livros:
            print("---------------------")
            print("LISTA DE LIVROS:")
            for livro in livros:
                print(f"\n{livro[1]} por {livro[2]} ({livro[3]})")  # Exibe os dados
        else:
            print("Nenhum livro cadastrado.")

    # Atualiza as informações de um livro pelo ID
    def atualizar_livro(self, id, novo_titulo, novo_autor, novo_ano):
        self.cursor.execute('''
            UPDATE livros
            SET titulo = %s, autor = %s, ano = %s
            WHERE id = %s
        ''', (novo_titulo, novo_autor, novo_ano, id))  # Atualiza os dados
        self.conexao.commit()                          # Salva no banco
        print("Livro atualizado com sucesso!")

    # Deleta um livro pelo ID
    def deletar_livro(self, id):
        self.cursor.execute('DELETE FROM livros WHERE id = %s', (id,))
        self.conexao.commit()  # Remove o livro do banco
        print("\nLivro deletado com sucesso!")

    # Quando o objeto for destruído, a conexão com o banco será fechada
    def __del__(self):
        self.conexao.close()

# Função com o menu para o usuário interagir com a biblioteca
def menu():
    biblioteca = Biblioteca()  # Cria uma instância da classe Biblioteca

    while True:
        print("---------------------")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Sair")
        print("---------------------")
        opcao = input("Escolha uma opção: ")

        # Opção 1: adicionar novo livro
        if opcao == "1":
            titulo = input("\nTítulo do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano de publicação: "))
            biblioteca.adicionar_livro(titulo, autor, ano)

        # Opção 2: listar todos os livros
        elif opcao == "2":
            biblioteca.listar_livros()

        # Opção 3: atualizar dados de um livro
        elif opcao == "3":
            print("---------------------")
            id = int(input("ID do livro a ser atualizado: "))
            novo_titulo = input("Novo título: ")
            novo_autor = input("Novo autor: ")
            novo_ano = int(input("Novo ano: "))
            biblioteca.atualizar_livro(id, novo_titulo, novo_autor, novo_ano)

        # Opção 4: deletar um livro
        elif opcao == "4":
            print("---------------------")
            id = int(input("ID do livro a ser deletado: "))
            biblioteca.deletar_livro(id)

        # Opção 5: sair do programa
        elif opcao == "5":
            print("---------------------")
            print("\nSaindo...\n")
            break

        # Caso a opção digitada seja inválida
        else:
            print("---------------------")
            print("\nOpção inválida! Tente novamente.\n")

# Chama o menu para iniciar o programa
menu()
