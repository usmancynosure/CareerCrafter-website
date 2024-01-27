from flask import Flask, jsonify, render_template, request, redirect, url_for, flash

app = Flask(__name__) #flask app starter pack


Jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Lahore, Pakistan',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Islamabad, Pakistan',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',

  }
]

@app.route("/")
def hello():
  return render_template("home.html",jobs=Jobs  )


@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
