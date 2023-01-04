from flask import Flask, render_template, request
from encrypt import encrypt_with_shift

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_message', methods=["GET", "POST"])
def user_message(): 
    original_msg= "The user's message will appear here"
    coded_msg ="The coded message will appear here"

    if request.method =='POST':
        original_msg= request.form['message']
        shift = int(request.form['shift'])
        code_action = request.form['code-action']
        #coded_msg=encrypt_with_shift(original_msg, shift)
        if code_action == "encrypt":
            coded_msg=encrypt_with_shift(original_msg, shift)
        elif code_action =="decrypt":
            coded_msg = encrypt_with_shift(original_msg, -shift)
    elif request.method=='GET':
        original_message = ''
        number = ''
        code_action=''

    return render_template('user_message.html', original_msg=original_msg, coded_msg=coded_msg)

if __name__ == '__main__':
    app.run()

# Instructions for this project can be found here:
# https://education.launchcode.org/lchs/chapters/flask-intro/project.html
