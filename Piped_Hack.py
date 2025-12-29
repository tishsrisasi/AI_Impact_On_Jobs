import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Page config
st.set_page_config(page_title="AI Impact Analysis", page_icon="🛠", layout="wide")

# Title
st.title("AI Impact by 2030")
st.write("Analysing jobs to be impacted by AI by 2030")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('AI_Impact_On_Jobs_2030_piped.csv')
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

# Experience filter
Experience_range = st.sidebar.slider(
    "Years of Experience",
    min_value=int(df['Years_Experience'].min()),
    max_value=int(df['Years_Experience'].max()),
    value=(0, 30)
)

# Avg_Salary filter
salary_range = st.sidebar.slider(
    "Average Salary",
    min_value=int(df['Average_Salary'].min()),
    max_value=int(df['Average_Salary'].max()),
    value=(10000, 150000)
)

# Education filter
Education_filter = st.sidebar.radio(
    "Level of Education",
    options=['All', "Master's", 'PhD', 'High School', "Bachelor's"]
)

# Apply filters
filtered_df = df[
    (df['Years_Experience'] >= Experience_range[0]) & 
    (df['Years_Experience'] <= Experience_range[1]) &
    (df['Average_Salary'] >= salary_range[0]) & 
    (df['Average_Salary'] <= salary_range[1])
]

if Education_filter == "Master's":
    filtered_df = filtered_df[filtered_df['Education_Level'] == "Master's"]
elif Education_filter == 'PhD':
    filtered_df = filtered_df[filtered_df['Education_Level'] == "PhD"]
elif Education_filter == "High School":
    filtered_df = filtered_df[filtered_df['Education_Level'] == "High School"]
elif Education_filter == "Bachelor's":
    filtered_df = filtered_df[filtered_df['Education_Level'] == "Bachelor's"]
else:
    filtered_df = df


# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Visualisations", "ML Model", "Data"])

with tab1:
    # Basic info
    st.header("Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Filtered Jobs", len(filtered_df))
    with col2:
        st.metric("Total Features", len(df.columns))
    with col3:
        st.metric("Filtered Average Salary", 
                  f"{filtered_df['Average_Salary'].mean():.1f}k")
    with col4:
        pct_shown = len(filtered_df) / len(df) * 100
        st.metric("Data Shown", f"{pct_shown:.1f}%")
    
    # Basic statistics
    st.subheader("Statistics")
    st.write(filtered_df.describe())

with tab2:
    st.header("Data Visualisations")
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Average Salary Distribution
        st.subheader('Average Salary Distribution')
        fig1, ax1 = plt.subplots()
        ax1.hist(filtered_df['Average_Salary'], bins=5, color='skyblue', edgecolor='black')
        ax1.set_xlabel('Average Salary')
        ax1.set_ylabel('Average')
        st.pyplot(fig1)
         
    with col2:
        # Experience distribution
        st.subheader("Years of Experience")
        fig2, ax2 = plt.subplots()
        ax2.hist(filtered_df['Years_Experience'], bins=5, color='skyblue', edgecolor='black')
        ax2.set_xlabel('Years of Experience')
        ax2.set_ylabel('Count')
        st.pyplot(fig2)

    # Risk Category distribution
    st.subheader("Risk Distribution")
    fig, ax = plt.subplots()
    risk_counts = filtered_df['Risk_Category'].value_counts()
    colors = ['#2ecc71', '#e74c3c', '#3498db']
    if len(risk_counts) > 0:
        ax.pie(risk_counts, labels=['Medium', 'High', 'Low'], 
                autopct='%1.1f%%', colors=colors)
    st.pyplot(fig)
    
    # Correlation heatmap
    st.subheader("Correlation Matrix")
    numerical_cols = filtered_df.select_dtypes(include='number').columns.tolist()
    if len(filtered_df) > 10:
        correlation_matrix = filtered_df[numerical_cols].corr()
        fig3, ax3 = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0, ax=ax3)
        st.pyplot(fig3)

