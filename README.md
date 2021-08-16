# Launcher

## how to run the app:

1. first activate virtualenv:

```bash
source ./venv/bin/activate
```

or on windows:

```bash
.\venv\Scripts\activate
```

2. install dependencies:

```bash
pip install -r requirements.txt
```

3. and finally run the app:

```bash
unicorn main:app --reload
```

Note: `--reload` is helpful in development for hot reloading app after any file chenges, but it's not required for running the app.

4. run tests:

```bash
pytest
```

it's normal to see errors while tests are running. it may some of models haven't traind yet.
so please run the commands (or hit the routes) for train them first.