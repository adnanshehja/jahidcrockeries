#!/usr/bin/env python3
"""Build collections.html for Jahid Crockeries from a single catalog table."""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = "images"

# (file, category, title, meta, description, layout)
# layout: "" normal | "wide" | "tall"
CATALOG = [
    # ---------------- BONE CHINA: DINNER SETS ----------------
    ("bone-china/mirana.jpeg", "bone", "Mirana",
     "Bone china &middot; 24-carat gold",
     "Sculpted Grandeur — a classical ornament service in white porcelain with 24-carat gold detailing. Available in 32 and 52-piece sets.",
     "wide"),
    ("bone-china/teal-marble.jpeg", "bone", "Ocean Marble",
     "Bone china &middot; gold rim",
     "Deep teal, emerald and gold swirled like polished marble. Our most dramatic service — made for a table that wants to be remembered.",
     "tall"),
    ("bone-china/noir-botanical.jpeg", "bone", "Noir Botanical",
     "Bone china &middot; gold rim",
     "Ink-black botanical illustration on bright white bone china, edged in gold. Graphic, modern and quietly luxurious.",
     "tall"),
    ("bone-china/china-marble.jpeg", "bone", "Midnight Marble",
     "Bone china &middot; gold rim",
     "Ink blue, teal and gold marbling across a complete dinner service. Rich, moody and unmistakably special.",
     ""),
    ("bone-china/royal-rose.jpeg", "bone", "Royal Rose",
     "Bone china &middot; classic floral",
     "The classic country rose — full blooms in warm pink and gold on ivory bone china. A traditional service for Eid and everyday.",
     "wide"),
    ("bone-china/poppy-gold.jpeg", "bone", "Poppy Gold",
     "Bone china &middot; gold border",
     "Warm amber poppies and soft gold leaves on a cream ground. A generous, sunny pattern that suits family lunches and festival tables.",
     ""),
    ("bone-china/meadow-bloom.jpeg", "bone", "Meadow Bloom",
     "Bone china &middot; gold rim",
     "Cornflowers, buttercups and trailing stems in blue, yellow and lilac. A fresh, English-garden service for tea and dessert.",
     ""),
    ("bone-china/ivory-vine-square.jpeg", "bone", "Ivory Vine",
     "Bone china &middot; square service",
     "Delicate gold vine scrollwork on square ivory plates with softly curved corners. Understated and elegant.",
     ""),
    ("bone-china/ivory-gold-rim.jpeg", "bone", "Ivory Gold Rim",
     "Bone china &middot; scalloped edge",
     "Pure ivory porcelain with a fine gold rim and a softly scalloped edge. The quietest kind of luxury.",
     ""),
    ("bone-china/cream-lattice.jpeg", "bone", "Cream Lattice",
     "Bone china &middot; gold lattice",
     "A fine gold lattice across cream porcelain. Light, refined and beautiful with white linen.",
     ""),
    ("bone-china/gold-band.jpeg", "bone", "Gold Band",
     "Bone china &middot; wide gold band",
     "A generous band of polished gold on pure white. Formal, festive and timeless.",
     ""),
    ("bone-china/gold-leaf.jpeg", "bone", "Gold Leaf",
     "Bone china &middot; gold foliage",
     "Trailing gold leaves scattered across white porcelain. Delicate detail that catches the light.",
     ""),
    ("bone-china/white-gold-scallop.jpeg", "bone", "White Gold Scallop",
     "Bone china &middot; gold edge",
     "Clean white porcelain finished with a slender gold edge and a sculpted rim.",
     ""),
    ("bone-china/gold-filigree-band.jpeg", "bone", "Gold Filigree",
     "Bone china &middot; 24-carat gold band",
     "A wide band of ornate gold filigree on pure white porcelain. The set you bring out when the table matters.",
     ""),
    ("bone-china/lilac-marble.jpeg", "bone", "Lilac Marble",
     "Bone china &middot; soft veining",
     "Soft lilac and sand marble veining with a fine gold edge. Gentle, contemporary and easy to live with.",
     ""),
    ("bone-china/orange-scroll.jpeg", "bone", "Orange Scroll",
     "Bone china &middot; gold scrollwork",
     "Amber florals framed by warm gold scrollwork on ivory. A rich, traditional service.",
     ""),
    ("bone-china/ivory-lace.jpeg", "bone", "Ivory Lace",
     "Bone china &middot; gold line",
     "Fine gold pinstripes and a textured band on ivory porcelain. Minimal, warm and very wearable.",
     ""),
    ("bone-china/blue-bloom.jpeg", "bone", "Blue Bloom",
     "Bone china &middot; hand-painted blue",
     "Cobalt blue blossoms on white, with a fine gold edge. A crisp, classic service.",
     ""),
    ("bone-china/china-gold-damask.jpeg", "bone", "Gilded Damask",
     "Bone china &middot; gold damask",
     "A classic gold damask border on bright white bone china, finished with a fine gold rim.",
     ""),
    ("bone-china/china-piano.jpeg", "bone", "Grand Piano",
     "Bone china &middot; gold rim",
     "A playful piano-key motif with a fine gold rim — a set for music lovers and modern tables alike.",
     ""),
    ("bone-china/china-azure.jpeg", "bone", "Azure Wave",
     "Bone china &middot; gold line",
     "Turquoise brushstrokes crossed with slender gold lines. Fresh and contemporary.",
     ""),
    ("bone-china/china-lilac.jpeg", "bone", "Lilac Bloom",
     "Bone china &middot; gold edging",
     "Purple bellflowers and fine gold edging on a soft ivory ground. Romantic without being fussy.",
     ""),
    ("bone-china/china-gilded-vine.jpeg", "bone", "Gilded Vine",
     "Bone china &middot; gold scroll",
     "Delicate gold vine scrollwork with warm copper accents. Understated and versatile.",
     ""),
    ("bone-china/china-rose.jpeg", "bone", "Rose Garden",
     "Bone china &middot; gold edge",
     "Blush roses, soft green leaves and a warm gold edge. A gentle, traditional service.",
     ""),
    ("bone-china/china-sahara.jpeg", "bone", "Sahara Gold",
     "Bone china &middot; sand floral",
     "A warm sand-toned floral border with gold detailing. Complete with plates, bowls, cups and saucers.",
     ""),
    ("bone-china/china-gold-square.jpeg", "bone", "Gold Square",
     "Bone china &middot; square plates",
     "Square plates with a bold gold border. Modern geometry with a formal finish.",
     ""),
    ("bone-china/china-white-gold.jpeg", "bone", "White &amp; Gold",
     "Bone china &middot; gold rim",
     "Crisp white porcelain with a clean gold rim — the essential service for any table.",
     ""),
    ("bone-china/rose-leaf-marble.jpeg", "bone", "Rose Leaf Marble",
     "Bone china &middot; pastel veining",
     "Pink and sage leaf veining across white porcelain. Soft, organic and unusual.",
     ""),
    ("bone-china/china-floral-shelf.jpeg", "bone", "Floral Shelf",
     "Bone china &middot; showroom",
     "A shelf of fine floral services in store — each pattern available as a complete set.",
     ""),
    ("bone-china/display-shelf-01.jpeg", "bone", "The Shelf",
     "Bone china &middot; showroom",
     "A full view of our dinner-set wall: gold rims, botanicals, dotted cream and classic checks.",
     "wide"),
    ("bone-china/display-shelf-02.jpeg", "bone", "Three Shelves",
     "Bone china &middot; showroom",
     "White, swirl and scroll patterns displayed across three shelves in the showroom.",
     ""),
    ("bone-china/noir-botanical-2.jpeg", "bone", "Noir Botanical &middot; Detail",
     "Bone china &middot; gold rim",
     "A closer look at the Noir Botanical service — hand-drawn foliage, gold handles and a sculpted tureen.",
     ""),
    ("bone-china/pink-magnolia.jpeg", "bone", "Pink Magnolia",
     "Bone china &middot; gold rim",
     "Blush magnolia branches on bright white bone china, every plate finished with a fine gold rim. A complete service with cups, saucers and serving bowls.",
     "wide"),
    ("bone-china/charcoal-leaf.jpeg", "bone", "Charcoal Leaf",
     "Bone china &middot; grey leaf",
     "Hand-drawn charcoal leaves on white porcelain with a soft grey-green rim. Botanical, graphic and very modern.",
     ""),
    ("bone-china/gold-starburst.jpeg", "bone", "Gold Starburst",
     "Bone china &middot; gold starburst",
     "Fine gold and taupe starbursts scattered across white porcelain, crossed by slender gold lines and a polished gold rim.",
     ""),
    ("bone-china/gold-starburst-2.jpeg", "bone", "Gold Starburst &middot; Detail",
     "Bone china &middot; gold starburst",
     "A second look at the starburst service — three plates and a tall gold-rimmed cup, photographed against black.",
     ""),
    ("bone-china/diamond-dots.jpeg", "bone", "Diamond Dots",
     "Bone china &middot; coloured studs",
     "Pure white plates and a gold-rimmed cup, each marked with a single column of small coloured diamond studs. Minimal and precise.",
     ""),
    ("bone-china/cobalt-feather.jpeg", "bone", "Cobalt Feather",
     "Bone china &middot; cobalt blue",
     "Cobalt feather plumes on fine grey stems across white porcelain. Cups, saucers and a full stack of dinner plates.",
     ""),

    # ---------------- TEA & COFFEE ----------------
    ("bone-china/tea-set-pastel-floral.jpeg", "tea", "Pastel Floral Tea Set",
     "Tea &amp; coffee &middot; 4 colours",
     "Pale yellow, white, blush and mint cups and saucers with soft floral medallions.",
     "wide"),
    ("bone-china/pastel-garden.jpeg", "tea", "Pastel Garden",
     "Tea &amp; coffee &middot; gold rim",
     "Delicate pastel cups with trailing florals and a fine gold rim.",
     ""),
    ("bone-china/pastel-bloom.jpeg", "tea", "Pastel Bloom",
     "Tea &amp; coffee &middot; 4 colours",
     "A quartet of pastel services — white, mint, cream and lilac — each with a floral centre.",
     ""),
    ("bone-china/pastel-cups.jpeg", "tea", "Pastel Cups",
     "Tea &amp; coffee &middot; floral",
     "Softly coloured cups and saucers with hand-painted blooms and gold rims.",
     ""),
    ("bone-china/pastel-trio.jpeg", "tea", "Pastel Trio",
     "Tea &amp; coffee &middot; mint, cream, white",
     "Three pastel services side by side — mint, cream and white — with fine gold edges.",
     ""),
    ("bone-china/gold-leaf-cups.jpeg", "tea", "Gold Leaf Cups",
     "Tea &amp; coffee &middot; gold foliage",
     "Teacups scattered with gold leaves, finished with a gold rim and handle.",
     ""),
    ("bone-china/white-gold-handle.jpeg", "tea", "White &amp; Gold Handle",
     "Tea &amp; coffee &middot; gold handle",
     "Pure white cups with a sculpted gold handle and a fine gold rim.",
     ""),
    ("bone-china/vintage-lace.jpeg", "tea", "Vintage Lace",
     "Tea &amp; coffee &middot; lace border",
     "A fine lace border in warm grey and gold on white porcelain. Quietly vintage.",
     ""),

    # ---------------- GLASSWARE ----------------
    ("glassware/gold-rim-tumblers.jpeg", "glass", "Gold Rim Tumblers",
     "Hammered glass &middot; set of six",
     "Six hammered-glass tumblers with a polished gold rim. Weighty in the hand and lovely for a toast.",
     "wide"),
    ("glassware/dispenser-clear.jpeg", "glass", "Crystal Dispenser",
     "Cut crystal &middot; chrome tap",
     "A cut-crystal drinks dispenser with a polished chrome tap and faceted lid.",
     ""),
    ("glassware/dispenser-amber.jpeg", "glass", "Amber Dispenser",
     "Cut crystal &middot; gold tap",
     "Amber-tinted cut glass with a gold-finish tap. Warm and vintage-inspired.",
     ""),
    ("glassware/dispenser-ribbed.jpeg", "glass", "Ribbed Dispenser",
     "Cut crystal &middot; ribbed",
     "A ribbed crystal dispenser with a bright chrome tap — clean and contemporary.",
     ""),
    ("glassware/glassware-wall.jpeg", "glass", "The Glass Wall",
     "Crystal &middot; showroom",
     "Our wall of cut crystal — glasses, cups, jugs and serving dishes.",
     "wide"),

    # ---------------- ENAMELWARE ----------------
    ("enamelware/enamel-pots-floral.jpeg", "enamel", "Floral Enamel Set",
     "Enamelled steel &middot; gold trim",
     "Enamelled steel pots with a hand-painted floral design and gold-finish handles.",
     "tall"),
    ("enamelware/enamel-pots-rose.jpeg", "enamel", "Rose &amp; Bird Set",
     "Enamelled steel &middot; gold trim",
     "Roses and garden birds on a creamy enamel ground, finished with gold rims and handles.",
     ""),
    ("enamelware/enamel-kettle-hand.jpeg", "enamel", "Enamel Kettle",
     "Enamelled steel &middot; gold handle",
     "A garden-floral enamel kettle with a gold-finish handle and lid.",
     ""),
    ("enamelware/enamel-set-red.jpeg", "enamel", "Red Casserole Set",
     "Enamelled steel &middot; three sizes",
     "A bright three-piece casserole set with deep red lids and a cheerful floral body.",
     ""),
    ("enamelware/enamel-pots-teal.jpeg", "enamel", "Teal Enamel Pots",
     "Enamelled steel &middot; gold trim",
     "Teal enamel pots with a gold rim and handle — a fresh take on a classic.",
     ""),
    ("enamelware/enamel-pots-blue.jpeg", "enamel", "Blue Enamel Pots",
     "Enamelled steel &middot; gold trim",
     "Cobalt blue enamel with gold detailing. Bold on the stove and on the table.",
     ""),
    ("enamelware/enamel-pots-red.jpeg", "enamel", "Red Enamel Pots",
     "Enamelled steel &middot; gold trim",
     "Warm red enamel pots with gold rims and handles.",
     ""),
    ("enamelware/enamel-pots-birds.jpeg", "enamel", "Bird Enamel Pots",
     "Enamelled steel &middot; gold trim",
     "Garden birds and blossom on a cream enamel ground with gold trim.",
     ""),
    ("enamelware/storage-bowls.jpeg", "enamel", "Storage Bowls",
     "Enamel &middot; set of six",
     "Stacking storage bowls with lids in a classic floral print.",
     ""),
    ("enamelware/storage-bowls-floral.jpeg", "enamel", "Floral Storage Bowls",
     "Enamel &middot; set of six",
     "Two stacks of floral storage bowls with snug lids — practical and pretty.",
     "wide"),
    ("enamelware/cookware-shop.jpeg", "enamel", "The Cookware Wall",
     "Enamel &middot; showroom",
     "Our cookware display — enamel pots, casseroles, kettles and storage.",
     ""),

    # ---------------- APPLIANCES ----------------
    ("appliances/stove-endure.jpeg", "appliance", "Endure Gas Stove",
     "Stainless steel &middot; two burner",
     "A stainless steel two-burner hob with gold-tone burners and a tempered glass top.",
     "wide"),
    ("appliances/stove-miyako-lorenzo.jpeg", "appliance", "Miyako Lorenzo",
     "Granite finish &middot; two burner",
     "Miyako Lorenzo two-burner gas stove in a granite finish with cast-iron pan supports.",
     ""),
    ("appliances/stove-miyako-monica.jpeg", "appliance", "Miyako Monica",
     "Glass top &middot; two burner",
     "Miyako Monica two-burner stove with a tempered glass surface and auto-ignition.",
     ""),
    ("appliances/stove-miyako-grey.jpeg", "appliance", "Miyako Grey",
     "Matte grey &middot; two burner",
     "A matte grey two-burner stove with a clean, modern profile.",
     ""),
    ("appliances/stove-franco.jpeg", "appliance", "Franco Gas Stove",
     "Stainless steel &middot; two burner",
     "Franco two-burner stove in stainless steel with a spill-proof design.",
     ""),
    ("appliances/franco-hood-lexus.png", "appliance", "Franco Lexus 5G Hood",
     "Range hood &middot; touch control",
     "Franco Lexus 5G range hood with touch controls and powerful suction.",
     "tall"),
    ("appliances/franco-hood-volvo.jpg", "appliance", "Franco Volvo Hood",
     "Range hood &middot; black",
     "Franco Volvo range hood in black with a slim, modern canopy.",
     ""),
    ("appliances/franco-stove-black.jpg", "appliance", "Franco Black Stove",
     "Glass top &middot; two burner",
     "Franco two-burner stove with a black glass surface and gold-tone knobs.",
     ""),
    ("appliances/franco-stove-flame.jpg", "appliance", "Franco Flame",
     "Gas stove &middot; two burner",
     "Franco two-burner stove shown with a live flame — strong, even heat.",
     ""),
    ("appliances/franco-stove-gloss.jpg", "appliance", "Franco Gloss",
     "Gloss finish &middot; two burner",
     "A gloss-finish Franco stove with a tempered glass top.",
     ""),
    ("appliances/franco-stove-gold.jpg", "appliance", "Franco Gold",
     "Gold trim &middot; two burner",
     "Franco two-burner stove with warm gold trim and a stainless body.",
     ""),
    ("appliances/franco-stove-steel.jpg", "appliance", "Franco Steel",
     "Stainless steel &middot; two burner",
     "Franco stove in brushed stainless steel with cast-iron supports.",
     ""),
    ("appliances/appliance-panasonic-mixer.jpeg", "appliance", "Panasonic Mixer Grinder",
     "Panasonic &middot; MX-GC3550",
     "Panasonic MX-GC3550 super mixer grinder with three jars.",
     ""),
    ("appliances/appliance-airfryer.jpeg", "appliance", "Jamaky Air Fryer",
     "Jamaky &middot; 8 litre",
     "Jamaky 8-litre air fryer with a visual window and digital controls.",
     ""),
    ("appliances/appliance-induction-niyama.jpeg", "appliance", "Niyama Induction Cooker",
     "Induction &middot; 2000W",
     "Niyama induction cooker with a crystal glass top and touch panel.",
     ""),
    ("appliances/appliance-induction-nova.jpeg", "appliance", "Nova Infrared Cooker",
     "Infrared &middot; 2000W",
     "Nova infrared cooker — fast, clean cooking with any flat-bottomed pot.",
     ""),
]

