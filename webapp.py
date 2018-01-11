from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['GET', 'POST')
def render_response():
    color = request.args['color']
    #The request object stores infor about the request sent to the server
    #args is a "MultiDict" - a dictionary that can hold more than one value per key
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    error = None
    if request.method == 'POST':
        if color == "blue":
            reply = "Nice! That's my favorite color, too!"
        else:
            reply = "Are you kidding me, " + color + "?! What a garbo color. Blue is clearly the best color"
         return render_template('response.html', response = reply, error=error)
    else:
        error = 'color invalid'
        return render_template('response.html', error=error)
   
def login():
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
