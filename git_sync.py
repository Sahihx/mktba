import os
from git import Repo

def sync_repo(repo_url, local_path):
    if not os.path.exists(local_path):
        print("Cloning repository...")
        Repo.clone_from(repo_url, local_path)
    else:
        print("Updating repository...")
        repo = Repo(local_path)
        repo.remotes.origin.pull()
