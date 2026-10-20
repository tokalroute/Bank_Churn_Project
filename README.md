 Bank Customer Churn Prediction System
An end-to-end Machine Learning solution for predicting bank customer churn risk. The system includes an automated training and evaluation pipeline, a high-performance FastAPI REST backend, an interactive Streamlit web dashboard, containerized deployment with Docker Compose, and automated testing with pytest and Ruff.
Architecture Overview
```mermaid
flowchart TD
Data[data/demo_churn.csv] --> Load[app/data.py]
Load --> TrainScript[train_model.py]
TrainScript --> Pipeline[app/training.py]
Pipeline --> Artifacts[artifacts/churn_model.joblib & metrics.json]
Artifacts --> ModelService[app/model_service.py]
ModelService --> FastAPI[app/main.py (FastAPI)]
User[User / Client] --> Streamlit[ui/streamlit_app.py (Streamlit UI)]
Streamlit -->|HTTP POST /predict| FastAPI
User -->|Direct HTTP Requests| FastAPI
```
Features

    Machine Learning Pipeline: Scikit-Learn `Pipeline` combining categorical `OneHotEncoder` and `RandomForestClassifier`.
    RESTful API: Fast and robust API endpoints with Pydantic data validation and structured response schemas.
    Risk Tier Scoring: Maps churn probabilities to actionable risk tiers:
        High Risk: $\ge 70%$
        Medium Risk: $30% - 69%$
        Low Risk: $< 30%$
    Interactive UI: User-friendly Streamlit web interface for single-customer churn analysis.
    Production-Ready Docker: Minimal Red Hat Universal Base Image containers running as non-root users.
    Automated Testing & Code Quality: 18 unit and integration tests with `pytest`, pre-commit hooks, and lightning-fast linting with `Ruff`.

Project Structure
```
Bank_Churn_Project/
├── .env.example # Environment variables template
├── .gitignore # Git ignore configuration
├── .pre-commit-config.yaml # Pre-commit hooks (Ruff & formatting)
├── Dockerfile.api # Docker container for FastAPI backend
├── Dockerfile.streamlit # Docker container for Streamlit frontend
├── docker-compose.yml # Docker Compose multi-service orchestrator
├── pyproject.toml # Project dependencies, pytest & ruff configs
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── train_model.py # Model training & artifact generation script
├── app/ # Backend application package
│ ├── config.py # App configurations & environment loading
│ ├── data.py # Data loading & stratified train/test split
│ ├── evaluation.py # Model evaluation metrics (accuracy, recall, f1)
│ ├── logging_config.py # Structured logging setup
│ ├── main.py # FastAPI application & route handlers
│ ├── model_service.py # Inference logic & risk categorization
│ ├── preprocessing.py # ColumnTransformer feature preprocessing
│ ├── schemas.py # Pydantic request models & validations
│ └── training.py # Pipeline definition & model training
├── artifacts/ # Serialized model & metrics
│ ├── churn_model.joblib # Trained Random Forest model weights
│ └── metrics.json # Evaluation metrics output
├── data/
│ └── demo_churn.csv # Customer dataset
├── tests/ # Pytest test suite (18 tests)
│ ├── conftest.py # Reusable test fixtures & TestClient
│ ├── test_api.py # FastAPI endpoint tests
│ ├── test_evaluation.py # Metric calculation tests
│ ├── test_model_service.py # Inference & risk tier tests
│ ├── test_preprocessing.py # Preprocessing pipeline tests
│ └── test_schemas.py # Pydantic model validation tests
└── ui/
└── streamlit_app.py # Streamlit interactive frontend
```
Step-by-Step Guide: Running the Project
Prerequisites

    Python 3.11+ (Python 3.14 fully supported)
    Pip package manager
    (Optional) Docker & Docker Compose

