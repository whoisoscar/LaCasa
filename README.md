**Background**
--
text here

**Installation**
--
To install files:
`````
git clone https://github.com/whoisoscar/LaCasa
`````
To Install Required Modules:
`````
pip install -r requirements.txt
`````

**Create and activate Virtual Enviornment**
--
Creating it:
`````
cd LaCasa
python3 -m venv ./lacasa
`````

Activating it (each time you open the folder):
````
source ./lacasa/bin/activate
````

**Usage**
--
`````
cd LaCasa
export FLASK_APP=app
export FLASK_DEBUG=1
flask run
`````


**To-do**
--
- [ ] Imrpove backend algo for sorting
- [ ] Add JS dunctionalities to frontend