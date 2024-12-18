#!/bin/bash

# Edit the ../.gitignore file to remove lines with "share" in them
# Like "share/python-wheels/". Then, force add the submodule
# cd ~/OneDrive/Documents/GitHub/notebooks
cd ../
git submodule add -f https://github.com/dbabbitt/share.git share

# Commit the changes
git commit -m "Added share submodule"