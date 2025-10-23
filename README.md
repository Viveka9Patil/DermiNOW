#  DermiNOW: AI-Based Dermatological Manifestation Detection

## Overview

DermiNOW is a Convolutional Neural Network (CNN)-based image classification web application built with Streamlit.
It assists in the early detection and analysis of dermatological conditions using image-based diagnostic modeling.
The application integrates machine learning with Ayurvedic recommendations to provide a holistic view of skin health for both patients and doctors.

---

## Features

* CNN Image Classification:
  Detects and classifies dermatological manifestations from uploaded skin images.

* Dual User Interface:
  Separate login and experience for **Patients** and **Doctors**, enabling customized workflows.

* Real-time Image Upload:
  Supports camera input and file uploads for skin image analysis.

* Skin Health Report:
  Allows patients to fill out digital medical history and lifestyle forms for report generation.

* Ayurvedic Recommendation System:
  Suggests Ayurvedic treatments and connects users to relevant doctors based on location and condition.

* Secure Login:
  Provides role-based access for patients and doctors with session state tracking.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Viveka9Patil/DermiNOW.git
cd DermiNOW
```

### Create and activate a virtual environment *(optional but recommended)*

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download the trained CNN model

The model (`my_model.h5`) is hosted under **GitHub Releases**.

* Manually download it:
  [Download my_model.h5](https://github.com/Viveka9Patil/DermiNOW/releases/download/v1.0.0/my_model.h5)


### Run the Streamlit application

```bash
streamlit run main.py
```

---

## Usage

### For Patients

  Login: Choose “Patient” and enter your credentials.
  Diagnosis Page: Upload or capture an image of your skin concern.
  Report Page: Fill in your skin health form and medical details.
  Ayurveda Page: View personalized Ayurvedic recommendations and suggested doctors.

### For Doctors

  Login: Choose “Doctor” and enter your credentials.
  Diagnosis Page: Analyze uploaded or captured patient images.
  Biopsy & Prescription: Add diagnostic observations and prescriptions.
  Patient Monitoring: Review patient records via uploaded mock data.

---

## Model & Methodology

  Model Type: CNN (Convolutional Neural Network)
  Framework: TensorFlow / Keras
  Image Preprocessing:

  * Resizing to `128×128`
  * Normalization (`pixel/255.0`)
  * RGB conversion if needed
  Output Classes:

  1. Acne and Rosacea
  2. Atopic Dermatitis
  3. Cellulitis / Impetigo / Bacterial Infections
  4. Eczema
  5. Hair Loss / Alopecia
  6. Pigmentation Disorders
  7. Lupus and Connective Tissue Diseases
  8. Melanoma / Nevi / Moles

---

## **Contributors**

Viveka Patil – [Viveka9Patil](https://github.com/Viveka9Patil)
Rujuta Thombre - [RujutaThombre](https://github.com/RujutaThombre)

## Acknowledgements

  Libraries & Frameworks:
  Streamlit, TensorFlow, Keras, OpenCV, scikit-learn, NumPy, Pandas.
  Concept & Design:
  Inspired by real-world dermatology datasets and traditional Ayurvedic medicine integration.

---

## Contact

For questions, collaborations, or feedback, please contact:
📧 [viveka9patil@gmail.com](mailto:viveka9patil@gmail.com)

