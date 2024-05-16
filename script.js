document.getElementById('search-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        const inputValue = this.value.trim(); // Get trimmed input value
        if (inputValue === '') {
            alert('Invalid Input');
        } else {
            console.log('You  searched for:', inputValue);

            // Send the input to the Flask server
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input: inputValue }) // Use 'input' as key
            })
            .then(response => response.json())
            .then(data => {
                // Handle response data here
                console.log('Search results:', data);
            })
            .catch(error => console.error('Error:', error));
        }
    }
});
