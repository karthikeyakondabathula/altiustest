from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = 'task.db'

# Setup DB on first run
def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tname TEXT,
                priority INTEGER,
                datepick DATE,
                status TEXT
            )
        ''')
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        taskname = request.form["taskname"]
        priority = int(request.form["priority"])
        datepick = request.form["datepicker"]

        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO task (tname, priority, datepick, status) VALUES (?, ?, ?, ?)",
                         (taskname, priority, datepick, "Pending"))
        return redirect("/")

    with sqlite3.connect(DB) as conn:
        items = conn.execute("SELECT * FROM task ORDER BY priority, datepick").fetchall()
        tot = len(conn.execute("SELECT * FROM task").fetchall())
        don = conn.execute("SELECT * FROM task WHERE status = \'Done\'").fetchall()
        print(tot, len(don))
    return render_template("index.html", items=items, total=int(tot), done=int(len(don)))




@app.route("/delete/<int:item_id>")
def delete(item_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM task WHERE id = ?", (item_id,))
    return redirect("/")



@app.route("/unmark/<int:item_id>")
def unmark(item_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("UPDATE task SET status = 'Pending' WHERE id = ?", (item_id,))
    return redirect("/")


@app.route("/donefilter")
def donefilter():
    with sqlite3.connect(DB) as conn:
        don = conn.execute("SELECT * FROM task WHERE status = \'Done\'").fetchall()

    return render_template("index.html", items=don)

    return redirect("/")


@app.route("/allfilter")
def allfilter():
    with sqlite3.connect(DB) as conn:
        don = conn.execute("SELECT * FROM task").fetchall()

    return render_template("index.html", items=don)

    return redirect("/")

@app.route("/pendingfilter")
def pendingfilter():
    with sqlite3.connect(DB) as conn:
        don = conn.execute("SELECT * FROM task WHERE status = \'Pending\'").fetchall()

    return render_template("index.html", items=don)

    return redirect("/")


@app.route("/mark/<int:item_id>")
def mark(item_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("UPDATE task SET status = 'Done' WHERE id = ?", (item_id,))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
