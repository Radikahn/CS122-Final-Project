### CS122-Final-Project: MoneyUrWay

# Members
- Radman Shahbazkhan and Miguel Lorenzo Viray

### Description
MoneyUrWay is a budgetting application that allows the user to input their financial details to create spending plans and visualize their spending habbits in correlation to their income.

### Dependencies --Executable file included--

# HIGHLY RECCOMEND:
Within the zip file there is a ```MoneyUrWay``` executable file that will run the project without the need for complicated dependency installation.

However if you must setup the project...

# Installation Instructions
This project MUST be ran on **3.9.21**

Step 0: create a virtual environment on python version 3.9.21

Step 1: ```pip install matplotlib==3.5.0```

Step 2: ```pip install "kivy[full]"```

Step 3: ```pip uninstall kivy-garden```

Step 4: ```pip install kivy-garden==0.1.4```

Step 5: ```pip uninstall numpy```

Step 6: ```pip install numpy==1.25```

Step 7: ```pip install seaborn```

Step 8: ```pip install sqlalchemy```

Step 9: ```python main.py```

# Pip Freeze Dependencies

altgraph==0.17.4
certifi==2025.4.26
charset-normalizer==3.4.2
cycler==0.12.1
docutils==0.21.2
ffpyplayer==4.5.2
filetype==1.2.0
fonttools==4.57.0
greenlet==3.2.1
idna==3.10
importlib_metadata==8.7.0
Kivy==2.3.1
Kivy-Garden==0.1.4
kiwisolver==1.4.7
matplotlib==3.5.0
numpy==1.25.0
packaging==25.0
pandas==2.2.3
pillow==10.4.0
Pygments==2.19.1
pyinstaller==6.13.0
pyinstaller-hooks-contrib==2025.4
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.3
seaborn==0.13.2
setuptools-scm==8.3.1
six==1.17.0
SQLAlchemy==2.0.40
tomli==2.2.1
typing_extensions==4.13.2
tzdata==2025.2
urllib3==2.4.0
zipp==3.21.0

### Project File Structure

# Modules

The project contains 4 modules: app, data_management, guiKivy, tests.

- app module:
    - Contains files to manage plotting graphs, making budgetting calculations, holds the main user class (user_accounts.py), and a custom exceptions class

- data_management module:
    - Contains all the files that manage how data is manipulated and stored (data persistence). This module includes files to create the sqlite3 table, the orm binding, and functions to manage csv functionality

- guiKivy module:
    - Contains the main gui file that has all the code for the various screens and user input handlers.

- tests module:
    - Contains the file for running our test cases on our ORM database.

# Main Files

There are two main "run" files in the project: ```main.py```, ```run_tests.py```, and ```MoneyUrWay```

- main.py is used to run the main project through python

- run_tests.py is used to run the test cases through python

- MoneyUrWay is an executable file used to run the project without python venv setup


### Bugs

There are currently no known bugs. The CSV functionality is only designed for the "developer". This means there are not direct functions within the GUI to manage the CSV, but rather through the code/console


