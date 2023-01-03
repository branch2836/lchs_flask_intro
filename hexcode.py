from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

# Code the 'valid_hex_chars' function here:
def valid_hex_chars(hex):
    valid = "1234567890abcdefABCDEF"
    isValid = True
    for char in hex:
        if char not in valid:
            isValid = False
            break;
    
    return isValid

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
    if request.method == 'POST':
        hex = request.form['hex']
        if len(hex) != 6:
            feedback = "Enter a correct Hex Value"
            hex= "FF0000"
        elif not valid_hex_chars(hex):
            hex="FF0000"
            feedback="Valid Hex characters are 0-9 and A-F"
        else:
            feedback = "Successful Submission"
    else:        
        hex = '00FF00'
        feedback = "feedback"

    return render_template('hex_form.html', hex=hex, feedback= feedback)

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
