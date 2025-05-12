# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db
                           )

#Recopilando feedback
@app.route("/opinion", methods=["POST"])
def submit_form():
    email = request.form["email"]
    text = request.form["text"]

    with open("opinion.txt", "a") as f:
        f.write(f"{email}, {text}\n")
            
    return render_template("result.html", email=email, text=text)

if __name__ == "__main__":
    app.run(debug=True)
