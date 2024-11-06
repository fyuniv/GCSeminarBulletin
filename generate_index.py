import os
from datetime import datetime

def generate_index_html(directory):
    # List all HTML files in the directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    # Sort files by filename date, newest first
    html_files.sort(reverse=True)
    
    # Generate HTML content
    html_content = """
    <html>
    <head>
        <title>Math Seminars at The Graduate Center of CUNY</title>
        <link href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Gothic A1', sans-serif;
                margin: 8%;
                line-height: 1.6; /* Increased line height */
                font-size: 16px; /* Adjusted font size */
                padding: 20px; /* Added padding */
            }
            h1 {
                text-align: center;
                font-size: 2.5em; /* Adjusted font size */
            }
            h2 {
                margin-top: 40px;
                font-size: 2em; /* Adjusted font size */
            }
            ul {
                list-style-type: disc; /* Changed to disc for bullets */
                padding-left: 20px; /* Added padding to align bullets */
            }
            li {
                margin: 10px 0;
            }
            a {
                text-decoration: none;
                color: #007BFF; /* Softer color for links */
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
    """
    html_content += '<h1>Weekly Bulletin of Math Seminars at The Graduate Center of CUNY</h1>'
    
    # Add Recent section
    html_content += "<h2>Recent</h2><ul>"
    for i, file in enumerate(html_files[:2]):
        file_title = os.path.splitext(file)[0]
        html_content += f"<li><a href='{file}'>Week {file_title}</a></li>"
    html_content += "</ul>"
    
    # Add Past section
    html_content += "<h2>Past</h2><ul>"
    for file in html_files[2:]:
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
