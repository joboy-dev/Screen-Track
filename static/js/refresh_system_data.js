function refreshCPUData() {
    $.ajax({
        url: "http://127.0.0.1:3100/",
        type: 'GET',
        success: function(data) {
            $('.cpu-data').html(data)
        }
    })
}

setInterval(refreshCPUData, 3500)