Simple Flask Example
=====================

### Initial instalation
```shell
# Enter the directory
cd simple-flask-example

# Create a virtual environment for the app
python -m venv venv

# ...and enter the virtual environment
source venv/bin/activate        # Linux/MacOS
.\venv\Scripts\Activate.ps1     # Windows (Powershell)
.\venv\Scripts\Activate.bat     # Windows (cmd.exe)

# Install all libraries
pip install -r requirements.txt

# Execute the program
python src/app.py
```

### Normal execution
```shell
# Enter the directory
cd simple-flask-example

# Enter the virtual environment
source venv/bin/activate        # Linux/MacOS
.\venv\Scripts\Activate.ps1     # Windows (Powershell)
.\venv\Scripts\Activate.bat     # Windows (cmd.exe)

# Execute the program
python src/app.py
```

### Exit the virtual environment
```shell
deactivate
```