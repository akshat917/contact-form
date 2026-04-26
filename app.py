from flask import Flask, render_template, request, jsonify
from supabase import create_client
import os

print("DEBUG URL:", os.getenv("SUPABASE_URL"))
print("DEBUG KEY:", os.getenv("SUPABASE_KEY"))

app = Flask(__name__)

SUPABASE_URL = os.getenv("https://mfmzzcxponmcwtpytwev.supabase.co")
SUPABASE_KEY = os.getenv("sb_publishable_YHz1BALbmb_81__-sifNwA_YR6q2TL7")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    supabase.table("contacts").insert({
        "name": data["name"],
        "email": data["email"],
        "message": data["message"]
    }).execute()

    return jsonify({"message": "Saved successfully!"})

