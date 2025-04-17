# Hacking-the-electronic-diary
This script is designed to improve the academic performance of a particular student in the [school data management system](https://github.com/devmanorg/e-diary/tree/master ), built on Django. It performs the following actions:
1. **Corrects grades:** Replaces all grades 2 and 3 with 5.
2. **Deletes comments:** Deletes all comments made to the student.
3. **Creates praise:** Creates random praise for a student on a given subject.
## How to install
- Create and activate a virtual environment
 ```
 python -m venv venv
 source ./venv/Scripts/activate # for Windows
 source ./venv/bin/activate #for Linux and macOS
 ```
- Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
- Clone [repository](https://github.com/devmanorg/e-diary/tree/master ) with Django code that defines the necessary models.
- Install libraries: [random](https://docs.python.org/3/library/random.html ), [logging](https://docs.python.org/3/library/logging.html ), [sys](https://docs.python.org/3/library/sys.html )
- Make sure that your Django project is configured and connected to a database containing data on students, grades, comments, lessons, subjects, and commendations.

## How to launch
To run the script, you can “copy paste” it entirely into the shell, or you can put the code file next to manage.py and connect via import. The second way is more convenient and reliable.
- The first method:
    Write in the console:
    ```
     python manage.py shell
     (import the necessary libraries, models, and constants)
    (Define the functions you have (inside the shell):)
    (call the corresponding function:
    fix_marks(schoolkid)
    )
    ```
- The second way:
    Copy the repository and create a folder in it `scripts.py `from this prototype, then run the script:
    ```
    python scripts.py 
    ```
