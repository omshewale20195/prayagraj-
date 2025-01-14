from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Dummy database for demonstration (use an actual database in production)
donations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']
        message = request.form['message']

        # Store the donation details
        donations.append({
            'name': name,
            'email': email,
            'amount': amount,
            'message': message
        })

        return redirect(url_for('qr_code'))
    return render_template('donate.html')

@app.route('/qr-code')
def qr_code():
    return render_template('qr_code.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/updates')
def updates():
    return render_template('updates.html', donations=donations)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Handle the contact form data (e.g., send email or save to database)
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
