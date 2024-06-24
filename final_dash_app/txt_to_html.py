from dash import html

def convert_txt_to_html(file_path):
    
    # Read in the lines
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    html_out = [html.P('')]
    for line in lines:
        html_out.append(html.P(line))

    # Return list of html p tag elements
    return html_out
