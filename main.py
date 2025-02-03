from bot.post import post_if_new_update, post_to_slack
from bot.read_latest_log import read_latest_changelog


def main():
    changelog_entry = read_latest_changelog()
    slack_channel = '#all-cicdscriptdemo'  # Specify your Slack channel here
    # post(slack_channel, changelog_entry)
    post_if_new_update()

if __name__ == "__main__":
    main()