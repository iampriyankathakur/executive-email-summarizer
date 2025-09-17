from src.action_extractor import extract_actions

def test_extract_actions():
    emails = ["John to send report by Friday.", "Mary to prepare budget."]
    actions = extract_actions(emails)
    assert "John to send report by Friday" in actions
    assert "Mary to prepare budget" in actions
