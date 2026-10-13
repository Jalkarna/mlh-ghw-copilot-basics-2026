def test_list_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert expected_activity in response.json()


def test_signup_success(client):
    # Arrange
    activity = "Soccer Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity}"}


def test_signup_rejected_when_activity_is_full(client):
    # Arrange
    activity = "Soccer Club"
    limit = 22
    emails = [f"student-{index}@mergington.edu" for index in range(limit)]

    # Act
    signup_responses = [
        client.post(f"/activities/{activity}/signup", params={"email": email})
        for email in emails
    ]
    full_response = client.post(
        f"/activities/{activity}/signup",
        params={"email": "next-student@mergington.edu"},
    )
    activities_response = client.get("/activities")

    # Assert
    assert all(response.status_code == 200 for response in signup_responses)
    assert full_response.status_code == 400
    assert full_response.json() == {"detail": "Activity is full"}
    assert len(activities_response.json()[activity]["participants"]) == limit


def test_duplicate_signup_rejected(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up"}


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity}"}


def test_signup_unknown_activity(client):
    # Arrange
    activity = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_unknown_activity(client):
    # Arrange
    activity = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_missing_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}


def test_signup_missing_email_query(client):
    # Arrange
    activity = "Soccer Club"

    # Act
    response = client.post(f"/activities/{activity}/signup")

    # Assert
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["query", "email"]


def test_unregister_missing_email_query(client):
    # Arrange
    activity = "Soccer Club"

    # Act
    response = client.delete(f"/activities/{activity}/signup")

    # Assert
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["query", "email"]
