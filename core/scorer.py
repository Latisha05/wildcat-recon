def score_url(url):
    score = 0

    keywords = ["admin", "login", "debug", "test", "api", "dev", "staging"]

    if "?" in url:
        score += 3

    if "=" in url:
        score += 2

    if any(k in url.lower() for k in keywords):
        score += 3

    if url.count("/") > 5:
        score += 1

    return score

def extract_api(urls):
    api_urls = []
    for url in urls:
        if "/api/" in url or "graphql" in url or "v1" in url or "v2" in url:
            api_urls.append(url)
    return list(set(api_urls))

def filter_high_risk(urls):
    results = []
    for url in urls:
        s = score_url(url)
        if s >= 5:
            results.append((url, s))
    return sorted(results, key=lambda x: x[1], reverse=True)