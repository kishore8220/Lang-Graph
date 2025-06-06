from chains import generation_chain , reflection_chain
from langchain_core.messages import BaseMessage , HumanMessage
from langgraph.graph import END , MessageGraph
from typing import List , Sequence


GENEARTE = "generate"
REFLECT = "reflect"
graph = MessageGraph()

def geneartive_graph(state):
    return generation_chain.invoke({
        "messages":state
    })

def reflective_state(state):
    res = reflection_chain.invoke({
        "messages":state
    })
    return [HumanMessage(content=res)]

graph.add_node(GENEARTE , geneartive_graph)
graph.add_node(REFLECT , reflective_state)

graph.set_entry_point(GENEARTE)

def should_continue(state):
    if (len(state)>4):
        return END
    return REFLECT

graph.add_conditional_edges(
    GENEARTE,
    should_continue,
    {
        REFLECT: REFLECT,
        END: END,
    }
)
graph.add_edge(REFLECT , GENEARTE)

app = graph.compile()

print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))
print(response.content)
