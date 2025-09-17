import re

def extract_actions(emails):
    actions = []
    pattern = r"(?i)(\b[A-Z][a-z]+)\s+to\s+([^.]+)"
    for email in emails:
        matches = re.findall(pattern, email)
        for match in matches:
            person, task = match
            actions.append(f"{person} to {task.strip()}")
    return actions
