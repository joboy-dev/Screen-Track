let url = `ws://${window.location.host}/ws/screentime/`

// Create web socket object
const socket = new WebSocket(url)

// Function to call when the connection is open
socket.onopen = function (event) {
    console.log('WebSocket connection opened:', event);
};

// Function to call when the connection is receiving messages
socket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log(`Data: ${data.message}`)

    // Check if 'cpu_percent' is present in the data
    if ('cpu_data' in data) {
        // Update the HTML element with the received data
        document.querySelector('.screen-time-data').innerText = `CPU Percent: ${data.cpu_percent}`;
    } else {
        console.error("Invalid data format received from server");
    }
    // document.querySelector('.screen-time-data').innerText = data.cpu_percent;
}

// Function to call when connection is closed
socket.onclose = function (event) {
    console.log('WebSocket connection closed:', event);
};