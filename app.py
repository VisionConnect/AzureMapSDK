from flask import Flask, render_template
import logging

app = Flask(__name__)

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    app.logger.info("Serving index.html")
    return render_template('index.html')  # This will serve your index.html

if __name__ == '__main__':
    app.run(debug=False)
