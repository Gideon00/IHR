from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, verify_license_number
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

# Config sessions
# app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///records.db")

# Set SQLite to WAL mode
# db.execute("PRAGMA journal_mode=WAL;")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
    

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure email was submitted
        if not request.form.get("email"):
            return apology("must provide email", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for email
        rows = db.execute("SELECT * FROM physicians WHERE email = ?", request.form.get("email"))

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid email and/or password", 403)

        # Remember which user has logged in
        session["physician_id"] = rows[0]["id"]
        session["name"] = rows[0]["firstName"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sign_in.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
       # Physician Authentication
        if not request.form.get("first_name"):
            return apology("must provide First Nmae", 400)
        elif not request.form.get("surname_name"):
            return apology("must provide Surname", 400)
        elif not request.form.get("email"):
            return apology("must provide a valid email", 400)
        elif db.execute("SELECT * FROM physicians WHERE email = ?", request.form.get("email")):
            return apology("User already exits", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        
        elif request.form.get("password") != request.form.get("confirmPassword"):
            return apology("password do not match confirmation password", 400)
        
        # Check if license is Valid
        if verify_license_number(request.form.get("license"))["valid"]:
            print("license is Valid:", request.form.get("license"))
        db.execute("INSERT INTO physicians (firstName, surName, email, hash) VALUES(?, ?, ?, ?)", request.form.get("first_name"), request.form.get("surname_name"), request.form.get("email"), generate_password_hash(request.form.get("password")))

        # redirect user to login
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("signup.html")
    
# Log User Out  
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/conversation", methods=["GET", "POST"])
def conversation():
    if request.method == "POST":
        data = request.json  # Parse JSON data from the request
        start = data.get("startRecording")  # Extract the specific field
        if start:
            # Add your logic to start recording here

            return jsonify({"message": "Recording started"}), 200
        else:
            return jsonify({"message": "Invalid request"}), 400
    else:
        return render_template("voice-recoding-in-progress-page.html")
    

@app.route("/transcript", methods=["GET", "POST"])
def transcript():
    if request.method == "POST":
        pass
    else:
        return render_template("transcript-page.html")