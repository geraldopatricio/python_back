from flask import Flask, request, jsonify
from mysql.connector import connect
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Função para criar uma conexão com o banco de dados
def create_db_connection():
    return connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Rota para criar um novo produto
@app.route('/produto', methods=['POST'])
def create_produto():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        codigo = request.json['codigo']
        produto = request.json['produto']

        cursor.execute("INSERT INTO tb_produto (codigo, produto) VALUES (%s, %s)", (codigo, produto))
        conn.commit()

        return jsonify({"message": "Produto criado com sucesso"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

# Rota para listar todos os produtos
@app.route('/produto', methods=['GET'])
def list_produtos():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, codigo, produto FROM tb_produto")
        produtos = cursor.fetchall()

        produtos_list = []
        for produto in produtos:
            produtos_list.append({
                "id": produto[0],
                "codigo": produto[1],
                "produto": produto[2]
            })

        return jsonify(produtos_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

# Rota para atualizar um produto
@app.route('/produto/<int:id>', methods=['PUT'])
def update_produto(id):
    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        codigo = request.json['codigo']
        produto = request.json['produto']

        cursor.execute("UPDATE tb_produto SET codigo = %s, produto = %s WHERE id = %s", (codigo, produto, id))
        conn.commit()

        return jsonify({"message": "Produto atualizado com sucesso"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

# Rota para deletar um produto
@app.route('/produto/<int:id>', methods=['DELETE'])
def delete_produto(id):
    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tb_produto WHERE id = %s", (id,))
        conn.commit()

        return jsonify({"message": "Produto deletado com sucesso"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()
