Steps-
1. Install DVC using the command 'pip install dvc'
2. Initialise the git and dvc (git init and dvc init)
3. In the terminal run the below the command, it will automatically create dvc.yaml file.
    dvc stage add -n __ -d __ -p __ -o __ ---> Run this command for every component.
4. DVC.dag for visualizing the pipeline structure.
5. Run 'dvc repro' for running the pipeline.