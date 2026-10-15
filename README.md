# Personal academic website

Built with [al-folio](https://github.com/alshedivat/al-folio) (Jekyll) and hosted for free on GitHub Pages.
Every push to `main` rebuilds and redeploys the site automatically (see `.github/workflows/deploy.yml`).

## How it is organised

| You want to…                     | Edit this                                                  |
| -------------------------------- | ---------------------------------------------------------- |
| Change your bio / photo          | `_pages/about.md`, `assets/img/prof_pic.jpg`               |
| Add or edit a paper              | `_bibliography/papers.bib` (one BibTeX entry per paper)    |
| Post a news item                 | add a file to `_news/` (copy an existing one)              |
| Update your CV                   | replace `assets/pdf/cv.pdf`; optionally `_data/cv.yml`     |
| Add a project card               | add a file to `_projects/` (copy `1_example_project.md`)   |
| List a GitHub repo on /software/ | `_data/repositories.yml`                                   |
| Add a course to /teaching/       | add a file to `_teachings/` (copy `example-course.md`)     |
| Add a mentor / collaborator      | `_data/people.yml` (photo optional, under `assets/img/people/`) |
| Add work experience / education  | `_data/cv.yml` → `Experience:` / `Education:` — fields `summary` (home timeline), `logo`, `abbr`, `placeholder: true` (hide from home) |
| Interests / skills on the home page | `_data/cv.yml` → `Interests:` / `Skills:`                |
| Change links / email             | `_data/socials.yml`                                        |
| Site title, name, URL, features  | `_config.yml` (top of the file)                            |

Everything is plain text. Edit on GitHub.com directly, or clone and edit locally — the site rebuilds on push either way.

## Dashboard (no file editing needed)

Open **`https://<username>.github.io/admin/`**. It has forms for news, papers, projects, people, experience/education, courses, your bio, and CV/photo uploads. Each submit makes one commit to this repo through GitHub's API, and the site rebuilds itself.

One-time setup: create a **fine-grained personal access token** (GitHub → Settings → Developer settings → Personal access tokens → Fine-grained) scoped to *this repository only* with **Contents: Read and write**, paste it into the dashboard's Setup tab and click *Test & save*. The token stays in that browser's local storage; anyone who has it can commit to this repo, so treat it like a password and use *Forget token* on shared machines. The dashboard page itself is public but does nothing without a token.

## Paper entries

Add any of these fields to a BibTeX entry to get buttons and badges on the publications page:

```
abbr        = {NeurIPS}            venue badge; colour/link in _data/venues.yml
selected    = {true}               show on the home page
bibtex_show = {true}               "BIB" button
pdf         = {paper.pdf}          file in assets/pdf/ or a full URL
arxiv       = {2401.01234}         arXiv ID
code        = {https://github.com/you/repo}
website / poster / slides / video / supp = {URL or file}
preview     = {paper.png}          thumbnail in assets/img/publication_preview/
award       = {Oral}               ribbon on the entry
doi         = {10.1000/xyz}
```

For a preprint, use `@misc` with `journal = {arXiv preprint}` or add `note = {Under review}`.

## First-time GitHub Pages setup (one time only)

1. Push this repo to `https://github.com/<username>/<username>.github.io`.
2. Wait for the **Deploy site** workflow under the **Actions** tab to finish (~2–3 min). It creates a `gh-pages` branch — never edit that branch.
3. **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)`** → Save.
4. The site is live at `https://<username>.github.io` a minute later.

### Custom domain (optional)

1. Buy a domain (GitHub Student Developer Pack includes a free one for a year).
2. At your registrar, add a `CNAME` record for `www` pointing to `<username>.github.io`, plus the four GitHub `A` records for the apex domain (listed in GitHub's Pages docs).
3. **Settings → Pages → Custom domain** → enter it, tick **Enforce HTTPS**.
4. In `_config.yml`, set `url:` to `https://yourdomain.com`.

## Preview locally (optional)

Easiest: open the repo in a **GitHub Codespace** (green Code button → Codespaces) — the dev container has Ruby set up; run `bundle install && bundle exec jekyll serve` and open the forwarded port.

With Docker on your machine: `docker compose up` then open <http://localhost:8080>.

## Adding a blog later

Create a `_posts/` folder with files named `YYYY-MM-DD-title.md`, add a `_pages/blog.md` from the al-folio template, and set `latest_posts.enabled: true` in `_pages/about.md`.

## Credits

Theme: [al-folio](https://github.com/alshedivat/al-folio), MIT License (see `LICENSE`).
