from flask import Flask, render_template, jsonify
import pyodbc
import logging

app = Flask(__name__)

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# Function to get properties from the database
def get_properties():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server;DATABASE=Irrigation_db;UID=user;PWD=password')
    cursor = conn.cursor()
    cursor.execute("SELECT Property_Name, Latitude, Longitude FROM Properties")
    properties = cursor.fetchall()
    conn.close()
    return [{'name': row[0], 'latitude': row[1], 'longitude': row[2]} for row in properties]

# Flask route to serve the property data as JSON
@app.route('/properties')
def properties():
    app.logger.info("Serving property data")
    return jsonify(get_properties())

# Route to serve the index.html
@app.route('/')
def index():
    app.logger.info("Serving index.html")
    return render_template('index.html')

# Start the application
if __name__ == '__main__':
    app.run(debug=False)

