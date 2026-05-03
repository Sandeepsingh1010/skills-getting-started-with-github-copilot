from src.app import activities


def test_unregister_removes_student_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "registered.student@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup"

    activities[activity_name]["participants"].append(email)
    assert email in activities[activity_name]["participants"]

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {email} from {activity_name}"
    }
    assert email not in activities[activity_name]["participants"]
