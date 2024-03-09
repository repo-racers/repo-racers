import os
import argparse
from github import Github
import json
import re

# Create the parser
parser = argparse.ArgumentParser(description="List repositories in a GitHub organization")

# Add the arguments
parser.add_argument('--token', type=str, help='The GitHub token')
parser.add_argument('--org', type=str, help='The GitHub organization')
parser.add_argument('--pattern', type=str, help='The pattern to match repository URLs')
parser.add_argument('--full', action='store_true', help='Print the full list of repositories')
parser.add_argument('--filtered', action='store_true', help='Print the filtered list of repositories')

# Parse the arguments
args = parser.parse_args()

# Read the GitHub token from an environment variable if not provided as an argument
token = args.token if args.token else os.getenv('GITHUB_ADMIN_TOKEN')

# Create a Github instance using the token
g = Github(token)

# Get the organization
org = g.get_organization(args.org if args.org else "cprime-talent")

# Get all repos in the organization
repos = org.get_repos()

# Define the pattern for the repository URLs
pattern = args.pattern if args.pattern else r".*"

# Convert repos to a list of dictionaries so it can be output as JSON
repos_full_list = [{"name": repo.name, "url": repo.html_url} for repo in repos]

# Convert repos to a list of dictionaries so it can be output as JSON
# and filter the list to only include repos that match the pattern
repos_filtered_list = [{"name": repo.name, "url": repo.html_url} for repo in repos if re.match(pattern, repo.html_url)]

# Print the full list of repositories if the --full argument is provided
if args.full:
    print("Full list of repositories:")
    for repo in repos_full_list:
        print(f"Name: {repo['name']}, URL: {repo['url']}")

# Print the filtered list of repositories if the --filtered argument is provided
if args.filtered:
    print("\nFiltered list of repositories:")
    for repo in repos_filtered_list:
        print(f"Name: {repo['name']}, URL: {repo['url']}")

print("\n")
