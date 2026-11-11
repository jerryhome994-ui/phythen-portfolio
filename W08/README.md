# W08 Mini Weather Dashboard
## 作品說明
本作品使用 Python 向 Open-Meteo API 取得未來 48 小時的天氣預報資料。
使用 Pandas 將 JSON 中的逐時資料整理成 DataFrame，再計算統計摘要，並使用 Matplotlib 繪製溫度與降雨機率圖表。
※ 本作品為在本機執行的靜態資料分析作品，不是 Streamlit 網頁應用程式。
## 資料來源
Open-Meteo Forecast API
## 使用技術
Python / requests / HTTP GET / JSON
Pandas / DataFrame / 資料統計
Matplotlib / 時間序列視覺化
## 分析內容
取得未來 48 小時的逐時天氣預報資料。
將資料轉成 DataFrame。
檢視資料筆數與欄位。
計算平均溫度、最高溫度與最低溫度。
計算平均降雨機率與最高降雨機率。
繪製逐時溫度變化圖與逐時降雨機率變化圖。
## 執行方式
先安裝套件：
>_ python -m pip install requests pandas matplotlib
再執行：
>_ python main.py
## 資料限制
本作品使用 API 提供的天氣預報資料，不是實際觀測紀錄。
統計摘要反映本次查詢取得的預報資料，不代表未來天氣一定會如此發生。
## 本週學習重點
API → JSON → Pandas DataFrame → Analysis → Visualization
