def check_eligibility(customer):
    """
    Check preliminary eligibility for a Home Credit LAP offer.
    """

    # 1. Validate property type
    property_type = customer.get("property_type", "").strip().lower()

    if property_type == "agricultural":
        return {
            "status": "DISQUALIFIED",
            "reason": "Agricultural property is not eligible."
        }

    if property_type not in ["residential", "commercial", "industrial"]:
        return {
            "status": "INCOMPLETE",
            "reason": "Valid property type is required."
        }

    # 2. Validate ownership
    ownership = customer.get("ownership_status", "").strip().lower()

    if ownership not in ["sole", "joint"]:
        return {
            "status": "INCOMPLETE",
            "reason": "Valid ownership information is required."
        }

    # 3. Validate original property documents
    documents_available = customer.get("original_documents_available")

    if documents_available is not True:
        if documents_available is False:
            return {
                "status": "DISQUALIFIED",
                "reason": "Original property documents are required."
            }

        return {
            "status": "INCOMPLETE",
            "reason": "Document availability must be confirmed."
        }

    # 4. Validate loan amount
    loan_amount = customer.get("loan_amount")

    if not isinstance(loan_amount, (int, float)) or isinstance(loan_amount, bool):
        return {
            "status": "INCOMPLETE",
            "reason": "A valid loan amount is required."
        }

    if loan_amount <= 0:
        return {
            "status": "INCOMPLETE",
            "reason": "Loan amount must be greater than zero."
        }

    if loan_amount > 7500000:
        return {
            "status": "DISQUALIFIED",
            "reason": "The maximum offer amount is ₹75 lakhs."
        }

    # 5. Validate occupation
    occupation = customer.get("occupation", "").strip().lower()

    if occupation not in ["salaried", "self-employed"]:
        return {
            "status": "INCOMPLETE",
            "reason": "Valid occupation information is required."
        }

    # 6. Validate income mode
    income_mode = customer.get("income_mode", "").strip().lower()

    if income_mode == "cash":
        return {
            "status": "DISQUALIFIED",
            "reason": "Income must be received through a bank."
        }

    if income_mode != "bank":
        return {
            "status": "INCOMPLETE",
            "reason": "Income mode must be confirmed."
        }

    # 7. Validate property market value
    market_value = customer.get("property_market_value")

    if (
        not isinstance(market_value, (int, float))
        or isinstance(market_value, bool)
        or market_value <= 0
    ):
        return {
            "status": "INCOMPLETE",
            "reason": "A valid property market value is required."
        }

    # 8. Validate repayment tenure
    tenure = customer.get("tenure_years")

    if not isinstance(tenure, (int, float)) or isinstance(tenure, bool):
        return {
            "status": "INCOMPLETE",
            "reason": "A valid repayment tenure is required."
        }

    if not 3 <= tenure <= 15:
        return {
            "status": "DISQUALIFIED",
            "reason": "Repayment tenure must be between 3 and 15 years."
        }

    # All specified preliminary criteria have passed.
    return {
        "status": "PRELIMINARILY_ELIGIBLE",
        "reason": "All specified preliminary eligibility checks passed."
    }