"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import json
from bson import BSON
from bson import json_util 
from bson.json_util import dumps
from flask import Flask
from flask import jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app



#client = MongoClient("mongodb+srv://Aadya:Aadya123@cluster0-ztgvb.azure.mongodb.net/test?retryWrites=true&w=majority")
#db = client['FaliedBanks']
#collection = db['Data']
#collection=client["FaliedBanks"]
#cursor = collection.find({})
#for document in cursor:
#    final = json.dumps(document, indent=4, default=json_util.default)
#    print(final)
#exit()
#db = collection["Data"]
#headData = db.find()
#row_list = []
#for i in headData:
#    row_list.append(i)
#cursor = collection.find({})
#for document in cursor:
#    final = json.dumps(document, indent=4, default=json_util.default)
#    print(final)
#exit()

@app.route('/')
def hello():
    return render_template("index.html")

#@app.route('/pie-chart')
#def google_pie_chart():
#    data = {'Task' : 'Number of registers', '2009' : 3, '2010' : 5, '2011' : 2, '2012' : 4, '2013' : 20, '2014' : 10, '2015' : 13, '2016' : 2,'2017' : 3,'2018' : 3,'2019' : 14,'2020' : 21}
#    return render_template('pie-chart.html')

@app.route('/bar-chart')
def google_bar_chart():
    return render_template('bar-chart.html')

@app.route('/bar-chart1')
def google_bar_chart1():
     return render_template('bar-chart1.html')


@app.route('/pie-chart')
def google_pie_chart():
	data = {'Task' : 'Number of registers', '2009' : 3, '2010' : 5, '2011' : 2, '2012' : 4, '2013' : 20, '2014' : 10, '2015' : 13, '2016' : 2,'2017' : 3,'2018' : 3,'2019' : 14,'2020' : 21}
#	print(data)
	return render_template('pie-chart.html', data=data)


#@app.route('/pie-chart')
#def google_line_chart():
#    data = db.inventory.find({
#        df.groupby(['joined']).count()
#        })
#    return render_template('line-chart.html', data=data)


#@app.route('/bar-chart')
#def google_bar_chart():
#    data = db.inventory.find({
#        df.groupby(['handle'],['Tweets, Likes, Followers']).sort({ natural: 1 }).limit(4)
#        })
#    return render_template('bar-chart.html', data=data)

#@app.route('/bar-chart1')
#def google_bar_chart1():
#     data = db.inventory.find({
#        df.groupby(['trollbot_score'],['Following, Likes']).count({ ['trollbot_score'] }).limit(4)
#        })
#     return render_template('bar-chart1.html', data=data)




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

#@app.route('/')
#def hello():
#    """Renders a sample page."""
#    return "Hello World!"

#if __name__ == '__main__':
#	app.run()

#from flask import Flask
#from flask_googlecharts import GoogleCharts
#from flask_googlecharts import BarChart
#from flask import jsonify, request, render_template

#app = Flask(__name__)
#charts = GoogleCharts(app)

#charts = GoogleCharts()

#app = Flask(__name__)
#charts.init_app(app)
#app = Flask(__name__)
#charts = GoogleCharts(app)

#my_chart = BarChart("my_chart")

#my_chart = BarChart("my_chart", options={'title': 'My Chart'})
#@app.route('/')
#def chart():
#    my_chart = BarChart("my_chart", options={'title': 'My Chart'}, data_url='D:\new-york-city-airbnb-open-data\AB_NYC_2019.csv')
#    return render_template('chart.html', data=my_chart)
#hot_dog_chart.add_column("string", "Competitor")
#hot_dog_chart.add_column("number", "Hot Dogs")
#hot_dog_chart.add_rows([["Matthew Stonie", 62],
#                        ["Joey Chestnut", 60],
#                        ["Eater X", 35.5],
#                        ["Erik Denmark", 33],
#                        ["Adrian Morgan", 31]])



