# app.py (Trecho)

QUIZ_DATA = [
    # Heian Shodan
    {"id": 1, "pergunta": "Qual é o primeiro movimento do Heian Shodan?", "opcoes": ["Gedan Barai (Kiba Dachi)", "Gedan Barai (Zenkutsu Dachi)", "Oi Zuki (Zenkutsu Dachi)"], "resposta_correta": "Gedan Barai (Zenkutsu Dachi)", "movimento_correto": "Gedan Barai"},
    {"id": 2, "pergunta": "Quantos movimentos tem o Heian Shodan?", "opcoes": ["20", "21", "25"], "resposta_correta": "21", "movimento_correto": "Número de movimentos"},
    {"id": 3, "pergunta": "Qual bloqueio alto protege a cabeça no Shodan?", "opcoes": ["Age Uke", "Gedan Barai", "Shuto Uke"], "resposta_correta": "Age Uke", "movimento_correto": "Age Uke"},

    # Heian Nidan
    {"id": 4, "pergunta": "Qual kata introduz movimentos em 'T' e troca de mãos?", "opcoes": ["Heian Nidan", "Heian Shodan", "Heian Sandan"], "resposta_correta": "Heian Nidan", "movimento_correto": "Heian Nidan"},
    {"id": 5, "pergunta": "Qual Heian introduz o chute mae-geri?", "opcoes": ["Heian Shodan", "Heian Nidan", "Heian Sandan"], "resposta_correta": "Heian Nidan", "movimento_correto": "Heian Nidan"},

    # Heian Sandan
    {"id": 6, "pergunta": "Qual técnica de defesa predomina no Heian Shodan?", "opcoes": ["Shuto-uke", "Gedan-barai", "Soto-uke"], "resposta_correta": "Gedan-barai", "movimento_correto": "Gedan-barai"},
    {"id": 7, "pergunta": "Qual é uma característica do Sandan?", "opcoes": ["Mais rotações", "Menos kiais", "Somente bloqueios baixos"], "resposta_correta": "Mais rotações", "movimento_correto": "Rotações"},

    # Heian Yondan
    {"id": 8, "pergunta": "Em qual Heian aparece o movimento com o salto de perna (yori)?", "opcoes": ["Heian Yondan", "Heian Shodan", "Heian Nidan"], "resposta_correta": "Heian Yondan", "movimento_correto": "Yondan"},
    {"id": 9, "pergunta": "Quantos movimentos possui o kata Heian Yodan", "opcoes": ["27", "26", "25"], "resposta_correta": "27", "movimento_correto": "27"},

    # Heian Godan
    {"id": 10, "pergunta": "Qual é uma marca do Heian Godan?", "opcoes": ["Movimentos mais rápidos", "Menos postura básica", "Sem kiais"], "resposta_correta": "Movimentos mais rápidos", "movimento_correto": "Velocidade"},
    {"id": 11, "pergunta": "Qual kata geralmente é ensinado por último entre os cinco heians?", "opcoes": ["Heian Godan", "Heian Shodan", "Heian Sandan"], "resposta_correta": "Heian Godan", "movimento_correto": "Godan"},

    # Perguntas mistas sobre termos e técnicas
    {"id": 12, "pergunta": "O que significa 'Gedan Barai'?", "opcoes": ["Bloqueio baixo", "Bloqueio alto", "Golpe de punho"], "resposta_correta": "Bloqueio baixo", "movimento_correto": "Gedan Barai"},
    {"id": 13, "pergunta": "O que é 'Gyaku Zuki'?", "opcoes": ["Punho invertido (contraposto)", "Bloqueio lateral", "Chute frontal"], "resposta_correta": "Punho invertido (contraposto)", "movimento_correto": "Gyaku Zuki"},
    {"id": 14, "pergunta": "Qual postura é longa e usada para avançar (front stance)?", "opcoes": ["Zenkutsu Dachi", "Kiba Dachi", "Sanchin Dachi"], "resposta_correta": "Zenkutsu Dachi", "movimento_correto": "Zenkutsu Dachi"},
    {"id": 15, "pergunta": "Qual é o propósito de praticar os cinco Heian?", "opcoes": ["Progredir técnica e coordenação", "Apenas competição", "Exercício aeróbico"], "resposta_correta": "Progredir técnica e coordenação", "movimento_correto": "Objetivo"},
    {"id": 16, "pergunta": "Qual movimento costuma preceder um Oi Zuki em muitos katas?", "opcoes": ["Gedan Barai", "Age Uke", "Shuto Uke"], "resposta_correta": "Gedan Barai", "movimento_correto": "Gedan Barai"},
    {"id": 17, "pergunta": "Em treinos, o que se busca ao executar Kiai?", "opcoes": ["Focar energia e respiração", "Melhorar equilíbrio", "Alongar músculos"], "resposta_correta": "Focar energia e respiração", "movimento_correto": "Kiai"},
    {"id": 18, "pergunta": "Qual técnica é conhecida como 'mão de lâmina'?", "opcoes": ["Shuto Uke", "Age Uke", "Gedan Barai"], "resposta_correta": "Shuto Uke", "movimento_correto": "Shuto Uke"},
    {"id": 19, "pergunta": "Qual é o termo para 'bloqueio médio'?", "opcoes": ["Uchi Uke", "Age Uke", "Gedan Barai"], "resposta_correta": "Uchi Uke", "movimento_correto": "Uchi Uke"},
    {"id": 20, "pergunta": "Quantos movimentos possui o kata Heian Sandan", "opcoes": ["20", "21", "22"], "resposta_correta": "20", "movimento_correto": "20"},

    # Perguntas adicionais para completar o banco
    {"id": 21, "pergunta": "Qual é o significado literal de 'Heian'?", "opcoes": ["Paz e tranquilidade", "Força máxima", "Velocidade"], "resposta_correta": "Paz e tranquilidade", "movimento_correto": "Heian"},
    {"id": 22, "pergunta": "Qual kata contém o movimento 'Tetsui Uchi'?", "opcoes": ["Heian Shodan", "Heian Godan", "Heian Yondan"], "resposta_correta": "Heian Shodan", "movimento_correto": "Tetsui Uchi"},
    {"id": 23, "pergunta": "Qual técnica é usada para atacar com a borda da mão?", "opcoes": ["Shuto Uke", "Gedan Barai", "Gyaku Zuki"], "resposta_correta": "Shuto Uke", "movimento_correto": "Shuto Uke"},
    {"id": 24, "pergunta": "O que costuma acompanhar um Kiai?", "opcoes": ["Exalação forte", "Inalação profunda", "Pausa respiratória"], "resposta_correta": "Exalação forte", "movimento_correto": "Kiai"},
    {"id": 25, "pergunta": "Qual é o objetivo de treinar várias katas seguidas?", "opcoes": ["Construir memória muscular", "Perder peso", "Aprender música"], "resposta_correta": "Construir memória muscular", "movimento_correto": "Memória muscular"},
    {"id": 26, "pergunta": "Qual kata costuma incluir movimentos de defesa e contra-ataque rápidos?", "opcoes": ["Heian Godan", "Heian Nidan", "Heian Shodan"], "resposta_correta": "Heian Godan", "movimento_correto": "Godan"},
    {"id": 27, "pergunta": "Qual técnica é um bloco descendente?", "opcoes": ["Gedan Barai", "Age Uke", "Shuto Uke"], "resposta_correta": "Gedan Barai", "movimento_correto": "Gedan Barai"},
    {"id": 28, "pergunta": "Qual é o termo para 'postura do cavalo'?", "opcoes": ["Kiba Dachi", "Zenkutsu Dachi", "Sanchin Dachi"], "resposta_correta": "Kiba Dachi", "movimento_correto": "Kiba Dachi"},
    {"id": 29, "pergunta": "Qual dos cinco Heian é tipicamente o mais avançado tecnicamente?", "opcoes": ["Heian Godan", "Heian Shodan", "Heian Nidan"], "resposta_correta": "Heian Godan", "movimento_correto": "Godan"},
    {"id": 30, "pergunta": "Qual é a melhor prática ao estudar kata?", "opcoes": ["Praticar devagar e corrigir forma", "Correr rápido sem corrigir", "Executar apenas mentalmente"], "resposta_correta": "Praticar devagar e corrigir forma", "movimento_correto": "Prática correta"}
]

