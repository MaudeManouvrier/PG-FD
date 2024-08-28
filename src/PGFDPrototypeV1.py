# https://github.com/MaudeManouvrier/PG-FD
# Please refer to the paper: Maude Manouvrier and Khalid Belhajjame, PG-FD: Mapping Functional Dependencies to the Future Property Graph Schema Standard, submitted.

import networkx as nx # for graph pattern
import re # for ascii art notation
import functional_dependencies # for FD

#to define a graph pattern - nodes should be defined in the same order of the graph pattern, x is the first node, y the second ...
def defineGraphPattern():
    GP = nx.MultiDiGraph()
    nbNodes = int(input("Number of nodes:"))
    nbEdges = int(input("Number of edges:"))
    for n in range(nbNodes):
        L = input("Node label:")
        GP.add_node(L)
    for e in range(nbEdges):
        el = input("Edge label:")
        n1l = input("Node 1 label:")
        n2l = input("Node 2 label:")
        GP.add_edge(n1l,n2l,label=el)
    return GP

# Graph Pattern of the Example of Figure 3
def GPFigure3():
    GP = nx.MultiDiGraph()
    GP.add_node("y", label="Person")
    GP.add_node("x", label="Article")
    GP.add_edge("y", "x", key=0, label="AuthorOf")
    GP.add_edge("y", "x", key=1, label="ReviewerOf")
    return GP, [], False

# Graph Pattern of the Example of Figure 4
def GPFigure4():
    GP = nx.MultiDiGraph()
    GP.add_node("y", label="Conf")
    GP.add_node("x", label="Article")
    GP.add_edge("x", "y", key=0, label="SubmittedTo")
    GP.add_node("y'", label="Conf")
    GP.add_node("x'", label="Article")
    GP.add_edge("x'", "y'", key=0, label="SubmittedTo")
    return GP, ["x.title=x'.title","y.id=y'.id"], ["x.id=x'.id"]

# Graph Pattern of the Example of Figure 3 in ASCII format
def GPAsciiFigure3():
    GP = "(y:Person)-[:AuthorOf]->(x:Article)<-[:ReviewerOf]-(y:Person)"
    return GP, [], False

# Graph Pattern of the Example of Figure 4 in ASCII format
def GPAsciiFigure4():
    GP = "(x:Article)-[:SubmittedTo]->(y:Conf)\n(x':Article)-[:SubmittedTo]->(y':Conf)"
    return GP, ["x.title=x'.title","y.id=y'.id"], ["x.id=x'.id"]

# Graph Pattern of the Example Q1 of (Fan et al., 2017)
def GPGEDQ1():
    GP = nx.MultiDiGraph()
    GP.add_node("y", label="Person")
    GP.add_node("x", label="Product")
    GP.add_edge("y", "x", key=0, label="create")
    return GP, ['x .type = "video game"'], ['y.type = "programmer"']

# Graph Pattern of the Example Q2 of (Fan et al., 2017)
def GPGEDQ2():
    GP = nx.MultiDiGraph()
    GP.add_node("x", label="Country")
    GP.add_node("y", label="City")
    GP.add_node("z", label="City")
    GP.add_edge("x", "z", key=0, label="capital")
    GP.add_edge("x", "y", key=0, label="capital")
    return GP, [], ["y.name = z.name"]

# Graph Pattern of the Example Q7 of (Fan et al., 2017)
def GPGEDQ7():
    GP = nx.MultiDiGraph()
    GP.add_node("x", label="Album")
    GP.add_node("y", label="Album")
    return GP, ["x.title = y.title",  "x.release = y.release"], ["x.id = y.id"]


# From ChatGPT and adapted by MM
def cypher_ascii_to_networkx(cypher_ascii):
    # Create empty MultiDiGraph
    G = nx.MultiDiGraph()

    # Define pattern like example of figure 4
    pattern = r'\((.*?)\)-\[:(.*?)\]->\((.*?)\)<-\[:(.*?)\]-\((.*?)\)'

    matches = re.findall(pattern, cypher_ascii)

    # Add nodes and edges in MultiDiGraph
    for match in matches:
        target1, edge1_label, source, edge2_label, target2 = match
        G.add_node(source[:source.index(":")], label=source[source.index(":")+1:])
        G.add_node(target1[:target1.index(":")], label=target1[target1.index(":")+1:])
        G.add_node(target2[:target2.index(":")], label=target2[target2.index(":")+1:])
        G.add_edge(source[:source.index(":")], target1[:target1.index(":")],key=0, label=edge1_label)
        G.add_edge(source[:source.index(":")], target2[:target2.index(":")],key=1, label=edge2_label)
        return G

    # Define pattern like (source)-[:edgeLabel]->(target)
    pattern = r'\((.*?)\)-\[:(.*?)\]->\((.*?)\)'

    matches = re.findall(pattern, cypher_ascii)
    if matches == []:
        # Define pattern like (target)<-[:edgeLabel]-(source)
        pattern = r'\((.*?)\)<-\[:(.*?)\]-\((.*?)\)'
        matches = re.findall(pattern, cypher_ascii)
    # Add nodes and edges in MultiDiGraph
    for match in matches:
        source, edge_label, target = match
        G.add_node(source[:source.index(":")], label=source[source.index(":")+1:])
        G.add_node(target[:target.index(":")], label=target[target.index(":")+1:])
        G.add_edge(source[:source.index(":")], target[:target.index(":")], label=edge_label)
        return G


