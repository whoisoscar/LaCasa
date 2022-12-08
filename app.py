from flask import Flask, render_template, request, redirect, url_for
import random
#from heapq import heappop, heappush, heapify
from heapq_max import heappop_max, heappush_max, heapify_max

import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexNew.html')


@app.route('/questionaire', methods=["POST"])
def questionaire():
    data = request.form

    def convert_questionnaire():
        if data.get("q1") == "No" or data.get("q3") == "N/A" or data.get("q4") == "N/A" or data.get("q5") == "N/A":
            #In this case, education is not considered
            user_education = 0

        else:
            #In this case, education is considered and calculated
            if data.get("q2") == "Yes":
                user_education = 8
            elif data.get("q2") == "No":
                user_education = 2
            else:
                user_education = 0
            
            if data.get("q4") == "Yes":
                user_education += 8
            elif data.get("q4") == "No":
                user_education += 2
            else:
                user_education = 0
                
            user_education = user_education + (int(data.get("q3")) + int(data.get("q3")) - 1)

            user_education = user_education + (int(data.get("q5")) + int(data.get("q5")) - 1)

            user_education = int(round(user_education/34*9,0))
        
        #Calculating safety
        user_safety = 5 if data.get("q8") == "Yes" else 2

        user_safety += 2 if data.get("q9") == "Yes" else 4

        user_safety += int(data.get("q6"))

        user_safety += int(data.get("q7"))

        user_safety += int(data.get("q10"))

        user_safety = int(round(user_safety/25*5,0))

        return user_safety, user_education
    

    safety, education = convert_questionnaire()

    letter_convert = {
        9:"A%2B",
        8:"A",
        7:"A-",
        6:"B%2B",
        5:"B",
        4:"B-",
        3:"C%2B",
        2:"C",
        1:"D%2B",
        0:"N/A"
    }

    safety = letter_convert[safety]
    education = letter_convert[education]
    state = "Los Angeles, CA"
    price_range = data.get("q11")
    return redirect(f'{url_for("search_results")}?state={state}&education={education}&safety={safety}&price_range={price_range}')

@app.route('/search')
def search_results():
    state = request.args.get("state")
    education = request.args.get("education")
    safety = request.args.get("safety")

    price_range = request.args.get("price_range")

    letter_convert = {
        "A+":9,
        "A":8,
        "A-":7,
        "B+":6,
        "B":5,
        "B-":4,
        "C+":3,
        "C":2,
        "D+":1,
        "N/A":0
    }

    letter_convert_back = {
        9:"A+",
        8:"A",
        7:"A-",
        6:"B+",
        5:"B",
        4:"B-",
        3:"C+",
        2:"C",
        1:"D+",
        0:"N/A"
    }

    backend_price_range = price_range.replace(",","").split("-")
    backend_price_range = [int(x) for x in backend_price_range]
    backend_safety = letter_convert[safety]
    backend_education = letter_convert[education]

    #Creating empty binary tree
    possible_neighbours = []
    heapify_max(possible_neighbours)

    #Creating empty final list
    display = []

    #Creating Class
    #test
    class District:
        def __init__(self, name, education, safety, price):
            self.name = name
            self.education = int(education)
            self.safety = int(safety)
            self.price = int(price.replace(",", ""))
            self.rank = int(0)

        def calculate_points(self, input_education, input_safety, input_price):
            if self.price > input_price:
                return None

            else:
                difference_to_rank = {
                        0: 2,
                        -1:1,
                        1:3,
                        2:4,
                        3:4,
                        4:4,
                        5:4,
                        6:4,
                        -2:0,
                        -3:-1,
                        -4:-1,
                        -5:-2,
                        -6:-2
                    }
                if input_education != 0:
                    #If education level is 0, skip this part
                    
                    #Difference between actual education & input
                    difference = self.education - input_education
                    self.rank += difference_to_rank[difference]

                #Difference between actual safety & input
                difference = self.safety - input_safety
                self.rank += difference_to_rank[difference]
                
                heappush_max(possible_neighbours, (self.rank, self.name))


    LA_database = []
    with open("housing_data.csv", "r") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        for row in reader:
            LA_database.append(District(row[0], row[1], row[2], row[3]))

    # Creating function to use method of distric and rank them
    def ranking(database, user_education, user_safety, user_price):
        
        for i in database:
            
            i.calculate_points(user_education, user_safety, user_price)

        while len(display) != 5:
            try:
                aux = heappop_max(possible_neighbours)
            except:
                return "No results found"
            
            for i in LA_database:
                if i.name == aux[1]:
                    aux2 = [aux[0], aux[1], i.price, i.safety, i.education]

            display.append(aux2)
            display.sort(key=lambda e: (e[0], e[2]))
        
        return display

    results = ranking(LA_database, backend_education, backend_safety, backend_price_range[0])
    if results == "No results found":
        return "No results found"

    for result in results:
        result[2] = f'{result[2]:,}'
        result[3] = letter_convert_back[result[3]]
        result[4] = letter_convert_back[result[4]]
    

    return render_template('results.html', state=state, education=education, safety=safety, price_range=price_range, random_num=random.randint(9,60), results=results)