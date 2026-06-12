import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original activities
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Practice team skills and compete in local soccer matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["alex@mergington.edu", "maria@mergington.edu"]
        },
        "Basketball Club": {
            "description": "Train on court fundamentals and scrimmage against other teams",
            "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["jordan@mergington.edu", "nina@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and mixed media art projects",
            "schedule": "Mondays and Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["lucy@mergington.edu", "leo@mergington.edu"]
        },
        "Drama Club": {
            "description": "Practice acting, stagecraft, and put on school performances",
            "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
        },
        "Math Olympiad": {
            "description": "Solve challenging math problems and prepare for competitions",
            "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["hannah@mergington.edu", "liam@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore science topics through projects",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu", "noah@mergington.edu"]
        }
    }
    
    # Clear existing activities and restore original state
    activities.clear()
    activities.update(original_activities)
    
    yield  # Run the test
    
    # Clean up after test
    activities.clear()
    activities.update(original_activities)
