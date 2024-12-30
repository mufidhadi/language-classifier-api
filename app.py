from flask import Flask, request, jsonify
from transformers import AutoTokenizer
import onnxruntime as ort
import numpy as np
from languages import languages  # Import the language list

# Initialize Flask App
app = Flask(__name__)

# 🛡️ Load Tokenizer and ONNX Model
tokenizer = AutoTokenizer.from_pretrained('qanastek/51-languages-classifier')
ort_session = ort.InferenceSession("51-languages-classifier-onnx/model.onnx")


@app.route('/')
def home():
    return jsonify({"message": "Language Classifier API is running!"})


@app.route('/classify', methods=['POST'])
def classify_language():
    try:
        # 📝 Parse Input Text
        data = request.json
        input_text = data.get('text', '')

        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        # 🔄 Preprocess Input (No PyTorch tensors, only NumPy)
        inputs = tokenizer(input_text, return_tensors="np")  # Use NumPy directly
        inputs_onnx = {
            'input_ids': np.array(inputs['input_ids'], dtype=np.int64),
            'attention_mask': np.array(inputs['attention_mask'], dtype=np.int64)
        }

        if 'token_type_ids' in inputs:
            inputs_onnx['token_type_ids'] = np.array(inputs['token_type_ids'], dtype=np.int64)

        # 🚀 Run Inference
        outputs = ort_session.run(None, inputs_onnx)
        logits = outputs[0]

        # 🧠 Post-process
        predicted_class = np.argmax(logits, axis=-1)
        predicted_class = int(predicted_class[0]) if logits.ndim > 1 else int(predicted_class)

        # ✅ Validate and Return Results
        if 0 <= predicted_class < len(languages):
            lang_code, lang_name = languages[predicted_class]
            return jsonify({
                "input_text": input_text,
                "predicted_class_index": predicted_class,
                "predicted_language_code": lang_code,
                "predicted_language_name": lang_name
            })
        else:
            return jsonify({"error": "Predicted class is out of range"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
