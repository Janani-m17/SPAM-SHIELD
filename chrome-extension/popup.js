// SMS/Email Check
document.getElementById('checkSms').addEventListener('click', () => {
    const smsInput = document.getElementById('smsInput').value.trim();  // Trim whitespace
    if (smsInput) {
        fetch('http://localhost:5000/predict_sms', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input_sms: smsInput })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('smsResult').innerText = data.result;
            var resultLabel = document.getElementById('smsResult');
            if (data.result.trim().toLowerCase() === 'it is safe to proceed') {
                resultLabel.style.color = 'green';
            } else {
                resultLabel.style.color = 'red';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('smsResult').innerText = 'Error occurred';
        });
    } else {
        // If input is empty, show error message
        document.getElementById('smsResult').innerText = 'Please enter some text';
        document.getElementById('smsResult').style.color = 'red';
    }
});

// URL Check
document.getElementById('checkUrl').addEventListener('click', () => {
    const urlInput = document.getElementById('urlInput').value.trim();  // Trim whitespace
    if (urlInput) {
        fetch('http://localhost:5000/predict_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input_url: urlInput })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('urlResult').innerText = data.result;
            var resultLabel = document.getElementById('urlResult');
            if (data.result.trim().toLowerCase() === 'it is safe to proceed') {
                resultLabel.style.color = 'green';
            } else {
                resultLabel.style.color = 'red';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('urlResult').innerText = 'Error occurred';
        });
    } else {
        // If input is empty, show error message
        document.getElementById('urlResult').innerText = 'Please enter some text';
        document.getElementById('urlResult').style.color = 'red';
    }
});
