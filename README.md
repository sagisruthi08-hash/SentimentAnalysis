# Sentiment Analysis using Hugging Face and Streamlit

A simple web-based **Sentiment Analysis application** that uses a pre-trained Hugging Face Transformer model to determine whether a given sentence expresses **Positive** or **Negative** sentiment.

The application shows the predicted sentiment along with the model's confidence percentage through an interactive Streamlit web interface.

## Project Overview

This project demonstrates the integration of **Natural Language Processing (NLP)** and **Transformer-based AI models** into a simple and user-friendly web application.

The user provides a sentence through the Streamlit interface. The entered text is processed by a pre-trained sentiment analysis model from Hugging Face, which produces:

* Sentiment result: Positive or Negative
* Confidence percentage of the prediction

The prediction is then displayed directly on the Streamlit application.

## Key Features

* Interactive interface developed using Streamlit
* Pre-trained Transformer model from Hugging Face
* Classification into Positive and Negative sentiments
* Displays prediction confidence as a percentage
* Checks whether the input field is empty
* Uses Streamlit resource caching for better performance
* No separate model training is required
* Lightweight and easy-to-use NLP application

## Technologies and Tools

| Technology / Tool         | Purpose                                     |
| ------------------------- | ------------------------------------------- |
| Python                    | Main programming language                   |
| Streamlit                 | Used to build the interactive web interface |
| Hugging Face Transformers | Provides the pre-trained NLP model          |
| DistilBERT                | Performs sentiment classification           |
| PyTorch                   | Backend for the Transformer pipeline        |
| VS Code                   | Development environment                     |
| Git & GitHub              | Version control and project hosting         |

## AI Model

The application uses the following pre-trained model:

**Model:** `distilbert-base-uncased-finetuned-sst-2-english`

This model is a fine-tuned version of **DistilBERT** that performs sentiment classification using the Stanford Sentiment Treebank (SST-2) dataset.

The model identifies two sentiment categories:

* `POSITIVE`
* `NEGATIVE`

Along with the sentiment label, the model generates a confidence score indicating how certain it is about its prediction.

## How the Application Works

The application follows a straightforward NLP processing flow:

```text
User enters a sentence
          |
          v
   Streamlit Interface
          |
          v
     Input Validation
          |
          v
 Hugging Face Pipeline
          |
          v
    DistilBERT Model
          |
          v
  Sentiment Prediction
          |
          v
   Positive / Negative
          |
          v
     Confidence Score
          |
          v
    Result Displayed
```

### Workflow Explanation

**1. User Input**

The user enters a sentence into the text area provided by the Streamlit application.

**2. Input Validation**

The application verifies whether the user has entered any text. If the field is empty, a warning message is displayed.

**3. Model Processing**

The entered sentence is sent to the Hugging Face sentiment-analysis pipeline.

**4. Sentiment Classification**

The DistilBERT model processes the sentence and determines whether the sentiment is **Positive** or **Negative**.

**5. Confidence Calculation**

The model generates a confidence score along with the predicted sentiment.

**6. Result Display**

Streamlit displays the final sentiment result and its confidence percentage on the web page.

## Important Functions Used

### `st.set_page_config()`

This function configures the Streamlit page, such as:

* Page title
* Page icon
* Browser tab settings

Example:

```python
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="..."
)
```

### `st.title()`

Used to display the main heading or title of the Streamlit application.

### `st.text_area()`

Creates a text input area where users can enter sentences for sentiment analysis.

### `st.button()`

Creates the **Analyze Sentiment** button that triggers the prediction process.

### `st.cache_resource`

Used for caching the loaded AI model. This prevents the model from being loaded repeatedly whenever the user interacts with the application and helps improve performance.

### `pipeline()`

The Hugging Face `pipeline()` function provides a simple way to perform sentiment analysis with a pre-trained Transformer model.

```python
pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
```

### `sentiment_model(text)`

This function sends the user's sentence to the sentiment model and obtains the prediction.

### `st.success()` and `st.error()`

These Streamlit functions are used to show appropriate result messages based on whether the predicted sentiment is Positive or Negative.

## Project Structure

```text
sentiment-analysis/
│
├── app.py
├── requirements.txt
└── README.md
```

### Files

**`app.py`**

Contains the main Streamlit application, model loading, input processing, prediction logic, and result display.

**`requirements.txt`**

Contains the Python packages and dependencies required to execute the project.

**`README.md`**

Contains the documentation, installation procedure, and project information.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd sentiment-analysis
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL through which the application can be accessed.

## Example

### Input

```text
I really enjoyed this movie!
```

### Output

```text
Sentiment: POSITIVE
Confidence: 99.XX%
```

### Another Example

**Input:**

```text
The service was extremely disappointing.
```

**Output:**

```text
Sentiment: NEGATIVE
Confidence: XX.XX%
```

## Why DistilBERT?

DistilBERT is a **smaller and faster version of BERT** that maintains much of BERT's language understanding ability while using fewer computational resources.

Since this project uses a pre-trained model, there is no need to train a sentiment model from the beginning. This makes the application easier and faster to develop.

## Limitations

* The model supports only Positive and Negative sentiment categories.
* It may have difficulty understanding sarcasm or unclear statements.
* Prediction results can depend on the wording and context of the sentence.
* The model is designed specifically for English sentiment classification.

## Future Improvements

The project can be enhanced by adding the following features:

* Introduce Neutral sentiment classification
* Provide support for multiple languages
* Analyze multiple sentences or complete documents
* Maintain a history of previous sentiment results
* Display sentiment confidence visually
* Support batch sentiment analysis using CSV files
* Deploy the application online
* Add charts for sentiment statistics
* Improve the overall user interface
* Develop an API for integration with other applications

## Learning Outcomes

By completing this project, the following concepts are demonstrated:

* Natural Language Processing
* Transformer-based NLP models
* Hugging Face Transformers
* Use of pre-trained AI models
* Streamlit application development
* AI model inference
* Confidence score interpretation
* Python application development
* Git and GitHub usage

## Conclusion

This project demonstrates how a **pre-trained Transformer model** can be combined with **Streamlit** to create a practical and easy-to-use NLP application. It provides sentiment predictions and confidence scores without requiring the user to train an AI model from scratch.
