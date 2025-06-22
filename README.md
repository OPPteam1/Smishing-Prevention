# AI-based Smishing Message Detection System

## Description
---

This project aims to develop a machine learning model that automatically detects smishing (SMS phishing) messages. 

By analyzing the textual content of messages, the system classifies them as either benign or malicious, helping users 

avoid fraudulent scams.

---

## Team Contributions
-Hyunjin Phang: Expanded the dataset, Integrated components into a complete runnable script, Authored the project report

-Byulhwi Son : Expanded the dataset, Implemented model training code, Wrote the README file 

-Inseo Yoo   : Expanded the dataset, Developed the UI using Streamlit, Created usage examples, Recorded a demonstration video

---
## How the Dataset Was Built
---

1.Collection from Personal Devices

-Each team member collected both legitimate and spam SMS messages received on their personal mobile phones. 

-These messages were manually reviewed and labeled for use in model training.

2.Collection from Online Sources

-We gathered smishing and phishing message samples from news articles, online communities, blogs, and forums.

-Text content was also extracted from images of spam messages when available.

3.AI-based Sentence Generation and Augmentation

-Using ChatGPT, we generated various sentence types that mimic real-world smishing patterns.

-We also modified existing messages to create additional synthetic samples for more robust model training.

---

##  Model
---

### Model Details
---

We trained a Multinomial Naive Bayes classifier using a TF-IDF representation of SMS texts.  
Naive Bayes is known for its simplicity and speed, and it performs well on spam detection tasks involving short texts.

---

### Model Performance/Improvement
---
1.  Misclassification Cases, We found that simple, everyday words such as “응” (yes), “네” (okay), and “안녕” (hello) were

occasionally misclassified as smishing. This issue can be attributed to the following factors:

- Insufficient linguistic distinction between spam and legitimate messages in the training data

- Lack of training data for short-text messages

- Overfitting to specific words that frequently appear in smishing messages
![image](https://github.com/user-attachments/assets/c08c7711-45f8-4601-a015-d06230f0d7aa)

* Solution: To address this issue, we diversified the training data by including short, simple expressions such as "응", "네", and "안녕" with the label 0 (non-smishing). This helped the model better distinguish between harmless, everyday language and actual smishing content.
  
2. When testing the model with messages that were explicitly labeled and trained as legitimate (non-smishing),

![image](https://github.com/user-attachments/assets/5ddc6693-b35b-439f-8eb3-8c3b6c22a6bb)

* Solution: To improve the model’s robustness, we performed data augmentation by introducing benign messages that include commonly misinterpreted words extracted from smishing samples. This aimed to reduce false positives caused by keyword-based overfitting.

3. False Positives in Messages Containing Family Terms

Messages containing the word "엄마 (mom)" were consistently misclassified as smishing, even in clearly benign contexts.

* Solution: We manually analyzed feature importance and found overfitting to certain keywords like "엄마", "아빠" (mom, dad).
To mitigate this, we added more legitimate SMS messages that naturally include such terms to balance the training data.

---

## UI
---
We developed a simple and intuitive web-based user interface using Streamlit to allow users to interact with the smishing detection model.

* Features:
-Users can input any SMS message directly into the app.

-The app instantly classifies the message as either "Legitimate" or "Smishing" based on the trained model.

-The interface displays detection results in real time with visual feedback.

* How it works:

-The user types or pastes an SMS message into the input box.

-When the "Detect" button is clicked, the input is sent to the machine learning model.

-The prediction result is shown below the input field.

We chose Streamlit for its ease of use and quick deployment capabilities, making it ideal for rapid prototyping and demonstration purposes.

---

## Troubleshooting During UI Development
---
When we first started using Streamlit to build the user interface, the app window did not open properly, and the terminal showed errors or stalled without launching the local web page.

* Cause:

-Some required packages (like scikit-learn) were not installed in the environment.

-There were issues with model file dependencies (e.g., joblib could not find required modules).

-Streamlit sometimes failed silently if run in an incompatible or unstable environment (e.g., on certain macOS setups or with conflicting Python versions).

![image](https://github.com/user-attachments/assets/fc653025-f78d-4ec9-ab64-ad99e2e847e8)


* Solution:

-We checked and installed all necessary dependencies

-We ensured that the .pkl model was created and loaded in the same Python version and environment.

-After correcting the environment, we ran

-The app launched successfully in the browser

* Problem&Solution

-Streamlit does not run on Google Colab, so the trained model and vectorizer were saved as .pkl files (phising_model.pkl, vectorizer.pkl).

-We then developed and ran the full application locally using VS Code.

-The app was executed via the terminal using: streamlit run phishing_app.py

![image](https://github.com/user-attachments/assets/36e7f630-2889-44c9-a615-80ffaab2d311)


![image](https://github.com/user-attachments/assets/8827a883-e1fc-45be-9ea5-3257e2ecc0eb)


![image](https://github.com/user-attachments/assets/d991733f-285a-48d9-8161-9b88d5431999)


## How to run

1.  Train the Model on Google Colab:

- Open phisingTest.py in Google Colab.

- Uncomment the code that saves the model and vectorizer files.

- Run the script using the updated dataset (phising_dataset.csv).

- This will generate two files: phishing_model.pkl, vectorizer.pkl

![image](https://github.com/user-attachments/assets/2836f76f-fedb-4cf2-af86-9439959702e0)

![image](https://github.com/user-attachments/assets/3a98744e-2706-4245-9c8e-484904ff42cd)



2. Download Model Files:

- Download the generated .pkl files to your local machine.

- Place them in the same folder as phishing_app.py.

3. Run the Web App Locally (Streamlit does not work on Colab):

- Open the project folder in VS Code or your preferred IDE.

- Open a terminal in the project folder.

![image](https://github.com/user-attachments/assets/4aaf2a01-2c31-4d7c-bee8-158fd7bcf33b)


4. Launch the Streamlit App: streamlit run phishing_app.py

- This will open a web browser at http://localhost:8503/

- If prompted to enter an email for Streamlit, simply press Enter to skip it.

![image](https://github.com/user-attachments/assets/3c2cc907-e09c-42aa-a63c-6aecd06db7f5)


