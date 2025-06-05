## 🚀 COMO ACESSAR O PROJETO

### ✅ Passos:

1️⃣ **Tenha o [MySQL Workbench](https://www.mysql.com/products/workbench/)** instalado e **importe o arquivo `biblioteca.sql`** no seu banco de dados.

2️⃣ **Abra o arquivo `poo.py` em um interpretador de código** como o **Visual Studio Code**, **PyCharm** ou outro de sua preferência.

3️⃣ **⚠️ ATENÇÃO:**  
   No arquivo `poo.py`, **altere a senha do banco de dados** para a **sua senha do MySQL Workbench**, se houver.  
   O usuário padrão está como `"root"`, mas você pode alterar se necessário.

```python
# Exemplo de onde alterar no código:
conexao = mysql.connector.connect(
    host="localhost",
    user="root",          # <- Você pode trocar "root" por outro nome
    password="SUA_SENHA", # <- Substitua pela sua senha do MySQL
    database="biblioteca"
)
