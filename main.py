from flask import Flask, render_template, request, redirect, url_for
import pymysql
#Setup web microservice

app = Flask(__name__)
conn = pymysql.connect("localhost","root","","studentdb") #Connect Database

@app.route("/")
def index():
    with conn:
        cur = conn.cursor() # scanning db
        cur.execute("SELECT * FROM student") # execute
        rows = cur.fetchall() # import all db from table student
        return render_template("index.html", datas=rows)

@app.route("/addstudent")
def showform():
    return render_template("addstudent.html")

@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql ="Insert into student (fname, lname, phone) values(%s,%s,%s)" #Syntax for mariadb
            cursor.execute(sql, (fname, lname, phone))
            conn.commit() #Change data
        return redirect(url_for("index"))

@app.route("/update", methods=['POST'])
def update():
    if request.method == "POST":
        id_update = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql ="update student set fname=%s, lname=%s, phone=%s where id=%s" #Syntax for mariadb
            cursor.execute(sql, (fname, lname, phone, id_update))
            conn.commit() #Change data
        return redirect(url_for("index"))

@app.route("/delete/<string:id_data>", methods=['GET']) #id_data is number of id for deleting
def delete(id_data):
    with conn:
        cur = conn.cursor() # scanning db
        cur.execute("delete from student where id=%s",(id_data)) #%s is String
        conn.commit()
    return redirect(url_for("index"))

@app.route("/hello")
def hello():
    string = "Python Flask"
    return render_template("index.html", data=string) #Import index.html and import data to index.html


@app.route("/student")
def student():
    return "Anuchit Kumhomkul"

if __name__ == '__main__':
    app.run(debug=True)
