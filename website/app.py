from flask import Flask,render_template 
import sqlite3
import pathlib

app=Flask(__name__) 
base_path=pathlib.Path.cwd()
db_name="immigration.db"
file_path=base_path/db_name

@app.route("/") 
def index(): 
    return render_template("home-page.html") 


@app.route("/about") 
def about(): 
    return render_template("about.html") 

@app.route("/data") 
def data():
    con=sqlite3.connect(file_path)
    cursor=con.cursor()
    canada=cursor.execute("select * from canada limit 10").fetchall()
    con.close()
    return render_template("data.html", canada=canada)


if __name__=="__main__":
    app.run(debug=True)