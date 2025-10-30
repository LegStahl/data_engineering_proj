import requests
import pandas as pd

filename='set'


def save_as_csv(repos):

    df = pd.DataFrame(repos, columns=['name', 'url'])

    df.to_csv('repos.csv', index=False, encoding='utf-8-sig')
    print("Data in .csv was saved")


def search_github_repos(query: str, max_results: int = 5):

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        return []
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connection: {conn_err}")
        return []
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout is too over: {timeout_err}")
        return []
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
        return []

    try:
        data = response.json()
    except ValueError as json_err:
        print(f"Error of decoding json: {json_err}")
        return []

    repos = []
    for repo in data.get("items", [])[:max_results]:
        repos.append({
            "name": repo.get("full_name"),
            "url": repo.get("html_url")
        })

    return repos


def main():
    query=""
    with open(filename, "r") as f:
        query = [line.strip() for line in f if line.strip()]

    print(query)
    print(f"Looking for repos : '{query}'\n")
    repos = search_github_repos(query)

    if not repos:
        print("Repos weere not found or an error appeared.")
        return

    for idx, repo in enumerate(repos, start=1):
        print(f"{idx}. {repo['name']} — {repo['url']}")

    answer = input("Do you want to save data as .csv? Write 'yes' ot 'no'" )
    if answer == "yes":
        save_as_csv(repos)

if __name__ == "__main__":
    main()

