from core.installer import setup_tools
from modules.subdomain import get_subdomains
from modules.alive import filter_alive
from modules.crawler import crawl
from modules.urls import get_urls
from core.scorer import filter_high_risk, extract_api

import json
import os

def banner():
    print("""
██╗    ██╗██╗██╗     ██████╗  ██████╗ █████╗ ████████╗
██║    ██║██║██║     ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
██║ █╗ ██║██║██║     ██║  ██║██║     ███████║   ██║   
██║███╗██║██║██║     ██║  ██║██║     ██╔══██║   ██║   
╚███╔███╔╝██║███████╗██████╔╝╚██████╗██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   

        WILDCAT RECON ENGINE v2
""")

def save_output(all_urls, risky, api_urls):
    os.makedirs("output", exist_ok=True)

    with open("output/all_urls.txt", "w") as f:
        f.write("\n".join(all_urls))

    with open("output/high_risk.txt", "w") as f:
        for url, score in risky:
            f.write(f"{url} | Score: {score}\n")

    with open("output/api_endpoints.txt", "w") as f:
        f.write("\n".join(api_urls))

def main():
    banner()
    target = input("Enter target domain: ")

    print("\n[1] Setting up tools...")
    setup_tools()

    print("\n[2] Finding subdomains...")
    subs = get_subdomains(target)
    print(f"[+] Found {len(subs)} subdomains")

    print("\n[3] Checking alive hosts...")
    alive = filter_alive(subs)
    print(f"[+] Alive: {len(alive)}")

    print("\n[4] Crawling + Gathering URLs...")
    urls = crawl(alive)
    urls += get_urls(target)
    urls = list(set(urls))
    print(f"[+] Total URLs found: {len(urls)}")

    print("\n[5] Extracting API endpoints...")
    api_urls = extract_api(urls)
    print(f"[+] API endpoints: {len(api_urls)}")

    print("\n[6] Scoring URLs...")
    risky = filter_high_risk(urls)

    print("\n🔥 High Risk URLs:\n")
    for url, score in risky[:20]:
        print(f"{url}  [Score: {score}]")

    save_output(urls, risky, api_urls)

    print("\n[+] Results saved in /output folder")

if __name__ == "__main__":
    main()