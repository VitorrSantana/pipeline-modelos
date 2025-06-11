from sklearn.datasets import load_iris

df_iris = load_iris(as_frame=True).frame


def get_head_dataset():
    return df_iris.head()


def get_variables():
    col_target = list(df_iris[["target"]].columns)
    col_numeric = list(df_iris.select_dtypes(include=["number"]).columns)
    col_categor = list(df_iris.select_dtypes(include=["object"]).columns)

    dict_info_cols = {
        "numeric": [col for col in col_numeric if col_target[0] != col],
        "category": col_categor,
        "target": col_target,
    }
    return dict_info_cols
