from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def make_preprocessing():
    return ColumnTransformer(
        [("country", OneHotEncoder(handle_unknown="ignore"), ["Geography"])],
        remainder="passthrough",
    )

