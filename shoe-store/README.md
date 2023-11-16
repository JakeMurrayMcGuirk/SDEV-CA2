# Shoe Store


1. Set up a Python virtual environment and install the required Python dependencies:

      python3 -m venv env

      and download the listed modules in the read me file I have placed in the read me 


2. Create `.env` configuration file based on `env.sample`:
(Ill work on this myself)

3. Set up the database

    You'll need to create the database and set `DATABASE_URL` in
    the configuration file before you can run migrations and use the code.

    

        DATABASE_URL=sqlite:///file.db
 
 Please make sure youre in the shoe-store directry when you run this command 
    

4. Run migrations:

       

5. Run the server:

        pipenv run python manage.py runserver

6. Visit the browsable API at http://localhost:8000/api/v1/

7. Access the Django admin at http://localhost:8000/admin/

## Creating superuser

A superuser account can be created using the Django management command:

    pipenv run python manage.py createsuperuser

## Tests, linters and code coverage


To run the test suite:

    python manage.py test

To run the test suite and get code coverage statistics:

    coverage run manage.py test
    coverage report

To generate HTML reports, run this and open `htmlcov/index.html`
afterwards:

    coverage html

To format the code automatically using `black`, run it
from the project root directory:

    black .

To check for common programming errors or style problems,
run `ruff` linter in the project root directory:

    ruff --fix .

To automatically run `black` (formatting), `ruff` (linter)
and `isort` (sort/format package imports) on every git
commit, set up a git `pre-commit` hook:

    pre-commit install

Note that you'll need to have initialized your git repository for
the git pre-commit hook to be available. To test it without installation,
you can run:

    pre-commit run --all-files

## Continuous integration with GitHub Actions

This project comes with a GitHub Actions workflow that runs
the test suite and linters on every push to the repository.

See the `.github/workflows/django.yml` file for details.
