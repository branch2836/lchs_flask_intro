from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

# Code the 'valid_hex_chars' function here:

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
    if request.method == 'POST':
        hex = request.form['hex']
        feedback = "Successful Submission"
    else:        
        hex = '00FF00'
        feedback = "feedback"

    return render_template('hex_form.html', hex=hex, feedback= feedback)

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
