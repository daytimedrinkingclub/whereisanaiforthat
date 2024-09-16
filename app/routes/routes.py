# app/routes/routes.py
from flask import Blueprint, render_template, request
from supabase_client import supabase

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Fetch categories from the 'categories' table
    try:
        categories_response = supabase.table('categories').select('category').execute()
        categories = [item['category'] for item in categories_response.data]
    except Exception as e:
        categories = []
        print(f"Error fetching categories from Supabase: {e}")

    # Fetch AI tools, potentially filtered by category
    selected_category = request.args.get('category')
    try:
        query = supabase.table('ai_tools').select('*')
        if selected_category:
            query = query.eq('tool_category', selected_category)
        response = query.execute()
        data = response.data
    except Exception as e:
        data = []
        print(f"Error fetching data from Supabase: {e}")

    return render_template('index.html', data=data, categories=categories, selected_category=selected_category)