from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('.main/main.html')  # Adjust the path based on your folder structure

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
    