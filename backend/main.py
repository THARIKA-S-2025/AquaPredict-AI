from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="AquaPredict AI API",
    description="Prototype API for water-deficit assessment.",
    version="1.0.0",
)


class WaterAssessment(BaseModel):
    region: str = Field(min_length=1, max_length=100)
    water_supply_mld: float = Field(ge=0)
    water_demand_mld: float = Field(ge=0)


@app.get("/")
def home():
    return {
        "project": "AquaPredict AI",
        "status": "running",
        "note": "Prototype water-deficit assessment API",
    }


@app.post("/assess")
def assess_water(data: WaterAssessment):
    deficit = data.water_demand_mld - data.water_supply_mld

    if deficit > 0:
        status = "Potential shortage"
    elif deficit < 0:
        status = "Estimated supply exceeds demand"
    else:
        status = "Estimated supply equals demand"

    return {
        "region": data.region,
        "water_supply_mld": data.water_supply_mld,
        "water_demand_mld": data.water_demand_mld,
        "water_deficit_mld": round(deficit, 2),
        "assessment": status,
        "method": "Simplified supply-demand calculation",
        "is_machine_learning_prediction": False,
    }
