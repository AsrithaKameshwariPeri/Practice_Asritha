from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html', result="PASS", score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result="FAIL", score=score)

@app.route('/results/<int:marks>')
def results(marks):
    result = "fail" if marks < 60 else "success"
    return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c_programming = float(request.form['c_programming'])
        total_score = (science + maths + c_programming) / 3
        result = "fail" if total_score < 50 else "success"
        return redirect(url_for(result, score=total_score))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
