# AI-based Smishing Message Detection System

## Description
---

This project aims to develop a machine learning model that automatically detects smishing (SMS phishing) messages. 

By analyzing the textual content of messages, the system classifies them as either benign or malicious, helping users 

avoid fraudulent scams.

---

## Team Contributions
-Hyunjin Bang: Expanded the dataset, Integrated components into a complete runnable script, Authored the project report

-Byulhwi Son : Expanded the dataset, Implemented model training code, Wrote the README file 

-Inseo Yoo   : Expanded the dataset, Developed the UI using Streamlit, Created usage examples, Recorded a demonstration 

video

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

##  Model Performance
---
1.  Misclassification Cases, We found that simple, everyday words such as “응” (yes), “네” (okay), and “안녕” (hello) were

occasionally misclassified as smishing. This issue can be attributed to the following factors:

- Insufficient linguistic distinction between spam and legitimate messages in the training data

- Lack of training data for short-text messages

- Overfitting to specific words that frequently appear in smishing messages
![image](https://github.com/user-attachments/assets/c08c7711-45f8-4601-a015-d06230f0d7aa)

->To address this issue, we diversified the training data by including short, simple expressions such as "응", "네", and "안녕" with the label 0 (non-smishing). This helped the model better distinguish between harmless, everyday language and actual smishing content.
  
2. When testing the model with messages that were explicitly labeled and trained as legitimate (non-smishing),

![image](https://github.com/user-attachments/assets/5ddc6693-b35b-439f-8eb3-8c3b6c22a6bb)

->To improve the model’s robustness, we performed data augmentation by introducing benign messages that include commonly misinterpreted words extracted from smishing samples. This aimed to reduce false positives caused by keyword-based overfitting.

---

## UI
---

