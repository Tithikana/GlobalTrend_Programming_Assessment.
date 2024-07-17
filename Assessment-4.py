import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def clean_and_preprocess(df):
    # Separate features into numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
   
    # Create preprocessing pipelines for numerical and categorical data
    numerical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
   
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
   
    # Combine the numerical and categorical pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical_cols),
            ('cat', categorical_pipeline, categorical_cols)
        ])
   
    # Fit and transform the data
    df_cleaned = preprocessor.fit_transform(df)
   
    # Get feature names after transformation
    cat_columns = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)
    feature_names = numerical_cols.tolist() + cat_columns.tolist()
   
    # Convert the result back to a DataFrame
    df_cleaned = pd.DataFrame(df_cleaned, columns=feature_names)
   
    return df_cleaned

# Example usage
data = {
    'Age': [25, 30, 35, 40, None],
    'Salary': [50000, 60000, None, 80000, 70000],
    'City': ['New York', 'Los Angeles', 'New York', None, 'Los Angeles']
}
df = pd.DataFrame(data)

cleaned_df = clean_and_preprocess(df)
print(cleaned_df)
