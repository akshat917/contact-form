from flask import Flask, render_template, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv("https://mfmzzcxponmcwtpytwev.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1mbXp6Y3hwb25tY3d0cHl0d2V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxNzYwMTIsImV4cCI6MjA5Mjc1MjAxMn0.FW27EhIkKijRQVROZaosXvqU0dEjovDaI44i4ZQy8PI")

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

