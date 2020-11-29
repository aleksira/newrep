from flask import Flask, render_template,  url_for

app = Flask(__name__)

@app.route('/')
def main_page():
    m = url_for('main_page')
    q = url_for('questions')
    s = url_for('stats')
    return render_template('index.html', m=m, q=q, s=s)

@app.route('/questions')
def questions():
    main_url = url_for('main_page')
    s = url_for('stats')
    return render_template('questions.html', m=main_url, s=s)

@app.route('/stats')
def stats():
    main_url = url_for('main_page')
    s = url_for('stats')
    return render_template('stats.html', m=main_url, s=s)

if __name__ == '__main__':
    app.run()