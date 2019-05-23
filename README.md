# SI-671_Data-Mining

Code provided in this repository were written as part of the class SI 671: Data Mining.

*Note: Data used in class not included in the repository*

| Contents  | Description |
| ------------- | ------------- |
| Recommender Systems  | Implemented both Surprise and Splotlight packages used in recommendation systems, with output of suggested.<br><br>Data provided: CSV and JSON of reviewer, object reviewed, and score (1-5)<br><br>Result in Kaggle evaluation: 34/73|
| Graph Mining  | Using NetworkX:<br>1. Predict the 50,000 most likely links between nodes in a social network (50k links removed from provided data for reference)<br>2. Predict attributes/classes of unlabeled nodes, with underlying homophily as assumption.<br><br>Data provided: Edgelist of connected nodes, and attributes of most nodes in the network<br><br>Result in Kaggle evaluation: None available for 1st task, 12/50 for 2nd task|
| Spatial Data Mining  | Compute Local Getis-Ord G\* for words in provided data, and mapped words with regional preference using geopandas. Required use of multithreading to load data into memory<br><br>Data provided: Word counts for each region, region adjacency list, and code to plot census regions|
| Project: Community Detection for Federally paid vendor network  | Evaluated the use of the Louvain modularity and Clauset-Newman-Moore community detection algorithms in finding communities in vendors that are paid through federal grants, aiming to find specific trends in vendor behavior.<br><br>Analysis shows higher Freeman centrality versus baselines, potentially indicating regional vendor preference for universities.<br><br>Data used: Vendor transaction database for each partner university provided by the Institute for Research on Innovation and Science|

