from core.runner import run

def get_subdomains(domain):
    cmd = f"subfinder -d {domain} -silent"
    return list(set(run(cmd)))