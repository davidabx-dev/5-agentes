# 🤖 5-Agentes: Simulação de Sociedade Autônoma com AutoGen

> "O que acontece quando você tranca um Viking de 800 d.C., um Tubarão dos Negócios e um Gamer numa sala virtual?"

Este projeto é um experimento de **Sistemas Multi-Agentes (MAS)** utilizando o framework **Microsoft AutoGen** e LLMs de alta performance via **Groq API** (Llama 3 / Mixtral).

O objetivo foi testar a **persistência de persona** e a interação autônoma (sem humanos) até o limite da infraestrutura.

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![AI](https://img.shields.io/badge/AI-AutoGen%20%7C%20Groq-orange)

## 📸 O Caos em Imagens

### 1. O Conflito de Gerações
O Agente "Boleiro" (Gamer) acusando o Analista de ser "noob", enquanto o Viking tenta entender o conceito de "Dólar".
![Conversa Engraçada](Nome_da_sua_foto_1.png)

### 2. O Crash (Sucesso Absoluto)
O sistema rodou em loop tão intenso que consumiu **100.000 tokens** em poucos minutos, estourando o Rate Limit da API.
![Rate Limit Error](Nome_da_sua_foto_do_erro.png)

---

## 🧠 Os Agentes (Personas)

Cada agente possui um "System Prompt" complexo para garantir comportamentos distintos:

* **🛡️ Ragnar (O Viking):** Acredita que a internet é "Visão de Odin" e APIs são "Runas". Odeia covardia e não entende dinheiro moderno.
* **💼 Reginald (O Empresário):** Focado puramente em ROI, Lucro e "Business". Tenta monetizar a sala branca.
* **🎮 O Boleiro (Gamer):** Usa gírias como "tankar", "noob" e vê o mundo como uma partida ranqueada.
* **⚖️ O Analista:** Tenta calcular os riscos da situação (e é ignorado por todos).
* **🗳️ O Político:** Tenta criar alianças e falar bonito sem resolver nada.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Orquestração:** [Microsoft AutoGen](https://github.com/microsoft/autogen)
* **LLM Engine:** Groq API (Inference LPU)
* **Modelos:** `llama-3.3-70b` e `mixtral-8x7b`

## 🚀 Como Rodar

1. Clone o repositório:
```bash
git clone [https://github.com/davidabx-dev/5-agentes.git](https://github.com/davidabx-dev/5-agentes.git)
```
---

2. Instale as dependências:
```bash
pip install pyautogen openai

```

---

3. Configure sua API Key da Groq no arquivo `agentes.py`:
```bash
"api_key": "SUA_CHAVE_AQUI"
```

---

4. Execute a simulação:
```bash
python agentes.py
```

---

## 📜 Licença

Este projeto está licenciado sob a licença **MIT**.
Sinta-se livre para usar, estudar e modificar o código para fins de aprendizado.

---

## 👨‍💻 Autor

**DavidABx**

> "Desenvolvido com foco em **Performance** e **Arquitetura de Software**."

* **GitHub:** [@davidabx-dev](https://github.com/davidabx-dev)
* **LinkedIn:** [Conectar no LinkedIn](SEU_LINK_AQUI)
