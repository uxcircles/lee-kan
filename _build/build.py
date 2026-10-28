"""Build the Lee & Kan concept site.

    python3 _build/build.py

Writes index.html, services.html, fees.html, team.html and contact.html into
the repo root. Only needs Python 3.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OFFICIAL = "https://www.lee-kan.com/"
PHONE = "020 7287 8888"
TEL = "tel:+442072878888"
EMAIL = "info@lee-kan.com"
SRA_NO = "605819"
PDF = OFFICIAL  # policy PDFs stay on the official site


# ---------------------------------------------------------------- icons
def icon(name, cls="ic"):
    paths = {
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "ext": '<path d="M7 17 17 7M9 7h8v8"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "close": '<path d="M6 6l12 12M18 6 6 18"/>',
        "pound": '<path d="M17 20H7c2-1.5 3-3.5 3-6V8.5A3.5 3.5 0 0 1 16.5 7"/><path d="M6.5 13h8"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "hand": '<path d="M7 11V6.5a1.5 1.5 0 0 1 3 0V11M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V5.5a1.5 1.5 0 0 1 3 0V11M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-.5a6.5 6.5 0 0 1-5.3-2.7L3.6 14.6a1.6 1.6 0 0 1 2.5-2L7 13.6"/>',
        "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
        "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
        "train": '<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M8 20l-2 2M16 20l2 2M9 16v.01M15 16v.01"/>',
    }
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')


BRAND_MARK = (
    '<svg class="brand-mark" viewBox="0 0 48 48" fill="none" aria-hidden="true">'
    '<rect x="1.5" y="1.5" width="45" height="45" rx="2" stroke="currentColor" stroke-width="1.4"/>'
    '<rect x="5" y="5" width="38" height="38" rx="1" stroke="currentColor" stroke-width=".7" opacity=".55"/>'
    '<text x="24" y="31.5" text-anchor="middle" font-family="Source Serif 4, Georgia, serif" font-size="17" '
    'font-weight="500" fill="currentColor">L<tspan font-style="italic" fill="#a8813f">&amp;</tspan>K</text>'
    '</svg>'
)

NAV = [
    ("services.html", "Services"),
    ("fees.html", "Prices"),
    ("team.html", "Our team"),
    ("contact.html", "Contact"),
]


def brand():
    return (f'<a class="brand" href="index.html" aria-label="Lee &amp; Kan Solicitors, home">{BRAND_MARK}'
            '<span class="brand-text"><span class="brand-name">Lee <span>&amp;</span> Kan</span>'
            '<span class="brand-sub">Solicitors · Soho</span></span></a>')


def layout(page, title, description, body):
    current = ' aria-current="page"'
    nav = "\n".join(
        f'<a href="{href}"{current if href == page else ""}>{label}</a>' for href, label in NAV
    )
    return f"""<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0b2f35">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400;1,8..60,500&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">Concept</span><span class="concept-long">Concept redesign. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official Lee &amp; Kan Solicitors website</a>.</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">Designed by </span><strong>UX CIRCLES</strong> {icon("ext", "ic-ext")}</a>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    {brand()}
    <nav class="nav" id="site-nav" aria-label="Main">
      {nav}
      <div class="nav-extra">
        <a class="nav-phone" href="{TEL}">{icon("phone")}<span>{PHONE}</span></a>
        <a class="btn btn-primary" href="contact.html#enquiry">Get a quote</a>
      </div>
    </nav>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{icon("menu", "ic-open")}{icon("close", "ic-close")}</button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {brand()}
        <p>Solicitors on Lexington Street, Soho, advising individuals, families and businesses on property, company, immigration, private client and dispute matters.</p>
      </div>
      <div>
        <p class="footer-h">Visit</p>
        <address>4th Floor, 36 Lexington Street<br>London W1F 0LJ<br>DX 44725 Soho Square</address>
      </div>
      <div>
        <p class="footer-h">Contact</p>
        <ul>
          <li><a href="{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="contact.html#enquiry">Send an enquiry</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-h">Policies</p>
        <ul>
          <li><a href="fees.html">Prices &amp; service information</a></li>
          <li><a href="{PDF}Complaints.pdf" target="_blank" rel="noopener">Complaints policy</a></li>
          <li><a href="{PDF}LKPrivacy.pdf" target="_blank" rel="noopener">Privacy policy</a></li>
          <li><a href="{PDF}Data.pdf" target="_blank" rel="noopener">Data protection</a></li>
          <li><a href="{PDF}LKDiversity.pdf" target="_blank" rel="noopener">Diversity statistics</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <div>
        <p>Lee &amp; Kan Solicitors is authorised and regulated by the Solicitors Regulation Authority, SRA No. {SRA_NO}.</p>
        <p>&copy; Lee &amp; Kan Solicitors. Concept redesign by <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a>.</p>
      </div>
      <div class="sra-badge"><div><div><iframe frameborder="0" scrolling="no" allowTransparency="true" src="https://cdn.yoshki.com/iframe/55847r.html" title="SRA digital badge"></iframe></div></div></div>
    </div>
  </div>
