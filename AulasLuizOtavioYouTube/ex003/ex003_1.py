from typing import TypedDict, Annotated
from rich import print
import operator

from langgraph.graph import StateGraph, add_messages


# 1 - Definir o meu estado ===> Importante entender o conceito de State para o graph, pois é tudo state nesse cara
class State(TypedDict):
    nodes_path: Annotated[list[str], operator.add]

# 2 -  Definir os nodes
def node_a(state: State) -> State:
    nodes_path = state['nodes_path']
    output_state: State = {'nodes_path': ["Miltinho"]}
    print("> node a", f"{state=}", f"{output_state=}")
    return output_state

def node_b(state: State) -> State:
    nodes_path = state['nodes_path']
    output_state: State = {'nodes_path': ["Soares"]}
    print("> node b", f"{state=}", f"{output_state=}")
    return output_state

# 3 -  Definir o builder do grafo
builder = StateGraph(State)
builder.add_node('A', node_a)
builder.add_node('B', node_b)

# 4 - conectar as edges
builder.add_edge('__start__', 'A')
builder.add_edge('A', 'B')
builder.add_edge('B', '__end__')

# Compilar o grafo
graph = builder.compile()

# Gerar imagem do grafo
#graph.get_graph().draw_mermaid_png(output_file_path="./ex003/graph_image.png")

# Pegar o resultado do grapho
response = graph.invoke({"nodes_path": []})

# Resultado de todo o grapho
print()
print(f'{response=}')
print()