import os
#repo_path = "c:\\Users\\matej\Desktop\\2025PSA"
repo_path = r"c:\Users\matej\Desktop\2025PSA"
repo_name = "2025PSA"
repo_url =  "https://github.com/MatejBalaj/2025PSA.git"

def clone_repo(path, url):
    os.chdir(path)
    os.system("git clone "+ url)

clone_repo(repo_path, repo_url)


def add_file(path, rname, fname):
    os.chdir(path + "/" + rname)
    os.system("git add " + fname)

    #clone_repo(repo_path, repo_url)

    file = open(repo_path + "/" + repo_name + "/" + "/qwerty.txt", "w")
    file.write("nahoda")
    file.close()
    
def commit_changes(path, rname, message):
    os.chdir(path + "/" + rname)
    os.system("git commit -m \"" + message + "\"")
#clone_repo(repo_path, repo_url)

def push_git(path, rname):
    os.chdir(path + "/" + rname)
    os.system("git push")

#commit_changes(repo_path, repo_name, "commit from python")
push_git(repo_path, repo_name)


################################

file = open(repo_path + "/" + repo_name)