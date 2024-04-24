# PG-FD: Mapping Functional Dependencies to the Future Property Graph Schema Standard
*Under construction*

This repository contains the source code of PG-FD, a Python program that uses the *networkx*[^1] Python module of https://networkx.org/ and the *functional_dependencies*[^2] of https://oer.gitlab.io/cs/functional-dependencies.

>[!NOTE] 
For more details, please refer to the paper: Maude Manouvrier and Khalid Belhajjame, *PG-FD: Mapping Functional Dependencies to the Future Property Graph Schema Standard*, submitted.

Usage :

## To create the graph dependencies examples of our article 
To replay the examples of the article, user can execute function `GPFigureX()` or `GPAsciiFigureX()` (to translate a graph pattern definied using ASCII art notation of Cypher [^3]), with 'X' corresponding to the number of the figure in the article. User should, for example, execute `GPFigure4()` to translate the Graph dependency of Figure 4 in the article.

The functions return a *MultiDiGraph* of *networkx*[^1] Python module representing the graph pattern or a graph pattern defined in an ASCII art notation

##  To create the graph dependencies examples of article of (Fan et al., 2017)[^5]
To replay the examples of the article of (Fan et al., 2017)[^5], user can execute function `GPGEDQX()` with 'X' corresponding to the number of the example in the article of (Fan et al., 2017)[^5]. User should, for example, execute `GPGEDQ2()` to translate the Graph dependency *Q<sub>2</sub>* in the article of (Fan et al., 2017)[^5].

The functions return a *MultiDiGraph* of the *networkx*[^1] Python module representing the graph pattern or a graph pattern defined in an ASCII art notation

## To translate graph dependencies into PG-Schema[^4]
* To translate a GED[^5][^6] into PG-Schema, user should call function `GED2PGS(GP,X,Y)` with *GP* a *MultiDiGraph* of the *networkx*[^1] Python module representing the graph pattern or a graph pattern defined in an ASCII art notation, *X* and *Y* the right and left part of the graph dependency.
* To translate a gFD[^7] into PG-Schema, user should call function `gFD2PGS(L,P,fd)` with *L* a set of node labels, *P* a set of properties and *fd* a functional dependency defined using the *functional_dependencies*[^2] module.
* To translate a GD[^8] into PG-Schema, user should call function `GD2PGS(GP,X,Y)` with *GP* a *MultiDiGraph* of *networkx*[^1] Python module representing the graph pattern or a graph pattern defined in an ASCII art notation, *X* and *Y* the right and left part of the graph dependency.

All functions return a string corresponding to the PG-Schema[^4] translation.

[^1]: https://networkx.org/
[^2]: https://oer.gitlab.io/cs/functional-dependencies
[^3]: Francis, N., Green, A., Guagliardo, P., Libkin, L., Lindaaker, T., Marsault, V., Plantikow, S., Rydberg, M., Selmer, P., Taylor, A.: Cypher: An evolving query language for property graphs. In: SIGMOD Int. Conf. on Manag. of Data. pp. 1433–1445 (2018) - https://homepages.inf.ed.ac.uk/libkin/papers/sigmod18.pdf
[^4]: Angles, R., Bonifati, A., Dumbrava, S., Fletcher, G., Green, A., Hidders, J., Li, B., Libkin, L., Marsault, V., Martens, W., et al.: PG-Schema: Schemas for property
graphs. ACM on Manag. of Data 1(2), 1–25 (2023) - https://www.research.ed.ac.uk/en/publications/pg-schemas-schemas-for-property-graphs
[^5]: Fan, W., Lu, P.: Dependencies for graphs. In: ACM SIGMOD-SIGACT-SIGAI Symp. on Principles of Database Sys. pp. 403–416. ACM (2017) - https://www.pure.ed.ac.uk/ws/portalfiles/portal/44159778/pods17.pdf
[^6]: Fan, W., Lu, P.: Dependencies for graphs. ACM Trans. on Database Sys. (TODS) 44(2), 1–40 (2019) - https://homepages.inf.ed.ac.uk/wenfei/papers/TODS-GED.pdf
[^7]: Skavantzos, P., Link, S.: Normalizing Property Graphs. VLDB Endowment 16(11), 3031–3043 (2023) - https://dl.acm.org/doi/abs/10.14778/3611479.36115
[^8]: Zheng, X., Dasgupta, S., Gupta, A.: P2KG: Declarative Construction and Quality Evaluation of Knowledge Graph from Polystores. In: European Conf. on Advances in Databases and Info. Sys. (ADBIS). pp. 427–439. Springer (2023) - https://escholarship.org/content/qt30h5c8jj/qt30h5c8jj.pdf





