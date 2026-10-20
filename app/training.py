import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from app.config import config
from app.preprocessing import make_preprocessing

def train_model(X_train, y_train):
    model = Pipeline([
        ("preprocessing", make_preprocessing()),
        ("classifier", RandomForestClassifier(n_estimators=50, random_state=config.random_state)),
    ])
    model.fit(X_train, y_train)
    logging.info("Model training complete")
    return model
