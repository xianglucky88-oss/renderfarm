import pytest

def test_artifacts_is_open_gap():
    from src.renderfarm import artifacts
    with pytest.raises(NotImplementedError):
        artifacts.process({"id": "x"})

def test_wait_policy_is_open_gap():
    from src.renderfarm import wait_policy
    with pytest.raises(NotImplementedError):
        wait_policy.process({"id": "x"})
