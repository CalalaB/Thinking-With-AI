# "Thinking With AI" Course Creations

Classroom lessons and interactive tools made for "Thinking with AI" course at university. Each lesson is a single, self-contained file: an HTML page or a Python script.

## Lessons

| Lesson | File | What it covers |
|---|---|---|
| Base Conversion, Step by Step | [`base-conversion/index.html`](base-conversion/index.html) | Six worked conversions between decimal, binary and hexadecimal, including 8-bit overflow. Press **P** for presenter mode and step through each conversion with the arrow keys or a clicker. |
| E. coli Growth Calculator | [`e-coli-growth/index.html`](e-coli-growth/index.html) | Models E. coli doubling every 20 minutes and compares iterative and recursive algorithms on the same inputs. |
| Harbour Lane Café Roster | [`cafe-roster/index.html`](cafe-roster/index.html) | Builds a valid weekly roster for three café staff across morning, afternoon and evening shifts, or explains why none exists. Edit availability to rebuild the roster, check who can cover a shift, and run the test cases. |
| Temperature Converter | [`temperature-converter/temp_converter.py`](temperature-converter/temp_converter.py) | A debugged and PEP 8-styled Python program that converts Celsius to Fahrenheit and Kelvin, with input validation, an absolute-zero check and formatted output. |

## Using the lessons

Download the repository (Code → Download ZIP) and open any `index.html` file in a browser. Run the Python script with `python3 temperature-converter/temp_converter.py`. No installation or internet connection is needed, except that the base conversion and café roster pages load their fonts from Google Fonts and falls back to a standard monospace font when offline.
