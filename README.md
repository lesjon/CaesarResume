# CaesarResume
Get fields from the resume api to build custom display from the fields
# Authentication
create a `.env` file with your credentials to get your info:
```
USERNAME=<username>
PASSWORD=<password>
```

# Usage
## Create virtual environment to install libraries (not necessary in a container)
You can create a Python virtual environment and install the libraries specified in a `requirements.txt` file with the following steps:

1. **Create a virtual environment**: You can do this with the `venv` module, which is included in standard Python 3 installations. You can create the virtual environment in your project directory. In this example, I'm creating a virtual environment called `myenv`.

```bash
python3 -m venv myenv
```

2. **Activate the virtual environment**: The command to do this will vary depending on your operating system:

- On Unix or MacOS, run:

```bash
source myenv/bin/activate
```

- On Windows, run:

```bash
.\myenv\Scripts\activate
```

Once the virtual environment is activated, your command prompt will change to show the name of the activated virtual environment.

3. **Install libraries from `requirements.txt`**: You can do this with the `pip` command:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all specified libraries.

Remember to always activate the virtual environment before you start working on the project, and deactivate it when you're done:

```bash
deactivate
```

This command will exit out of the virtual environment.
## Run the program
```bash
python main.py
```