</footer>
<div class="mobile-cta">
  <a class="btn btn-ghost" href="{TEL}">{icon("phone")} Call us</a>
  <a class="btn btn-primary" href="contact.html#enquiry">Get a quote</a>
</div>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- content
AREAS = [
    ("residential", "Residential Property",
     "Buying, selling, letting, remortgaging, party wall and lease matters, whether it is your first home or an investment.",
     ["Freehold and leasehold purchases and sales", "Remortgages", "Letting, and buying to invest",
      "Party wall and lease disputes"],
     "From <strong>£1,800</strong> + VAT", "fees.html#freehold"),
    ("commercial", "Commercial &amp; Business Property",
     "Acquisitions and disposals of freehold and leasehold offices and suites, property development and business property, acting for banks and commercial clients.",
     ["Freehold and leasehold offices and suites", "Property development", "Business property matters", "Acting for banks and lenders"],
     None, None),
    ("company", "Company &amp; Commercial",
     "Acquisitions and disposals, partnerships, re-organisations, foreign company incorporation and administration, and insolvency.",
     ["Buying and selling businesses", "Partnerships and re-organisations", "Foreign company incorporation",
      "Insolvency"],
     None, None),
    ("immigration", "Immigration",
     "All forms of immigration work, from family and graduate visas to settlement, citizenship, BN(O) visas and appeals.",
     ["Family visas (spouse and child)", "Indefinite Leave to Remain", "British citizenship", "BN(O) visas",
      "Appeals and administrative reviews"],
     "From <strong>£1,000</strong> + VAT", "fees.html#immigration"),
    ("private-client", "Private Client",
     "Wills, probate and estate administration, trusts and tax, and advice for charities.",
     ["Wills", "Probate and Letters of Administration", "Trusts and tax", "Charities"],
     "<strong>£400</strong> an hour, partner-led", "fees.html#probate"),
    ("litigation", "Litigation &amp; Dispute Resolution",
     "We aim to resolve disputes without going to court where we can. Debt recovery, commercial contracts, employment disputes and libel.",
     ["Debt recovery", "Breach of commercial contract", "Employment disputes", "Libel"],
     "From <strong>£200</strong> an hour", "fees.html#debt"),
]

TEAM = [
    ("Dominic Lee", "Senior Partner", True, "Supervises the firm’s probate and estate administration work."),
    ("Sze-chun Kwok", "Partner", True, None),
    ("Tracy Ho", "Solicitor", False, None),
    ("Hsaio Mei Gibbons", "Consultant", False, None),
    ("Raymond Tang", "Consultant", False, None),
]


def initials(name):
    parts = name.replace("-", " ").split()
    return parts[0][0] + parts[-1][0]


def person(name, role, partner, bio, show_bio=False):
    b = f'<p class="bio">{bio}</p>' if (show_bio and bio) else ""
    return (f'<article class="person{" partner" if partner else ""} reveal"><div class="avatar" aria-hidden="true">{initials(name)}</div>'
            f'<h3>{name}</h3><p class="role">{role}</p>{b}</article>')


def cta_band():
    return f"""<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Ask us for an estimate.</h2>
      <p>Tell us about your matter and we will give you an estimate of costs before you instruct us.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light" href="contact.html#enquiry">Send an enquiry {icon("arrow")}</a>
      <a class="btn btn-outline-light" href="{TEL}">{icon("phone")} {PHONE}</a>
    </div>
  </div>
</section>"""


