from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Novara, Italy',
    'salary': '€ 30.000'
  },
  {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Milan, Italy',
  'salary': '€ 35.000'
  },
  {
    'id': 3,
    'title': 'Fronted',
    'location': 'remot',
  },
  {
    'id': 4,
    'title': 'Backend',
    'location': 'turin, Italy',
    'salary': '€ 20.000'
  },
]

@app.route('/')
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Hossein')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)