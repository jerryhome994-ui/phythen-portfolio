import streamlit as st

name = st.text_input("請輸入姓名:")
if name:
    st.write(f"Hello,{name}!")


options = ["國文", "英文", "數學"]
subject = st.selectbox("請選擇科目", options)
st.write(f"你選擇的科目是：{subject}")

mode = st.radio("分析方式", ["高於門檻", "低於門檻"])
if mode:
    st.write(f"你選擇的分析模式是:{mode}")

threshold = st.slider("分數門檻:", 0, 100, 60)
if threshold >= 60:
    st.balloons()
else:
    st.snow()
st.write(f"你設定的分數門檻是:{threshold}")

show_only = st.checkbox("只顯示符合條件的學生", value=True)

if show_only:
    st.write("啟動及格篩選模式...")
bonus = st.number_input("加分設定", min_value=0, max_value=10, value=0)
if st.button("開始分析"):
    st.success("開始執行分析！ ")

scores = [
    {"name": "小安", "subject": "數學", "score": 85},
    {"name": "小華", "subject": "數學", "score": 58},
    {"name": "小美", "subject": "英文", "score": 92},
    {"name": "小傑", "subject": "英文", "score": 65},
]

st.title("互動式成績查詢")
name = st.text_input("輸入姓名關鍵字")
subject = st.selectbox("選擇科目", ["全部", "數學", "英文"])
threshold = st.slider("最低分數", 0, 100, 60)

if st.button("查詢"):
    result = []
    for item in scores:
        if subject != "全部" and item["subject"] != subject:
            continue
        if name and name not in item["name"]:
            continue
        if item["score"] >= threshold:
            result.append(item)
    st.write("符合條件的資料：")
    if result:
        st.write(result)
    else:
        st.warning("沒有符合條件的資料")
