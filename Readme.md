# All Hands On Deck

This handy script will help you get both of your hands on a deck.

* Ever wish a particular bug wasn't assigned to you? I have.
* Ever go into a meeting not knowing how to explain that something's not done? Me too.
* Hate Jira? Gawd, it's terrible.

`all-hands-on-deck.py` will alleviate all your worries and help improve your standing with managers, directors and above.

## How does `all-hands-on-deck.py` work?

This job saving tool will go through every Jira ticket assigned to you and reassign it to a random person in your organization. Sucks for them but awesome for you, right?

### Installation
```
git clone https://github.com/jmathai/all-hands-on-deck.git
cd all-hands-on-deck
pip install -r requirements.txt
```

### Usage
```
# dry run to only display what would happen
./all-hands-on-deck.py http://jirahost.com jira_username jira_password jira_project
```

Once you're ready to free yourself of all Jiras you can run the same command and add another argument of `1` to the script.
