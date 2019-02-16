from flask import Flask, render_template, request
from scraper import get_votes
app = Flask(__name__)

## Make API calls in this file. Use name of elected official as first two parameters for get_votes(). 
## 'select' is the third param.
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		select_iss = request.form.get('issues')
		print(select_iss)
		select_loc = request.form.get('location')
		print(select_loc)
	return render_template('result.html')

if __name__ == "__main__":
	app.run(debug=True)
