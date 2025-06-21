import streamlit as st
from pathlib import Path
import numpy as np
import json
from PIL import Image

# ===== CONFIG =====
store_id_list = ["Cửa hàng 1", "Cửa hàng 2"]
family_ids_list = ["Pepsi", "COCA COLA"]

store_id_Name = st.selectbox("Chọn store_id", options=store_id_list)
family_id_Name = st.selectbox("Chọn family_id", options=family_ids_list)

if store_id_Name == "Cửa hàng 1":
    store_id = 0.0377358490566037
elif store_id_Name == "Cửa hàng 2":
    store_id = 0.0188679245283018

if family_id_Name == "Pepsi":
    family_id = 0.46875
elif family_id_Name == "COCA COLA":
    family_id = 0.6875

if st.button("Tiếp tục"):
    st.success("Đã chọn xong!")
    st.write("✅ Store ID:", store_id_Name)
    st.write("✅ Family ID:", family_id_Name)

    # === Load từ thư mục kết quả ===
    folder_name = f"store_{store_id}_family_{family_id}"
    result_dir = Path(f"./results/{folder_name}")
    if not result_dir.exists():
        st.error("❌ Không tìm thấy kết quả đã lưu!")
    else:
        # ===== Biểu đồ 1: Dự đoán vs Thực tế =====
        st.subheader("📉 Biểu đồ Dự đoán vs Thực tế")
        st.image(Image.open(result_dir / "eval_plot.png"))

        # ===== Biểu đồ 2: Dự báo 7 ngày tới =====
        st.subheader("🔮 Dự báo 7 ngày tới")
        st.image(Image.open(result_dir / "forecast_plot.png"))

        # ===== Metrics =====
        with open(result_dir / "metrics.json") as f:
            metrics = json.load(f)

        st.markdown(f"""
        ### 📊 Metrics:
        - MAE: `{metrics['MAE']:.2f}`
        - RMSE: `{metrics['RMSE']:.2f}`
        - R²: `{metrics['R2']:.2f}`
        """)

        # ===== Giá trị =====
        true_vals = np.load(result_dir / "true_last_30.npy")
        forecast_vals = np.load(result_dir / "forecast_next_7.npy")

        st.markdown("### ✅ Giá trị thực tế (30 ngày gần nhất):")
        st.write(np.round(true_vals, 2))

        st.markdown("### 🔮 Dự đoán doanh số 7 ngày tới:")
        for i, val in enumerate(forecast_vals, 1):
            st.write(f"Ngày +{i}: **{val:.2f}**")
