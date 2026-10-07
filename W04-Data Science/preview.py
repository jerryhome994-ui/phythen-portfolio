# 載入與檢視資料表內容
import pandas as pd
df = pd.read_csv('students.csv')
print(df.describe())
import pandas as pd
# 1. 讀取資料
df = pd.read_csv('students.csv')
# 2. 基本統計
math_avg = df['math'].mean()
eng_max = df['english'].max()
math_max = df['math'].max()
# 3. 輸出結果
print(f"班級數學平均：{math_avg:.1f} 分")
print(f"英文最高分：{eng_max} 分")
print(f"數學最高分：{math_max} 分")
