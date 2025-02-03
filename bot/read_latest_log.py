def read_latest_changelog():
    with open('CHANGELOG.md', 'r') as file:
        content = file.read().strip()
        entries = content.split('\n\n')  # Assuming entries are separated by two newlines
        if entries:
            return entries[0]
    return None


def save_last_posted_update(update):
    with open('last_posted_update.txt', 'w') as file:
        file.write(update)

def load_last_posted_update():
    try:
        with open('last_posted_update.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None  # No update has been posted yet
