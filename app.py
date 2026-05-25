import os
import sqlite3
from flask import Flask, redirect, url_for, session, render_template, request
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"}
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    redirect_uri = url_for("auth_callback", _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route("/auth/google/callback")
def auth_callback():
    token = google.authorize_access_token()
    user_info = token.get("userinfo")
    session["user"] = user_info
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    user = session.get("user")

    if not user:
        return redirect("/")

    return render_template("dashboard.html", user=user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route('/split-step')
def split_step():

    user = session.get("user")

    if not user:
        return redirect("/")

    return render_template("split_step.html")

@app.route("/drills")
def drills():
    user = session.get("user")

    if not user:
        return redirect("/")

    search = request.args.get("search", "")
    skill_level = request.args.get("skill_level", "")
    focus_area = request.args.get("focus_area", "")

    connection = sqlite3.connect("drills.db")
    cursor = connection.cursor()

    query = "SELECT * FROM drills WHERE 1=1"
    params = []

    if search:
        query += """
        AND (
            title LIKE ?
            OR description LIKE ?
            OR instructions LIKE ?
            OR tags LIKE ?
        )
        """
        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    if skill_level:
        query += " AND skill_level = ?"
        params.append(skill_level)

    if focus_area:
        query += " AND focus_area = ?"
        params.append(focus_area)

    cursor.execute(query, params)
    drills = cursor.fetchall()

    cursor.execute("SELECT DISTINCT skill_level FROM drills WHERE skill_level IS NOT NULL AND skill_level != ''")
    skill_levels = cursor.fetchall()

    cursor.execute("SELECT DISTINCT focus_area FROM drills WHERE focus_area IS NOT NULL AND focus_area != ''")
    focus_areas = cursor.fetchall()

    connection.close()

    return render_template(
        "drills.html",
        drills=drills,
        search=search,
        selected_skill_level=skill_level,
        selected_focus_area=focus_area,
        skill_levels=skill_levels,
        focus_areas=focus_areas
    )


if __name__ == "__main__":
    app.run(debug=True)