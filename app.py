from flask import Flask, render_template, request, redirect
from db.connect import get_connection

app = Flask(__name__)

# Home Route - Displays cars
@app.route('/')
def index():
    car_names = [
        "Innova Crysta",
        "Tempo Traveller",
        "Toyota Etios",
        "Toyota Rumion",
        "Maruti Suzuki Swift",
        "Premium SUVs",
        "Mini Buses",
        "Chevrolet Tavera"
    ]
    return render_template('index.html', car_names=car_names)

# Form Submission Route
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/thankyou')

# Thank You Page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
