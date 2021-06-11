# :sparkles: PYTHON-DECAF :sparkles:

### Getting your launch base ready!

#### Check for python on terminal.

```bash
python3 --version
# python --version # If python3
```

### Instansiate virtual environment (Linux).

```bash
python3 -m venv env
source env/bin/activate
# You should see a small $(yourEnvironment) prompt in terminal.
```

### Instansiate virtual environment in powershell. (Windows, ofcourse)

```powershell
py -3.9 -m venv env
.\env\Scripts\Activate
```

<hr>

### REPL

#### Read Evaluate Print Loop

##### Instantaneous code, instantaneous feedback. :rocket:

> It's more like a scratch area.<br>
>
> '\>>>' represents a REPL prompt.

### Print, assign different datatypes in REPL

### Github search API

<hr/>

### Variables.

Variables in Python allow us to store information and give it a label that we can use to retrieve that information later.

### Dynamic Language

Because Python is a dynamic language, you’ll notice we don’t need to declare the type of the variables before we store data in them.

That means that this is valid Python code:

> x = 42

Unlike typed languages, the type of what’s contained in Python variables can change at any time.

### Install Open-CV

```bash
# Make sure your pip is not too far behind/old
pip -v
pip install --upgrade pip
# Open-CV contrib makes sure extra packages contributed by cimmunity is available as well!
pip install scikit-build opencv-contrib-python
```
