#!/usr/bin/env python3
"""
Template cleanup script for overcast-to-pages GitHub template.
Replaces hardcoded GitHub URLs with the new repository's URLs.
"""

import os
import re
import sys


def get_repo_info():
    """Extract repository owner and name from environment variables."""
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    if not github_repository:
        print("Error: GITHUB_REPOSITORY environment variable not set")
        sys.exit(1)
    
    owner, repo = github_repository.split('/')
    return owner, repo


def update_readme(owner, repo):
    """Update README.md with new repository URLs."""
    readme_path = 'README.md'
    
    if not os.path.exists(readme_path):
        print("Warning: README.md not found")
        return
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Replace hardcoded GitHub URLs
    replacements = [
        # Settings URLs
        (r'https://github\.com/hbmartin/overcast-to-pages/settings/secrets/actions/new',
         f'https://github.com/{owner}/{repo}/settings/secrets/actions/new'),
        (r'https://github\.com/hbmartin/overcast-to-pages/settings/pages',
         f'https://github.com/{owner}/{repo}/settings/pages'),
        
        # Actions URLs
        (r'https://github\.com/hbmartin/overcast-to-pages/actions/workflows/scrape\.yml',
         f'https://github.com/{owner}/{repo}/actions/workflows/scrape.yml'),
        (r'https://github\.com/hbmartin/overcast-to-pages/actions',
         f'https://github.com/{owner}/{repo}/actions'),
        
        # GitHub Pages URL
        (r'https://hbmartin\.github\.io/overcast-to-pages/',
         f'https://{owner}.github.io/{repo}/'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Updated README.md with URLs for {owner}/{repo}")


def main():
    """Main function to run the cleanup."""
    owner, repo = get_repo_info()
    update_readme(owner, repo)
    print("Template cleanup completed successfully!")


if __name__ == '__main__':
    main()