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
MANDATORY y.name = z.name WITHIN (y:city)<-[:capital]-(x)-[:capital]->(z:city)`
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

