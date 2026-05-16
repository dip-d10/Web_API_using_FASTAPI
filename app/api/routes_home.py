from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def home():
    return JSONResponse(
        content={
            "message": "Welcome to Car Price Prediction API (Demo Project)",
            "instructions": {
                "step_1": {
                    "action": "Login first via /docs -> /login",
                    "username": "admin",
                    "password": "admin"
                },
                "step_2": {
                    "action": "Copy the access token returned after login"
                },
                "step_3": {
                    "action": "Go to /docs -> /predict",
                    "token_header": "Paste your token here",
                    "api_key": "demo_key"
                },
                "step_4": {
                    "action": "Provide car details and get predicted resale price"
                }
            },
            "demo_input": {
                "company": "Maruti",
                "year": 2015,
                "owner": "First",
                "fuel": "Petrol",
                "seller_type": "Individual",
                "transmission": "Manual",
                "km_driven": 160000,
                "mileage_mpg": 45,
                "engine_cc": 1250,
                "max_power_bhp": 82,
                "torque_nm": 120,
                "seats": 5
            },
            "docs_url": "https://web-api-using-fastapi.onrender.com/docs"
        }
    )