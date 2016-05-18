from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "HiThere"

@app.route('/', methods=["GET"])
def index():
    return render_template("dojo_survey.html")

@app.route('/process', methods=['POST', 'GET'])
def process():


    if request.method == "POST":
        form_data = {}
        if len(request.form['name'])< 1:
            flash("Name cannot be empty! Please enter your name and submit again.")
            return redirect ('/')
        elif len(request.form['comment'])< 1:
            flash("Comment cannot be empty! Please enter a comment and submit again.")
            return redirect ('/')
        elif len(request.form['comment']) > 120:
            flash("Comment can only be 120 characters long. Please edit and submit again.")
            return redirect ('/')
        else:
            flash("You have filled in all required fields.")
        for key in request.form:
            form_data[key] = request.form[key]
        session['form_data'] = form_data

    # name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # comment = request.form['comment']
        return redirect('/process')
    return render_template("result.html", data = session['form_data'])

if __name__ == "__main__":
    app.run(debug=True)