# ---------------------------------------------------------------------------
# The catalogue is split across the site's two pages.
# ---------------------------------------------------------------------------
TABLEWARE_CATS = ("bone", "tea", "glass")
KITCHEN_CATS = ("appliance", "enamel")


def group_for(item):
    """The filter bucket an item lands in on the kitchen page."""
    path, cat, title, meta, desc, layout = item
    if cat == "enamel":
        return "cookware"
    low = path.lower()
    if "hood" in low:
        return "hood"
    if "stove" in low:
        return "stove"
    return "small"


def esc(s):
    return html.escape(s, quote=True)


def plain(s):
    """Turn the &middot; / &amp; entities used in CATALOG into real characters."""
    return html.unescape(s)


def attr(s):
    """Attribute-safe text: decode the entities we wrote, then escape once."""
    return html.escape(plain(s), quote=True)


def card(item, group=None):
    path, cat, title, meta, desc, layout = item
    bucket = group or cat
    cls = "g-item"
    if layout == "wide":
        cls += " g-item--wide"
    elif layout == "tall":
        cls += " g-item--tall"
    alt = attr(f"{plain(title).replace('&', 'and')} — {plain(meta).replace('·', '-')} — Jahid Crockeries")
    sizes = "32 pcs &amp; 52 pcs available" if cat == "bone" else ""
    sizes_line = (
        f'\n          <span class="g-item__sizes">{sizes}</span>' if sizes else ""
    )
    return f'''      <button class="{cls}" type="button" data-cat="{bucket}"
        data-title="{attr(title)}" data-meta="{attr(meta)}" data-desc="{attr(desc)}"
        data-sizes="{sizes}" data-image="{IMG}/{path}" aria-label="View {attr(title)}">
        <img src="{IMG}/{path}" alt="{alt}" loading="lazy">
        <span class="g-item__cap"><strong>{title}</strong><span>{meta}</span>{sizes_line}
        </span>
      </button>'''


