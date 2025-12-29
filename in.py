# Prediction Interface
st.markdown("---")
st.header("Make a Prediction")
    
if 'model' in st.session_state:
    st.write("Enter the details below to predict divorce probability:")
        
    # Create input form
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
            
        with col1:
            age_input = st.number_input(
                "Age at Marriage",
                min_value=18,
                max_value=60,
                value=25,
                step=1
            )
                
            marriage_duration_input = st.number_input(
                "Marriage Duration (years)",
                min_value=0,
                max_value=50,
                value=5,
                step=1
            )
                
            num_children_input = st.number_input(
                "Number of Children",
                min_value=0,
                max_value=10,
                value=0,
                step=1
            )
            
        with col2:
            infidelity_input = st.selectbox(
                "Infidelity Occurred?",
                options=[0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes"
            )
                
            # Add more inputs based on your dataset features
            # Example placeholders - replace with actual features from your CSV:
            communication_input = st.slider(
                "Communication Quality (1-10)",
                min_value=1,
                max_value=10,
                value=5
            )
                
            financial_stress_input = st.slider(
                "Financial Stress Level (1-10)",
                min_value=1,
                max_value=10,
                value=5
            )
            
        with col3:
            # Add more feature inputs as needed
            emotional_support_input = st.slider(
                "Emotional Support (1-10)",
                min_value=1,
                max_value=10,
                value=5
            )
                
            conflict_resolution_input = st.slider(
                "Conflict Resolution (1-10)",
                min_value=1,
                max_value=10,
                value=5
            )
                
            intimacy_level_input = st.slider(
                "Intimacy Level (1-10)",
                min_value=1,
                max_value=10,
                value=5
            )
            
        # Submit button
        submit_button = st.form_submit_button("Predict Divorce Probability")
        
        if submit_button:
            # Create input dataframe with all features
            # Note: You'll need to match the exact feature names from your dataset
            input_data = pd.DataFrame({
                'age_at_marriage': [age_input],
                'marriage_duration_years': [marriage_duration_input],
                'num_children': [num_children_input],
                'infidelity_occurred': [infidelity_input],
                'communication_quality': [communication_input],
                'financial_stress': [financial_stress_input],
                'emotional_support': [emotional_support_input],
                'conflict_resolution': [conflict_resolution_input],
                'intimacy_level': [intimacy_level_input]
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
                if prediction == 1:
                    st.error("**High Risk of Divorce**")
                    st.metric("Divorce Probability", f"{prediction_proba[1]:.1%}")
                else:
                    st.success("**Low Risk of Divorce**")
                    st.metric("Not Divorced Probability", f"{prediction_proba[0]:.1%}")
            
            with col2:
                st.write("**Probability Breakdown:**")
                st.write(f"- Not Divorced: {prediction_proba[0]:.1%}")
                st.write(f"- Divorced: {prediction_proba[1]:.1%}")
                
                # Visual representation
                fig, ax = plt.subplots(figsize=(6, 2))
                categories = ['Not Divorced', 'Divorced']
                probabilities = prediction_proba
                colors = ['#2ecc71', '#e74c3c']
                ax.barh(categories, probabilities, color=colors)
                ax.set_xlim(0, 1)
                ax.set_xlabel('Probability')
                for i, v in enumerate(probabilities):
                    ax.text(v + 0.02, i, f'{v:.1%}', va='center')
                st.pyplot(fig)

else:
    st.warning("Please train the model first using the 'Train Model' button above.")


# Prediction Interface
st.markdown("---")
st.header("Make a Prediction")
    
if 'model' in st.session_state:
    st.write("Enter the details below to predict AI Impact probability:")
        
    # Create input form
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
            
        with col1:
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
                          
        with col2:
            edu_input = st.selectbox(
                "Level of Education",
                options=["Master's", 'PhD', 'High School', "Bachelor's"]
                # format_func=lambda x: "No" if x == 0 else "Yes"
            )
            
        # Submit button
        submit_button = st.form_submit_button("Predict AI Impact Probability")
        
        if submit_button:
            # Create input dataframe with all features
            # Note: You'll need to match the exact feature names from your dataset
            input_data = pd.DataFrame({
                'Average_Salary': [salary_input],
                'Years_Experience': [exp_input],
                'Education_Level': [edu_input]
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