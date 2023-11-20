function refreshData() {
    $.ajax({
        url: "{% url 'screentrackapp:home' %}",
        type: 'GET',
        success: function(data) {
            // $('#cpu-percent').text(data + '%');
            // console.log('Data', data.cpu_percent);
            $('#cpu-percent').html(data)

        }
    })
}

setInterval(refreshData, 3500)

// function refreshData() {
//     $.ajax({
//         url: "{% url 'screentrackapp:home' %}",
//         type: 'GET',
//         success: function(data) {
//             $('#cpu-percent').html(data)
//             // console.log('Data', data.cpu_percent);
//         }
//     })
// }

// setInterval(refreshData, 3500)