# SI671 Fall 2018 HW1 Recommender System

Chosen path in the assignment led to implementing 2 existing packages for recommender systems, namely:
* Surprise (http://surpriselib.com/)
* Spotlight (https://github.com/maciejkula/spotlight)

## Results
Evaluation of results used RMSE of predictions made on an unlabeled test set. Based on Kaggle Private scores:
* Surprise (using SVD and a parameter grid search): 1.02229 
* Spotlight (using non-negative matrix factorization): 1.43769
