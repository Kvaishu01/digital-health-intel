import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# For demo: train a simple model on Iris dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

def predict(data: list[dict]):
    """
    Predict class labels for given data.
    Expects a list of dicts with same structure as iris features.
    """
    df = pd.DataFrame(data)
    preds = model.predict(df)
    return preds.tolist()
