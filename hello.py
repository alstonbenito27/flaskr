from flask import Flask,render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
#localhost:5000
@app.route('/')

def index():
    fav = ["me","onlyme","alsome"]
    stuff = "This is <strong>BOLD</strong> Text "
    return render_template("index.html",stuff = stuff,fav = fav)

#localhost:5000/user/(any name)
@app.route('/user/<name>')
#pass the name into the html file
def user(name):
    return render_template("user.html",name=name)

#create custom error page

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

#use debug to show the error and provide runtime feedback
if __name__ == '__main__':
    app.run(debug=True)