MAP = """<svg viewBox="0 0 600 420" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Map: 36 Lexington Street, between Oxford Circus and Piccadilly Circus">
  <rect width="600" height="420" fill="#dde9e8"/>
  <g fill="#cfdedc">
    <rect x="20" y="20" width="150" height="110" rx="4"/><rect x="200" y="20" width="120" height="110" rx="4"/><rect x="350" y="20" width="230" height="110" rx="4"/>
    <rect x="20" y="160" width="150" height="100" rx="4"/><rect x="350" y="160" width="230" height="100" rx="4"/>
    <rect x="20" y="290" width="150" height="110" rx="4"/><rect x="200" y="290" width="120" height="110" rx="4"/><rect x="350" y="290" width="230" height="110" rx="4"/>
    <rect x="200" y="160" width="40" height="100" rx="4"/><rect x="280" y="160" width="40" height="100" rx="4"/>
  </g>
  <g stroke="#fffdf9" stroke-width="14" stroke-linecap="round">
    <path d="M0 145H600"/><path d="M0 275H600"/><path d="M185 0V420"/><path d="M335 0V420"/>
  </g>
  <path d="M260 145V275" stroke="#fffdf9" stroke-width="18" stroke-linecap="round"/>
  <g font-family="Public Sans, sans-serif" font-size="11" fill="#4b5654" letter-spacing=".08em">
    <text x="272" y="215" transform="rotate(-90 272 215)" text-anchor="middle" font-weight="600" fill="#0f3e45">LEXINGTON ST</text>
    <text x="440" y="140" text-anchor="middle">BEAK ST</text>
    <text x="440" y="270" text-anchor="middle">BREWER ST</text>
    <text x="96" y="140" text-anchor="middle">BROADWICK ST</text>
  </g>
  <g font-family="Public Sans, sans-serif" font-size="11.5" font-weight="600" fill="#0b2f35">
    <g transform="translate(70 52)"><circle r="13" fill="#fffdf9" stroke="#c03a2b" stroke-width="4"/><rect x="-16" y="-3" width="32" height="6" fill="#1b3a8a"/><text x="22" y="4">Oxford Circus</text></g>
    <g transform="translate(410 378)"><circle r="13" fill="#fffdf9" stroke="#c03a2b" stroke-width="4"/><rect x="-16" y="-3" width="32" height="6" fill="#1b3a8a"/><text x="22" y="4">Piccadilly Circus</text></g>
  </g>
  <g transform="translate(260 196)">
    <circle r="30" fill="#145560" opacity=".14"/>
    <path d="M0 8s-16-14-16-26a16 16 0 0 1 32 0C16-6 0 8 0 8z" fill="#0f3e45"/>
    <circle cy="-18" r="6" fill="#c9a86b"/>
  </g>
</svg>"""


# ---------------------------------------------------------------- pages
def home():
    areas = "\n".join(
        f'<a class="area reveal" href="services.html#{slug}"><span class="area-num">{i:02d}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<span class="more">Learn more {icon("arrow")}</span></a>'
        for i, (slug, name, blurb, *_rest) in enumerate(AREAS, 1)
    )
    team = "\n".join(person(*p) for p in TEAM)
    body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Solicitors in Soho, London</p>
      <h1>Straightforward legal advice, <em>without the surprises.</em></h1>
      <p class="lede">Property, business, immigration and private client work for individuals, families and companies. We tell you the likely cost at the outset, keep you updated as your matter moves, and avoid delays.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="contact.html#enquiry">Get a cost estimate {icon("arrow")}</a>
        <a class="btn btn-ghost" href="fees.html">See our prices</a>
      </div>
      <ul class="hero-meta">
        <li>{icon("shield")} SRA regulated, No. {SRA_NO}</li>
        <li>{icon("pound")} Fixed fees for conveyancing and visas</li>
        <li>{icon("pin")} Lexington Street, W1F</li>
      </ul>
    </div>
    <aside class="contact-card reveal" aria-labelledby="talk">
      <h2 id="talk">Talk to us</h2>
      <p>Call to speak to the right fee earner, or send us a few details about your matter.</p>
      <ul class="channels">
        <li><a href="{TEL}">{icon("phone")}<span><small>Telephone</small><strong>{PHONE}</strong></span></a></li>
        <li><a href="mailto:{EMAIL}">{icon("mail")}<span><small>General enquiries</small><strong>{EMAIL}</strong></span></a></li>
        <li><div>{icon("pin")}<span><small>Office</small><strong>4/F, 36 Lexington Street, W1F 0LJ</strong></span></div></li>
      </ul>
      <a class="btn btn-light" href="contact.html#enquiry">Send an enquiry {icon("arrow")}</a>
    </aside>
  </div>
</section>

