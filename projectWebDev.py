from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Mehvish"
    age = "16"
    ascii = "°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸"
    return render_template('project.html', name = name, age = age, ascii = ascii)

@app.route('/father')
def father():
    name = "Irfan"
    age = "Favorite Color: Red"
    ascii = "@( * O * )@"
    return render_template('project.html', name = name, age = age, ascii = ascii)

@app.route('/mother')
def mother():
    name = "Wahida"
    age = "Favorite Color: Pink"
    ascii = "٩(̾●̮̮̃̾•̃̾)۶"
    return render_template('project.html', name = name, age = age, ascii = ascii)

@app.route('/sister')
def sister():
    name = "Misbah"
    age = "12"
    ascii = "٩(- ̮̮̃-̃)۶"
    return render_template('project.html', name = name, age = age, ascii = ascii)

@app.route('/friend')
def friend():
    name = "Mariam"
    age = "17"
    ascii = "@('_')@"
    return render_template('project.html', name = name, age = age, ascii = ascii)

app.run()