import os
from datetime import datetime

def generate_index_html(directory):
    # List all HTML files in the directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    # Sort files by modification time, newest first
    html_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    
    # Generate HTML content
    html_content = "<html><head><title>Weekly Bulletin of Math Seminars at The Graduate Center of CUNY</title></head><body>"
    html_content += "<h1>Latest Bulletins</h1>"
    html_content += "<ul>"
    
    for i, file in enumerate(html_files):
        file_path = os.path.join(directory, file)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        if i == 0:
            html_content += f"<li><strong><a href='{file}'>{file}</a> - {mod_time}</strong></li>"
        else:
            html_content += f"<li><a href='{file}'>{file}</a> - {mod_time}</li>"
    
    html_content += "</ul></body></html>"
    
    # Write the index.html file
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write(html_content)

# Directory containing the HTML files
directory = 'WeeklyBulletins'

# Generate the index.html file
generate_index_html(directory)

print("index.html has been generated successfully.")
