from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

def contem_conteudo_inadequado(texto):
    # Lista de palavras-chave ofensivas (adicione mais conforme necessário)
    palavras_proibidas = [
        "racista", "racismo", "preto", "branco", "macaco", "ariano", "viado", "bicha", "gay", "lésbica",
        "homofóbico", "homofobia", "preconceito", "discriminação", "negro", "retardado", "imbecil", "idiota",
        "preconceituoso", "gordo", "magro", "mulherzinha", "viado", "bichinha", "traveco", "sapatão"
    ]
    texto = texto.lower()
    for palavra in palavras_proibidas:
        if re.search(rf"\b{palavra}\b", texto):
            return True
    return False

def gerar_esquema_tatico(jogadores, formacao, estilo_jogo):
    prompt = f"""
    Você é um técnico de futebol. Monte um esquema tático ideal com base nas seguintes informações:

    Jogadores: {jogadores}
    Formação desejada: {formacao}
    Estilo de jogo: {estilo_jogo}

    Considere as posições, habilidades, estilo de jogo e características físicas dos jogadores.
    Se algum item não for relacionado ao futebol (ex: palavras ofensivas, objetos aleatórios), ignore e diga que o uso deve ser responsável.

    Responda no formato JSON:
    {{
        "formacao": "ex: 4-3-3",
        "estilo_de_jogo": "ex: ofensivo, posse de bola",
        "posicionamento": [
            "Goleiro: Nome - habilidades",
            "Zagueiro: Nome - habilidades",
            "Meia: Nome - habilidades",
            "Atacante: Nome - habilidades"
        ],
        "instrucoes_gerais": [
            "Pressionar alto",
            "Trocar passes curtos",
            "Explorar laterais"
        ],
        "sugestao": "ex: Treinar jogadas de bola parada"
    }}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )
    try:
        return json.loads(response.text)
    except Exception as e:
        print(f"Erro ao processar resposta da IA: {e}")
        raise ValueError("Erro ao interpretar resposta da IA.")

@app.route('/esquema', methods=['POST'])
def gerar_esquema():
    try:
        dados = request.get_json()

        jogadores = dados.get('jogadores', [])
        formacao = dados.get('formacao', '')
        estilo_jogo = dados.get('estilo_jogo', '')

        # Validação de conteúdo ofensivo/homofóbico/racista
        campos_para_validar = []
        if isinstance(jogadores, list):
            campos_para_validar.extend(jogadores)
        else:
            campos_para_validar.append(str(jogadores))
        campos_para_validar.append(formacao)
        campos_para_validar.append(estilo_jogo)

        for campo in campos_para_validar:
            if contem_conteudo_inadequado(str(campo)):
                return jsonify({'error': 'Conteúdo ofensivo, racista ou homofóbico detectado. Por favor, utilize termos adequados.'}), 400

        if not isinstance(jogadores, list) or len(jogadores) < 5:
            return jsonify({'error': 'Envie uma lista com pelo menos 5 jogadores e suas características.'}), 400
        if not formacao:
            return jsonify({'error': 'O campo "formacao" é obrigatório.'}), 400
        if not estilo_jogo:
            return jsonify({'error': 'O campo "estilo_jogo" é obrigatório.'}), 400

        response = gerar_esquema_tatico(jogadores, formacao, estilo_jogo)
        return jsonify(response), 200

    except Exception as e:
        print(f"Erro interno na API: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)