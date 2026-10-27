AquaPredict AI — Model Documentation

Current Status

The included Python API uses a deterministic water-deficit calculation. It does not currently contain a trained machine-learning model.

Current Method

Water deficit is calculated as:

"Water Demand - Available Water Supply"

The result is a simplified estimate based on user-provided values.

Proposed Machine-Learning Development

A future version may investigate Random Forest or XGBoost for regional scarcity-risk classification, or suitable time-series models for forecasting.

Required Training Data

Potential inputs include rainfall, groundwater observations, temperature, reservoir storage, supply, demand, and historical shortage outcomes.

Each field requires verified provenance, units, timestamps, and geographical coverage.

Evaluation

A future model should be evaluated on unseen historical periods using appropriate metrics. Classification tasks may use precision, recall, F1-score, and confusion matrices. Forecasting tasks may use suitable error metrics and baseline comparisons.

Limitations

No trained model, measured prediction accuracy, or validated future forecast is claimed by the current implementation.
