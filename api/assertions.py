from playwright.sync_api import APIResponse


def assert_status(response: APIResponse, expected_status: int, action: str) -> None:
    assert response.status == expected_status, (
        f"{action} failed. Expected status {expected_status}, "
        f"got {response.status}. Response: {response.text()}"
    )


def assert_json_has_keys(response_body: dict, required_keys: list[str], action: str) -> None:
    missing_keys = [key for key in required_keys if key not in response_body]
    assert not missing_keys, f"{action} response missing keys: {missing_keys}. Body: {response_body}"
