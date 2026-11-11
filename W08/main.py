import requests
import pandas as pd
import matplotlib.pyplot as plt

# API 端點網址
url = "https://api.open-meteo.com/v1/forecast"

# 設定 API 請求參數
params = {
    "latitude": 25.03,
    "longitude": 121.56,
    "hourly": "temperature_2m,precipitation_probability",
    "forecast_days": 2,
    "timezone": "Asia/Taipei",
}

# 發送 GET 請求並解析 JSON 回應
response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()

# 從 API 獲取小時資料並建立 DataFrame
df = pd.DataFrame(data["hourly"])

# 轉換時間欄位格式
df["time"] = pd.to_datetime(df["time"])

# 驗證資料結構
print("資料形狀：", df.shape)
print("欄位：", list(df.columns))
print(df.head())

# 計算溫度統計值 (平均/最高/最低)
temperature_mean = df["temperature_2m"].mean()
temperature_max = df["temperature_2m"].max()
temperature_min = df["temperature_2m"].min()

# 計算降雨機率統計值 (平均/最高)
rain_probability_mean = df["precipitation_probability"].mean()
rain_probability_max = df["precipitation_probability"].max()

# 格式化輸出統計摘要至終端機
print("=== Weather Summary ===")
print(f"資料筆數：{len(df)}")
print(f"平均溫度：{temperature_mean:.1f} °C")
print(f"最高溫度：{temperature_max:.1f} °C")
print(f"最低溫度：{temperature_min:.1f} °C")
print(f"平均降雨機率：{rain_probability_mean:.1f} %")
print(f"最高降雨機率：{rain_probability_max:.1f} %")

# 設定中文字型與負號顯示
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 繪製折線圖
plt.figure(figsize=(11, 5))
plt.plot(df["time"], df["temperature_2m"], marker="o", label="Temperature")
plt.xlabel("時間")
plt.ylabel("降雨機率(%)")  # 依原圖對應標籤
plt.title("台北市 未來雨天降雨機率")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
