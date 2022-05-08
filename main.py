import json
from flask import Flask
from flask import render_template


app = Flask(__name__)   

@app.route('/')
def home():
    with open('data-storage/greeting-price.json') as f:
        master = 25
        price_list = json.load(f)
        return render_template('index.html', price_list=price_list, master=master)


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
    with open('data-storage/city_area.json') as file:
        area = json.load(file)
    return render_template('contact.html', area=area)


# def footer_time():
#     today = str(datetime.date.today()).split('-')
#     today = today[0]
#     return render_template('footer.html', year=today)


if __name__ == '__main__':
   app.run(debug='True')
