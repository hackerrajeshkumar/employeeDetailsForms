from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_db"
)

# Create the employee table if it doesn't exist
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        mobile_number VARCHAR(20) NOT NULL,
        email VARCHAR(255) NOT NULL,
        birth_date DATE NOT NULL,
        special_interests TEXT,
        learning_institutions TEXT
    )
""")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        mobile_number = request.form['mobile_number']
        email = request.form['email']
        birth_date = request.form['birth_date']
        special_interests = request.form['special_interests']
        learning_institutions = request.form['learning_institutions']

        cursor = db.cursor()
        query = "INSERT INTO employees (name, address, mobile_number, email, birth_date, special_interests, learning_institutions) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, address, mobile_number, email, birth_date, special_interests, learning_institutions)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('index'))  # Redirect to the index page

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)