# Resume Screening App

This repository contains code for a web-based Resume Screening App using Streamlit. The app employs a machine learning model to predict the category of a resume based on its content. The predicted category is then displayed, along with a colorful meter representing the confidence level and an accuracy gauge.

## Prerequisites

Ensure you have the required libraries installed by running:

```bash
pip install streamlit nltk plotly
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository.git
```

2. Navigate to the project directory:

```bash
cd your-repository
```

3. Run the app:

```bash
streamlit run your_script.py
```

4. Upload a resume (in .txt or .pdf format) using the provided file uploader.

5. View the predicted category, confidence meter, and accuracy gauge.

## Models and Dependencies

- **Streamlit:** A Python library for creating web applications with minimal effort.
- **Pickle:** Used to serialize and deserialize Python objects, loading the trained machine learning model and TF-IDF vectorizer.
- **NLTK:** Natural Language Toolkit for text processing tasks, including cleaning the resume text.
- **Plotly:** Used for creating interactive and visually appealing plots and gauges.

## Models Included

- **Classifier (clf.pkl):** Trained machine learning model for predicting resume categories.
- **TF-IDF Vectorizer (tfidf.pkl):** Pre-trained TF-IDF vectorizer for feature extraction.

## Categories

The model predicts resumes into the following categories:

- Java Developer
- Testing
- DevOps Engineer
- Python Developer
- ...

## Author

Created by Suraj Sanap.

## Acknowledgments

The app includes an audio file "welcome.mp3" for a welcoming sound effect.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to customize and use it according to your needs.
