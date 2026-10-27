AquaPredict AI — Technical Design Document

1. Purpose

AquaPredict AI aims to support water-resource planning by combining environmental indicators, water-supply and demand analysis, GIS visualization, and potential conservation interventions.

2. Functional Requirements

1. Allow users to select or enter a region.
2. Display available environmental and water-resource information.
3. Calculate water deficit from supply and demand.
4. Visualize geographical information where location data is available.
5. Explain the inputs and assumptions used in assessments.
6. Present potential conservation measures.
7. Distinguish real measurements from synthetic data.
8. Display limitations and uncertainty.

3. Non-Functional Requirements

- Usable on desktop and mobile screens.
- Validate user inputs.
- Avoid exposing API credentials.
- Handle missing data and service failures.
- Provide clear descriptions of assessment methods.
- Avoid presenting unvalidated estimates as confirmed forecasts.

4. Water-Deficit Calculation

The prototype uses the simplified equation:

"Water Deficit = Water Demand - Available Water Supply"

Example:

- Estimated demand: 100 million litres per day.
- Estimated supply: 80 million litres per day.
- Estimated deficit: 20 million litres per day.

This calculation assumes that the supply and demand figures refer to compatible periods and geographical areas. It does not account for all water-system constraints.

5. API Design

GET "/"

Returns the API status and project information.

POST "/assess"

Accepts a region identifier, estimated supply, and estimated demand.

Example request:

{
  "region": "Region_A",
  "water_supply_mld": 80,
  "water_demand_mld": 100
}

Example response:

{
  "region": "Region_A",
  "water_supply_mld": 80.0,
  "water_demand_mld": 100.0,
  "water_deficit_mld": 20.0,
  "assessment": "Potential shortage",
  "method": "Simplified supply-demand calculation",
  "is_machine_learning_prediction": false
}

6. Data Storage

The initial assessment API does not require a database. The demonstration CSV file stores illustrative records.

A future implementation may use PostgreSQL/PostGIS to store geographical features, regional measurements, data-source metadata, and historical observations.

7. Machine-Learning Extension

A future forecasting component could use Random Forest, XGBoost, or time-series models, depending on the data available.

A reliable model requires:

- Sufficient historical observations.
- Defined geographical and temporal units.
- Reliable shortage outcome labels.
- Missing-data handling.
- Chronological train-validation-test splits for forecasting.
- Comparison against simple baseline methods.
- Appropriate evaluation metrics.
- Monitoring for changes in data quality and model performance.

The current assessment API does not train or run a machine-learning model.

8. GIS Design

A GIS module can display risk areas and potential water sources on a map. Each feature should include its source, coordinates, update date, and relevant limitations.

A mapped source must not be assumed to be potable, legally accessible, environmentally suitable, or capable of meeting local demand.

9. Security

- Store secrets outside source code.
- Validate API input.
- Use HTTPS when deployed.
- Apply suitable access controls to private data.
- Minimize personal information collected through reporting features.

10. Limitations

The current API performs a simplified supply-demand calculation. It does not independently predict future scarcity, access live government datasets, verify water quality, or calculate engineering feasibility.

These capabilities require additional implementation and validation.
