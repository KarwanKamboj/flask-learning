from flask import Flask # flask is class imported to build application
from flask import render_template

app = Flask(__name__)  # app is an object(instance) of application created
                        # name is a special variable contains name of the current file or module
                        # flask uses it to locate templates,static and other files
@app.route("/")   # decorater, to execute particular function when user visits the url
def home():       # / represents homepage of website
    return render_template("index.html",name ="Karwan") # sends response to the web browser
                        # html pages using templates can also be returned such as return render_template("index.html")
if __name__ == "__main__": # to check that file is executed directly,not imported to other file
    app.run(debug=True)  # enables debug mode ,so that whenever there is changes the server automatically loads
                        # app.run() starts the application