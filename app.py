import streamlit as st
from pathlib import Path
import numpy as np
import json
from PIL import Image

# ===== CONFIG =====
st.set_page_config(page_title="Demo bai tap lon nhom 5", layout="centered")
st.subheader("Demo bai tap lon nhom 5")
store_id_list = ["Cửa hàng 1", "Cửa hàng 2"]
family_ids_list = ["Deli", "Eggs"]
Models = ["tcn", "gru", "transformer"]
store_id_Name = st.selectbox("Chọn store_id", options=store_id_list)
family_id_Name = st.selectbox("Chọn family_id", options=family_ids_list)
Models_name = st.selectbox("Chọn mô hình", options=Models)
if store_id_Name == "Cửa hàng 1":
    store_id = 0.0377358490566037
elif store_id_Name == "Cửa hàng 2":
    store_id = 0.0188679245283018
if family_id_Name == "Deli":
    family_id = 0.46875
elif family_id_Name == "Eggs":
    family_id = 0.6875

if st.button("Tiếp tục"):
    st.subheader(f"Dự đoán bằng mô hình {Models_name} cho {store_id_Name} - {family_id_Name}")
    st.success("Đã chọn xong!")
    st.write("✅ Store ID:", store_id_Name)
    st.write("✅ Family ID:", family_id_Name)
    st.write("✅ Model :", Models_name)

    # === Load từ thư mục kết quả ===
    folder_name = f"store_{store_id}_family_{family_id}_Model_{Models_name}"
    result_dir = Path(f"./results/{folder_name}")
    if not result_dir.exists():
        st.error("❌ Không tìm thấy kết quả đã lưu!")
    else:

        # # ===== Biểu đồ 2: Dự báo 7 ngày tới =====
        # st.subheader("🔮 Dự báo 7 ngày tới")
        # st.image(Image.open(result_dir / "forecast_plot.png"))

    
        # true_vals = np.load(result_dir / "true_last_30.npy")
        # forecast_vals = np.load(result_dir / "forecast_next_7.npy")

        # st.markdown("### ✅ Giá trị thực tế (30 ngày gần nhất):")
        # st.write(np.round(true_vals, 2))

        # st.markdown("### 🔮 Dự đoán doanh số 7 ngày tới:")
        # for i, val in enumerate(forecast_vals, 1):
        #     st.write(f"Ngày +{i}: **{val:.2f}**")
