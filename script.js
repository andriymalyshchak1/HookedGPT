document.getElementById('search-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        if(this.value.trim() === ''){
            alert('Invalid Input');
        }
        else {
            const input = this.value.trim();
            console.log('You searched for:', input);

            // Send the input to the Flask server
            fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ value: input })
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        }
    }
});