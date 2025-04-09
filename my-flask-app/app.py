from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# A route that takes user input and returns it
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

