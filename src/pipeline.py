import argparse, json
from summarizer import get_summary
from action_extractor import extract_actions

def process_emails(path):
    with open(path, "r") as f:
        data = json.load(f)
    emails = data["thread"]

    summary = get_summary(emails)
    actions = extract_actions(emails)

    result = {"summary": summary, "actions": actions}
    with open("data/output_summary.json", "w") as out:
        json.dump(result, out, indent=2)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to JSON with email thread")
    args = parser.parse_args()
    process_emails(args.file)
