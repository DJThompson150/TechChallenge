# AA/ML Tech Challenge: MNIST Digit Recognizer

Welcome to the pilot tech challenge from the Advanced Analytics SO - rolling your own digit recognizer!

**Before proceeding, please make sure you have enrolled in this assignment on GitHub Classrooms by following [this link](https://classroom.github.com/a/sFqE7KqF).** 

## Intro
The goal of this tech challenge is for the learner to practice:
 * Multi-class classification techniques
 * Computer vision fundamentals and simple neural networks
 * Delivering reproducible model-building projects

You'll accomplish these goals by developing a model that can classify examples from the MNIST handwriting dataset, one of the standard "hello world" datasets for computer vision and neural networks. 

## Prerequisites
[TODO]
 * A local installation of Python (≥3.6). Anaconda distributions will work fine.
 * An account on [Kaggle](https://www.kaggle.com)
 * Some terminal to run CLI tools (Mac users are good; Windows may use Git Bash or PowerShell)

## Getting Started

Beyond creating your own repository, you'll have to do a few other setup tasks before getting to the fun part of the assignment.

### Create a Kaggle API Key

Follow Kaggle's [instructions](https://github.com/Kaggle/kaggle-api#api-credentials) for creating and downloading API credentials.

### Downloading data

You will train your model with data from Kaggle's [Digit Recognizer competition](https://www.kaggle.com/c/digit-recognizer/data). 

To initialize your project, you will _not_ be downloading the data from your browser. Rather, fire up your favorite terminal, navigate to the root of this project, and run the following command: 

```PowerShell
make data
```

This will download two files, `train.csv` and `test.csv`, into the `data/external` directory of this project.

## Deliverables

### Evaluation
[TODO]: explore having assignees score against Kaggle's `test.csv` and providing a script that submits 
those predictions via CLI for eval

[TODO]: how does GH classrooms let assignees notify us that they're "done"?

Your submission will be evaluated on its categorization accuracy when predicting labels in a holdout dataset. There is no pass/fail threshold, but your accuracy should be able to reach the high 90's just by using the popular kernels available on Kaggle as examples.

## Project Organization
For this pilot, we've provided you a modified version of the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/), which proposes the project structure that appears below. While you are welcome to modify the repository to your liking, we strongly encourage you to follow this template (see coookiecutter's discussion of "why you should use this project structure").


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
