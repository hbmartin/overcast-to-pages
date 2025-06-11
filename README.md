# overcast-to-pages

## Setup:

1. Use the template button to create your own repository
2. Go to https://overcast.fm/account and open your web inspector (usually command-option-i)
3. Find your login cookie e.g. in Chrome DevTools under Application > Cookies > https://overcast.fm and copy the value for `o`
4. In your new repository, go to ⚙️ Settings tab > [*] Secrets and variables  (sidebar) > Actions > New repository secret
5. Enter the name `OVERCAST_COOKIE` and paste the `o` value from step 3 as the value
6. Click "Add secret"
7. Go to the ▶️ Actions tab > Download latest data (sidebar) > Run workflow (gray button) > Run workflow (popup green button)
