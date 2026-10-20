import pandas as pd

from app.config import FEATURES
from app.preprocessing import make_preprocessing


def test_preprocessing_transformer():
    transformer = make_preprocessing()
    df = pd.DataFrame(
        [
            {
                "CreditScore": 600,
                "Geography": "France",
                "Age": 40,
                "Tenure": 3,
                "Balance": 50000.0,
                "NumOfProducts": 2,
                "HasCrCard": 1,
                "IsActiveMember": 1,
            }
        ]
    )

    transformed = transformer.fit_transform(df[FEATURES])
    assert transformed is not None
    assert transformed.shape[0] == 1
    # Check that output has correct dimensions (OneHotEncoder creates
    # binary cols for Geography + passthrough features)
    assert transformed.shape[1] >= len(FEATURES)