<section class="section section-white" id="services">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">What we do</p><h2>Six areas of practice, one team.</h2></div>
      <p>Whether you are buying a home, investing in property, running a business or planning for the future, the same small team will look after your matter from start to finish.</p>
    </div>
    <div class="areas">
{areas}
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">How we work</p><h2>What you can expect from us.</h2></div>
      <p>Going to law can be expensive and slow. We work to make it neither.</p>
    </div>
    <div class="promises">
      <div class="promise reveal">{icon("pound")}<h3>Costs up front</h3><p>An estimate of costs before you instruct us, and updates on the costs position as your matter proceeds.</p></div>
      <div class="promise reveal">{icon("clock")}<h3>No needless delays</h3><p>We know how much delay costs you and your business, so we keep matters moving.</p></div>
      <div class="promise reveal">{icon("hand")}<h3>Easy to work with</h3><p>Approachable people who take time to understand your objectives and work with you on solutions.</p></div>
      <div class="promise reveal">{icon("link")}<h3>Well connected</h3><p>A wide range of connections means we can often help beyond the matter in hand.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">Transparent pricing</p><h2>Typical fees, published.</h2></div>
      <p>Most conveyancing and immigration work is quoted as a fixed fee. Other matters are charged at hourly rates, and we will always estimate the hours first.</p>
    </div>
    <div class="fee-grid">
      <div class="fee-card reveal"><span class="label">Freehold purchase or sale</span><span class="price">£1,800<small> – £2,000</small></span><p>Up to £500,000, plus VAT and disbursements.</p></div>
      <div class="fee-card reveal"><span class="label">Leasehold purchase or sale</span><span class="price">£2,000<small> – £2,200</small></span><p>Up to £500,000, plus VAT and disbursements.</p></div>
      <div class="fee-card reveal"><span class="label">Remortgage (lender only)</span><span class="price">£800<small> freehold</small></span><p>Based on a £200,000 mortgage. Leasehold £1,000. Plus VAT.</p></div>
      <div class="fee-card reveal"><span class="label">Visitor or graduate visa</span><span class="price">£1,000</span><p>Plus VAT. Home Office fees are paid separately.</p></div>
    </div>
    <p class="fee-note">Every quote depends on the facts of your matter. <a class="text-link" href="fees.html">Full prices and service information {icon("arrow")}</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">Our people</p><h2>A professional, dedicated team.</h2></div>
      <p>Partner-led and small enough that you will always know who is handling your matter.</p>
    </div>
    <div class="team">
{team}
    </div>
    <p class="fee-note"><a class="text-link" href="team.html">Meet the team {icon("arrow")}</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="visit reveal">
      <div class="visit-copy">
        <p class="eyebrow">Visit us</p>
        <h2>In the heart of Soho.</h2>
        <address>4th Floor, 36 Lexington Street<br>London W1F 0LJ</address>
        <dl>
          <dt>Phone</dt><dd><a href="{TEL}">{PHONE}</a></dd>
          <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          <dt>DX</dt><dd>44725 Soho Square</dd>
          <dt>Tube</dt><dd>Oxford Circus or Piccadilly Circus</dd>
        </dl>
        <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=36+Lexington+Street+London+W1F+0LJ" target="_blank" rel="noopener">Open in Maps {icon("ext")}</a>
      </div>
      <div class="visit-map">{MAP}</div>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("index.html", "Lee &amp; Kan Solicitors | Solicitors in Soho, London",
                  "Lee & Kan Solicitors in Soho, London: residential and commercial property, company, immigration, private client and litigation. Clear, published fees.",
                  body)


def services():
    jump = "".join(f'<a href="#{slug}">{name}</a>' for slug, name, *_ in AREAS)
    blocks = []
    for i, (slug, name, blurb, items, price, link) in enumerate(AREAS, 1):
        ticks = "".join(f"<li>{t}</li>" for t in items)
        price_html = f'<span class="price-tag">{price} · <a href="{link}">see prices</a></span>' if price else \
            '<span class="price-tag">Quoted on enquiry, with an estimate before you instruct us</span>'
        matter = name.replace("&amp;", "&")
        blocks.append(f"""<article class="svc reveal" id="{slug}">
  <div class="svc-side"><span class="area-num">{i:02d}</span><h2>{name}</h2></div>
  <div class="svc-body">
    <p>{blurb}</p>
    <ul class="ticks">{ticks}</ul>
    <div class="svc-foot">
      <a class="btn btn-primary" href="contact.html?matter={matter.replace(' ', '+').replace('&', '%26')}#enquiry">Ask about this {icon("arrow")}</a>
      {price_html}
    </div>
  </div>
</article>""")
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Services</p>
    <p class="eyebrow">Services</p>
    <h1>A wide range of legal services, under one roof.</h1>
    <p class="lede">From a first home to a company acquisition, we handle long and complex matters as carefully as short and straightforward ones.</p>
    <nav class="jump" aria-label="Jump to a service">{jump}</nav>
  </div>
</section>
<section class="section-tight">
  <div class="container">
{chr(10).join(blocks)}
  </div>
