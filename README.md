
# ⚽ Esquema Tático com IA – Backend

Este projeto é uma API Flask que utiliza a API da Google GenAI (Gemini) para gerar automaticamente esquemas táticos de futebol com base nos jogadores informados, a formação desejada e o estilo de jogo. Também realiza uma verificação de conteúdo ofensivo para garantir o uso responsável da ferramenta.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.11+**
* **Flask 3.1.1**
* **Flask-CORS**
* **Google GenAI API**
* **dotenv**
* **gunicorn** (produção)
* **Vercel** (deploy opcional)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` e adicione sua chave da API do Google GenAI:

```
GOOGLE_API_KEY=your_google_genai_api_key
```

---

## 🧠 Funcionalidades

* ✅ Geração automática de esquemas táticos com base em:

  * Lista de jogadores e suas habilidades
  * Formação desejada (ex: 4-3-3)
  * Estilo de jogo (ex: ofensivo, retranca, etc.)
* 🚫 Filtro de conteúdo ofensivo (homofobia, racismo, palavrões, etc.)
* 🔁 Formato de resposta padronizado em **JSON**
* 🌐 Suporte a CORS (Cross-Origin Resource Sharing)

---

## 📥 Endpoint

### `POST /esquema`

Gera um esquema tático com base nos dados enviados.

#### Corpo da requisição (JSON):

```json
{
  "jogadores": [
    "João - rápido e habilidoso",
    "Carlos - bom na bola aérea",
    "Lucas - marcação forte",
    "Rafael - criativo e ágil",
    "Pedro - chute potente"
  ],
  "formacao": "4-3-3",
  "estilo_jogo": "posse de bola"
}
```

#### Resposta esperada:

```json
{
  "formacao": "4-3-3",
  "estilo_de_jogo": "posse de bola",
  "posicionamento": [
    "Goleiro: Pedro - bom reflexo",
    "Zagueiro: Carlos - forte na bola aérea",
    ...
  ],
  "instrucoes_gerais": [
    "Pressionar alto",
    "Trocar passes curtos"
  ],
  "sugestao": "Treinar jogadas de bola parada"
}
```

#### Possíveis erros:

* `400 Bad Request` → Conteúdo ofensivo ou campos ausentes
* `500 Internal Server Error` → Falha na geração ou na IA

---

## 🔐 Segurança

* Verificação de linguagem ofensiva nos campos enviados
* Uso de variáveis de ambiente para proteger a chave da API
* CORS habilitado com configurações seguras por padrão

---

## ⚙️ Deploy

Este projeto pode ser facilmente implantado na [Vercel](https://vercel.com/) usando o seguinte `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

---

## 📄 Licença

Este projeto é de uso educacional e pessoal. Para fins comerciais, entre em contato com o autor.

---

## ✍️ Autor

**Nicolas (Nicão FPP)**
📸 Instagram: [@npnicolass](https://instagram.com/npnicolass)

---

