Structured design.<br/>

Wireless Sensor Netowork (WSN):<br/>
+ LAUNCHXL-CC2650<br/>
+ CC2538<br/>
<br/>
- Sensor:<br/>
<<<<<<< HEAD
+ DHT11(Temperature + Humidity) -> MQ2 (Gas)<br/>
+ BMP 80(Temperature + Pressure)<br/>
+ AM321(Motion) + MG90S(Servo) -> Door<br/>
=======
+ DHT11(Temparature + Humidity) -> MQ2 (Gas)<br/>
+ BMP 180(Temperature + Pressure)<br/>
+ PIR AM312(Motion) + MG90S(Servo) -> Door<br/>
>>>>>>> 3b1054c03cb9041b5deda236f30a68f83a8efc02
+ BH1750(Light)<br/>
+ Fan(HVAC)<br/>
+ Relay 4 channels 5V
<br/>
- Camera:<br/>
+ Raspberry Pi Camera Module V2 NoIR<br/>
<br/>
- Voice <br/>
+ Alexa Voice Service / Google Assistant 
<br/>
- Gateway:<br/>   
+ LAUNCHXL-CC2650 + Raspberry 4<br/>
<br/>
- Broker MQTT:<br/>
+ Local:  Really Small Message Broker(rsmb) +  Mosquitto<br/>
+ Remote: EMQ X Cloud<br/>
<br/>s
- Database:  PostgreSQL on GCP<br/>
<br/>
- Webserver:<br/>
+ Frontend: Boostrap 5<br/>
+ Backend: Flask(Python), JavaScript<br/>
<br/>
Kien, Pham Quoc<br/>
HCMUT.<br/>
