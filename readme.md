# Art Thief

[![Python Coverage](https://codecov.io/gh/alma-frankenstein/art_thief/branch/main/graph/badge.svg)](https://codecov.io/gh/alma-frankenstein/art_thief)

![Python Flake8](https://github.com/alma-frankenstein/art_thief/workflows/Flake8/badge.svg)
![Python Safety](https://github.com/alma-frankenstein/art_thief/workflows/Python%20Safety/badge.svg)
![Python Security Audit](https://github.com/alma-frankenstein/art_thief/workflows/Python%20Security%20Audit/badge.svg)
![Python Tests](https://github.com/alma-frankenstein/art_thief/workflows/Python%20Tests/badge.svg)
![Python MyPy](https://github.com/alma-frankenstein/art_thief/workflows/MyPy/badge.svg)


# Art Thief


## Description
Art thief pulls random, high resolution images from the art auction website artsy.net and displays them on your browser.


## Setup

To run on your localhost, clone this repo using:

```git clone https://github.com/alma-frankenstein/art_thief.git art_thief```

cd to the art_thief directory.

Create a virtual environment for the project:
* Run ```python3 -m venv venv```
* Activate it with ```source venv/bin/activate```

Run ```pip install -r requirements.txt``` to install dependencies

Create a migration repository for a database: ```flask db init```

Still with the virtual environment activated, run ```flask run```, then open the browser window indicated
(this will probably be http://127.0.0.1:5000/). Refresh the browser page to load a new picture.


## Testing

To run the test suite:
* Make sure the virtual environment is activated (see above)
* Go to the src directory: ```cd src```
* Run ```python -m pytest tests``` to run tests


## Technologies Used

* Python
* Flask
* Pillow






