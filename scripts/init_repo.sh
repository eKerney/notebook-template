#!/bin/bash

# set default branch for new repo's to main
git config --global init.defaultBranch main

# Function to display usage/help
usage() {
    echo "Usage: $0 <project-name> <username>"
    echo ""
    exit 1
}
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    usage
fi

if [[ "$#" < 2 ]]; then 
    echo "must provide both args <origin-url> <project-name>"
else
    echo "# $1" >> README.md
    git init
    git add README.md
    git commit -m "$1 init commit"
    gh repo create "$1" --public --source=. --remote=origin --push
    gh repo edit "$2"/"$1" --default-branch main
    git remote -v 
    # git branch -M main
    # git remote add origin "$1"
    # git push -u origin main
fi
