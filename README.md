# ESP32 溫濕度 IoT 監控系統
這是一個基於 MicroPython 的實作專案，使用 ESP32 讀取 DHT11 數據，顯示於 OLED，並透過 MQTT 傳送到雲端。

## 硬體清單
* ESP32 開發板(使用ESP32-WROOM-32E)
* DHT11 溫濕度感測器 
* SSD1306 OLED 螢幕 (I2C)

## 功能
* Wi-Fi 自動連線
* MQTT 即時數據傳輸 (使用 EMQX Broker)
* 本地 OLED 數值顯示

## 接線方式
* DHT11 (Signal : Pin 13)
* OLED (SCL: Pin 22, SDA : Pin 21)
* VCC: 接 3.3V
