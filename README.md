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

## 軟體需求
- 韌體: MicroPython v1.20+ 
- 函式庫: `umqttsimple.py`, `ssd1306.py`
- 開發工具: VS Code + MicroPico Extension

## 實驗流程
初始化：接通 ESP32 電源，啟動手機熱點（確認頻段為 2.4GHz），並上傳main.py, ssd1306.py, umqttsimple.py至開發版上(三個檔案右鍵點選upload project to pico)。

連線檢查：按下Terminal的Run, 觀察 Terminal 是否出現 Wi-Fi is connected。

通訊握手：確認 MQTT Connected! 字樣出現，代表已成功與雲端 Broker 建立連線。

雲端驗證：

* 開啟 EMQX Web Client 網頁。

* 設定 Host 為 broker.emqx.io 並進行 Connect。

* 訂閱 (Subscribe) 主題：xxxProject/#。(主題為舉例，一定要和main.py內的設定相同才能接收資料)

數據分析：觀察網頁接收到的 Payload 是否與 OLED 顯示之溫濕度一致。
