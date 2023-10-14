import streamlit as st
import pickle
import re
import nltk
import plotly.graph_objects as go

nltk.download('punkt')
nltk.download('stopwords')

# loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

# web app
def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])
    st.audio("welcome.mp3", format="audio/mp3")

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = clean_resume(resume_text)
        input_features = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        # Display the predicted category
        st.subheader("Predicted Category:")
        st.markdown(f"<h2 style='color: red'>{category_name}</h2>", unsafe_allow_html=True)

        # Create colorful meter for categories
        st.subheader("Category Meter:")
        category_meter = st.progress(0.0)
        if prediction_id in category_mapping:
            # Adjust the progress based on the prediction (you can customize colors)
            category_meter.progress((prediction_id + 1) / len(category_mapping))

        # Add a footer with your name
        st.text("Created by Suraj Sanap")

        # Display accuracy as a Plotly gauge
        st.subheader("Accuracy:")
        accuracy_value = 0.85  # Replace with the actual accuracy value
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=accuracy_value,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Accuracy", 'font': {'size': 24}},
            delta={'reference': 1.0, 'increasing': {'color': "RebeccaPurple"}},
            gauge={
                'axis': {'range': [0, 1], 'tickwidth': 0.1, 'tickcolor': "darkblue"},
                'bar': {'color': 'blue'},  # Change the color here
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 0.5], 'color': 'red'},
                    {'range': [0.5, 0.8], 'color': 'yellow'},
                    {'range': [0.8, 1], 'color': 'green'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 0.9}}))

        fig.update_layout(paper_bgcolor="lavender", font={'color': "darkblue", 'family': "Arial"})
        st.plotly_chart(fig)


# python main
if __name__ == "__main__":
    main()
