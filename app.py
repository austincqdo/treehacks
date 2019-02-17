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
			double_dict[candidate]['Phone #'] = "N/A"
			if double_dict[candidate]['votes'] == []:
				double_dict[candidate]['votes'] = ["N/A"]
			if double_dict[candidate]['First Name'] == "Eleini":
				double_dict[candidate]['First Name'] = "Eleni"
				double_dict[candidate]['Bio'] = "In 1992, Eleni started her career as a staff member of the California Democratic Party in Sacramento and worked in the historic election, which elected two women to the U.S. Senate and turned California blue. \
				After the election, Eleni joined her family business, AKT Development, one of California’s most respected housing development firms. Over the next 18 years, Eleni worked her way up from project manager to president. \
				Her work delivering housing for middle-class families in the Sacramento region earned her recognition as one of Sacramento’s most prominent businesswomen.\
				In 2010, Eleni was appointed by President Barack Obama as the U.S. Ambassador to Hungary and served side-by-side President Obama and Secretary Hillary Clinton promoting democracy."
				double_dict[candidate]['Phone #'] = "(415) 857-0921"
				double_dict[candidate]['donations'] = ["Kounalakis, Eleni Tsakopolous: $7,679,896.00", "California Association of Realtors: $29,200.00", \
				"Northern California Regional Council of Carpenters: $29,200.00", "Spanos Companies, including Alex G Spanos & Affiliated Entities: $19,600.00"]
			if double_dict[candidate]['First Name'] == "Marc":
				double_dict[candidate]['Phone #'] = "(650) 691-2121"
				double_dict[candidate]['donations'] = ["Berman, Marc: $73,700", "Pivot Group Inc.: $18,534", "California Association Of Realtors: $17,000", \
				"Northern California Regional Council Of Carpenters: $15,000"]
			if double_dict[candidate]['First Name'] == "Anna":
				double_dict[candidate]['Phone #'] = "(650) 323-2984"
				double_dict[candidate]['donations'] = ["Votesane PAC: $58,000", "Oracle Corp: $21,480", "Stanford University: $19,350", \
				"Kleiner, Perkins et al: $18,900"]
	return render_template('result.html', first=double_dict['Candidate0'], second=double_dict['Candidate1'], \
	third=double_dict['Candidate5'], area=select_loc, topic=select_iss.replace("_", " "))

if __name__ == "__main__":
	app.run(debug=True)