def inject(page, name, grid_html):
    start = f"<!-- GRID:{name}:START -->"
    end = f"<!-- GRID:{name}:END -->"
    if start not in page or end not in page:
        raise SystemExit(f"missing {name} markers — add {start} … {end}")
    head, rest = page.split(start, 1)
    _, tail = rest.split(end, 1)
    return head + start + "\n" + grid_html + "\n      " + end + tail


def main():
    tableware = [i for i in CATALOG if i[1] in TABLEWARE_CATS]
    kitchen = [i for i in CATALOG if i[1] in KITCHEN_CATS]

    # Lead the kitchen page with stoves and hoods, then small appliances,
    # then cookware — matching the order the hero promises.
    kitchen_order = ["stove", "hood", "small", "cookware"]
    kitchen.sort(key=lambda i: kitchen_order.index(group_for(i)))

    root = Path(__file__).resolve().parent.parent
    pages = {
        "index.html": ("TABLEWARE", tableware, None),
        "appliances.html": ("KITCHEN", kitchen, group_for),
    }

    for name, (marker, items, grouper) in pages.items():
        path = root / name
        if not path.exists():
            print(f"skip {name} (not created yet)")
            continue
        grid = "\n".join(card(i, grouper(i) if grouper else None) for i in items)
        path.write_text(inject(path.read_text(encoding="utf-8"), marker, grid), encoding="utf-8")
        print(f"{name}: {len(items)} photos")

    print(f"tableware {len(tableware)} + kitchen {len(kitchen)} = {len(CATALOG)}")


if __name__ == "__main__":
    main()
