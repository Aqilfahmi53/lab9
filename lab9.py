import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Lab 9 | Chart Design", layout="centered")
AUTHOR = "Aqil Fahmi"
sales = pd.DataFrame({
    "Branch": ["Kedah", "Perak", "Penang", "Perlis", "Johor", "Sabah"],
    "Units": [96, 99, 98, 100, 97, 98],
})
st.title("How chart design changes the sales story")
version = st.radio("Choose a chart", ["Cluttered", "Improved"], horizontal=True)

fig, ax = plt.subplots(figsize=(9, 4.8))
if version == "Cluttered":
    ax.bar(sales["Branch"], sales["Units"],
           color=["#8FB9A8", "#D8B365", "#B2ABD2", "#5E3C99", "#D67968", "#6997B6"])
    ax.set_ylim(95, 101)
    ax.set_facecolor("#E8E8E8")
    ax.grid(True, color="white", linewidth=2)
    ax.set_title("SALES PERFORMANCE!!!")
else:
    highest = sales["Units"].max()
    leader = sales.loc[sales["Units"].idxmax(), "Branch"]
    spread = highest - sales["Units"].min()
    colors = ["#A74817" if value == highest else "#738594" for value in sales["Units"]]
    bars = ax.bar(sales["Branch"], sales["Units"], color=colors)
    ax.set_ylim(0, 110)
    ax.set_yticks(range(0, 101, 20))
    ax.bar_label(bars, fmt="%.0f", padding=4)
    ax.set_title(f"{leader} leads at {highest} units; all six branches are within {spread} units",
                 fontsize=13, loc="left", pad=14)
    ax.spines[["right", "top", "left"]].set_visible(False)
    ax.tick_params(length=0)
    # Direct labels provide exact values. The baseline and scale remain visible.
ax.set_ylabel("Sales (units)")
fig.text(0.02, 0.025, f"Data: fictional practice values (2026) | Chart: {AUTHOR}",
         fontsize=9, color="#404952")
fig.tight_layout(rect=(0, 0.08, 1, 1))
st.pyplot(fig)
plt.close(fig)
