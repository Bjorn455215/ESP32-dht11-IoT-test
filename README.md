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
* 初始化  ：接通 ESP32 電源，啟動手機熱點（確認頻段為 2.4GHz），並上傳main.py, ssd1306.py, umqttsimple.py至開發版上(三個檔案右鍵點選upload project to pico)。
  
* 連線檢查：按下Terminal的Run, 觀察 Terminal 是否出現 Wi-Fi is connected。
  
* 通訊握手：確認 MQTT Connected! 字樣出現，代表已成功與雲端 Broker 建立連線。
  
* 雲端驗證：
  * 開啟 EMQX Web Client 網頁並按下Connect Now。  https://www.emqx.com/en/mqtt/public-mqtt5-broker
    
  * 設定 Host 為 broker.emqx.io 並進行 Connect(圖片舉例設定方式)。
    <img width="1358" height="506" alt="image" src="https://github.com/user-attachments/assets/73b9cdfb-cfc8-4682-aac2-4bee3c5bb887" />


  * 點選New Subscription並設定主題名稱：xxxProject/#。(主題為舉例，一定要和main.py內的設定相同才能接收資料)
    <img width="670" height="819" alt="image" src="https://github.com/user-attachments/assets/8858f1d5-c57d-4a16-9ba8-6fe4a4d7e820" />


* 數據分析：觀察網頁接收到的 Payload 是否與 OLED 顯示之溫濕度一致。
  <img width="690" height="691" alt="image" src="https://github.com/user-attachments/assets/d448c54d-bd7f-4149-95e9-bb933ab12a21" />
  <img width="1016" height="762" alt="166598" src="https://github.com/user-attachments/assets/3eb6156a-ffb5-42ad-95dc-8700b16186fa" />
 
