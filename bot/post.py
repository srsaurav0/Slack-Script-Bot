import os

import yaml
from bot.read_latest_log import load_last_posted_update, read_latest_changelog, save_last_posted_update
from slack_sdk import WebClient # type: ignore
from slack_sdk.errors import SlackApiError # type: ignore

def load_config(file_path="config.yaml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


# Load the configuration
config = load_config()

# Initialize a Slack client
client = WebClient(token=config.get('SLACK_BOT_TOKEN'))


def post_to_slack(channel, message):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print("Message posted successfully:", response["message"]["text"])
    except SlackApiError as e:
        print(f"Error posting message: {e}")


def post_if_new_update():
    last_posted_update = load_last_posted_update()
    latest_changelog_entry = read_latest_changelog()

    if latest_changelog_entry and latest_changelog_entry != last_posted_update:
        post_to_slack(config.get('SLACK_CHANNEL'), latest_changelog_entry)
        save_last_posted_update(latest_changelog_entry)
    else:
        print("No new updates to post.")



