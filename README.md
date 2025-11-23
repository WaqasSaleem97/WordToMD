# Instructions

1. Create directories in your repository:
   - .github/workflows/
   - .github/scripts/

2. Copy the following files (preserving their paths) into your repository's .github directory:
   - .github/workflows/word-to-md.yml
   - .github/scripts/fix_md_images.py
   - .github/scripts/fix_pandoc_ast.py

<img width="1877" height="921" alt="image" src="https://github.com/user-attachments/assets/e585ec33-5f9c-44fd-ac38-02253792e735" />

   Ensure the directory structure in the repo matches the paths above so the workflow can find the scripts.

3. Generate a Personal Access Token (classic) with the required scopes:
   - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token.
<img width="1263" height="902" alt="image" src="https://github.com/user-attachments/assets/49435ad2-9a42-4d00-aa65-021a38b098d2" />
   - Give it an expiration and a descriptive name.
   - Select the following scopes at minimum:
     - repo
     - workflow
<img width="1421" height="922" alt="image" src="https://github.com/user-attachments/assets/328dc305-3fc1-4241-96c0-edd49389300d" />
   - Click Generate and copy the token now (you will not be able to view it again).
<img width="983" height="398" alt="image" src="https://github.com/user-attachments/assets/bf255ca1-385e-4150-a63b-2d508fe390e1" />

4. Save the token as a repository Actions secret (do NOT commit the token into the repository):
<img width="1150" height="218" alt="image" src="https://github.com/user-attachments/assets/354457e0-2220-4114-b57d-3ddc288653b2" />
   - Go to your repository → Settings → Secrets and variables → Actions → New repository secret.   
   - Name the secret: `GH_PAT`
   - Paste the token value and save.
<img width="1430" height="907" alt="image" src="https://github.com/user-attachments/assets/657a7f19-34f1-4791-ae85-e878b1258bef" />

Important security notes:
- Never commit the PAT into the repository files. Store it only as a repository secret.
- Restrict the token scopes and set an expiration. Revoke the token when no longer needed.
