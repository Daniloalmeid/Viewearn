from flask import Flask, render_template, request, jsonify
from solana_transfer import enviar_token_para_usuario

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard-user')
def dashboard_user():
    return render_template('dashboard-user.html')

@app.route('/dashboard-creator')
def dashboard_creator():
    return render_template('dashboard-creator.html')

@app.route('/register-creator')
def register_creator():
    return render_template('register-creator.html')

# ✅ ROTA PARA ENVIAR TOKENS AO USUÁRIO
@app.route("/recompensar", methods=["POST"])
def recompensar_usuario():
    data = request.json
    wallet = data.get("wallet")
    tokens = data.get("tokens", 1.0)

    if not wallet:
        return jsonify({"status": "erro", "mensagem": "Carteira não informada"}), 400

    try:
        tx_response = enviar_token_para_usuario(wallet, tokens)
        return jsonify({"status": "sucesso", "tx": tx_response}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
