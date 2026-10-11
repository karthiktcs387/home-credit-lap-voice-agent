# Home Credit Loan Against Property (LAP) Qualification Voice Agent

## Project Overview

This project implements an AI-powered voice agent for Home Credit to conduct preliminary eligibility checks for existing customers interested in a Loan Against Property (LAP).

The voice agent communicates with customers, explains the loan offer, collects property and financial information, checks eligibility criteria, and determines the appropriate next steps.

The maximum loan amount is ₹75 lakhs, subject to preliminary eligibility checks and further verification by the lending team.

## Objectives

- Automate preliminary Loan Against Property qualification.
- Communicate with customers using a conversational AI voice agent.
- Collect essential property and financial details.
- Apply eligibility rules consistently.
- Identify customers who do not meet the preliminary criteria.
- Direct customers with existing property loans or loan-transfer requests to a specialist.
- Maintain call recordings and transcripts for review.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Retell AI
- REST API
- Visual Studio Code

## Project Structure

```text
home-credit-voice-agent/
│
├── app/
│   ├── eligibility.py
│   └── main.py
│
├── prompts/
│   └── system_prompt.txt
│
├── tests/
│   └── test_eligibility.py
│
├── call_recording.wav
├── call_transcript.txt
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## Eligibility Criteria

The voice agent evaluates the following criteria:

1. Property Type: Residential, commercial, and industrial properties are eligible for preliminary assessment. Agricultural properties are disqualified.
2. Ownership: Sole and joint ownership are accepted.
3. Original Documents: The customer must have the original property documents available.
4. Loan Amount: The maximum loan amount is ₹75,00,000. Customers requesting more are offered the maximum limit.
5. Occupation: Salaried and self-employed customers are considered.
6. Income Verification: Income must be received through a bank account. Cash-only income does not qualify.
7. Property Market Value: The estimated market value is collected for assessment.
8. Loan Tenure: The permitted tenure is between 3 and 15 years, inclusive.

Customers requesting an existing property-loan transfer or EMI reduction are referred to a loan-transfer specialist.

Final approval, interest rates, and loan terms are subject to the lender's verification and decision.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd home-credit-voice-agent
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

The application runs locally at:

```text
http://127.0.0.1:8000
```

### API Documentation

Open the following address in your browser:

```text
http://127.0.0.1:8000/docs
```

Use the interactive Swagger documentation to test the API.

## API Endpoint

### Check Eligibility

**Method:** POST

**Endpoint:**

```text
/check-eligibility
```

### Sample Request

```json
{
  "property_type": "Residential",
  "ownership_status": "Sole",
  "original_documents_available": true,
  "loan_amount": 5000000,
  "occupation": "Salaried",
  "income_mode": "Bank",
  "property_market_value": 8000000,
  "tenure_years": 10
}
```

### Expected Result

The API evaluates the submitted customer information and returns a preliminary eligibility status.

Possible outcomes include:

- `PRELIMINARILY_ELIGIBLE`
- `DISQUALIFIED`
- `INCOMPLETE`

The result is not a final loan approval.

## Testing

The project includes unit tests for important eligibility scenarios.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

The tests cover scenarios such as:

- Eligible customer
- Agricultural property
- Cash-based income
- Missing original property documents
- Loan amount exceeding the maximum limit
- Invalid loan tenure

## Voice Agent

The voice agent was configured using Retell AI.

Its responsibilities include:

- Greeting customers professionally.
- Explaining the Loan Against Property offer.
- Collecting customer eligibility information.
- Answering questions within the provided context.
- Respecting customer requests to stop or receive a callback.
- Referring existing-loan transfer requests to the appropriate specialist.
- Communicating the preliminary outcome without promising loan approval.

Call recordings and transcripts are maintained for testing and evaluation.
## Live Link
https://agent.retellai.com/orb/agent_4f7ed48590fd42e68d3cf566e7?token=b807896230e6bf6965e7a94951c94dc8

## Project Files

- `app/eligibility.py`: Contains the preliminary eligibility-checking logic.
- `app/main.py`: Defines the FastAPI application and eligibility endpoint.
- `prompts/system_prompt.txt`: Contains the voice agent's instructions and business rules.
- `tests/test_eligibility.py`: Contains unit tests for eligibility scenarios.
- `call_recording.wav`: Sample voice-agent test recording.
- `call_transcript.txt`: Transcript of the recorded test conversation.
- `requirements.txt`: Lists the Python dependencies.

## Security Notes

- Do not commit `.env` files or API keys to a public repository.
- Keep credentials and private customer information confidential.
- Use synthetic customer information for demonstrations.
- Share recordings and transcripts only through authorized links.

## Limitations

This project performs preliminary qualification only. It does not provide final loan approval, guarantee disbursement, or determine the lender's final interest rate.

## Conclusion

The Home Credit LAP Qualification Voice Agent demonstrates how conversational AI can automate preliminary customer qualification, apply consistent eligibility rules, and support efficient customer handoffs.

The project combines a Retell AI voice agent with a Python-based FastAPI eligibility service to demonstrate conversational qualification and rule-based validation.
