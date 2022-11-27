# LaCasa
LaCasa aims to help you find the ideal neighbourhood.

A flask app that reads and filters data using binary trees.

# Table of contents
1. [Introduction](#introduction)
2. [Installation & Usage](#Installation-&-Usage)
3. [Further Improvements](#Further-Improvements)
4. [Credits](#credits)

# Introduction
This application was created for our Algorithms & Data Structures class. The project instructions were to create an app using at least one of the algorithms used in class. 

We came up with LaCasa, an app that helps you find the ideal neighbourhood using mainly Binary Trees and Heap-queues by assigning rankings to key attributes to filter and find the ideal nieghboorhood. These rankings were based uppon conclusions reached from user surveys and other reaserch. So far, the algorithm uses `Education`, `Safety` and `Price range` as attributes for determining the ideal neighbourhood.

The app is accessed from a web-view where the user is prompted with a 10-question survey to help determine his levels of preference for the aforementioned factors. Alternatively, the user can also do this manually by exiting the form, and on the main page, entering the values (ranked A-D) manually if they are familiar with the rankings.

Once the algorithm is ran on our server, it returns the 5 best results in order of relevance and displays them on the web-page where the complete result details are displayed. The user can then edit the search queries, and re-run the algorithm to find a new set of results.

**Limitations**

- The algorithm is currently limited to the state of Los Angeles, and its 67 neighbourhoods in the dataset.

## File Architecture
- `app.py` - The main flask app file that includes the routes and other app logic as well as all the sorting logic. The sorting logit includes the classes created and the algorithms used for sorting.
- `templates` - The folder that contains all the html files used for the web-view.
- `static` - The folder that contains all the static files used for the web-view.
- any other files are self-explanatory.

# Installation & Usage

## First-time install

Clone the files:
`````
git clone https://github.com/whoisoscar/LaCasa
`````

**Create and activate a Virtual Environment**

Creating the venv:
`````
cd LaCasa
python3 -m venv ./lacasa
`````
Activating the venv (each time you open the folder):
````
source ./lacasa/bin/activate
````
**Install modules**

To install required modules:
`````
pip install -r requirements.txt
`````
## Usage
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

# Further improvements
- [ ] Expand the data set with more neighbourhoods and variables.

# Credits
This project was created for our Algorithms and Data Structures course at IE University. The project was created by: 
- Joaquín de Tord
- Duarte Barbosa
- Manuel Mena
- Simão Varandas
- Giacomo Pedersoli
- Oscar Tluszcz
