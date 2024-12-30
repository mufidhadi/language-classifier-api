# 🚀 Language Classifier API with ONNX & Flask

This project provides a lightweight REST API for language classification using an ONNX model and Flask. The application eliminates dependencies on heavy frameworks like PyTorch or TensorFlow, making it efficient and container-friendly.

## 📚 **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Thanks & Credits](#credits)

---

## 📝 **Overview**
This project utilizes an ONNX model exported from the HuggingFace Transformers library for language classification across 51 languages. The backend is built with Flask, providing a RESTful API for text classification.

---

## 🌟 **Features**
- Supports **51 languages**.
- Lightweight **ONNX Runtime** inference.
- REST API with Flask.
- Dockerized deployment.
- No PyTorch or TensorFlow dependency.

---

## ⚙️ **Setup Instructions**

### 📥 **1. Clone the Repository**
```bash
git clone https://gitlab.com/mufidhadi/language-classifier-api.git
cd language-classifier-onnx
```

### 📦 **2. Install Dependencies**
Ensure you have Python installed.
```bash
pip install -r requirements.txt
```

### 🚀 **3. Run the Application**
```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

---

## 🔧 **Environment Variables**
- `TRANSFORMERS_NO_FRAMEWORK=1`: Disable PyTorch/TensorFlow dependencies.

---

## 📑 **API Documentation**

### 📝 **Classify Text**
- **Endpoint:** `POST /classify`
- **Content-Type:** `application/json`

#### **Request Example:**
```json
{
    "text": "What type of unit is the 777D?"
}
```

#### **Response Example:**
```json
{
    "input_text": "What type of unit is the 777D?",
    "predicted_class_index": 9,
    "predicted_language_code": "en-US",
    "predicted_language_name": "English - United States"
}
```

---

## 🐳 **Docker Deployment**

### 📦 **1. Build Docker Image**
```bash
docker-compose build
```

### 🚀 **2. Start the Container**
```bash
docker-compose up -d
```

### 🔍 **3. Access the API**
API will be available at `http://localhost:5000`

### 🛑 **4. Stop the Containers**
```bash
docker-compose down
```

---

## 🛠️ **Technologies Used**
- **Python 3.9**
- **Flask**
- **ONNX Runtime**
- **HuggingFace Transformers**
- **Docker**

---

## 📄 **License**
This project is licensed under the **MIT License**.

---

## 🤗 **Thanks & Credits**
Thanks to https://huggingface.co/qanastek/51-languages-classifier for the language classification model

---

Happy coding! 🚀✨ If you encounter any issues, feel free to open an issue or contribute to the project!