from flask import Blueprint, render_template
from supabase_client import supabase

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Fetch data from the 'ai_tools' table
    try:
        response = supabase.table('ai_tools').select('*').execute()
        data = response.data
    except Exception as e:
        data = []
        print(f"Error fetching data from Supabase: {e}")
    return render_template('index.html', data=data)