from flask import session, request, redirect, url_for
from sqlalchemy import text
from backend import app, db

from backend.db_schema import User, Snippet


@app.route("/api/login", methods=["GET", "POST"])
def login():
    data = request.get_json() if request.is_json else request.form
    if request.method == "POST":
        username = data.get("username") if request.is_json else request.form["username"]
        password = data.get("password") if request.is_json else request.form["password"]

        query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
        result = db.session.execute(text(query))
        user = result.fetchone()

        if user:
            session["username"] = user.username
            return {
                "status": "success",
                "user": {"id": user.id, "username": user.username},
            }

    return {"status": "error", "message": "Ungültige Zugangsdaten."}


@app.route("/api/logout")
def logout():
    try:
        session.pop("username", None)
        return {"status": "success", "message": "Erfolgreich ausgeloggt."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.route("/api/register", methods=["GET", "POST"])
def register():
    error = None
    data = request.get_json() if request.is_json else request.form
    print("Received registration data:", data)  # Debug-Ausgabe
    if request.method == "POST":
        username = data.get("username")
        password = data.get("password")
        retypepassword = data.get("retypepassword")

        if password != retypepassword:
            return {"status": "error", "message": "Passwörter stimmen nicht überein."}

        neuer_user = User(username=username, password=password)
        db.session.add(neuer_user)
        db.session.commit()
        session["username"] = username
        return {
            "status": "success",
            "user": {"id": neuer_user.id, "username": neuer_user.username},
        }

    return {"status": "error", "message": error or "Registrierung fehlgeschlagen."}


@app.route("/api/search")
def search():
    q = request.args.get("q", "")

    query = f"SELECT * FROM snippets WHERE title LIKE '%{q}%' OR content LIKE '%{q}%'"
    result = db.session.execute(text(query))
    items = result.fetchall()

    return {"status": "success", "items": [dict(row) for row in items]}


@app.route("/api/snippets")
def snippets():
    query = "SELECT * FROM snippets"
    result = db.session.execute(text(query))
    items = result.fetchall()

    return {"status": "success", "items": [dict(row) for row in items]}


@app.route("/api/snippets/<int:snippet_id>")
def snippet_detail(snippet_id):
    query = f"SELECT * FROM snippets WHERE id = {snippet_id}"
    result = db.session.execute(text(query))
    item = result.fetchone()

    if item:
        return {"status": "success", "item": dict(item)}
    else:
        return {"status": "error", "message": "Snippet nicht gefunden."}


@app.route("/api/snippets/create", methods=["POST"])
def create_snippet():
    title = request.form["title"]
    content = request.form["content"]

    neuer_snippet = Snippet(title=title, content=content)
    db.session.add(neuer_snippet)
    db.session.commit()

    return {
        "status": "success",
        "item": {"id": neuer_snippet.id, "title": neuer_snippet.title},
    }
