import operator
from typing import TypedDict, Annotated, Literal
from rich import print
from dataclasses import dataclass
from langgraph.graph import END, StateGraph, add_messages, START


@dataclass
class State:
    nodes_path: Annotated[list[str], operator.add]
    current_number: int = 0

# 2 -  Definir os nodes
def node_a(state: State) -> State:
    output_state: State = State(nodes_path=['Miltinho'], current_number=state.current_number)
    print("> node a", f"{state=}", f"{output_state=}")
    return output_state

def node_b(state: State) -> State:
    output_state: State = State(nodes_path=['Soares'], current_number=state.current_number)
    print("> node b", f"{state=}", f"{output_state=}")
    return output_state

def node_c(state: State) -> State:
    output_state: State = State(nodes_path=['Moraes'], current_number=state.current_number)
    print("> node c", f"{state=}", f"{output_state=}")
    return output_state


# Função condicional
def the_conditional(state: State) -> Literal["node B", "node C"]:
    if state.current_number >= 50:
        return 'node C'
    
    return 'node B'

# 3 -  Definir o builder do grafo
builder = StateGraph(State)
builder.add_node('A', node_a)
builder.add_node('B', node_b)
builder.add_node('C', node_c)

# 4 - conectar as edges
builder.add_edge(START, 'A')
builder.add_conditional_edges('A', the_conditional, {
    'node B': 'B',
    'node C': 'C'
})
builder.add_edge('B',  END)
builder.add_edge('C',  END)


# Compilar o grafo
graph = builder.compile()


# Pegar o resultado do grapho
response = graph.invoke(State(nodes_path=[], current_number=50))

# Resultado de todo o grapho
print()
print(f'{response=}')
print()


# Gerar imagem do grafo
graph.get_graph().draw_mermaid_png(output_file_path="./ex003/graph2_image.png")
