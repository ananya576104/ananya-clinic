from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def insert_into_db(name, email, phone, message):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, email, phone, message) VALUES (?, ?, ?, ?)",
              (name, email, phone, message))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    insert_into_db(data['name'], data['email'], data['phone'], data['message'])
    return "Thank you! We'll get back to you soon."

if __name__ == '__main__':
    app.run(debug=True)
