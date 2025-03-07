

class HtmlReport:
    """ Class for generating an HTML report with the analysis results. """
    #----------------------------------------------------------------
    @staticmethod
    def generate_html_report(html_file, sorted_clues, sorted_categories, sorted_answers):
        """ Generate an HTML report with navigation and tables. """

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Scraped Data Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }}
                nav {{
                    background: #333;
                    padding: 15px;
                    text-align: center;
                }}
                nav a {{
                    color: white;
                    text-decoration: none;
                    margin: 0 20px;
                    font-size: 18px;
                }}
                .container {{
                    max-width: 1000px;
                    margin: 20px auto;
                    padding: 20px;
                    background: white;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 5px;
                }}
                h2 {{
                    text-align: center;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background: #333;
                    color: white;
                }}
                .section {{
                    display: none;
                }}
                .active {{
                    display: block;
                }}
            </style>
            <script>
                function showSection(sectionId) {{
                    document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
                    document.getElementById(sectionId).classList.add('active');
                }}
            </script>
        </head>
        <body>

            <nav>
                <a href="#" onclick="showSection('clues')">Clue Results</a>
                <a href="#" onclick="showSection('categories')">Category Results</a>
                <a href="#" onclick="showSection('answers')">Answer Results</a>
            </nav>

            <div class="container">
                <div id="clues" class="section active">
                    <h2>The Most Common Clue Values</h2>
                    <table>
                        <tr><th>Clue</th><th>Category</th><th>Answer</th><th>Occurrences</th></tr>
        """
        for (clue, category, answer), count in sorted_clues:
            html_content += f"<tr><td>{clue}</td><td>{category}</td><td>{answer}</td><td>{count}</td></tr>"

        html_content += """
                    </table>
                </div>

                <div id="categories" class="section">
                    <h2>The Most Common Categories</h2>
                    <table>
                        <tr><th>Category</th><th>Occurrences</th></tr>
        """
        for category, count in sorted_categories:
            html_content += f"<tr><td>{category}</td><td>{count}</td></tr>"

        html_content += """
                    </table>
                </div>

                <div id="answers" class="section">
                    <h2>The Most Common Answers</h2>
                    <table>
                        <tr><th>Answer</th><th>Occurrences</th></tr>
        """
        for answer, count in sorted_answers:
            html_content += f"<tr><td>{answer}</td><td>{count}</td></tr>"

        html_content += """
                    </table>
                </div>
            </div>

        </body>
        </html>
        """

        with open(html_file, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"\n✅ HTML report successfully saved at: {html_file}")
