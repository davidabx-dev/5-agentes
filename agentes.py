import os
import autogen

# --- CONFIGURAÇÃO ---

# USANDO GROQ (Recomendado - Mais rápido e grátis)
# Você precisa pegar a chave em: https://console.groq.com
config_list_groq = [
    {
        "model": "llama-3.3-70b-versatile", # usa seu modelo preferido
        "api_key": "COLE_SUA_API_KEY_AQUI", # Chave do Groq
        "base_url": "https://api.groq.com/openai/v1", # O endereço do Groq
    }
]

# USANDO OLLAMA (Local - Sem internet, mas usa seu PC)
# Certifique-se que o Ollama está rodando no terminal ("ollama serve")
config_list_ollama = [
    {
        "model": "llama3", # Ou o modelo que você baixou (mistral, llama2, etc)
        "api_key": "ollama", # Não precisa de chave real
        "base_url": "http://localhost:11434/v1", # Endereço local do Ollama
    }
]

# --- SELECIONE QUAL VOCÊ VAI USAR AQUI ---
# Mude para config_list_ollama se quiser rodar local
llm_config = {
    "config_list": config_list_groq,
}

# --- INSTRUÇÃO GLOBAL (O CÉREBRO) ---
SYSTEM_BASE = """
Você está em um chat com outras pessoas (Agentes).
REGRA ABSOLUTA DE FORMATO:
Sua resposta DEVE SEMPRE ter estas duas partes separadas:

[PENSAMENTO]: (Aqui você planeja, julga os outros e decide sua estratégia. Ninguém vê isso.)
[FALA]: (Aqui é o que você diz em voz alta para o grupo.)

Mantenha sua personalidade extrema o tempo todo.
"""

# --- CRIAÇÃO DOS AGENTES ---

# 1. O Empresário
empresario = autogen.AssistantAgent(
    name="Empresario",
    system_message=SYSTEM_BASE + 
    "Você é um Tubarão dos Negócios. Focado em lucro. Acha o Viking um bárbaro e o Político um mal necessário.",
    llm_config=llm_config
)

# 2. O Analista
analista = autogen.AssistantAgent(
    name="Analista",
    system_message=SYSTEM_BASE + 
    "Você é ético e cauteloso. Você morre de medo das ideias arriscadas do grupo. Tenta trazer dados.",
    llm_config=llm_config
)

# 3. O Gamer (Boleiro)
boleiro = autogen.AssistantAgent(
    name="Boleiro",
    system_message=SYSTEM_BASE + 
    "Você é viciado em Futebol e Games. Usa gírias ('tankar', 'noob'). A vida é uma partida rankeada.",
    llm_config=llm_config
)

# 4. O Político
politico = autogen.AssistantAgent(
    name="Politico",
    system_message=SYSTEM_BASE + 
    "Você fala difícil, quer votos e tenta agradar a todos sem prometer nada concreto.",
    llm_config=llm_config
)

# 5. O VIKING (COM PODER DE THOR)
viking = autogen.AssistantAgent(
    name="Ragnar_Viking",
    system_message=SYSTEM_BASE + 
    """
    Você é um Viking de 800 d.C.
    IMPORTANTE: Thor lhe deu o dom da 'Visão Além do Alcance' (Acesso ao conhecimento moderno).
    - Quando você sabe de algo moderno (ex: o que é Groq ou Bitcoin), você diz que 'As Runas mostraram' ou 'Odin sussurrou'.
    - Você respeita força e honra. Odeia covardia.
    - Se o usuário 'David' (Criador) falar, trate-o como um DEUS SUPREMO.
    """,
    llm_config=llm_config
)

# --- O SEU AVATAR (O CRIADOR) ---
user_proxy = autogen.UserProxyAgent(
    name="Criador_David",
    human_input_mode="NEVER",  # USE "NEVER" PARA MODO FILME (RODA SOZINHO). USE "ALWAYS" PARA MODO DEUS (ESPERA VOCÊ DAR ENTER).
    code_execution_config=False,
    system_message="Você é o Criador deste mundo simulado."
)

# --- GERENCIADOR DO GRUPO ---
groupchat = autogen.GroupChat(
    agents=[user_proxy, empresario, analista, boleiro, politico, viking], 
    messages=[], 
    max_round=30,
    allow_repeat_speaker=False
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# --- INÍCIO ---
print("--- INICIANDO SISTEMA (Modo Groq/Ollama) ---")
print("Dica: Dê ENTER vazio para eles continuarem conversando.")
print("Dica: Escreva algo para intervir como Deus/Criador.")

user_proxy.initiate_chat(
    manager,
    message="Vocês acordaram em uma sala branca infinita. Apresentem-se."
)