#!/usr/bin/env python

from sys import argv

from jira import JIRA
from random import choice

"""
argv[0] -> script
argv[1] -> server
argv[2] -> username
argv[3] -> password
argv[4] -> project
argv[5] -> mode
"""
server = argv[1] if len(argv) >= 2 else None
username = argv[2] if len(argv) >= 3 else None
password = argv[3] if len(argv) >= 4 else None
project = argv[4] if len(argv) >= 5 else None
mode = argv[5] if len(argv) >= 6 else None

jira = JIRA({'server': server}, basic_auth=(username, password))

def get_users():
    users = jira.search_assignable_users_for_projects('', project)
    return users

def get_my_issues():
    issues = jira.search_issues('issuetype in (standardIssueTypes(), subTaskIssueTypes(), Story) AND status in (Open, "In Dev", "To Do", "In QA", "In Progress", "QA Verify", Idea, "In UX") AND assignee = currentUser() and project = {}'.format(project), maxResults=False)
    return issues

def all_hands_on_deck():
    print "ALL HANDS ON DECK"

    users = get_users()
    issues = get_my_issues()
    
    for issue in issues:
        user = choice(users)
        print 'assigning {} to {}'.format(issue.key, user.key)
        if mode == '1':
            jira.assign_issue(issue, user.key)

def main():
    all_hands_on_deck()

if __name__ == "__main__":
    main()
