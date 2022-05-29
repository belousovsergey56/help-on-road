import json
import datetime

from flask import Flask
from flask import render_template
from random import choice

app = Flask(__name__)

contact_data = {'tel': '+79315787670', 'tg': 'https://t.me/nikname', 'wts': 'https://wa.me/79315787670', 'mail': 'info@svr.ru'}

def footer_time():
    today = str(datetime.date.today()).split('-')
    today = today[0]
    year = f'© 2012 - {today}'
    return year


@app.route('/')
def home():
    with open('data-storage/greeting-price.json', encoding='UTF-8') as f:
        master = choice((25, 26, 27, 28, 29, 30))
        price_list = json.load(f)
        return render_template('index.html', price_list=price_list, master=master, year=footer_time(), telephone=contact_data)


@app.route('/about')
def about():
    return render_template('about.html', year=footer_time())


@app.route('/services')
def services():
    with open('data-storage/services.json', encoding='UTF-8') as file:
        item = json.load(file)
        return render_template('services.html', item=item, year=footer_time())


@app.route('/feedback')
def create_feedback():
    with open('data-storage/feedbacks.json', encoding='UTF-8') as file:
        feedback = json.load(file)
        return render_template('feedback.html', feedback=feedback, year=footer_time())


@app.route('/contact')
def contact():
    with open('data-storage/city_area.json', encoding='UTF-8') as file:
        area = json.load(file)
    return render_template('contact.html', area=area, year=footer_time(), contact=contact_data)


if __name__ == '__main__':
    app.run()