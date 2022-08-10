# <Project Name>

## Environment Setup
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. In Terminal, go to the root directory of this project.
3. Run the following commands to create Python virtual environment, and install dependencies.
    ```sh
    conda create -y -n <project-name> python=3.10
    conda activate <project-name>

    pip install -r requirements.txt
    ```
## Run program

## Run unit tests
1. In Terminal, go to the root directory of this project.
2. Run the following commands.
    ```sh
    pytest --cov=. --cov-config=.coveragerc tests \
        --cov-report=html \
        --cov-report=xml \
        --cov-report term
    ```    
3. When the tests finish, find coverage report under [coverage_html_report](coverage_html_report) folder, and open [index.html](coverage_html_report) via Web browser.
