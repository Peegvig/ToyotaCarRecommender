function getRecommendations() {
    const userPreferences = {
        intendedUse: document.getElementById('use').value,  // Correct ID here
        keyFactors: document.getElementById('factors').value,  // Correct ID here
        minBudget: document.getElementById('minBudget').value,  // Correct ID here
        maxBudget: document.getElementById('maxBudget').value  // Correct ID here
    };
    fetch('/get_recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userPreferences)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recommendations').innerHTML = data.recommendations;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
