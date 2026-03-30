from core.runner import run

def crawl(urls):
    input_data = "\n".join(urls)
    cmd = f"echo '{input_data}' | katana -silent -depth 3"
    return list(set(run(cmd)))