from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
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


# Thank You Page (for later after contact form)
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
