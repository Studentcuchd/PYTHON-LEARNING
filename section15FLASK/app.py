from flask import Flask,render_template

# use flask to create app

app=Flask(__name__)


emp_data={
    0:{
        "name":"Parag",
        "age":19
    },
    1:{
        "name":"Bajaj",
        "age":20
    }
}


# create route using decorator
@app.route("/")
def home():
    return "Hello guys this is home"


@app.route("/data/<int:emp_id>")
def data(emp_id):
    
    """ 
    no use of html
        return f"Name of employye is {emp_details["name"]} and age of emplyee is {emp_details["age"]}"    
    """
    
    
    # return error page
    emp_details=emp_data.get(emp_id)
    if not emp_details:
        return render_template("error.html",message=f"You donot have accsess of this empolyee with name")
    
    return render_template("empdetails.html",emp_details=emp_details)
# run
if __name__=="__main__":
    app.run(debug=True)