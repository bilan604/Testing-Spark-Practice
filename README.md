# PySpark Application Template

You can create a PySpark application using this template. This template utilizes VS Code Dev container, so you do not need to install Spark yourself.

## Environment Setup
1. Install Docker or Podman.
2. Install Visual Studio Code. If Podman is used, change `remote.containers.dockerPath` to `podman`.
3. Install Extension `ms-vscode-remote.remote-containers`
4. In Github, click `User this template`.
5. Open this project in Container: `remote-containers.openFolder`

## Run program

## Run unit tests
There are multiple ways to run unit tests, as shown below. Spark unit tests takes reletatively longger time to start and run, but should finish at minutes level.

### Using VS Code GUI
1. In dev container, open Testing tab
2. Follow GUI icons

### Using terminal
1. In Terminal of dev container, go to root directory of this project.
2. Run the following commands.
    ```sh
    pytest --cov=. --cov-config=.coveragerc tests \
        --cov-report=html \
        --cov-report=xml \
        --cov-report term
    ```    
3. When the tests finish, find coverage report under [coverage_html_report](coverage_html_report) folder, and open [index.html](coverage_html_report) via Web browser.
