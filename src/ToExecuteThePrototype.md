### Python modules required:
* *network* module - cf. doc. https://pypi.org/project/networkx/
```
pip install networkx
```
* *functional-dependencies* module - cf. doc. https://pypi.org/project/functional-dependencies/
```
pip install functional-dependencies
```
### To execute PG_FD
- PGFDPrototypeV1.py: corresponds to the prototype for the ABDIS article.
- PGFDPrototypeV2.py: corresponds to an extension of the ADBIS prototype.

To execute 
  - Copy functional-dependencies.py, run_PGFD.py and PGFDPrototypeV2.py in the same repository
  - Run run_PGFD.py

### To replay [examples](https://github.com/MaudeManouvrier/PG-FD/blob/main/src/sampleResults.md) of the article or examples of [(Fan et al., 2017)](https://www.pure.ed.ac.uk/ws/portalfiles/portal/44159778/pods17.pdf)

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
