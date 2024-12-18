#!/bin/bash

# Define the array of specific repositories
REPOS=(
    "$HOME/OneDrive/Documents/GitHub/age-of-empires-ii"
    "$HOME/OneDrive/Documents/GitHub/airline-sentiment"
    "$HOME/OneDrive/Documents/GitHub/bitcoin"
    "$HOME/OneDrive/Documents/GitHub/caglorithm-notebooks-fork"
    "$HOME/OneDrive/Documents/GitHub/CodingChallenge"
    "$HOME/OneDrive/Documents/GitHub/countryinfo"
    "$HOME/OneDrive/Documents/GitHub/covid19"
    "$HOME/OneDrive/Documents/GitHub/data-science-5k"
    "$HOME/OneDrive/Documents/GitHub/dave-babbitt-technical-assessment"
    "$HOME/OneDrive/Documents/GitHub/glowing-octo-carnival"
    "$HOME/OneDrive/Documents/GitHub/itm-analysis-reporting-1"
    "$HOME/OneDrive/Documents/GitHub/job-hunting"
    "$HOME/OneDrive/Documents/GitHub/joy-plots"
    "$HOME/OneDrive/Documents/GitHub/march-madness"
    "$HOME/OneDrive/Documents/GitHub/mimetic_tribes"
    "$HOME/OneDrive/Documents/GitHub/MineCraft"
    "$HOME/OneDrive/Documents/GitHub/mobile-phone-activity"
    "$HOME/OneDrive/Documents/GitHub/notebooks"
    "$HOME/OneDrive/Documents/GitHub/oscars"
    "$HOME/OneDrive/Documents/GitHub/ramadan-2015"
    "$HOME/OneDrive/Documents/GitHub/rpc"
    "$HOME/OneDrive/Documents/GitHub/Simulations"
    "$HOME/OneDrive/Documents/GitHub/Skills"
    "$HOME/OneDrive/Documents/GitHub/squarify"
    "$HOME/OneDrive/Documents/GitHub/StatsByCountry"
    "$HOME/OneDrive/Documents/GitHub/StatsByUSState"
    "$HOME/OneDrive/Documents/GitHub/Strauss-Howe"
    "$HOME/OneDrive/Documents/GitHub/technical-interview-challenges"
    "$HOME/OneDrive/Documents/GitHub/TensorFlow"
    "$HOME/OneDrive/Documents/GitHub/texas-flooding"
    "$HOME/OneDrive/Documents/GitHub/text-classification"
    "$HOME/OneDrive/Documents/GitHub/transcriptions-notebook"
    "$HOME/OneDrive/Documents/GitHub/Twitter"
    "$HOME/OneDrive/Documents/GitHub/web-scrapers"
    "$HOME/OneDrive/Documents/GitHub/word-cloud"
    "$HOME/OneDrive/Documents/GitHub/Word2Vec"
    "$HOME/OneDrive/Documents/GitHub/Wordle"
)

# Loop through each repositories directory
# echo "Loop through each repositories directory"
for repo in "${REPOS[@]}"; do
    # echo "Checking if the $repo directory contains a .git folder"
    if [ -d "$repo/.git" ]; then
        # echo "Updating repository: $repo"
        cd "$repo" || continue
        
        # Check if the submodule exists
        if [ -d "share" ]; then
            repo_name=$(basename "$repo")
            echo "Updating submodule in repository: $repo_name..."
            git submodule update --remote --merge
        fi
        
    fi
done