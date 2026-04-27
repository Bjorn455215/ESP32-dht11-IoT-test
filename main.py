import machine
import dht
import time
from umqttsimple import MQTTClient
import ssd1306

# ================== 1. 你的專屬設定區 ==================
WIFI_SSID = "自己的網路名稱"
WIFI_PASS = "自己的網路密碼"

MQTT_BROKER = "broker.emqx.io"
client_id = "自己的ID(隨意設)" 

TOPIC_TEMP = b"XXXProject/temp"
TOPIC_HUM  = b"XXXProject/humi"

# ================== 2. 硬體初始化 ==================
# DHT11 接 GPIO 13
sensor = dht.DHT11(machine.Pin(13))

# OLED 接 I2C (SCL=22, SDA=21)
try:
    i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except:
    print("OLED Init Failed")

# ================== 3. 功能函式 ==================
def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
    print('Wi-Fi is connected:', wlan.ifconfig())

def display_status(t, h, s):  # 把函數名改成 display_status
    try:
        oled.fill(0)
        oled.text("Bjorn IoT Hub", 0, 0)
        oled.text("-" * 16, 0, 10)
        oled.text("Temp: {} C".format(t), 0, 25)
        oled.text("Humi: {} %".format(h), 0, 40)
        oled.text(s, 0, 55)   # 這裡用傳進來的變數 s
        oled.show()
    except Exception as e:
        print("OLED Error:", e)

# ================== 4. 執行主程式 ==================
connect_wifi()

client = MQTTClient(client_id, MQTT_BROKER, keepalive=60)

mqtt_connected = False
try:
    client.connect()
    print("MQTT Connected!")
    mqtt_connected = True
except Exception as e:
    print("MQTT connection failed:", e)

while True:
    try:
        time.sleep(5) 
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        
        print("Statistics: Temp {}C, Humi {}%".format(t, h))

        if mqtt_connected:
            try:
                client.publish(TOPIC_TEMP, str(t).encode())
                client.publish(TOPIC_HUM, str(h).encode())
                status_msg = "MQTT: Sent OK" # 這裡定義為 status_msg
            except:
                status_msg = "MQTT: Pub Error"
        else:
            status_msg = "MQTT: Offline"

        display_status(t, h, status_msg)

    except Exception as e:
        print("Sensor Error:", e)
        display_status("--", "--", "Error")
