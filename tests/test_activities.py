def test_get_activities_returns_activity_dictionary(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "Chess Club" in payload
    assert set(["description", "schedule", "max_participants", "participants"]).issubset(
        payload["Chess Club"].keys()
    )
