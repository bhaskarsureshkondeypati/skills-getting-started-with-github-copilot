import sys
from pathlib import Path

# Add src to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_get_activities(client):
    """Test getting all activities
    
    Arrange: client is provided by fixture
    Act: send GET request to /activities
    Assert: response contains all 9 activities
    """
    # Arrange - client is provided by fixture
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert len(data) == 9


def test_signup_for_activity_success(client):
    """Test successful signup for an activity
    
    Arrange: choose new email and existing activity
    Act: send POST request to signup endpoint
    Assert: response confirms signup
    """
    # Arrange
    activity_name = "Chess Club"
    email = "newemail@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Signed up {email} for {activity_name}"


def test_signup_for_activity_already_signed_up(client):
    """Test signup fails when student already signed up
    
    Arrange: choose email already in activity participants
    Act: send POST request to signup endpoint
    Assert: response is 400 with duplicate error
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in participants
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_for_nonexistent_activity(client):
    """Test signup fails for non-existent activity
    
    Arrange: choose activity name that doesn't exist
    Act: send POST request to signup endpoint
    Assert: response is 404 not found
    """
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_remove_participant_success(client):
    """Test successfully removing a participant
    
    Arrange: choose participant already in an activity
    Act: send DELETE request to remove participant endpoint
    Assert: response confirms removal
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Removed {email} from {activity_name}"


def test_remove_participant_not_found(client):
    """Test removal fails when participant not in activity
    
    Arrange: choose email not in activity participants
    Act: send DELETE request to remove participant endpoint
    Assert: response is 404 not found
    """
    # Arrange
    activity_name = "Chess Club"
    email = "notinlist@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_remove_from_nonexistent_activity(client):
    """Test removal fails for non-existent activity
    
    Arrange: choose activity name that doesn't exist
    Act: send DELETE request to remove participant endpoint
    Assert: response is 404 not found
    """
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
