# aaml-tc01-mnist

Welcome to the pilot tech challenge from the Advanced Analytics SO - rolling your own digit recognizer!

## Intro
The goal of this tech challenge is for the learner to practice:
 * Multi-class classification techniques
 * Computer vision fundamentals and simple neural networks
 * Delivering reproducible model-building projects

You'll accomplish these goals by developing a model that can classify examples from the MNIST handwriting dataset, one of the standard "hello world" datasets for computer vision and neural networks. 

## Data
You will train your model with data from Kaggle. Once you've made your own copy of this assignment, navigate to the [Kaggle Digit Recognizer](https://www.kaggle.com/c/digit-recognizer/data) challenge, download `train.csv`, and store it in your local copy of the project. You do **not** need to use the `test.csv` provided on the Kaggle challenge; we will use a separate dataset for evaluation. Do not upload data to GitHub.


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
