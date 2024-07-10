import requests
from datetime import datetime

# GitHub username
username = "ZigaoWang"


# Fetch repositories from GitHub API
def fetch_repositories(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# Generate portfolio content
def generate_portfolio(repos):
    portfolio = "## Zigao Wang's Project Portfolio\n\n"
    for repo in repos:
        if repo['fork']:
            continue  # Skip forked repositories
        name = repo['name']
        description = repo['description']
        language = repo['language']
        license = repo['license']['name'] if repo['license'] else "No License"
        updated_at = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")
        url = repo['html_url']

        portfolio += f"### [{name}]({url})\n"
        portfolio += f"- **Description**: {description}\n"
        portfolio += f"- **Language**: {language}\n"
        portfolio += f"- **License**: {license}\n"
        portfolio += f"- **Last Updated**: {updated_at}\n\n"

    return portfolio


# Main function
def main():
    repos = fetch_repositories(username)
    portfolio_content = generate_portfolio(repos)

    # Update README.md file
    with open("README.md", "w") as file:
        file.write(portfolio_content)

    print("Portfolio updated successfully!")


if __name__ == "__main__":
    main()