import os
from datetime import datetime

def generate_index_html(directory):
    # List all HTML files in the directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    # Sort files by modification time, newest first
    html_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    
    # Generate HTML content
    html_content = "<html><head><title>Math Seminars at The Graduate Center of CUNY</title></head><body>"
    html_content += '<h1 style="text-align: center;">Weekly Bulletin of Math Seminars at The Graduate Center of CUNY</h1>'
    
    # Add Recent section
    html_content += "<h2>Recent</h2><ul>"
    for i, file in enumerate(html_files[:4]):
        file_title = os.path.splitext(file)[0]
        html_content += f"<li><a href='{file}'>Week {file_title}</a></li>"
    html_content += "</ul>"
    
    # Add Past section
    html_content += "<h2>Past</h2><ul>"
    for file in html_files[4:]:
        file_title = os.path.splitext(file)[0]
        html_content += f"<li><a href='{file}'>Week {file_title}</a></li>"
    html_content += "</ul>"
    
    html_content += "</body></html>"
    
    # Write the index.html file
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write(html_content)

# Directory containing the HTML files
directory = 'WeeklyBulletins'

# Generate the index.html file
generate_index_html(directory)

print("index.html has been generated successfully.")