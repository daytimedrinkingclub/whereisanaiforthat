# app/routes/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from supabase_client import supabase
from app.forms.submit_form import SubmitForm
from app.services.supabase_data_service import submit_tool

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

    return render_template('home/home.html', data=data, categories=categories, selected_category=selected_category)

@main.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        # Process the submitted form data and insert it into the Supabase table using the submit_tool service
        form_data = {
            'tool_name': form.tool_name.data,
            'tool_link': form.tool_link.data,
            'product_hunt_link': form.product_hunt_link.data,
            'tool_categories': form.tool_categories.data,
            'tool_description': form.tool_description.data,
            'tool_tags': form.tool_tags.data
        }
        if submit_tool(form_data):
            return redirect(url_for('main.index'))
    return render_template('home/submit.html', form=form)

@main.route('/about')
def about():
    return render_template('home/about.html')
