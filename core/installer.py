import shutil
import os

TOOLS = {
    "subfinder": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "httpx": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "katana": "go install github.com/projectdiscovery/katana/cmd/katana@latest",
    "gau": "go install github.com/lc/gau/v2/cmd/gau@latest",
    "waybackurls": "go install github.com/tomnomnom/waybackurls@latest"
}

def check_tool(tool):
    return shutil.which(tool) is not None

def install_tool(tool, cmd):
    print(f"[+] Installing {tool}...")
    os.system(cmd)

def setup_tools():
    for tool, cmd in TOOLS.items():
        if not check_tool(tool):
            install_tool(tool, cmd)
        else:
            print(f"[✓] {tool} already installed")