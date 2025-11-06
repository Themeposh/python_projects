from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    users = ['Alice', 'Bob', 'Charlie']
    return render_template('about.html', users=users)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', username=username)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    # return f"Form submitted! Hello, {username}!"
    return render_template('user_info.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
