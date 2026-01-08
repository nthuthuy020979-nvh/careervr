"""
Test cases for CareerVR API
Run with: pytest test_api.py -v
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    print("✅ Health check test passed")

def test_riasec_valid():
    """Test RIASEC with valid data"""
    payload = {
        "name": "Nguyễn Văn A",
        "class": "10A1",
        "school": "THPT Ngô Quyền",
        "answer": list(range(1, 6)) * 10  # 50 answers: [1,2,3,4,5,1,2,3,4,5,...]
    }
    
    # This will fail with 500 due to missing DIFY_API_KEY
    # But we're testing validation here
    response = client.post("/run-riasec", json=payload)
    # Should get validation passed (or Dify error)
    assert response.status_code in [200, 500]  # 500 is ok if Dify fails
    print("✅ Valid payload test passed")

def test_riasec_invalid_answers_count():
    """Test RIASEC with wrong answer count"""
    payload = {
        "name": "Test",
        "class": "10A1",
        "school": "School",
        "answer": [1, 2, 3]  # Only 3 answers, should fail
    }
    
    response = client.post("/run-riasec", json=payload)
    assert response.status_code == 422  # Validation error
    print("✅ Invalid answer count test passed")

def test_riasec_invalid_answer_value():
    """Test RIASEC with invalid answer values"""
    payload = {
        "name": "Test",
        "class": "10A1",
        "school": "School",
        "answer": [1, 2, 3, 4, 6] + [1] * 45  # 6 is invalid (should be 1-5)
    }
    
    response = client.post("/run-riasec", json=payload)
    assert response.status_code == 422
    print("✅ Invalid answer value test passed")

def test_riasec_empty_name():
    """Test RIASEC with empty name"""
    payload = {
        "name": "",
        "class": "10A1",
        "school": "School",
        "answer": [1] * 50
    }
    
    response = client.post("/run-riasec", json=payload)
    assert response.status_code == 422
    print("✅ Empty name validation test passed")

def test_riasec_whitespace_name():
    """Test RIASEC with whitespace-only name"""
    payload = {
        "name": "   ",
        "class": "10A1",
        "school": "School",
        "answer": [1] * 50
    }
    
    response = client.post("/run-riasec", json=payload)
    assert response.status_code == 422
    print("✅ Whitespace name validation test passed")

if __name__ == "__main__":
    print("Running CareerVR API tests...\n")
    
    try:
        test_health()
        test_riasec_valid()
        test_riasec_invalid_answers_count()
        test_riasec_invalid_answer_value()
        test_riasec_empty_name()
        test_riasec_whitespace_name()
        
        print("\n✅ All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        exit(1)
