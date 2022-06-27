from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/nos-prix')
def nos_prix():
  return render_template('nos-prix.html')

@app.route('/notre_equipe')
def notre_equipe():
  return render_template('notre_equipe.html')

@app.route('/section-des-enfants')
def section_enfants():
  return render_template('section-des-enfants.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')


app.run(host='0.0.0.0', port=81)