$(function () {
    var pressure6 = $('.pressure6');
    var gas7 = $('.gas7');
    var temperature9 = $('.temperature9');
    var humidity9 = $('.humidity9');
    var light10 = $('.light10');

    $.ajax({
        type: 'GET',
        url: '/api/sensor_data',
        success: function (data) {
            var pressValue = data[0].value.Press;
            var gasValue = data[1].value.adc;
            var tempValue = data[3].value.Temp;
            var humValue = data[3].value.Hum;
            var lightValue = data[4].value.Light;
            pressure6.append(pressValue);
            gas7.append(gasValue);
            temperature9.append(tempValue);
            humidity9.append(humValue);
            light10.append(lightValue);
        }
    });
    $.ajax({
        type: 'GET',
        url: '/api/actuator_data',
        success: function (data) {
            console.log(data)
        }
    });
});