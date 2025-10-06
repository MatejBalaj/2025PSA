import os
#repo_path = "c:\\Users\\matej\Desktop\\2025PSA"
repo_path = r"c:\Users\matej\Desktop\2025PSA"
repo_name = "2025PSA"
repo_url =  "https://github.com/MatejBalaj/2025PSA.git"

def clone_repo(path, url):
    os.chdir(path)
    os.system("git clone "+ url)

clone_repo(repo_path, repo_url)


a = 6