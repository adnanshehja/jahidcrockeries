# Jahid Crockeries — website

A two-page marketing site for **Jahid Crockeries**, 1 Super "A" Market,
Baitul Mukarram (Ground Floor), Dhaka 1000.

- **Owner:** Md. Jahid Hasan
- **Phone / WhatsApp:** 01400 993386 · 01400 669930 · 01686 753701
- **Email:** jahidcrockeries@gmail.com

> **No prices are shown anywhere on the site.** Dinner sets carry the line
> “32 pcs & 52 pcs available” instead, and every product links straight to
> WhatsApp so the owner can quote the current price himself.

---

## The two pages

| File | What it is | Photos |
| --- | --- | --- |
| `index.html` | **Dinner & Glass** — hero, the full tableware catalogue (dinner sets, tea & coffee, glassware), the Mirana signature showcase, showroom videos, testimonials, story, FAQ, visit/map | 51 |
| `appliances.html` | **Kitchen & Appliances** — hero, “also in store” range strip, the full kitchen catalogue (gas stoves, hoods, small appliances, cookware), service band, visit/map | 27 |

All 78 photographs are split across the two pages — nothing is hidden on a
third page. Both share `styles.css` and `app.js`.

### How the split works

The catalogue table in `tools/build-gallery.py` is the single source of truth.
Each photo has a category, and the category decides which page it lands on:

| Category | Page | Filter button |
| --- | --- | --- |
| `bone` | Dinner & Glass | Dinner Sets |
| `tea` | Dinner & Glass | Tea & Coffee |
| `glass` | Dinner & Glass | Glassware |
| `appliance` | Kitchen & Appliances | Gas Stoves / Hoods / Small Appliances |
| `enamel` | Kitchen & Appliances | Cookware |

Appliances are split into stoves, hoods and small appliances automatically from
the filename (`stove-…`, `franco-hood-…`, everything else is “small”).

---

## Previewing locally

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>. Opening `index.html` directly by
double-clicking also works, but a local server is closer to real hosting.

---

## How to edit

### Adding or changing a photo

1. Drop the photo into the right folder under `images/`
   (`bone-china/`, `glassware/`, `enamelware/`, `appliances/`).
2. Add one row to `CATALOG` in `tools/build-gallery.py`:

```python
("bone-china/new-pattern.jpeg", "bone", "New Pattern",
 "Bone china &middot; gold rim",
 "One or two sentences describing the piece.",
 ""),          # "", "wide" or "tall" for the grid layout
```

3. Regenerate both catalogues:

```bash
python3 tools/build-gallery.py
```

The script rewrites the grid between the `<!-- GRID:…:START -->` and
`<!-- GRID:…:END -->` markers in each page, and prints how many photos went to
each one. **Do not hand-edit inside those markers** — the next build replaces it.

### The Mirana showcase

The large “signature collection” block sits just below the tableware catalogue
on `index.html`. Its two set-size cards are plain HTML — edit the numbers,
headings and copy there.

### Page copy and sections

Everything outside the grid markers is normal HTML. The hero, section headings,
“also in store” list, testimonials, FAQ and visit details are all hand-written
in `index.html` / `appliances.html`.

### Contact links

The WhatsApp number appears as `https://wa.me/8801400993386` and the phone
links as `tel:+8801400993386`. Search-and-replace those two strings to change
the number everywhere (both pages).

---

## Notes for hosting

- The site is fully static — upload the folder to any host (cPanel, Netlify,
  Vercel, GitHub Pages) with `index.html` as the entry point.
- Fonts load from Google Fonts. Everything else is local.
- Total size is about 29 MB: `images/` about 13 MB and `video/` about 15 MB for
  the three clips embedded on the homepage. If the host has a bandwidth limit,
  compress the videos to roughly 720p H.264 (target ~2–3 MB each) and keep the
  same filenames.
- The Google Maps embed on the Visit section needs normal internet access. If
  it is ever blocked, the section falls back to a designed map panel, so it
  still looks finished.
- Two extra clips (`dinner-set-detail.mp4`, `collection-sweep.mp4`) are not used
  on the site and are kept outside this folder, in
  `../jahid crokeries /unused-videos/`.

### Deploying with GitHub + Vercel

1. Push the **contents** of this folder so `index.html` sits at the repository
   root (or set Vercel's **Root Directory** to `jahid-crockeries` if you push
   the parent folder).
2. In Vercel choose **Add New → Project**, import the repo, and leave Framework
   Preset as **Other** — no build command, no output directory.
3. Deploy. `index.html` becomes the home page and `appliances.html` the second
   page; both work as normal `.html` URLs, no rewrites needed.
4. After the first deploy, copy the `*.vercel.app` address into the `og:image`
   tags on both pages as a full URL (`https://…/images/…`). WhatsApp and
   Facebook need an absolute path to show a preview card.

---

## Structure

```
jahid-crockeries/
├── index.html                # Dinner & Glass  (51 photos)
├── appliances.html           # Kitchen & Appliances (27 photos)
├── styles.css
├── app.js                    # shared: nav, reveal, filters, lightbox, FAQ
├── favicon.svg
├── images/
│   ├── bone-china/           # 46 photos
│   ├── glassware/            # 5
│   ├── enamelware/           # 11
│   ├── appliances/           # 16
│   └── brand/                # 1 (owner portrait)
├── video/                    # 3 clips
└── tools/
    └── build-gallery.py      # catalogue table + grid generator
```

---

Designed & developed by **Adnan Shaikh**.
