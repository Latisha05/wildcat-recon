from core.runner import run

def filter_alive(subdomains):
    urls = []
    for sub in subdomains:
        urls.append(f"http://{sub}")
        urls.append(f"https://{sub}")

    input_data = "\n".join(urls)

    cmd = f"echo '{input_data}' | httpx -silent -threads 100 -timeout 5"
    return list(set(run(cmd)))