# app.py

from flask import Flask, render_template, request, redirect, url_for, session
import random
import copy
import os

app = Flask(__name__)
# Use SECRET_KEY from environment in production; fallback for local dev
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key')

# Usamos o `QUIZ_DATA` definido no início do arquivo (com as perguntas preenchidas).

# --- Rotas da Aplicação ---

@app.route('/')
def home():
    """Página inicial/de boas-vindas."""
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Gerencia o quiz: exibe perguntas (GET) e processa respostas (POST)."""
    
    # Ao carregar a página (GET)
    if request.method == 'GET':
        # Limpa resultados anteriores
        session.pop('respostas_usuario', None)

        # Criamos uma cópia embaralhada das perguntas e das opções para exibir
        perguntas_para_exibir = copy.deepcopy(QUIZ_DATA)
        random.shuffle(perguntas_para_exibir)
        for p in perguntas_para_exibir:
            random.shuffle(p['opcoes'])

        # Seleciona apenas 20 perguntas para a execução (ou menos se o banco for menor)
        perguntas_para_exibir = perguntas_para_exibir[:20]

        # Salva na sessão os IDs das perguntas que foram exibidas (para avaliação posterior)
        session['perguntas_em_exibicao'] = [p['id'] for p in perguntas_para_exibir]

        # Envia a lista embaralhada de perguntas para o template
        return render_template('quiz.html', perguntas=perguntas_para_exibir)

    # Ao enviar o formulário (POST)
    elif request.method == 'POST':
        # Obtém todas as respostas enviadas pelo formulário
        respostas_usuario = request.form 
        
        # Armazena na sessão para uso na página de resultados
        session['respostas_usuario'] = respostas_usuario.to_dict() 
        
        # Redireciona para a página de resultados
        return redirect(url_for('results'))

@app.route('/results')
def results():
    """Calcula a pontuação e exibe os resultados detalhados."""
    
    # 1. Recupera as respostas da sessão e a lista de perguntas que foram exibidas
    respostas_usuario = session.get('respostas_usuario')
    perguntas_exibidas = session.get('perguntas_em_exibicao')
    if not respostas_usuario or not perguntas_exibidas:
        # Se não houver respostas ou perguntas exibidas na sessão, redireciona para o quiz
        return redirect(url_for('quiz'))

    acertos = 0
    feedback_detalhado = []

    # 2. Compara as respostas do usuário apenas com as perguntas que foram exibidas
    for pergunta_id in perguntas_exibidas:
        # garante tipo int
        pid = int(pergunta_id)
        pergunta = next((p for p in QUIZ_DATA if p['id'] == pid), None)
        if pergunta is None:
            continue

        chave_resposta = f"pergunta_{pid}"
        resposta_dada = respostas_usuario.get(chave_resposta)

        esta_correta = (resposta_dada == pergunta['resposta_correta'])
        if esta_correta:
            acertos += 1

        feedback_detalhado.append({
            'pergunta': pergunta['pergunta'],
            'sua_resposta': resposta_dada,
            'resposta_correta': pergunta['resposta_correta'],
            'esta_correta': esta_correta
        })

    # 5. Envia os dados para o template
    return render_template(
        'results.html', 
        acertos=acertos, 
        total_perguntas=len(perguntas_exibidas),
        feedback=feedback_detalhado
    )

if __name__ == '__main__':
    # Em produção o servidor WSGI (gunicorn) será usado; para desenvolvimento:
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)