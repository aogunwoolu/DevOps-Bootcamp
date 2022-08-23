### GIT

- **Git status**: tells you the current state of git
- **git config user.name ='[name]'**: sets config name
- **git config user.name**: shows config name
- **git config --list**: shows all 
- **git add [name of file]**: adds file to be tracked by git
  - multiple files can be added
    - **git add [file 1] [file 2] [file 3] ...**
  - all files can be added
    - **git add .**
- **git commit -m [commit message]**: commits to local branch with the associated message
- **git log**: produces everything that has occurs in the git history
  - listed in reverse chronological order
  - redirects to a scroll menu
  - ***space*** to scroll down
  - **Q** to exit/quit
- **git log --oneline**: produces every change, with info on one line
- **git checkout [change id]**: go to another state (the past/another branch)
  - **git checkout main/master**: go back to the most recent changes
- **git branch**: shows branches
- **git branch [branch name]**: create a branch
  - does not checkout to branch
- **git merge [branch name]**: merges 2 branches together (may cause conflicts)
  - constantly merge with main to keep up to date
  - **three different approaches**:
    1. **fast forward merge (default)**: fast fowards one of the branches to reach the other
- **git diff**: compare branches
- **git remote add [remote name] [remote url]**: creates a remote branch connected to the local branch
- **git remote**: shows all remote branches
- **git push -u [remote] [local]**: pushes from local branch to remote branch
  - **-u**: upstream
- **git clone [remote url]**: downloads git folder to the current working directory

### Pipenv

- **pipenv install**: installs from piplock file
- **pipenv install [module]**: installs specific module to virtual env + piplock
- **pipenv shell**: opens pipenv shell
- **pipenv run [command]**: runs command using pipenv shell

### Flask

- **flask --app [app to run] run**: run a flask application
- **flask --app [app to run]  --debug run**: run a flask application in debug mode