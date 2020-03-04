# GeoNetAnalysis

## Contact

## Software Requirement
*Python
*MATLAB

## Package Requirement
* [NetworkX](https://github.com/networkx/networkx) (Based Graph library)
* [NetworKit](https://github.com/kit-parco/networkit) (Pairwise bidirectional dijkstra algorithm)
* [CVXPY](https://github.com/cvxgrp/cvxpy) (LP solver for Optimal transportation)
* [NumPy](https://github.com/numpy/numpy) (CVXPY support)
* [POT](https://github.com/rflamary/POT) (For approximate Optimal transportation distance)

## Explanation
* GraphRicciCurvature-master(folder): This code is used for calculating Ollivier-Ricci Curvature[Ni] and Forman-Ricci Curvature[Sreejith](https://github.com/saibalmars/GraphRicciCurvature).
* NodesCurvature.py: This code is used for calculating nodes' Ollivier-Ricci Curvature and Forman-Ricci Curvature.
* LaplacianMatrix.m: This code is used for calculating the Laplacian spectrum of a network.
* RemoveEdges.py: This code is used for edges attack experiments.
* RemoveNodes.py: This code is used for nodes attack experiments.
* EdgeAttackResultsPlot.py: This code is used for the presentation of the edges attack experiments' results.
* NodeAttackResultsPlot.py: This code is used for the presentation of the nodes attack experiments' results.
* README.md: Explanation document.

## References
[Ni]: Ni, C.-C., Lin, Y.-Y., Gao, J., Gu, X., and Saucan, E. 2015. "Ricci curvature of the Internet topology" (Vol. 26, pp. 2758–2766). Presented at the 2015 IEEE Conference on Computer Communications (INFOCOM), IEEE. [arXiv](https://arxiv.org/abs/1501.04138)
[Sreejith]: Sreejith, R. P., Karthikeyan Mohanraj, Jürgen Jost, Emil Saucan, and Areejit Samal. 2016. “Forman Curvature for Complex Networks.” Journal of Statistical Mechanics: Theory and Experiment 2016 (6). IOP Publishing: 063206. [arxiv](https://arxiv.org/abs/1603.00386)
