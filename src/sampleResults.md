### To replay the gFD translation example of our article
```python
L, P, fd = gFDArticleExample()
print("Translation of the gFD example of our article into PG-Schema:\n",gFD2PGS(L,P,fd))
```
***
Translation of the gFD example of our article into PG-Schema:

` FOR x.ConfName WITHIN x:Conf
	WHERE x.Acronym IS NOT NULL AND x.ConfName IS NOT NULL
		EXCLUSIVE MANDATORY x.Acronym`
***

### To replay the translation of GED example of Figure 3 in our article
```python
GP, X, Y = GPFigure3()
print("Translation of Figure 3 GED example into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation of Figure 3 GED example into PG-Schema:

` FOR (x:Article)
COUNT 0 OF (y:Person)-[:AuthorOf]->(x)<-[:ReviewerOf]-(y:Person)` 
***

### To replay the translation of GED example of Figure 4 in our article
```python
GP, X, Y = GPFigure4()
print("Translation of Figure 4 GED example into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation of Figure 4 GED example into PG-Schema:

`FOR (x:Article)
IDENTIFIER x.title,y.id WITHIN (x)-[:SubmittedTo]->(y:Conf)` 
***

### To replay the translation of GD example of our article
```python
GP, X, Y = GPFigure1()
print("Translation example of GD of our article into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation example of GD of our article into PG-Schema:

`FOR (x:Article)
WHERE exists edge e,L(e)=SubmittedTo
MANDATORY (x)-[e]->(y) WITHIN (x)-[:SubmittedTo]->(y:Conf)`
***

### To replay the translation of example Q1 of [(Fan et al., 2017)](https://www.pure.ed.ac.uk/ws/portalfiles/portal/44159778/pods17.pdf)
```python
GP, X, Y = GPGEDQ1()
print("Translation example Q1 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation example Q1 of (Fan et al., 2017) into PG-Schema:

`FOR (x:Product)
WHERE x .type = "video game"
MANDATORY y.type = "programmer" WITHIN (y:Person)-[:create]->(x)`
***

### To replay the translation of example Q2 of [(Fan et al., 2017)](https://www.pure.ed.ac.uk/ws/portalfiles/portal/44159778/pods17.pdf)
```python
GP, X, Y = GPGEDQ2()
print("Translation example Q2 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation example Q2 of (Fan et al., 2017) into PG-Schema:

`FOR (x:Country)
MANDATORY y.name = z.name WITHIN (x)-[:capital]->(z:City)`
***

### To replay the translation of example Q7 of [(Fan et al., 2017)](https://www.pure.ed.ac.uk/ws/portalfiles/portal/44159778/pods17.pdf)
```python
GP, X, Y = GPGEDQ7()
print("Translation example Q7 of (Fan et al., 2017) into PG-Schema:\n", GED2PGS(GP,X,Y), sep="")
```
***
Translation example Q7 of (Fan et al., 2017) into PG-Schema:

`FOR (x:Album)
IDENTIFIER x.title ,x.release `
***

### To define your own GED 
1. Define a Graph Pattern :
	* Calling function `defineGraphPattern()` or
 	* Translating an ASCII art graph into a Graph Pattern by calling  function `cypher_ascii_to_networkx(GPAscii)` with `GPAscii` a string defining a graph in ASCII notation
    	***
    	Example of Graph pattern of Figure 3 :
    	 ```python
    	 GPAscii = "(y:Person)-[:AuthorOf]->(x:Article)<-[:ReviewerOf]-(y:Person)"
         GP = cypher_ascii_to_networkx(GPAscii)
     	 ```
        ***
2. Define $X$ and $Y$ as list of strings or boolean *False*
	***
	Examples:

	`X, Y = [], False`

	`X, Y = ["x.title=x'.title","y.id=y'.id"], ["x.id=x'.id"]`
	***
3. Call function `GED2PGS(GP,X,Y)`

### To define your own GD 
1. Create a Graph Pattern ike for GED - see above.
2. Define $X$ and $Y$ as list of strings with:
	* $X$ being a list of one string containing one string with an exist condition, for example `X = ["exists edge e","L(e)=SubmittedTo"]`
 	* $Y$ being a list of one string describing a graph pattern in ASCII notation, for example `Y = ["(x)-[e]->(y)"]`
3. Call function  `GD2PGS(GP,X,Y)`

### To define your own gFD 
1. Define *L* as a string, for example `L = "Conf"`
2. Define *P* as a set of strings, for example `P={"Acronym","ConfName"}`
3. Define *fd* as a functional dependencies using function `FD()` of the [functional dependencies Python module](https://oer.gitlab.io/cs/functional-dependencies/), for example `fd = FD("ConfName", "Acronym")`
4. Call function `gFD2PGS(L,P,fd)`

### To define your own relational FD 
1. Define *fd* as a functional dependencies using function `FD()` of the [functional dependencies Python module](https://oer.gitlab.io/cs/functional-dependencies/), for example `FD("address", "region")`
2. Call function `Rel2PGS(fd,R)` with `R` a string correspondinfg to the name of the relation
