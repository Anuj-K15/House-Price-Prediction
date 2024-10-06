document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const bhk = document.getElementById('bhk').value;
    const type = document.getElementById('type').value;
    const area = document.getElementById('area').value;
    const region = document.getElementById('region').value;
    
    const data = { bhk: bhk, type: type, area: area, region: region };

    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        
        const resultDiv = document.getElementById('prediction-result');
        resultDiv.innerHTML = `<h2>Predicted House Price</h2><p>The estimated price is: ₹${data.price} Lakhs</p>`;
    })
    .catch(error => console.error('Error:', error));
});