Step 1: Navigate to Project Directory & Set Up Virtual Environment
Open your terminal and navigate to the project directory:
```bash
cd Bank_Churn_Project
```
On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
On Windows (Command Prompt):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```
On Linux / macOS (Bash / Zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
(Optional) Install development and testing tools:
```bash
pip install pytest httpx ruff pre-commit
```
Step 3: Train the Machine Learning Model
Before starting the API, generate the trained model artifact and evaluation metrics:
```bash
python train_model.py
```
Expected Output:
```
INFO: Loaded 1000 rows
INFO: Model training complete
INFO: Evaluation: {'accuracy': 0.728, 'recall': 0.291, 'f1': 0.38}
INFO: Model saved to artifacts/churn_model.joblib
INFO: Metrics saved to artifacts/metrics.json
```
Step 4: Run the Application Locally
Terminal 1 — Start the FastAPI Backend:
```bash
uvicorn app.main:app --reload --port 8000
```

    Interactive API Documentation (Swagger): http://127.0.0.1:8000/docs
    Alternative Documentation (ReDoc): http://127.0.0.1:8000/redoc
    API Health Check: http://127.0.0.1:8000/health

Terminal 2 — Start the Streamlit Frontend UI:
Open a new terminal window, activate the virtual environment, and run:
```bash
cd Bank_Churn_Project
streamlit run ui/streamlit_app.py
```

    Frontend Web Dashboard: http://localhost:8501

Alternative: Run with Docker Compose
To start both services in isolated containers without setting up a local Python environment:
```bash
cd Bank_Churn_Project
Build and start services in the background
docker compose up -d --build
View real-time container logs
docker compose logs -f
Stop and remove containers
docker compose down
```

    Streamlit UI: http://localhost:8501
    FastAPI Docs: http://localhost:8000/docs

Step-by-Step Guide: Running Tests
The test suite includes 18 unit and integration tests covering input validation, feature transformation, inference logic, metric evaluation, and FastAPI endpoints.
1. Run All Tests
```bash
pytest
```
2. Run All Tests with Verbose Output
```bash
pytest -v
```
3. Run a Specific Test Module
```bash
Test FastAPI endpoints
pytest tests/test_api.py -v
Test Pydantic schema validation
pytest tests/test_schemas.py -v
Test preprocessing & OneHotEncoder
pytest tests/test_preprocessing.py -v
Test model inference service
pytest tests/test_model_service.py -v
Test evaluation metrics
pytest tests/test_evaluation.py -v
```
4. Run a Single Test Function
```bash
pytest tests/test_api.py::test_predict_single_endpoint -v
```
5. Run Tests with Code Coverage (if `pytest-cov` is installed)
```bash
pytest --cov=app tests/ -v
```
Code Quality, Linting & Formatting
1. Run Ruff Linter
```bash
Check code for issues
ruff check .
Check and automatically fix issues
ruff check --fix .
```
2. Run Ruff Code Formatter
```bash
Check formatting without modifying files
ruff format --check .
Format all files in place
ruff format .
```
3. Set Up & Run Git Pre-Commit Hooks
```bash
Install hooks into git
pre-commit install
Run hooks across all tracked files manually
pre-commit run --all-files
```
API Reference
Method
	
Endpoint
	
Description
`GET`
	
`/health`
	
Health check verifying model status
`GET`
	
`/model/info`
	
Returns model name and evaluation metrics
`POST`
	
`/predict`
	
Predict churn probability for a single customer
`POST`
	
`/predict/batch`
	
Batch predictions for 1 to 50 customers
Example Request (`POST /predict`)
```json
{
"credit_score": 650,
"geography": "France",
"age": 42,
"tenure": 5,
"balance": 75000.0,
"num_of_products": 2,
"has_credit_card": true,
"is_active_member": true
}
```
Example Response
```json
{
"prediction": 0,
"churn_probability": 0.24,
"risk_level": "Low"
}
```
Environment Variables
Copy `.env.example` to `.env` to customize settings:
Variable
	
Default Value
	
Description
`API_URL`
	
`http://127.0.0.1:8000`
	
Target API URL used by Streamlit frontend
`DATA_PATH`
	
`data/demo_churn.csv`
	
Relative or absolute path to customer dataset
`MODEL_PATH`
	
`artifacts/churn_model.joblib`
	
Path where model weights are stored/loaded
`METRICS_PATH`
	
`artifacts/metrics.json`
	
Path where evaluation metrics JSON is saved
`LOG_LEVEL`
	
`INFO`
	
Application log level (`DEBUG`, `INFO`, `WARN`, `ERROR`)








