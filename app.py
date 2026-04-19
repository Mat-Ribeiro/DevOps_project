from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

@app.route('/')
def home():
    return "API de Tarefas rodando 🚀"

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    data = request.get_json()
    tarefas.append(data)
    return jsonify({"mensagem": "Tarefa adicionada!"})

@app.route('/tarefas/<int:index>', methods=['DELETE'])
def deletar_tarefa(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
        return jsonify({"mensagem": "Tarefa removida!"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)