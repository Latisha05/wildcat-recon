from core.runner import run

def get_urls(domain):
    print("[+] Fetching URLs from gau...")
    gau_urls = run(f"gau {domain}")

    print("[+] Fetching URLs from waybackurls...")
    wayback_urls = run(f"waybackurls {domain}")

    return list(set(gau_urls + wayback_urls))