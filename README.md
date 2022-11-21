# Background
text here


# First-time install

## Clone files
To install files:
`````
git clone https://github.com/whoisoscar/LaCasa
`````

## Create and activate Virtual Enviornment
Creating it:
`````
cd LaCasa
python3 -m venv ./lacasa
`````
Activating it (each time you open the folder):
````
source ./lacasa/bin/activate
````
## Install modules
To Install Required Modules:
`````
pip install -r requirements.txt
`````
# Usage
`````
cd LaCasa
`````
`````
export FLASK_APP=app
`````
`````
export FLASK_DEBUG=1
`````
`````
flask run
`````

# To-do
- [ ] Imrpove backend algo for sorting
- [ ] Add JS dunctionalities to frontend