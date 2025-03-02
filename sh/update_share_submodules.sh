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

# Define the maximum message length as a variable
MAX_MESSAGE_LENGTH=79

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

            # Calculate the middle message
            middle_message="Updating submodule in $repo_name repository"

            # Check if the length of the middle message exceeds the maximum length
            if [ ${#middle_message} -gt $MAX_MESSAGE_LENGTH ]; then

                # Truncate the message to the maximum length and prepend with "..."
                middle_message="...${middle_message: -$((MAX_MESSAGE_LENGTH - 3))}"

            fi

            # Calculate the length of the (possibly truncated) middle message
            line_length=${#middle_message}

            # Generate a line of '=' characters with the same length as the middle message
            separator=$(printf '=%.0s' $(seq 1 $line_length))

            # Print the dynamically generated lines and the message
            echo "$separator"
            echo "$middle_message"
            echo "$separator"

            git submodule update --remote --merge
        fi

    fi
done

# Define source and destination paths in Unix-style
SOURCE="$HOME/OneDrive/Documents/GitHub/notebooks/share"
DESTINATION="$HOME/OneDrive/Documents/GitHub/color/share"

# Check if the source folder exists
if [ -d "$SOURCE" ]; then

    # Convert Unix-style paths to Windows-style paths
    WIN_SOURCE=$(cygpath -w "$SOURCE")
    WIN_DESTINATION=$(cygpath -w "$DESTINATION")

    # Extract parent and child directories for readability
    PARENT_SOURCE=$(basename "$(dirname "$SOURCE")")/$(basename "$SOURCE")
    PARENT_DESTINATION=$(basename "$(dirname "$DESTINATION")")/$(basename "$DESTINATION")

    # Calculate the middle message
    middle_message="Copying $PARENT_SOURCE to $PARENT_DESTINATION"

    # Calculate the length of the middle message
    line_length=${#middle_message}

    # Generate a line of '=' characters with the same length as the middle message
    separator=$(printf '=%.0s' $(seq 1 $line_length))

    # Print the dynamically generated lines and the message
    echo "$separator"
    echo "$middle_message"
    echo "$separator"

    # Copy the folder, overriding any existing content in the destination
    # robocopy "$WIN_SOURCE" "$WIN_DESTINATION" /NFL /NDL /NS /NC /NJH /NJS  # ERROR : Invalid Parameter #3 : "C:/Program Files/Git/NFL"
    robocopy $WIN_SOURCE $WIN_DESTINATION
    echo "Copy completed successfully."

else
    echo "Source folder $SOURCE does not exist. Skipping copy."
fi