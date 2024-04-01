from nodes import getAnswers, Answer
import pyvis
import networkx as nx


def app():
    

    clustering_algorithms_dt = nx.DiGraph()
    
    
    answers : list[Answer] = getAnswers()
    
    for answer in answers:
        clustering_algorithms_dt.add_edge(answer.source, answer.target, description = answer.description, label = answer.response)
        
    net = pyvis.network.Network(notebook=True, cdn_resources='remote', directed=True,
                                    height="100%", width="100%", bgcolor="#e8f1ff", font_color="#000c1f")
    
    net.force_atlas_2based(damping=1)
    net.toggle_stabilization(False)
    
    
    for node in clustering_algorithms_dt.nodes:
        if (node.question == "Data Characteristics"):
            net.add_node(node.question, label=f"{node.question}", title = f"{node.description}", color="red", size = 35)
        
        else:
            net.add_node(node.question, label=f"{node.question}", title = f"{node.description}")
        
    
    for edge in clustering_algorithms_dt.edges:
        net.add_edge(edge[0].question, edge[1].question , title=clustering_algorithms_dt.edges[edge]["description"], label=clustering_algorithms_dt.edges[edge]["label"])

    net.show("index.html")

    with open("index.html", "r") as file:
        data = file.readlines()
    with open("index.html", "w") as file:
        for line in data:
            if '<meta charset="utf-8">' in line:
                file.write(line)
                file.write(
                    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
                file.write(
                    '<link rel="stylesheet" href="index.css">\n')
            else:
                file.write(line)
    print("===> Modified index.html")
    
if __name__ == "__main__":
    app()
