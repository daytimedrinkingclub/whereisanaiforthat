from supabase_client import supabase

def submit_tool(form_data):
    try:
        data = {
            'tool_name': form_data['tool_name'],
            'tool_link': form_data['tool_link'],
            'product_hunt_link': form_data['product_hunt_link'],
            'tool_categories': form_data['tool_categories'],
            'tool_description': form_data['tool_description'],
            'tool_tags': form_data['tool_tags']
        }
        supabase.table('tool_submission').insert(data).execute()
        return True
    except Exception as e:
        print(f"Error inserting data into Supabase: {e}")
        return False
