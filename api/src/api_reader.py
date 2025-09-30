import requests

def fetch_part_data(part, api_key):
    url = "https://api.octopart.com/graphql"  # пример GraphQL endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    query = {
        "query": """
        query {
            search(q: "%s", limit: 1) {
                results {
                    part {
                        mpn
                        manufacturer {
                            name
                        }
                    }
                }
            }
        }
        """ % part
    }
    resp = requests.post(url, json=query, headers=headers)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    api_key = ''
    with open("key", "r") as f:
        api_key = f.read().strip()
    print(api_key)

    part = "LM358"
    data = fetch_part_data(part, api_key)
    print(data)

    houses = load_data_from_api(API_URL, 50)
    result = convert_to_df_and_save(houses, OUTPUT_FILENAME)

    print(result.info())
    print(result["name"].head(10))


if __name__ == "__main__":
    main()
