from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {"title": "Software Engineer", "location": "Seattle, WA", "salary": "$120,000"},
    {"title": "Data Analyst", "location": "New York, NY", "salary": "$80,000"},
    {"title": "Web Developer", "location": "San Francisco, CA", "salary": "$100,000"},
    {"title": "Project Manager", "location": "London, UK", "salary": "£50,000"},
    {"title": "Graphic Designer", "location": "Paris, France", "salary": "€40,000"}
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Wassen')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)