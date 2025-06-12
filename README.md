# Overcast to Pages

A web app that syncs your Overcast listening history to automatically create a personal episodes page. It displays all the episodes you've listened to in a clean, searchable interface.

## Setup:

1. [Fork this repository](https://github.com/hbmartin/overcast-to-pages/fork).
2. Go to [https://overcast.fm/account](https://overcast.fm/account) and open your web inspector (usually ⌘-option-i)
3. Find your login cookie and copy the value for `o`
   1. e.g. in Chrome under `Application` > `Cookies` > `https://overcast.fm` 

4. [Add an action repository secret](https://github.com/hbmartin/overcast-to-pages/settings/secrets/actions/new)
5. Enter Name: `OVERCAST_COOKIE` and Secret: paste the `o` value from step #3
6. Click the green button `Add secret`
7. Go to [Pages Settings](https://github.com/hbmartin/overcast-to-pages/settings/pages) > `Source` (dropdown) > Choose `GitHub Actions`
8. Start your first [scrape run](https://github.com/hbmartin/overcast-to-pages/actions/workflows/scrape.yml) > `Run workflow` (gray button) > `Run workflow` (popup green button)
9. After the `scrape` and `pages` workflow runs successfully complete ([watch them here](https://github.com/hbmartin/overcast-to-pages/actions)), your episodes page will be at [https://hbmartin.github.io/overcast-to-pages/](https://hbmartin.github.io/overcast-to-pages/)

Hooray! 🎉 Your episodes page and will now continue to update daily.

You can also [interact with your podcast database directly using datasette](https://lite.datasette.io/?install=datasette-mp3-audio&url=https://hbmartin.github.io/overcast-to-pages/overcast.db#/overcast/)

## Legal

This project is licensed under the [Apache License Version 2.0](LICENSE.txt).

Overcast and the Overcast logo are trademarks of Overcast.fm.

All podcast content is copyright of their respective owners.

## Authors

* [Harold Martin](https://www.linkedin.com/in/harold-martin-98526971/) - harold.martin at gmail
