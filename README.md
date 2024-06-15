**Build the requirements**:

Create virtual environment

    python3.10 -m venv .venv

    source ./.venv/bin/activate

Read: https://pypi.org/project/pip-tools/

    python -m pip install pip-tools

**Build the requirements**

    pip install -r requirements.txt

**Commit hooks**

    https://pre-commit.com/

    pip install pre-commit

    Run:

        pre-commit install

        Make sure you have created a git branch before running below command and make sure the existance of file:

            .pre-commit-config.yaml

        pre-commit run --all-files

Make sure that:

    export FLASK_APP=flaskpine.py

To test:

    flask test

    flask test --coverage


** Database migration

    Make sure that:

    export FLASK_APP=flaskpine.py

    First run this to create migration directory:

    flask db init

    $ flask db migrate

    $ flask db upgrade

    Careful when renaming columns, the created migration script will drop the column and create a new one.
    That is not what you want.

    flask load_data > db_backup/logs/log.file 2>&1

    flask test > db_backup/logs/log.file 2>&1
