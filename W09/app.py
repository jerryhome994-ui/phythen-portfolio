import streamlit as st

name = st.text_input("請輸入姓名:")
st.write("Ex. 創作者姓名")

interest = st.text_input("感興趣的資訊主題:")
st.write("Ex. Python web App 開發")

if st.button("建立我的學習名片"):
    if name.strip() == "" or interest.strip() == "":
        st.warning("請輸入完整的資訊！")
    else:

        st.success("學習名片建立完成！")
        st.write("### 我的學習名片")
        st.write("姓名：", name)
        st.write("興趣主題：", interest)
        st.write("我正在學習 Python，")
        st.write("希望透過程式解決生活中的問題。")
