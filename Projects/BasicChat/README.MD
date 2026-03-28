## 🟢 Projeto 1 — Chat Agent Estruturado (Fundação)

### 🎯 Objetivo

Sair do “hello world” e entender:

- mensagens  
- estado  
- fluxo básico com LangGraph  

---

### 📌 Descrição

Um chat simples que:

- recebe input do usuário  
- mantém histórico  
- responde de forma consistente com um system prompt  

---

### 🧱 Componentes obrigatórios

- StateGraph  
- AgentState com `add_messages`  
- 1 node (`call_llm`)  
- loop de interação  

---

### 📈 Evolução dentro do projeto

#### Nível 1
Chat simples (sem memória persistente)

#### Nível 2
Adicionar personalidade via system prompt

#### Nível 3
Logging das mensagens (debug real)

---

### 🧠 O que você aprende

- Como o LangGraph gerencia estado  
- Estrutura mínima de um agente  
- Diferença entre input / output / state  