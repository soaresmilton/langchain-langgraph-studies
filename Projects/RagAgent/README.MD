# PROJETO RAG

1 - Primeiro definimos o loader.py ==> responsável por carregar os arquivos e retorna uma lista de Documentos, onde cada documento é um dicionário com as chaves 'content' e 'metadata'.

2 - Segundo passo é o chunking.py ==> responsável por dividir os documentos em pedaços menores (chunks) para facilitar a indexação e recuperação.

3 - Terceiro passo é o embedding.py ==> responsável por transformar os chunks em vetores numéricos usando um modelo de embedding, como o OpenAI Embeddings.

4 - vector_store.py ==> responsável por armazenar os vetores de embedding em um banco de dados vetorial, como o FAISS, para permitir a recuperação eficiente.

5 - retrieval.py ==> responsável por recuperar os chunks relevantes do banco de dados vetorial com base em uma consulta de texto.