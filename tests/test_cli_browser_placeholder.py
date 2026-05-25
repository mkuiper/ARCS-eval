from companion_safety_eval.adapters.browser_manual import BrowserManualAdapter


def test_browser_manual_adapter_explains_handoff():
    adapter = BrowserManualAdapter()
    response = adapter.send("hello", [])
    assert "manual browser handoff" in response.content.lower()
    assert response.metadata["adapter"] == "browser_manual"
