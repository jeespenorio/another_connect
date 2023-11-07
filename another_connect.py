import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1hyRMA8JifszoD-c2rDlikRO_jVmqQFccEcz5Z9B5aJY/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="0")

#usecols=[0,1]
#can be usecols=list(range(2)))
#can also be usecols=list(range(2))), worksheet="Sheet 1 or Sheet2"

st.dataframe(data)

st.subheader("Inventory Health Check")
sql = '''
SELECT
    "Product ID",
    "Product Name",
    "Supplier",
    "Current Inventory Level",
    "Reorder Level"
FROM
    Product
WHERE
    "Current Inventory Level" < "Reorder Level"
ORDER BY
    "Reorder Level" DESC;
'''
df_inventory_health = conn.query(spreadsheet=url, sql=sql)
st.dataframe(df_inventory_health)
