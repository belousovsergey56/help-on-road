import json
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    with open('data-storage/greeting-price.json') as f:
        price_list = json.load(f)
        return render_template('index.html', price_list=price_list)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    with open('data-storage/services.json') as file:
        item = json.load(file)
        return render_template('services.html', item=item)


@app.route('/feedback')
def create_feedback():
    with open('data-storage/feedbacks.json') as file:
        feedback = json.load(file)
        return render_template('feedback.html', feedback=feedback)

@app.route('/contact')
def contact():
    return render_template('contact.html')

#TODO
#автоматизировать дату в футере

    
if __name__ == '__main__':
    app.run(debug='True')
