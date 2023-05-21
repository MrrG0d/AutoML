{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6d4550e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from nbimporter import NotebookLoader\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.metrics import r2_score\n",
    "\n",
    "class MyAutoML:\n",
    "    def __init__(self, data: pd.DataFrame, target: str):\n",
    "        self.data = data\n",
    "        self.target = target\n",
    "\n",
    "    def _preprocess_data(self):\n",
    "        # Обработка данных\n",
    "        object_columns = data.columns[data.dtypes == \"object\"]\n",
    "        df_preprocessor = DataFramePreprocessor(object_columns, scaler=StandardScaler(), imputer=SimpleImputer())\n",
    "        X_train_selected, X_test_selected, y_train, y_test = df_preprocessor.process(data)\n",
    "\n",
    "        X_train_selected, X_test_selected, y_train, y_test = df_preprocessor.process(self.data, self.target)\n",
    "        self.X_train_selected = X_train_selected\n",
    "        self.X_test_selected = X_test_selected\n",
    "        self.y_train = y_train\n",
    "        self.y_test = y_test\n",
    "\n",
    "    def train_and_evaluate(self):\n",
    "        self._preprocess_data()\n",
    "\n",
    "        # Обучение и тестирование моделей\n",
    "        models = [LinearRegressionModel(), ElasticNetModel(), RandomForestRegressorModel(), GradientBoostingRegressorModel()]\n",
    "        # выбираем наилучшую модель\n",
    "        best_model = None\n",
    "        best_score = -float(\"inf\")\n",
    "        for model in models:\n",
    "            model.fit(X_train_selected, y_train)\n",
    "            y_pred = model.predict(X_test_selected)\n",
    "            r2 = r2_score(y_test, y_pred)\n",
    "        \n",
    "            if r2 > best_score:\n",
    "                best_model = model\n",
    "                best_score = r2\n",
    "        \n",
    "            print(f\"{type(model).__name__} R²: {r2:.4f}\")\n",
    "        \n",
    "        print(f\"Best model: {type(best_model).__name__} with R-squared score {best_score}\")\n",
    "    \n",
    "        return best_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "22b2db82",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
