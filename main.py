 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """Main page of the application."""
    return render_template('index.html')

# Define the route for destinations
@app.route('/destinations')
def destinations():
    """Display a list of European destinations."""
    # Fetch all destinations from the database
    destinations = get_all_destinations()
    return render_template('destinations.html', destinations=destinations)

# Define the route for a specific destination
@app.route('/destination/<destination_id>')
def destination_details(destination_id):
    """Display detailed information about a specific destination."""
    # Fetch the destination details from the database
    destination = get_destination_details(destination_id)
    return render_template('destination_details.html', destination=destination)

# Define the route for the itinerary
@app.route('/itinerary')
def itinerary():
    """Allow users to create and manage their travel itineraries."""
    # Fetch the user's itinerary from the database
    itinerary = get_user_itinerary()
    return render_template('itinerary.html', itinerary=itinerary)

# Define the route for adding a destination to the itinerary
@app.route('/add_destination', methods=['POST'])
def add_destination():
    """Add a destination to the user's itinerary."""
    # Get the destination ID from the request
    destination_id = request.form.get('destination_id')
    # Add the destination to the user's itinerary in the database
    add_destination_to_itinerary(destination_id)
    # Redirect to the itinerary page
    return redirect(url_for('itinerary'))

# Define the route for removing a destination from the itinerary
@app.route('/remove_destination', methods=['POST'])
def remove_destination():
    """Remove a destination from the user's itinerary."""
    # Get the destination ID from the request
    destination_id = request.form.get('destination_id')
    # Remove the destination from the user's itinerary in the database
    remove_destination_from_itinerary(destination_id)
    # Redirect to the itinerary page
    return redirect(url_for('itinerary'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
