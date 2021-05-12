from flask import Flask, render_template
import xlsx_utils

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('students.html', table=xlsx_utils.get_xlsx())


if __name__ == "__main__":
    app.run()