# From ChatGPT
def networkx_to_cypher_ascii(graph):
    cypher_ascii = ""
    for source, target, attrs in graph.edges(data=True):
        if "x" in source:
            source_label = f"({source})"
        else:
            source_label = f"({source}:{graph.nodes[source]['label']})"
        if "x" in target:
            target_label = f"({target})"
        else:
            target_label = f"({target}:{graph.nodes[target]['label']})"
        edge_label = attrs['label']
        cypher_ascii += f"{source_label}-[:{edge_label}]->{target_label}\n"
    return cypher_ascii.strip()

# Inverse (source)->[:edgeLabel]-(target) into (target)-[:edgeLabel]<-(source)
def inverseAscii(cypher_ascii):
    inverseAscii = ""
    pattern = r'\((.*?)\)-\[:(.*?)\]->\((.*?)\)'
    matches = re.findall(pattern, cypher_ascii)

    for match in matches:
        source, edge_label, target = match
        inverseAscii+= "(" + target + ")" + "<-" + "[:" + edge_label + "]-" + "(" + source + ")"
    return inverseAscii

# To create the correct WITHIN
def merge_cypher_strings(cypher_string):
    merged_cypher_string = ""
    parts = cypher_string.split("\n")
    merged_parts = []
    nbmerged = 0

    for part in parts:
        if part not in merged_parts:
            if nbmerged == 1:
                merged_parts.append(inverseAscii(part).replace("(x)",""))
            if(nbmerged==0):
                merged_parts.append(part)
                nbmerged += 1
    #if the second strings begins by a node (i.e. a parenthesis)
    if merged_parts[1][0]=="(":
        merged_cypher_string = "".join(merged_parts[::-1])
    else: merged_cypher_string = "".join(merged_parts)

    return merged_cypher_string

# To translate GED into PG-Schema
def GED2PGS(GP,X,Y):
    constraint = "FOR ("
    litteralX = ""
    litteralY = ""
    nodes = []
    for node_id, node_data in GP.nodes(data=True):
        nodes+=[node_id]

    # If DF is emptyset -> False
    if X == [] and Y == False:
        if len(nodes)==2 and GP.number_of_edges()!=0:
            constraint += "x:"+GP.nodes['x']['label']+")\nCOUNT 0 OF " +merge_cypher_strings(networkx_to_cypher_ascii(GP))

    elif X == [] and Y != []:
        constraint += "x:"+GP.nodes['x']['label']+")\nMANDATORY "
        for litteral in Y:
            litteralY += litteral
            litteralY +=","
        constraint += litteralY[:len(litteralY)-1]
        if GP.number_of_edges()!=0:
            constraint += " WITHIN " + networkx_to_cypher_ascii(GP).split()[0]

    elif X != [] and Y != []:
        constraint += "x:"+GP.nodes['x']['label']+")"
        # Y contains an id litteral
        if len(Y)==1 and 'id' in Y[0]:
            constraint += "\nIDENTIFIER "
            for litteral in X:
                litteralX += litteral[:litteral.index("=")]
                litteralX +=","
            constraint += litteralX[:len(litteralX)-1]
        else:
            constraint += "\nWHERE "
            for litteral in X:
                litteralX += litteral
                litteralX +=","
            constraint += litteralX[:len(litteralX)-1]
            constraint += "\nMANDATORY "
            for litteral in Y:
                litteralY += litteral
                litteralY +=","
            constraint += litteralY[:len(litteralY)-1]
        if GP.number_of_edges()!=0:
            constraint += " WITHIN " + networkx_to_cypher_ascii(GP).split()[0]

    return constraint


# Graph Pattern of the Example of Figure 1
def GPFigure1():
    GP = nx.MultiDiGraph()
    GP.add_node("y", label="Conf")
    GP.add_node("x", label="Article")
    GP.add_edge("x", "y", key=0, label="SubmittedTo")
    return GP, ["exists edge e","L(e)=SubmittedTo"], ["(x)-[e]->(y)"]

