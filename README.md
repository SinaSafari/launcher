# Launcher

## how to run the app:

1. first activate virtualenv:

```bash
$ source ./venv/bin/activate
```

or on windows:

```bash
$ .\venv\Scripts\activate
```

2. install dependencies:

```bash
$ pip install -r requirements.txt
```

3. and finally run the app:

```bash
$ unicorn main:app --reload
```

Note: `--reload` is helpful in development for hot reloading app after any file chenges, but it's not required for running the app.

4. run tests:

```bash
$ pytest
```

it's normal to see errors while tests are running. it may some of models haven't traind yet.
so please run the commands (or hit the routes) for train them first.

---

## using cli helper

1. run the app:

```bash
$ python launcher.py -s
```

or

```bash
$ python launcher.py --serve
```

2. run test:

```bash
$ python launcher.py -t
```

or

```bash
$ python launcher.py --test
```

3. run code formatter:

```bash
$ python launcher.py -f
```

or

```bash
$ python launcher.py --format
```

4. update `requirements.txt` with current dependencies:

```bash
$ python launcher.py -u
```

or

```bash
$ python launcher.py --updaterequirements
```