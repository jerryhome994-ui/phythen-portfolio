scores = [78, 92, 65, 88, 73, 95, 81, 69, 84, 90]
 
highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)
top3 = sorted(scores, reverse=True)[:3]
 
print("=== 成績分析 ===")
print("資料筆數：", len(scores))
print("最高分：", highest)
print("最低分：", lowest)
print("平均：", average)
print("前三名：", top3)