</section>
{cta_band()}
"""
    return layout("services.html", "Services | Lee &amp; Kan Solicitors",
                  "Residential and commercial property, company and commercial, immigration, private client, and litigation and dispute resolution in Soho, London.",
                  body)


def rates(trainee=True):
    t = '<div class="rate"><span>Trainee Solicitor / Paralegal</span><strong>£200 <small>/ hour</small></strong></div>' if trainee else ""
    return f"""<div class="rates">
  <div class="rate"><span>Partner</span><strong>£400 <small>/ hour</small></strong></div>
  <div class="rate"><span>Assistant Solicitor</span><strong>£300 <small>/ hour</small></strong></div>
  {t}
</div>"""


def fees():
    sections = [
        ("policy", "Our approach"), ("rates", "Hourly rates"), ("freehold", "Freehold sale &amp; purchase"),
        ("leasehold", "Leasehold sale &amp; purchase"), ("mortgages", "Mortgages &amp; remortgages"),
        ("probate", "Probate"), ("immigration", "Immigration"), ("debt", "Debt recovery"),
    ]
    toc = "".join(f'<li><a href="#{a}">{b}</a></li>' for a, b in sections)

    imm = [
        ("Family visa (spouse / child), entry clearance", "£2,000 – £2,200", "Home Office fee £1,846<br>Immigration Health Surcharge £1,035 per year"),
        ("Family visa (spouse / child), extension", "£1,800 – £2,000", "Home Office fee £1,846<br>Immigration Health Surcharge £1,035 per year"),
        ("Graduate and High Potential Individual visas", "£1,000", "Home Office fee £822<br>Immigration Health Surcharge £1,035 per year"),
        ("10-year long residence ILR (settlement)", "£1,900 – £2,100", "Home Office fee £2,885"),
        ("Other Indefinite Leave to Remain (settlement)", "£1,800 – £2,000", "Home Office fee £2,885"),
        ("Naturalisation as a British citizen", "£1,200", "Home Office fee £1,500"),
        ("British National (Overseas) visa", "£1,200", "Home Office fee £250 (5 years) / £180 (30 months)<br>Immigration Health Surcharge £1,035 per year"),
        ("Visitor visa (6 months)", "£1,000", "Home Office fee £115"),
        ("Immigration appeal (First-tier Tribunal)", "£2,500 – £3,500", "Court fee £140 (oral hearing)<br>Barrister’s fee for complex cases, plus VAT"),
        ("Administrative review", "£600 – £800", "Home Office fee £80"),
    ]
    imm_rows = "".join(f"<tr><td>{a}</td><td class=\"num\">{b}</td><td>{c}</td></tr>" for a, b, c in imm)

    def conv_table(kind, low, start):
        return f"""<div class="table-wrap"><table class="fee-table">
<thead><tr><th>Matter</th><th>Estimated fee</th></tr></thead>
<tbody>
<tr><td>{kind} purchase<small>Up to £500,000</small></td><td class="num">{low}<small>plus VAT and disbursements</small></td></tr>
<tr><td>{kind} purchase<small>£500,000 to £1,000,000</small></td><td class="num">From {start}<small>plus VAT and disbursements</small></td></tr>
<tr><td>{kind} sale<small>Up to £500,000</small></td><td class="num">{low}<small>plus VAT and disbursements</small></td></tr>
<tr><td>{kind} sale<small>£500,000 to £1,000,000</small></td><td class="num">From {start}<small>plus VAT and disbursements</small></td></tr>
<tr><td>Purchase or sale<small>£1,000,000 and above</small></td><td class="num">Hourly rate<small>all work by a Partner</small></td></tr>
</tbody></table></div>"""

    cost_factors = """<ul class="bullets">
