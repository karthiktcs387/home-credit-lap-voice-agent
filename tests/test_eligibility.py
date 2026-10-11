import unittest

from app.eligibility import check_eligibility


class TestEligibility(unittest.TestCase):

    def setUp(self):
        self.customer = {
            "property_type": "residential",
            "ownership_status": "sole",
            "original_documents_available": True,
            "loan_amount": 5000000,
            "occupation": "salaried",
            "income_mode": "bank",
            "property_market_value": 10000000,
            "tenure_years": 10
        }

    def test_eligible_customer(self):
        result = check_eligibility(self.customer)
        self.assertEqual(
            result["status"],
            "PRELIMINARILY_ELIGIBLE"
        )

    def test_agricultural_property(self):
        self.customer["property_type"] = "agricultural"
        result = check_eligibility(self.customer)
        self.assertEqual(result["status"], "DISQUALIFIED")

    def test_cash_income(self):
        self.customer["income_mode"] = "cash"
        result = check_eligibility(self.customer)
        self.assertEqual(result["status"], "DISQUALIFIED")

    def test_missing_original_documents(self):
        self.customer["original_documents_available"] = False
        result = check_eligibility(self.customer)
        self.assertEqual(result["status"], "DISQUALIFIED")

    def test_loan_above_limit(self):
        self.customer["loan_amount"] = 8000000
        result = check_eligibility(self.customer)
        self.assertEqual(result["status"], "DISQUALIFIED")

    def test_invalid_tenure(self):
        self.customer["tenure_years"] = 20
        result = check_eligibility(self.customer)
        self.assertEqual(result["status"], "DISQUALIFIED")


if __name__ == "__main__":
    unittest.main()