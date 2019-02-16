from flask import Flask, render_template, request
from scraper import get_votes
from project import output_data
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
		double_dict = output_data(select_loc)
		for candidate in double_dict:
			double_dict[candidate]['votes'] = get_votes(double_dict[candidate]['First Name'], \
			double_dict[candidate]['Last Name'], select_iss)
	return render_template('result.html', first=double_dict['Candidate0'], second=double_dict['Candidate1'], \
	third=double_dict['Candidate5'])

if __name__ == "__main__":
	app.run(debug=True)
