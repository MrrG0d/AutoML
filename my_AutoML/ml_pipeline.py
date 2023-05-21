import pandas as pd
from nbimporter import NotebookLoader
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score

class MyAutoML:
    def __init__(self, data: pd.DataFrame, target: str):
        self.data = data
        self.target = target

    def _preprocess_data(self):
        # Обработка данных
        object_columns = data.columns[data.dtypes == "object"]
        df_preprocessor = DataFramePreprocessor(object_columns, scaler=StandardScaler(), imputer=SimpleImputer())
        X_train_selected, X_test_selected, y_train, y_test = df_preprocessor.process(data)

        X_train_selected, X_test_selected, y_train, y_test = df_preprocessor.process(self.data, self.target)
        self.X_train_selected = X_train_selected
        self.X_test_selected = X_test_selected
        self.y_train = y_train
        self.y_test = y_test

    def train_and_evaluate(self):
        self._preprocess_data()

        # Обучение и тестирование моделей
        models = [LinearRegressionModel(), ElasticNetModel(), RandomForestRegressorModel(), GradientBoostingRegressorModel()]
        # выбираем наилучшую модель
        best_model = None
        best_score = -float("inf")
        for model in models:
            model.fit(X_train_selected, y_train)
            y_pred = model.predict(X_test_selected)
            r2 = r2_score(y_test, y_pred)
        
            if r2 > best_score:
                best_model = model
                best_score = r2
        
            print(f"{type(model).__name__} R²: {r2:.4f}")
        
        print(f"Best model: {type(best_model).__name__} with R-squared score {best_score}")
    
        return best_model