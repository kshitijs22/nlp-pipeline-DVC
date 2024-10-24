Problem Statement - Sentiment Analysis

A simple yet effective usecase to understand the MLOPs concept of creating the pipeline using DVC (Data Version Control)

Components - Data Ingestion, Data PreProcessing, Feature Engineering, Model Building, Model Evaluation

Steps-
1. Install DVC using the command 'pip install dvc'
2. Initialise the git and dvc (git init and dvc init)
3. In the terminal run the below the command, it will automatically create dvc.yaml file.
    dvc stage add -n __ -d __ -p __ -o __ ---> Run this command for every component.
4. DVC.dag for visualizing the pipeline structure.
5. Run 'dvc repro' for running the pipeline.