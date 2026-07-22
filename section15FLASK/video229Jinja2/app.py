from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)

shop_details={
    1:{
        "name":"Gen store",
        "Open":"6am"
    }
}

# @app.route("/")
# def home():
#     return "Welcome to the shop buddy"

@app.route("/")
def home():
    return render_template("homes.html",shop_details=shop_details)

@app.route("/data/<int:shop_id>")
def shopdetail(shop_id):
    shop_info=shop_details.get(shop_id)
    
    if not shop_info:
        return render_template("error.html")
    
    return render_template("detail.html",shop_info=shop_info)



# using get method for this 

# @app.route("/form")
# def form():
#     return render_template("form.html")


@app.route("/form/data", methods=["GET","POST"])
def get_data():
    
    if request.method=="POST":
        name=request.form.get('name')
        open=request.form.get('open')
        shop_id=len(shop_details.keys())+1
        shop_details[shop_id]={"name":name,"Open":open}
        
        # return f"shop added with id {shop_id}"
        
        return redirect(url_for ('shopdetail',shop_id=shop_id))
    return render_template("form.html")
    
if __name__=="__main__":
    app.run(debug=True)