# Decision Tree Algorithms

We recommend that you install Python 3.8 for your operating system. 
Download the installer here: https://www.python.org/downloads.

The dataset used is from the company Lending Club published on [Kaggle](https://www.kaggle.com/wordsforthewise/lending-club).

This project implements 4 algorithms to induce a decision tree: **Brute force, ID3, CART and Genetic**.

The file `./main` request the function that was set up in the file `./config.py`.

Example:

```
run_config = {
    "algorithm": "brute",
    "recurrence": 11,
    "create_csv": True
}
```

## References

* To implement CART, the [scikit-learn](https://scikit-learn.org/stable/) library was used
* The implementation of the genetic algorithm was adapted from [Wojcik98](https://github.com/Wojcik98/evolutionary-decision-tree)
