#!/bin/bash
# Run this file to build notebook

# activate environment
conda activate MKdocs

# build structure
python utils/build_yml.py
python utils/build_changelog.py

# deploy
mkdocs gh-deploy --clean
