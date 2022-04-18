# Hermit's Heaven  
website for school.  
everything you see on this site is obviously fake.  
---
## Build
1) Prerequisites  
    1.1) Make sure you have Python 3.8+ installed. If you have not, download it from its [official website](https://www.python.org/). Also make sure interpreter's executable is in PATH  
2) Downloading repository  
    2.1) Download the repository (via the big green "Code" button above, or any other way you prefer to download git repositories)  
    2.2) Place it somewhere, let's say in `C:/hermits-heaven.github.io/`. We will refer to this path as `<REPO_PATH>` later, for convenience  
3) Build repository  
    3.1) Open the terminal (`cmd` on Windows), and run `cd <REPO_PATH>` (replace <REPO_PATH> with the path you placed the repository in)  
    3.2) Run `pip install -r requirements.txt`  
    3.3) Wait for packages to install, check for any errors  
    3.4) Run `python build.py`. Check for any errors, if there is no output then everything is OK  
    3.5) Run `mkdir deploy && cd deploy`  
    3.6) Run `python -m http.server`.  
    3.7) Open in your browser http://localhost:8000/  
    3.8) Observe the results  
You don't have to exactly follow these steps, just make sure that you have installed packages from requirements.txt, and have run `build.py` script, as well as started some sort of server inside of deploy/ directory, so paths inside htmls would resolve correctly

    