# To Translate GD into PG-Schema
def GD2PGS(GP,X,Y):
    constraint = "FOR ("
    litteralX = ""
    litteralY = ""
    nodes = []
    for node_id, node_data in GP.nodes(data=True):
        nodes+=[node_id]
    constraint += "x:"+GP.nodes['x']['label']+")\nMANDATORY "

    if "exists edge" in X[0]:
        variable = X[0][len("exists edge "):]
        egde_label = X[1][X[1].index("=")+1:]

        pattern = r'\((.*?)\)-\[(.*?)\]->\((.*?)\)'
        matches = re.findall(pattern, Y[0])
        for match in matches:
            source, edge, target = match

        constraint += edge + "," + target + " WITHIN " + "(" + source + ")" + "-" + "[" + edge + ":" + egde_label + "]-" + "(" + target + ":" + GP.nodes['y']['label'] + ")"

    elif "exists node" in X[0]:
        variable = X[0][len("exists node "):]
        node_label = X[1][X[1].index("=")+1:]

        pattern = r'\((.*?)\)->\((.*?)\)'
        matches = re.findall(pattern, Y[0])
        for match in matches:
            source, target = match
        constraint += "e," + target + " WITHIN " + "(" + source + ")" + "-" + "[e]" +"-(" + target + ":" + GP.nodes['y']['label'] + ")"
    return constraint

#gFD example of our article
def gFDArticleExample():
    L = "Conf"
    P = {"Acronym","ConfName"}
    fd = FD("ConfName", "Acronym")
    return L, P , fd

# To translate gFD into PG-Schema
def gFD2PGS(L,P,fd):
    constraint = "FOR "
    for label in fd.rhs:
            constraint += "x." + label + ","
    constraint = constraint[:len(constraint)-1] + " WITHIN x"
    if type(L) == set:
        for label in L:
            constraint += ":" + label
    else:  constraint += ":" + L
    constraint += "\n\tWHERE "
    if type(P) == set:
        for label in P:
            constraint += "x." + label + " IS NOT NULL AND "
        constraint = constraint[:len(constraint)-1-4]
        constraint += "\n\t\tEXCLUSIVE MANDATORY "
    for label in fd.lhs:
            constraint += "x." + label + ","
    constraint = constraint[:len(constraint)-1]
    return constraint

# Relational FD example of our article
def relExample():
    fd = FD("address", "region")
    return fd,"R"

# To translate relational FD into PG-Schema
def Rel2PGS(fd,R):
    constraint = "FOR "
    for label in fd.rhs:
            constraint += "x." + label + ","
    constraint = constraint[:len(constraint)-1]

    constraint +=" WITHIN (x:" + R + ") EXCLUSIVE MANDATORY "
    for label in fd.lhs:
            constraint += "x." + label + ","
    constraint = constraint[:len(constraint)-1]
    return constraint


# Run examples of our article or GED examples of (Fan et al., 2017) by default.
if __name__ == '__main__':

    # For gFD translation - using the example of our article
    L, P, fd = gFDArticleExample()
    print("Translation of the gFD example of our article into PG-Schema:\n",gFD2PGS(L,P,fd))
    print()

    # For GED example of Figure 3 of our article
    GP, X, Y = GPFigure3()
    print("Translation of Figure 3 GED example into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For GED example of Figure 3 in Ascii format
    GPAscii, X, Y = GPAsciiFigure3()
    GP = cypher_ascii_to_networkx(GPAscii)
    print("Translation Translation of Figure 3 GED example (in Ascii) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For GED example of Figure 4 of our article
    GP, X, Y = GPFigure4()
    print("Translation of Figure 4 GED example into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # GED example of Figure 4 in Ascii format
    GPAscii, X, Y = GPAsciiFigure4()
    GP = cypher_ascii_to_networkx(GPAscii)
    print("Translation of Figure 4 GED example (in Ascii) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For example Q1 of (Fan et al., 2017)
    GP, X, Y = GPGEDQ1()
    print("Translation example Q1 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For example Q2 of (Fan et al., 2017)
    GP, X, Y = GPGEDQ2()
    print("Translation example Q2 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For example Q7 of (Fan et al., 2017)
    GP, X, Y = GPGEDQ7()
    print("Translation example Q7 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
    print()

    # For example of GD of our article
    GP, X, Y = GPFigure1()
    print("Translation example of GD of our article into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")

    # To define user Graph Pattern
    # GP = defineGraphPattern()
    # X = [] # define the right part of the graph dependency -- see examples below
    # Y = [] # define the left part of the graph dependency -- see examples below
    # print("Translation into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")