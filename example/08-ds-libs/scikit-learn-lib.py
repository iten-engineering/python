# =============================================================================
# Python examples - data science library SciKit Learn
# =============================================================================

# SciKit-learn enthält Funktionen zum:
# - Supervised-learning (Classification, Regression)
# - Unsupervised-learning (Clustering,  Density-estimation)
# - Data Preparation (Preprocessing, Feature extraction, Feature selection)
# - Estimator scoring

# -----------------------------------------------------------------------------
# Supervised-learning sample
# -----------------------------------------------------------------------------

# Estimators sind Objekte die die folgenden Methoden implementieren
# - fit(features, target): von features und target Daten lernen
# - predict(features): von features, target Werte voraussagen
# - score(features, target): den Estimator evaluieren

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
data   = boston.data
target = boston.target

reg = LinearRegression()
reg.fit(data, target)

prediction = reg.predict(data)
score = reg.score(data, target)

print(score)

# -----------------------------------------------------------------------------
# Data Preparation Preprocessing sample
# -----------------------------------------------------------------------------

# Für die Datenvorbereitung steht das sklearn.preprocessing Package zur Verfügung
# - Es gibt verschiedene Prozessoren mit den Methoden
#   - fit(data): bereitet den Processor vor
#   - transform(data): transformiert die Daten

# from sklearn import preprocessing
# p = preprocessing.data.StandardScaler()
# p.fit(data)
# normed_data = p.transform(data)

# -----------------------------------------------------------------------------
# Estimator scoring
# -----------------------------------------------------------------------------

# Die Qualität eines Estimators kann mit Funktionen von sklearn.metrics analysiert werden.
# Die Scoring-Funktionen nehmen die Target-Werte und eine Voraussage als Argumente

# from sklearn import metrics
# metrics.mean_squared_error(target, prediction)
# metrics.roc_auc_score(target, prediction)

# =============================================================================
# The end.

