import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("Weddel Seal Bioacoustic Classification")
st.header("Bar Graph of Ping Counts")

data_path = "test1.csv"
df = pd.read_csv(data_path)

st.dataframe(df)

# Create a bar graph using matplotlib
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.bar(df["Hydrophone #"], df["flags"])  # Replace with your desired column for x-axis
max_flags = df['flags'].max()  # Find the maximum value in "flags" column
upper_limit = max_flags * 1.5  # Add a buffer (e.g., 10%) to the maximum value
ax.set_ylim(bottom=0, top=upper_limit)
ax.set_xlabel("Location")
ax.set_ylabel("Number of pings")
ax.set_title("Bar Graph of Weddel Seal bioacoustic classfication")

# ... rest of your code ...

# Increase figure width (adjust value as needed)
fig.set_size_inches(12, 6)  # Example: width = 12 inches, height = 6 inches

# Use tight_layout() to avoid potential layout issues
plt.tight_layout()

# Convert Matplotlib figure to a byte array
fig_buf = io.BytesIO()
fig.savefig(fig_buf, format='png')
fig_buf.seek(0)

# Display the image in Streamlit
st.image(fig_buf, caption="Bar Graph", use_column_width=True)






