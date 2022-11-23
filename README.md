## What is this project for?

This Project is created for clone project and extract infomation of specific repository

## Getting start

1. activate venv

`source ./.venv/bin/activate`

2. setting config files

run

`make config`

and update each config path

`.env` is apply for normal execution and `.test.env` is apply for test execution.

3. clone projects

`make clone_projects`

This commmand create `project.csv` below the `DB_ROOT_PATH` folder you speficy in .env and clone project below the `PROJECT_ROOT_PATH`
