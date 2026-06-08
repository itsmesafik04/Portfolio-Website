from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print("\n--- New Contact Message ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return render_template(
        'index.html',
        success="Your message has been submitted successfully!"
    )

if __name__ == '__main__':
    app.run(debug=True)