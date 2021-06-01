var temp = 30
let displayColor = function() {
    if (temp < 10) {
        return '#00ffff'
    } else if (temp > 35) {
        return '#ff0000'
    } else {
        return '#00ff00'
    }
};
new Chart(document.getElementById("myChart"), {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                temp,
                70-temp,
            ],
                backgroundColor: [
                displayColor(),
                "#FFFFFF",
            ],
            borderWidth: 1,
            borderColor: '#000'
        }],
        labels: [
            "Temperature",
        ]
    },
    options: {
        title: {
            display: true,
            text: 'Temperature'
        }
}
});



// var displayColor = function() {
//     if (temp < 10) {
//         return '#00ffff'
//     } else if (temp > 35) {
//         return '#ff0000'
//     } else {
//         return '#00ff00'
//     }
// };
// var config = {
//     type: 'doughnut',
//     data: {
//         datasets: [{
//             data: [
//                 temp,
//                 70-temp,
//             ],
//                 backgroundColor: [
//                 displayColor(),
//                 "#FFFFFF",
//             ],
//             borderWidth: 1,
//             borderColor: '#000'
//         }],
//         labels: [
//             "Temperature",
//         ]
//     },
//     options: {
//         responsive: true
//     }
// };

