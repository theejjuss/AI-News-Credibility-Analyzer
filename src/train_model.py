import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from data_loader import load_data
from preprocessing import clean_text
from feature_extraction import extract_features, vectorizer

def train():
    data = load_data()
    data["text"] = data["text"].apply(clean_text)

    X = extract_features(data["text"])
    y = data["label"]

    # Train/validation split (IMPORTANT FOR VIVA)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 🔥 Class-weighted model (professional touch)
    base_model = LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        solver="liblinear"
    )

    # 🔥 Probability calibration
    model = CalibratedClassifierCV(base_model)
    model.fit(X_train, y_train)

    # Evaluation (YOU MUST SHOW THIS IN REPORT)
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Professional model trained & saved.")

if __name__ == "__main__":
    train()
