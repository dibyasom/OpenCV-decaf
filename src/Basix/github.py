import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def createQuery(languages, min_stars=6000):
    # f-string
    query = f"stars:>{min_stars} "

    # Github search API expected format.
    for lang in languages:
        query += f"language:{lang} "

    return query


def mostStarred(languages, sort="stars", order="desc"):
    # Generate query
    query = createQuery(languages)
    params = {"q": query, "sort": sort, "order": order}

    # Send a request to github server
    response = requests.get(GITHUB_API_URL, params=params)
    statusCode = response.status_code

    if statusCode != 200:
        raise RuntimeError(f"\nAn error occured! \tHTTP code: {statusCode}")
    else:
        responseJson = response.json()
        return responseJson["items"]


# Point of entry
if __name__ == "__main__":
    languages = ["python", "javascript"]

    # Ctrl click to jump to source.
    response = mostStarred(languages=languages)
    for res in response:
        print(
            f"Name: {res['name']} | Stars: {res['stargazers_count']}\nDescription: {res['description']}\n")
