from flask import Flask,render_template
import sqlite3 as sql
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def hello():
    conn=sql.connect("universe.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from user")
    data=cur.fetchall()
    return render_template("sample.html",data=data)

if __name__=="__main__":
    app.run(debug=True)