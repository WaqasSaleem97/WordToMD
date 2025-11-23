# Instructions

1. Create directories in your repository:
   - .github/workflows/
   - .github/scripts/

2. Copy the following files (preserving their paths) into your repository's .github directory:
   - .github/workflows/word-to-md.yml
   - .github/scripts/fix_md_images.py
   - .github/scripts/fix_pandoc_ast.py

   Ensure the directory structure in the repo matches the paths above so the workflow can find the scripts.

3. Generate a Personal Access Token (classic) with the required scopes:
   - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token.
   - Give it an expiration and a descriptive name.
   - Select the following scopes at minimum:
     - repo
     - workflow
   - Click Generate and copy the token now (you will not be able to view it again).

4. Save the token as a repository Actions secret (do NOT commit the token into the repository):
   - Go to your repository → Settings → Secrets and variables → Actions → New repository secret.
   - Name the secret: `GH_PAT`
   - Paste the token value and save.

Important security notes:
- Never commit the PAT into the repository files. Store it only as a repository secret.
- Restrict the token scopes and set an expiration. Revoke the token when no longer needed.
