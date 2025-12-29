# Labour Group filter
Labour_filter = st.sidebar.radio(
    "Industry/Sector",
    options=['All', "Manual_Trade_Service", 'Digital_Creative', 'Private_Professional', "Public_Sector"]
)

if Labour_filter == "Manual_Trade_Service":
    filtered_df = filtered_df[filtered_df['Labour_Group'] == "Manual_Trade_Service"]
elif Labour_filter == 'Digital_Creative':
    filtered_df = filtered_df[filtered_df['Labour_Group'] == "Digital_Creative"]
elif Labour_filter == "Private_Professional":
    filtered_df = filtered_df[filtered_df['Labour_Group'] == "Private_Professional"]
elif Labour_filter == "Public_Sector":
    filtered_df = filtered_df[filtered_df['Labour_Group'] == "Public_Sector"]
else:
    filtered_df = df
