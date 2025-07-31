from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "name": "Soumaya",
        "stamp": "August 1, 2025",
        "mem_date": {
            "first_date": "3rd of April • Arribat Center → Mega Mall",
            "first_touch": "Marina Salé • first time we held hands",
            "first_kiss": "12th of July • sunset"
        },
        "admires": ["Your serenity" , "beauty" , "love" , "compassion" , "I love everything about you down to your last minute detail"],
        "promise": "I promise to keep loving you—if not the same way I do now, then more. All of my love will be for you, and you only.",
        # Code-unlock messages (you’ll text her the codes at those times)
        "codes": [
            {"code": "ROSE",  "label": "Morning Gift", "msg": "You are my first thought every morning."},
            {"code": "SMILE", "label": "Noon Gift",    "msg": "Even from afar, your smile is my sunshine."},
            {"code": "STAR",  "label": "Evening Gift", "msg": "The sunset will never be as beautiful as our first kiss."},
            {"code": "KISS",  "label": "Night Gift",   "msg": "Sleep peacefully, my forever. I am yours in every dream."}
        ]
    }
    return render_template("index.html", **data)

# app.py
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # lets you test with PORT too
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
