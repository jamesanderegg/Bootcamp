from flask import Flask, render_template
from pymongo import MongoClient
import get_data

app = Flask(__name__)

client = MongoClient('localhost',27017)
    
db = client.mars_data
collection = db.mars_data    
new_data = collection.find_one()

@app.route('/')
def index():
    

    return(render_template('index.html', data=new_data))

@app.route('/scrape')
def scrape():
     new_data = get_data.scraaaaape()

     return index()

@app.route('/hemispheres/')
def hemispheres():


    return render_template('hemispheres.html', data=new_data)

if __name__ == "__main__":
    app.run(debug=True)