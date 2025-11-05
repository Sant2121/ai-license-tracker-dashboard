
### 🧩 app.py
```python
from fastapi import FastAPI

app = FastAPI(title="AI License Tracker Dashboard")

mock_data = {
    "total_licenses": 256,
    "active": 230,
    "expired": 26,
    "monthly_revenue": "₹1,85,000",
    "usage_stats": {"OpenAI": 120, "Anthropic": 45, "BharatGen": 65}
}

@app.get("/stats")
def get_stats():
    return mock_data
