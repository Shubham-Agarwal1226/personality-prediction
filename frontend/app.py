from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def index():
    if request.method == "POST":
        about = request.form.get('about') #calculate HEXACO score and MBTI type and store them in variables
        return render_template('index.html', scroll='result', result=about) #return the variables
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)