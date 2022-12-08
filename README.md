# LaCasa
LaCasa aims to help you find the ideal neighbourhood.

A flask app that reads and filters data using binary trees.

<table>
  <tr>
    <td>
      <img src="https://i.imgur.com/QXSFwq8.png" alt="Lorem ipsum" title="Lorem ipsum">
    </td>
    <td>
      <img src="https://i.imgur.com/OKcgPnI.png" alt="Dolor sit" title="Dolor sit">
    </td>
    <td>
      <img src="https://i.imgur.com/xEd1SIi.png" alt="Amet consectetur" title="Amet consectetur">
    </td>
  </tr>

  <tr>
    <td>Survey Pop-up</td>
    <td>Home Page</td>
    <td>Results Page</td>
  </tr>
</table>

*Disclosure: the app was developped on MacOS Monterey 12.4 using Python 3.7.3*

# Table of contents
1. [Introduction](#introduction)
2. [Installation & Usage](#Installation-&-Usage)
3. [Further Improvements](#Further-Improvements)
4. [Credits](#credits)

# Introduction
This application was created for our Algorithms & Data Structures class. The project instructions were to create an app using at least of the algorithms used in class.

We came up with LaCasa, an app that helps you find the ideal neighbourhood using mainly Binary Trees and Heap-queues by assigning rankings to key attributes to filter and find the ideal neighbourhood. These rankings were based upon conclusions reached from user surveys and other research. So far, the algorithm uses `Education`, `Safety` and `Price range` as attributes for determining the ideal neighbourhood.

The app is accessed from a web-view where the user is prompted with a 10-question survey to help determine his levels of preference for the aforementioned factors *(look at survey screenshot for reference)*. Alternatively, the user can also do this manually by exiting the form, and on the main page, entering the values (ranked A-D) manually if they are familiar with the rankings *(look at homepage screenshot for reference)*.

Once the algorithm is run on our server, it returns the 5 best results in order of relevance and displays them on the web-page where the complete result details are displayed. The user can then edit the search queries, and re-run the algorithm to find a new set of results *(look at results screenshot for reference)*.

**Limitations**

- The algorithm is currently limited to the state of Los Angeles, and its 67 neighbourhoods in the dataset.

## File Architecture
- `app.py` - The main flask app file that includes the routes and other app logic as well as all the sorting logic. The sorting logit includes the classes created and the algorithms used for sorting.
- `templates` - The folder that contains all the html files used for the web-view.
- `static` - The folder that contains all the static files used for the web-view.
- any other files are self-explanatory.

## The Dataset
The dataset provides information about 67 neighbourhoods in the LA region. Its content is relevant for anyone interested into understanding if a specific district is relevant for their needs. The following variables are presented: 
- Name: For each row, it contains the name of the neighbourhood
- Education Ranking: From 1 to 9 ranking the level of public school education, 1 being the worst and 9 the best
- Safety Ranking: From 1 to 5, represented the level of neighbourhood safety, being 1 the worst and 5 the best
- Average House Price: The estimated average housing price

This dataset was manually constructed by our group, taking as a source Niche.com *(check bibliography for reference)*. Niche provides ratings for the previously mentioned variables in letters ranging from D+ to A+.

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
- [ ] Create a function to automatically scrape niche.com.
- [ ] Expand the data set with more neighbourhoods.
- [ ] Expand the data set with more variables.
- [ ] Improve questions in the survey to be more accurate.
- [ ] Include other elements of relevance in neighbourhood details (e.g. nearest gym, restaurants, etc.)

# Resources Used
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Heapq](https://docs.python.org/3/library/heapq.html)
- [Niche.com](https://www.niche.com/)
- [Figma](https://www.figma.com/)

# Credits
This project was created for our Algorithms and Data Structures course at IE University. The project was created by:
- Duarte Barbosa
- Joaquín de Tord
- Manuel Mena
- Giacomo Pedersoli
- Oscar Tluszcz
- Simão Varandas
