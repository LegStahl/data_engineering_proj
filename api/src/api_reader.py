import requests

filename='set'

def search_github_repos(query: str, max_results: int = 5):
    """
    Ищет репозитории на GitHub по заданному запросу и возвращает список словарей с названием и ссылкой.
    """
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Проверяем HTTP-код ответа
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return []
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Ошибка соединения: {conn_err}")
        return []
    except requests.exceptions.Timeout as timeout_err:
        print(f"Превышено время ожидания: {timeout_err}")
        return []
    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
        return []

    try:
        data = response.json()
    except ValueError as json_err:
        print(f"Ошибка декодирования JSON: {json_err}")
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
    print(f"Поиск репозиториев GitHub по запросу: '{query}'\n")
    repos = search_github_repos(query)

    if not repos:
        print("Репозитории не найдены или произошла ошибка.")
        return

    for idx, repo in enumerate(repos, start=1):
        print(f"{idx}. {repo['name']} — {repo['url']}")


if __name__ == "__main__":
    main()

