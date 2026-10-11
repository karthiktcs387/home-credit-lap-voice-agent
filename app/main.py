from fastapi import FastAPI
from pydantic import BaseModel
from app.eligibility import check_eligibility

app = FastAPI(
    title="Home Credit LAP Qualification API",
    description="Preliminary Loan Against Property eligibility checker",
    version="1.0.0"
)


class Customer(BaseModel):
    property_type: str
    ownership_status: str
    original_documents_available: bool
    loan_amount: float
    occupation: str
    income_mode: str
    property_market_value: float
    tenure_years: int


@app.get("/")
def home():
    return {
        "message": "Home Credit LAP Qualification API is running"
    }


@app.post("/check-eligibility")
def check_customer_eligibility(customer: Customer):
    customer_data = customer.model_dump()
    result = check_eligibility(customer_data)

    return result