<li>the legal title is defective, or the title is unregistered</li>
<li>a management company must give a deed of covenant or consent</li>
<li>we need to comply with a restriction on the title</li>
<li>the correct consents were not obtained for alteration works</li>
<li>there is more than one mortgage secured on the property</li>
<li>you are buying or selling at auction, from a lender under a power of sale, or have tight deadlines</li>
<li>documents or information have to be requested more than once</li>
<li>the property is subject to a rent charge</li>
<li>you are receiving financial contributions from third parties, or using Help to Buy or a complex funding arrangement</li>
<li>the property is a new build or is being transferred out of an existing title</li>
</ul>"""

    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Prices</p>
    <p class="eyebrow">Prices &amp; service information</p>
    <h1>What our work costs, before you instruct us.</h1>
    <p class="lede">So there are no unwanted surprises, we will give you an estimate of likely costs and disbursements before you instruct us, and tell you straight away if we identify additional work.</p>
  </div>
</section>
<section class="section-tight">
  <div class="container fees-layout">
    <nav class="toc" aria-label="On this page"><p>On this page</p><ol>{toc}</ol>
      <a class="btn btn-primary" href="contact.html#enquiry">Ask for a quote</a></nav>
    <div>
      <section class="fee-sec" id="policy">
        <h2>Our approach</h2>
        <p>We work within the estimated cost unless your matter turns out to be more complex, or it is difficult to know in advance what will be involved. In those cases we let you know in advance and agree an hourly rate with you.</p>
        <div class="callout"><strong>VAT.</strong> All our fees, fixed or hourly, are subject to VAT at the current standard rate (20% at the time of publishing). Home Office fees, the Immigration Health Surcharge and HM Land Registry fees are not.</div>
        <p>Fixed fee work is carried out or supervised by a Partner or Assistant Solicitor, and any work by a Trainee Solicitor or Paralegal is supervised. You can check each fee earner’s details on the <a href="https://www.sra.org.uk/consumers/register/" target="_blank" rel="noopener">SRA register</a>, or ask us.</p>
      </section>

      <section class="fee-sec" id="rates">
        <h2>Hourly rates</h2>
        <p>Where a fixed fee isn’t possible, we charge by the hour according to the qualification and experience of the person doing the work, and give you an estimate of the time involved first.</p>
        {rates()}
        <p>All rates are plus VAT.</p>
      </section>

      <section class="fee-sec" id="freehold">
        <h2>Freehold sale &amp; purchase</h2>
        <p>The fee depends on the value of the property, the complexity of the title and whether third parties are involved. For transactions of £1,000,000 or more we charge hourly; a typical matter takes 10 to 15 hours.</p>
        {conv_table("Freehold", "£1,800 – £2,000", "£2,000")}
        <h3>Disbursements</h3>
        <div class="table-wrap"><table class="fee-table">
          <thead><tr><th>Item</th><th>Cost</th></tr></thead>
          <tbody>
            <tr><td>HM Land Registry official copies (sale)<small>Per document</small></td><td class="num">£3<small>no VAT</small></td></tr>
            <tr><td>Telegraphic transfer fee</td><td class="num">£15<small>plus VAT</small></td></tr>
            <tr><td>Searches (purchase only)<small>Third-party fees vary by authority; any difference is adjusted on completion</small></td><td class="num">£500<small>minimum on account</small></td></tr>
            <tr><td>Stamp Duty Land Tax (purchase only)</td><td>See <a href="https://www.gov.uk/stamp-duty-land-tax" target="_blank" rel="noopener">HMRC rates</a></td></tr>
          </tbody>
        </table></div>
        <h3>How long it takes</h3>
        <p>A sale typically completes in four to eight weeks, depending on the buyer’s searches and the co-operation of all parties. In a chain, dates have to be agreed by everyone.</p>
        <details class="more-info"><summary>What could change the cost?</summary><div>{cost_factors}</div></details>
        <details class="more-info"><summary>The purchase process, step by step</summary><div>
          <ol class="steps">
            <li>Once we have the memorandum of sale, we check your identity and source of funds and take money on account for searches.</li>
            <li>The seller’s solicitors send the contract pack: title, plan, protocol forms, contract and EPC.</li>
            <li>We investigate title, order searches, approve the contract, draft the transfer and raise enquiries.</li>
            <li>With your mortgage offer, searches and replies in, we send you a written report on title.</li>
            <li>You sign the contract and transfer, by post or at our office.</li>
            <li>We exchange contracts. From this point the deal is binding.</li>
            <li>We draw down your mortgage, or ask for the balance needed to complete.</li>
            <li>On completion we send the funds and tell you and the agents so keys can be released.</li>
            <li>We file your SDLT return (or LTT in Wales) and register you as owner at HM Land Registry.</li>
          </ol></div></details>
        <details class="more-info"><summary>The sale process, step by step</summary><div>
          <ol class="steps">
            <li>We obtain your title from HM Land Registry, or ask for your deeds if it is unregistered.</li>
            <li>We send you the property forms to complete.</li>
            <li>We prepare the contract pack for the buyer’s solicitors.</li>
            <li>We agree a completion date with you, the buyer and any related purchase.</li>
            <li>We exchange contracts. You are then committed to completing on the agreed date.</li>
            <li>On completion we pay off your mortgage and the estate agent, and send you the proceeds or use them for your purchase.</li>
          </ol></div></details>
        <details class="more-info"><summary>Exclusions</summary><div>
          <p>These prices are for individuals selling or buying their own home. Extra work is likely if the property is tenanted, you are acting as a company director, the property is being transferred out of an existing title, or you are selling as an executor or attorney.</p></div></details>
      </section>

      <section class="fee-sec" id="leasehold">
        <h2>Leasehold sale &amp; purchase</h2>
        <p>Leasehold matters involve the freeholder or managing agent, so the work, and the fee, is a little higher. A typical £1,000,000+ matter takes 12 to 17 hours. Land Registry, bank transfer, search and SDLT costs are the same as freehold.</p>
        {conv_table("Leasehold", "£2,000 – £2,200", "£2,200")}
        <h3>Third-party charges</h3>
        <p>Freeholders, landlords and managing agents set their own charges, which may or may not carry VAT. We tell you what they are as soon as we know.</p>
        <div class="split" style="gap:32px">
          <div><h4>When selling</h4><ul class="bullets"><li>Management / pre-sale pack</li><li>Certificate of consent</li><li>Deed of covenant</li><li>Joining a management company</li><li>Transfer of share certificate</li></ul></div>
          <div><h4>When buying</h4><ul class="bullets"><li>Deed of covenant</li><li>Certificate of compliance</li><li>Notice of transfer and/or charge</li><li>Share certificate costs</li><li>Ground rent and service charge apportionments</li></ul></div>
        </div>
      </section>

      <section class="fee-sec" id="mortgages">
        <h2>Mortgages &amp; remortgages</h2>
        <p>When we act only for the lender, the fee is based on the size of the advance. For a mortgage of £200,000:</p>
        <div class="table-wrap"><table class="fee-table">
          <thead><tr><th>Property</th><th>Fee</th></tr></thead>
          <tbody>
            <tr><td>Freehold</td><td class="num">£800<small>plus VAT and disbursements</small></td></tr>
            <tr><td>Leasehold</td><td class="num">£1,000<small>plus VAT and disbursements</small></td></tr>
            <tr><td>Advances above £200,000</td><td class="num">Hourly quote</td></tr>
          </tbody>
        </table></div>
        <p>Disbursements are as for a purchase, except that no Stamp Duty Land Tax is payable on a remortgage. Each lender may have its own requirements.</p>
      </section>

      <section class="fee-sec" id="probate">
        <h2>Probate</h2>
        <p>Probate is the process of administering someone’s estate after they die: gathering their money, assets and possessions, paying taxes and debts, and passing on the inheritance. Where there is no Will, the estate is administered under a Grant of Administration and the rules of intestacy.</p>
        <h3>What we can do</h3>
        <ul class="bullets">
          <li>Gather full details of the estate’s assets and debts, usually the longest stage</li>
          <li>Complete the inheritance tax return and pay any tax due</li>
          <li>Apply for the Grant of Probate or Grant of Administration</li>
          <li>Repay the deceased’s outstanding debts</li>
          <li>Advertise the Trustee Act notice</li>
          <li>Distribute the estate according to the Will</li>
        </ul>
        <p>All probate work is supervised by our senior partner, Dominic Lee. Most estates take about a year. International estates, and disputes between executors, beneficiaries, creditors or HMRC, can take longer.</p>
        <h3>Cost</h3>
        {rates(trainee=False)}
        <p>We estimate the hours from what you tell us about the estate. Alternatively, we may charge 0.2% of the gross value of the estate with a reduced hourly rate. Court fees and official copies of the grant are extra, as is any work after the grant is issued.</p>
      </section>

      <section class="fee-sec" id="immigration">
        <h2>Immigration</h2>
        <p>Work is carried out by a Partner or our Immigration Consultant, who has handled immigration matters since 2021 and has been a registered barrister in Hong Kong since 2012. We handle the application from start to finish: forms and covering letter, biometric appointment, paying UKVI and IHS fees, document checklists and review, uploading the bundle and chasing UKVI for updates.</p>
        <div class="table-wrap"><table class="fee-table">
          <thead><tr><th>Matter</th><th>Our fee (+ VAT)</th><th>Expected disbursements</th></tr></thead>
          <tbody>{imm_rows}</tbody>
        </table></div>
        <p class="fee-note">Home Office fees from 4 October 2023; Immigration Health Surcharge from 6 February 2024. These are not subject to VAT. Applications submitted from outside the UK may cost more because of exchange rates and card surcharges. Other possible costs: bank transfer £5–£15 + VAT, courier about £50 + VAT, postage at Post Office rates.</p>
      </section>

      <section class="fee-sec" id="debt">
        <h2>Debt recovery</h2>
        <p>We review your contracts or leases, negotiate a settlement, write to the debtor in line with the Civil Procedure Rules, apply to court, attend hearings or instruct counsel, instruct bailiffs and enforce any court order.</p>
        {rates()}
        <p>Court fees depend on the value and nature of the claim; see <a href="https://www.gov.uk/make-court-claim-for-money/court-fees" target="_blank" rel="noopener">GOV.UK court fees</a>. Other possible costs: bank transfer £5–£15 + VAT, courier about £50 + VAT, postage, bailiff fees and HM Land Registry fees.</p>
      </section>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("fees.html", "Prices &amp; Service Information | Lee &amp; Kan Solicitors",
                  "Fixed fees for conveyancing, remortgages and visas, plus hourly rates for probate and debt recovery at Lee & Kan Solicitors, Soho.",
                  body)


def team():
    people = "\n".join(person(*p, show_bio=True) for p in TEAM)
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Our team</p>
    <p class="eyebrow">Our team</p>
    <h1>The people who will look after your matter.</h1>
    <p class="lede">A partner-led practice. Ask for anyone by name on {PHONE}, or check a fee earner’s details on the SRA register.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="team team-lg">
{people}
    </div>
  </div>
</section>
<section class="section section-white">
  <div class="container split">
    <p class="pull">We aim to understand your objectives and problems, and work with you in finding solutions.</p>
    <div class="prose">
      <p>We aim to give the best possible service to our clients, whether the matter is long and complex or short and straightforward.</p>
      <p>Alongside the competence and reliability you would expect from any law practice, we know you also expect speed, and we understand how important it is to avoid delays for you and your business.</p>
      <p>You will find us easy to work with and approachable, and with our wide range of connections we can often help beyond the matter in hand.</p>
      <a class="text-link" href="https://www.sra.org.uk/consumers/register/" target="_blank" rel="noopener">Search the SRA register {icon("ext")}</a>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("team.html", "Our Team | Lee &amp; Kan Solicitors",
                  "Meet the partners, solicitors and consultants at Lee & Kan Solicitors, Lexington Street, Soho.",
                  body)


def contact():
    options = "".join(f'<option>{n.replace("&amp;", "&")}</option>' for _, n, *_ in AREAS)
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Contact</p>
    <p class="eyebrow">Contact</p>
    <h1>Tell us what you need.</h1>
    <p class="lede">Call us, or send a few details and we will come back to you with next steps and an estimate of costs.</p>
  </div>
</section>
<section class="section">
  <div class="container contact-grid">
    <div>
      <ul class="contact-list">
        <li><span class="ic-wrap">{icon("phone")}</span><div><small>Telephone</small><a href="{TEL}"><strong>{PHONE}</strong></a><p>The quickest way to reach the fee earner handling your matter.</p></div></li>
        <li><span class="ic-wrap">{icon("mail")}</span><div><small>Email</small><a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a><p>General enquiries only. For an existing matter, please email your fee earner directly or call us.</p></div></li>
        <li><span class="ic-wrap">{icon("pin")}</span><div><small>Office</small><strong>4th Floor, 36 Lexington Street, London W1F 0LJ</strong><p>DX 44725 Soho Square</p></div></li>
        <li><span class="ic-wrap">{icon("train")}</span><div><small>Getting here</small><strong>Oxford Circus or Piccadilly Circus</strong><p>Both a short walk through Soho.</p></div></li>
      </ul>
      <div class="visit-map" style="border-radius:14px;overflow:hidden;min-height:0;aspect-ratio:600/420">{MAP}</div>
    </div>
    <form class="form" id="enquiry-form" novalidate>
      <h2 id="enquiry">Send an enquiry</h2>
      <p>This opens an email to {EMAIL} with your details filled in. Please don’t include confidential documents at this stage.</p>
      <div class="field-row">
        <div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="phone">Phone <span style="font-weight:400;color:var(--ink-mute)">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="matter">What is it about?</label><select id="matter" name="matter">{options}<option>Something else</option></select></div>
      <div class="field"><label for="message">Your message</label><textarea id="message" name="message" required placeholder="A few lines about your matter, and any deadlines."></textarea></div>
      <button class="btn btn-primary" type="submit">Write email {icon("arrow")}</button>
      <p class="form-note">Sending an enquiry doesn’t make you a client. We’ll confirm terms and costs in writing before any work begins. See our <a href="{PDF}LKPrivacy.pdf" target="_blank" rel="noopener">privacy policy</a>.</p>
    </form>
  </div>
</section>
"""
    return layout("contact.html", "Contact | Lee &amp; Kan Solicitors",
                  "Contact Lee & Kan Solicitors: 4th Floor, 36 Lexington Street, London W1F 0LJ. Telephone 020 7287 8888.",
                  body)


if __name__ == "__main__":
    for name, fn in [("index.html", home), ("services.html", services), ("fees.html", fees),
                     ("team.html", team), ("contact.html", contact)]:
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)