# Machine Learning Model
with tab3:
    st.header("Random Forest Model")
    
    # Prepare data
    @st.cache_data
    def prepare_data(dataframe):
        # Copy data
        X = dataframe.drop(['Automation_Probability_2030', 'Risk_Category', 'Risk_Category_Code'], axis=1).copy()
        y = dataframe['Risk_Category'].copy()
        
        # Encode categorical variables
        label_encoders = {}
        categorical_cols = X.select_dtypes(include=['object']).columns
        
        for col in categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            label_encoders[col] = le
        
        return X, y, label_encoders
    
    # Train model button
    if st.button("Train Model"):
        with st.spinner("Training model with Random Forest..."):
            # Prepare data
            X, y, encoders = prepare_data(df)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Train model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Predictions
            y_pred = model.predict(X_test)
            
            # Store in session state
            st.session_state['model'] = model
            st.session_state['encoders'] = encoders
            st.session_state['features'] = X.columns.tolist()
            
            # Display metrics
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Model Performance")
                accuracy = accuracy_score(y_test, y_pred)
                st.metric("Accuracy", f"{accuracy:.2%}")
                
                # Confusion Matrix
                st.subheader("Confusion Matrix")
                cm = confusion_matrix(y_test, y_pred)
                fig, ax = plt.subplots()
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
                ax.set_xlabel('Predicted')
                ax.set_ylabel('Actual')
                st.pyplot(fig)
            
            with col2:
                st.subheader('Classification Report')
                st.write(classification_report(y_test, y_pred, target_names=['Medium', 'High', 'Low']))
            
            # Feature Importance plot
            st.subheader("Feature Importance")
            importance_df = pd.DataFrame({
                'feature': X.columns,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False).head(10)
                
            fig2, ax2 = plt.subplots()
            ax2.barh(importance_df['feature'], importance_df['importance'])
            ax2.set_xlabel('Importance')
            st.pyplot(fig2)

            st.success("Model trained successfully!")
    
    # Prediction Interface
    st.markdown("---")
    st.header("Make a Prediction")
    
    if 'model' in st.session_state:
        st.write("Enter the details below to predict AI Impact probability:")
        
        # Create input form
        with st.form("prediction_form"):
            salary_input = st.number_input(
                "Average Annual Salary",
                min_value=30000,
                max_value=150000,
                value=30000,
                step=1000
            )
                
            exp_input = st.number_input(
                "Years of Experience",
                min_value=0,
                max_value=30,
                value=0,
                step=1
            )
            
            # Submit button
            submit_button = st.form_submit_button("Predict AI Impact Probability")
        
            if submit_button:
                # Create input dataframe with all features
                # Note: You'll need to match the exact feature names from your dataset
                input_data = pd.DataFrame({
                    'Average_Salary': [salary_input],
                    'Years_Experience': [exp_input]
                })
            
                # Ensure all features from training are present
                # Add any missing features with default values if needed
                for feature in st.session_state['features']:
                    if feature not in input_data.columns:
                        input_data[feature] = 0  # or appropriate default
            
                # Reorder columns to match training data
                input_data = input_data[st.session_state['features']]
            
                # Encode categorical variables if any
                for col in input_data.columns:
                    if col in st.session_state['encoders']:
                        # Handle encoding for categorical features
                        pass  # Implement if you have categorical features
            
                # Make prediction
                prediction = st.session_state['model'].predict(input_data)[0]
                prediction_proba = st.session_state['model'].predict_proba(input_data)[0]
            
                # Display results
                st.markdown("---")
                st.subheader("Prediction Results")
            
                col1, col2 = st.columns(2)
            
                with col1:
                    if prediction == 2:
                        st.error("**Medium Risk of Impact**")
                        st.metric("AI Impact Probability", f"{prediction_proba[2]:.1%}")
                    elif prediction == 1:
                        st.error("**High Risk of Impact**")
                        st.metric("AI Impact Probability", f"{prediction_proba[1]:.1%}")
                    else:
                        st.success("**Low Risk of Impact**")
                        st.metric("AI Impact Probability", f"{prediction_proba[0]:.1%}")
            
                with col2:
                    st.write("**Probability Breakdown:**")
                    st.write(f"- Medium Impact: {prediction_proba[2]:.1%}")
                    st.write(f"- High Impact: {prediction_proba[1]:.1%}")
                    st.write(f"- Low Impact: {prediction_proba[0]:.1%}")
                
                    # Visual representation
                    fig, ax = plt.subplots(figsize=(6, 2))
                    categories = ['Medium', 'High', 'Low']
                    probabilities = prediction_proba
                    colors = ['#2ecc71', '#e74c3c', '#3984db']
                    ax.barh(categories, probabilities, color=colors)
                    ax.set_xlim(0, 1)
                    ax.set_xlabel('Probability')
                    for i, v in enumerate(probabilities):
                        ax.text(v + 0.02, i, f'{v:.1%}', va='center')
                    st.pyplot(fig)

    else:
        st.warning("Please train the model first using the 'Train Model' button above.")
    
    # Display existing model info
    if 'model' in st.session_state:        
        # Show top features
        st.subheader("Top 5 Most Important Features")
        model = st.session_state['model']
        features = st.session_state['features']
        
        importance_df = pd.DataFrame({
            'feature': features,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False).head(5)
        
        for idx, row in importance_df.iterrows():
            st.write(f"- **{row['feature']}**: {row['importance']:.3f}")

with tab4:
    st.header("Raw Data")
    st.dataframe(filtered_df)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="filtered_impact_data.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("**AI Impact Analysis:** Analysis jobs to be impacted by AI by 2030")
