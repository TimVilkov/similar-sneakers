similar-sneakers
==============================


**Author:** Timofey Vilkov 

**Supervisor:** Panchuk Georgii

**Formulation of the problem:** 
Creating a text2image platform based on multimodal models for searching similar sneakers by user text description.

**Roadmap:**
- Searching sites with large number of items (01.01.2023 — 01.03.2023)
    - analyze the quality of content
    - estimate complexity of parsing
- Implement parser for scraping image and text data from sneaker platforms (05.03.2023 — 15.03.2023)
    - write parser
    - parse and scrape data
    - extract data from raw responses
    - collecting images 
- EDA (15.03.2023 — 20.03.2023)
- Data subsample labeling (20.03.2023 — 27.03.2023)
-  Research multimodal models, сhoosing the best one (27.03.2023 — 20.04.2023)
    - define metrics for decision making
    - evaluation of selected models using labelled subset of the data
    - choosing the best model
- ML system design (27.03.2023 — 15.04.2023)
- ML system implementation (15.04.2023 — 15.05.2023)
    - writing code for inference
    - hosted app on the server
    - create bot
    - create base flow for interact with user
    - logging base metrics about load on the model
- Inference optimization (15.05.2023 — 31.05.2023)


**Data description:**
Data: parsed shoe items from  https://www.ssense.com/.

Used endpoints:
- https://www.ssense.com/en-id/men/shoes.json 
- https://www.ssense.com/en-id/women/shoes.json

Raw data: [raw_data_urls.json](https://drive.google.com/file/d/1_AV2qeNhgLBQhHCqvCX32LwecxtRUUPQ/view?usp=sharing)

CSV with urls: [url_dataset.csv](https://drive.google.com/file/d/1wjcCLON6mK-wjriYHQsaz4Cks1ehty50/view?usp=sharing)

Default image resolution: **940x960**

Dataset size: **42240** images 

Features:
 - brand
 - name (not always unique, e.g. Black Leather Loafers)
 - gender
 - categories
 - images
 - seoKeyword
 - priceByCountry
 - url

**Service description:**
Telegram bot with comfortable UX for user

**Stack:**
TBD

Project Organization
------------

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
    ├── sneakers           <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── make_dataset.py
    │   │   ├── curl_params.py
    |   |   └── ssense_scrapings.ipynb
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
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
