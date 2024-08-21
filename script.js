 // JavaScript to handle form submission
 document.getElementById('ingredientsForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    const ingredients = document.getElementById('ingredients').value;
    
    // Convert the ingredients string to an array
    const ingredientsArray = ingredients.split(',').map(item => item.trim());
    
    // Send the POST request to the FastAPI backend
    fetch('http://127.0.0.1:8000/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: ingredientsArray })
    })
    .then(response => response.json())
    .then(data => {
        // Display the predicted dish
        document.getElementById('predictedDish').textContent = `Predicted Dish: ${data.predicted_dish}`;
    })
    .catch(error => console.error('Error:', error));
});