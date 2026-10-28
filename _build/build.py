"""Build the Lee & Kan concept site.

    python3 _build/build.py

Writes the English pages into the repo root and the Traditional Chinese pages
into zh/. Text is written as L(English, 繁體中文). Only needs Python 3.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OFFICIAL = "https://www.lee-kan.com/"
PHONE = "020 7287 8888"
TEL = "tel:+442072878888"
EMAIL = "info@lee-kan.com"
SRA_NO = "605819"
PDF = OFFICIAL  # policy PDFs stay on the official site
SRA_REGISTER = "https://www.sra.org.uk/consumers/register/"

LANG = "en"


def L(en, zh):
    return zh if LANG == "zh" else en


def asset(path):
    return ("../" if LANG == "zh" else "") + path


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

PAGES = ["index.html", "services.html", "fees.html", "team.html", "contact.html"]


def nav_items():
    return [
        ("services.html", L("Services", "服務範圍")),
        ("fees.html", L("Prices", "收費")),
        ("team.html", L("Our team", "團隊")),
        ("contact.html", L("Contact", "聯絡我們")),
    ]


def brand():
    return (f'<a class="brand" href="index.html" aria-label="{L("Lee &amp; Kan Solicitors, home", "Lee &amp; Kan Solicitors 主頁")}">{BRAND_MARK}'
            '<span class="brand-text"><span class="brand-name">Lee <span>&amp;</span> Kan</span>'
            f'<span class="brand-sub">{L("Solicitors · Soho", "律師 · 倫敦蘇豪")}</span></span></a>')


def lang_switch(page):
    en_href = ("../" if LANG == "zh" else "") + page
    zh_href = page if LANG == "zh" else "zh/" + page
    cur = ' aria-current="true"'
    return (f'<div class="lang-switch" aria-label="{L("Language", "語言")}">'
            f'<a href="{en_href}" lang="en-GB" hreflang="en-GB"{cur if LANG == "en" else ""}>EN</a>'
            f'<a href="{zh_href}" lang="zh-Hant" hreflang="zh-Hant"{cur if LANG == "zh" else ""}>繁中</a></div>')


def layout(page, title, description, body):
    current = ' aria-current="page"'
    nav = "\n".join(
        f'<a href="{href}"{current if href == page else ""}>{label}</a>' for href, label in nav_items()
    )
    html_lang = L("en-GB", "zh-Hant-HK")
    zh_fonts = "&family=Noto+Sans+TC:wght@400;500;600&family=Noto+Serif+TC:wght@500;600" if LANG == "zh" else ""
    return f"""<!doctype html>
<html lang="{html_lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0b2f35">
<link rel="alternate" hreflang="en-GB" href="{("../" if LANG == "zh" else "") + page}">
<link rel="alternate" hreflang="zh-Hant" href="{page if LANG == "zh" else "zh/" + page}">
<link rel="icon" href="{asset("assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400;1,8..60,500{zh_fonts}&display=swap">
<link rel="stylesheet" href="{asset("assets/css/style.css")}">
</head>
<body class="lang-{LANG}">
<a class="skip" href="#main">{L("Skip to content", "跳到主要內容")}</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">Concept</span><span class="concept-long">{L(f'Concept redesign. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official Lee &amp; Kan Solicitors website</a>.', f'改版概念設計，並非 <a href="{OFFICIAL}" target="_blank" rel="noopener">Lee &amp; Kan Solicitors 官方網站</a>。')}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{L("Designed by ", "設計：")}</span><strong>UX CIRCLES</strong> {icon("ext", "ic-ext")}</a>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    {brand()}
    <nav class="nav" id="site-nav" aria-label="{L("Main", "主選單")}">
      {nav}
      <div class="nav-extra">
        <a class="nav-phone" href="{TEL}">{icon("phone")}<span>{PHONE}</span></a>
        <a class="btn btn-primary" href="contact.html#enquiry">{L("Get a quote", "索取報價")}</a>
      </div>
    </nav>
    <div class="header-tools">
      {lang_switch(page)}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{L("Menu", "選單")}">{icon("menu", "ic-open")}{icon("close", "ic-close")}</button>
    </div>
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
        <p>{L("Solicitors on Lexington Street, Soho, advising individuals, families and businesses on property, company, immigration, private client and dispute matters.",
              "位於倫敦蘇豪 Lexington Street 的律師行，為個人、家庭及企業處理物業、公司、移民、遺囑遺產及爭議事務。")}</p>
      </div>
      <div>
        <p class="footer-h">{L("Visit", "地址")}</p>
        <address>4th Floor, 36 Lexington Street<br>London W1F 0LJ<br>DX 44725 Soho Square</address>
      </div>
      <div>
        <p class="footer-h">{L("Contact", "聯絡")}</p>
        <ul>
          <li><a href="{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="contact.html#enquiry">{L("Send an enquiry", "網上查詢")}</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-h">{L("Policies", "政策文件")}</p>
        <ul>
          <li><a href="fees.html">{L("Prices &amp; service information", "收費及服務資料")}</a></li>
          <li><a href="{PDF}Complaints.pdf" target="_blank" rel="noopener">{L("Complaints policy", "投訴政策（英文）")}</a></li>
          <li><a href="{PDF}LKPrivacy.pdf" target="_blank" rel="noopener">{L("Privacy policy", "私隱政策（英文）")}</a></li>
          <li><a href="{PDF}Data.pdf" target="_blank" rel="noopener">{L("Data protection", "資料保護（英文）")}</a></li>
          <li><a href="{PDF}LKDiversity.pdf" target="_blank" rel="noopener">{L("Diversity statistics", "多元化統計（英文）")}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <div>
        <p>{L(f"Lee &amp; Kan Solicitors is authorised and regulated by the Solicitors Regulation Authority, SRA No. {SRA_NO}.",
              f"Lee &amp; Kan Solicitors 由英格蘭及威爾斯律師監管局（SRA）授權及監管，SRA 編號 {SRA_NO}。")}</p>
        <p>&copy; Lee &amp; Kan Solicitors. {L("Concept redesign by", "改版概念設計：")} <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a>.</p>
      </div>
      <div class="sra-badge"><div><div><iframe frameborder="0" scrolling="no" allowTransparency="true" src="https://cdn.yoshki.com/iframe/55847r.html" title="{L("SRA digital badge", "SRA 數字徽章")}"></iframe></div></div></div>
    </div>
  </div>
</footer>
<div class="mobile-cta">
  <a class="btn btn-ghost" href="{TEL}">{icon("phone")} {L("Call us", "致電")}</a>
  <a class="btn btn-primary" href="contact.html#enquiry">{L("Get a quote", "索取報價")}</a>
</div>
<script src="{asset("assets/js/main.js")}"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- content
def areas():
    return [
        ("residential", L("Residential Property", "住宅物業"),
         L("Buying, selling, letting, remortgaging, party wall and lease matters, whether it is your first home or an investment.",
           "買賣、出租、轉按、共用牆及租約事務，無論是首置還是投資物業。"),
         [L("Freehold and leasehold purchases and sales", "永久業權及租賃業權物業買賣"), L("Remortgages", "轉按"),
          L("Letting, and buying to invest", "出租及投資物業"), L("Party wall and lease disputes", "共用牆及租約糾紛")],
         L("From <strong>£1,800</strong> + VAT", "<strong>£1,800</strong> 起（另加增值稅）"), "fees.html#freehold"),
        ("commercial", L("Commercial &amp; Business Property", "商業物業"),
         L("Acquisitions and disposals of freehold and leasehold offices and suites, property development and business property, acting for banks and commercial clients.",
           "永久業權及租賃業權寫字樓的收購與出售、物業發展及商業物業事務，代表銀行及商業客戶。"),
         [L("Freehold and leasehold offices and suites", "永久業權及租賃業權寫字樓"), L("Property development", "物業發展"),
          L("Business property matters", "商業物業事務"), L("Acting for banks and lenders", "代表銀行及貸款機構")],
         None, None),
        ("company", L("Company &amp; Commercial", "公司及商業"),
         L("Acquisitions and disposals, partnerships, re-organisations, foreign company incorporation and administration, and insolvency.",
           "收購與出售、合夥、重組、海外公司註冊及管理，以及無力償債事務。"),
         [L("Buying and selling businesses", "企業收購及出售"), L("Partnerships and re-organisations", "合夥及重組"),
          L("Foreign company incorporation", "海外公司註冊"), L("Insolvency", "無力償債")],
         None, None),
        ("immigration", L("Immigration", "移民"),
         L("All forms of immigration work, from family and graduate visas to settlement, citizenship, BN(O) visas and appeals.",
           "各類移民事務：家庭及畢業生簽證、永久居留、入籍、BN(O) 簽證及上訴。"),
         [L("Family visas (spouse and child)", "家庭簽證（配偶及子女）"), L("Indefinite Leave to Remain", "永久居留（ILR）"),
          L("British citizenship", "入籍英國"), L("BN(O) visas", "BN(O) 簽證"),
          L("Appeals and administrative reviews", "上訴及行政覆核")],
         L("From <strong>£1,000</strong> + VAT", "<strong>£1,000</strong> 起（另加增值稅）"), "fees.html#immigration"),
        ("private-client", L("Private Client", "遺囑、遺產及信託"),
         L("Wills, probate and estate administration, trusts and tax, and advice for charities.",
           "遺囑、遺產承辦及管理、信託與稅務，以及慈善機構事務。"),
         [L("Wills", "訂立遺囑"), L("Probate and Letters of Administration", "遺囑認證及遺產管理書"),
          L("Trusts and tax", "信託及稅務"), L("Charities", "慈善機構")],
         L("<strong>£400</strong> an hour, partner-led", "合夥人處理，每小時 <strong>£400</strong>"), "fees.html#probate"),
        ("litigation", L("Litigation &amp; Dispute Resolution", "訴訟及爭議解決"),
         L("We aim to resolve disputes without going to court where we can. Debt recovery, commercial contracts, employment disputes and libel.",
           "我們會盡量在不入稟法院的情況下解決爭議。追討欠款、商業合約、僱傭糾紛及誹謗。"),
         [L("Debt recovery", "追討欠款"), L("Breach of commercial contract", "違反商業合約"),
          L("Employment disputes", "僱傭糾紛"), L("Libel", "誹謗")],
         L("From <strong>£200</strong> an hour", "每小時 <strong>£200</strong> 起"), "fees.html#debt"),
    ]


def team_members():
    return [
        ("Dominic Lee", L("Senior Partner", "首席合夥人"), True,
         L("Supervises the firm’s probate and estate administration work.", "負責督導本行的遺產承辦及管理工作。")),
        ("Sze-chun Kwok", L("Partner", "合夥人"), True, None),
        ("Tracy Ho", L("Solicitor", "律師"), False, None),
        ("Hsaio Mei Gibbons", L("Consultant", "顧問"), False, None),
        ("Raymond Tang", L("Consultant", "顧問"), False, None),
    ]


def initials(name):
    parts = name.replace("-", " ").split()
    return parts[0][0] + parts[-1][0]


def person(name, role, partner, bio, show_bio=False):
    b = f'<p class="bio">{bio}</p>' if (show_bio and bio) else ""
    return (f'<article class="person{" partner" if partner else ""} reveal"><div class="avatar" aria-hidden="true">{initials(name)}</div>'
            f'<h3 lang="en">{name}</h3><p class="role">{role}</p>{b}</article>')


def cta_band():
    return f"""<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>{L("Ask us for an estimate.", "先問報價，再作決定。")}</h2>
      <p>{L("Tell us about your matter and we will give you an estimate of costs before you instruct us.", "告訴我們你的情況，我們會在你正式委託前提供費用估算。")}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light" href="contact.html#enquiry">{L("Send an enquiry", "網上查詢")} {icon("arrow")}</a>
      <a class="btn btn-outline-light" href="{TEL}">{icon("phone")} {PHONE}</a>
    </div>
  </div>
</section>"""


def map_svg():
    label = L("Map: 36 Lexington Street, between Oxford Circus and Piccadilly Circus",
              "地圖：36 Lexington Street，位於牛津圓環站與皮卡迪利圓環站之間")
    return f"""<svg viewBox="0 0 600 420" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{label}">
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
    area_cards = "\n".join(
        f'<a class="area reveal" href="services.html#{slug}"><span class="area-num">{i:02d}</span><h3>{name}</h3><p>{blurb}</p>'
        f'<span class="more">{L("Learn more", "了解更多")} {icon("arrow")}</span></a>'
        for i, (slug, name, blurb, *_rest) in enumerate(areas(), 1)
    )
    team = "\n".join(person(*p) for p in team_members())
    body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{L("Solicitors in Soho, London", "倫敦蘇豪區律師行")}</p>
      <h1>{L("Straightforward legal advice, <em>without the surprises.</em>", "清楚的法律意見，<em>收費不會有意外。</em>")}</h1>
      <p class="lede">{L("Property, business, immigration and private client work for individuals, families and companies. We tell you the likely cost at the outset, keep you updated as your matter moves, and avoid delays.",
                          "為個人、家庭及公司處理物業、商業、移民及遺囑遺產事務。我們一開始就告訴你大概費用，過程中隨時更新進度，並盡量避免延誤。")}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="contact.html#enquiry">{L("Get a cost estimate", "索取費用估算")} {icon("arrow")}</a>
        <a class="btn btn-ghost" href="fees.html">{L("See our prices", "查看收費")}</a>
      </div>
      <ul class="hero-meta">
        <li>{icon("shield")} {L(f"SRA regulated, No. {SRA_NO}", f"受 SRA 監管，編號 {SRA_NO}")}</li>
        <li>{icon("pound")} {L("Fixed fees for conveyancing and visas", "物業轉讓及簽證定額收費")}</li>
        <li>{icon("pin")} {L("Lexington Street, W1F", "Lexington Street, W1F")}</li>
      </ul>
    </div>
    <aside class="contact-card reveal" aria-labelledby="talk">
      <h2 id="talk">{L("Talk to us", "聯絡我們")}</h2>
      <p>{L("Call to speak to the right fee earner, or send us a few details about your matter.", "致電可直接聯絡負責律師，或留下你的案件資料。")}</p>
      <ul class="channels">
        <li><a href="{TEL}">{icon("phone")}<span><small>{L("Telephone", "電話")}</small><strong>{PHONE}</strong></span></a></li>
        <li><a href="mailto:{EMAIL}">{icon("mail")}<span><small>{L("General enquiries", "一般查詢")}</small><strong>{EMAIL}</strong></span></a></li>
        <li><div>{icon("pin")}<span><small>{L("Office", "辦公室")}</small><strong>4/F, 36 Lexington Street, W1F 0LJ</strong></span></div></li>
      </ul>
      <a class="btn btn-light" href="contact.html#enquiry">{L("Send an enquiry", "網上查詢")} {icon("arrow")}</a>
    </aside>
  </div>
</section>

<section class="section section-white" id="services">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">{L("What we do", "服務範圍")}</p><h2>{L("Six areas of practice, one team.", "六個專業範疇，同一團隊跟進。")}</h2></div>
      <p>{L("Whether you are buying a home, investing in property, running a business or planning for the future, the same small team will look after your matter from start to finish.",
            "無論是買樓、投資物業、經營生意還是為將來作打算，都由同一個團隊由始至終跟進你的事務。")}</p>
    </div>
    <div class="areas">
{area_cards}
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">{L("How we work", "我們的做法")}</p><h2>{L("What you can expect from us.", "你可以期待甚麼。")}</h2></div>
      <p>{L("Going to law can be expensive and slow. We work to make it neither.", "打官司往往又貴又慢，我們盡力令兩者都不會發生。")}</p>
    </div>
    <div class="promises">
      <div class="promise reveal">{icon("pound")}<h3>{L("Costs up front", "費用預先說明")}</h3><p>{L("An estimate of costs before you instruct us, and updates on the costs position as your matter proceeds.", "委託前提供費用估算，案件進行期間亦會更新費用狀況。")}</p></div>
      <div class="promise reveal">{icon("clock")}<h3>{L("No needless delays", "避免不必要延誤")}</h3><p>{L("We know how much delay costs you and your business, so we keep matters moving.", "我們明白延誤對你和你的生意影響有多大，所以會積極推進事務。")}</p></div>
      <div class="promise reveal">{icon("hand")}<h3>{L("Easy to work with", "容易溝通")}</h3><p>{L("Approachable people who take time to understand your objectives and work with you on solutions.", "平易近人，花時間了解你的目標，與你一起找出解決方法。")}</p></div>
      <div class="promise reveal">{icon("link")}<h3>{L("Well connected", "人脈廣泛")}</h3><p>{L("A wide range of connections means we can often help beyond the matter in hand.", "廣泛的業界網絡，往往能在案件以外提供更多協助。")}</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">{L("Transparent pricing", "收費透明")}</p><h2>{L("Typical fees, published.", "常見收費，清楚列明。")}</h2></div>
      <p>{L("Most conveyancing and immigration work is quoted as a fixed fee. Other matters are charged at hourly rates, and we will always estimate the hours first.",
            "大部分物業轉讓及移民事務採用定額收費；其他事務按時收費，我們一定會先估算所需時數。")}</p>
    </div>
    <div class="fee-grid">
      <div class="fee-card reveal"><span class="label">{L("Freehold purchase or sale", "永久業權買賣")}</span><span class="price">£1,800<small> – £2,000</small></span><p>{L("Up to £500,000, plus VAT and disbursements.", "樓價 £500,000 以下，另加增值稅及代支費用。")}</p></div>
      <div class="fee-card reveal"><span class="label">{L("Leasehold purchase or sale", "租賃業權買賣")}</span><span class="price">£2,000<small> – £2,200</small></span><p>{L("Up to £500,000, plus VAT and disbursements.", "樓價 £500,000 以下，另加增值稅及代支費用。")}</p></div>
      <div class="fee-card reveal"><span class="label">{L("Remortgage (lender only)", "轉按（只代表銀行）")}</span><span class="price">£800<small>{L(" freehold", " 永久業權")}</small></span><p>{L("Based on a £200,000 mortgage. Leasehold £1,000. Plus VAT.", "以 £200,000 按揭計算。租賃業權 £1,000。另加增值稅。")}</p></div>
      <div class="fee-card reveal"><span class="label">{L("Visitor or graduate visa", "訪客或畢業生簽證")}</span><span class="price">£1,000</span><p>{L("Plus VAT. Home Office fees are paid separately.", "另加增值稅。內政部申請費另計。")}</p></div>
    </div>
    <p class="fee-note">{L("Every quote depends on the facts of your matter.", "所有報價視乎個別案件情況而定。")} <a class="text-link" href="fees.html">{L("Full prices and service information", "完整收費及服務資料")} {icon("arrow")}</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">{L("Our people", "我們的團隊")}</p><h2>{L("A professional, dedicated team.", "專業、盡心的團隊。")}</h2></div>
      <p>{L("Partner-led and small enough that you will always know who is handling your matter.", "由合夥人主理，規模精簡，你一定知道是誰在處理你的事務。")}</p>
    </div>
    <div class="team">
{team}
    </div>
    <p class="fee-note"><a class="text-link" href="team.html">{L("Meet the team", "認識團隊")} {icon("arrow")}</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="visit reveal">
      <div class="visit-copy">
        <p class="eyebrow">{L("Visit us", "到訪")}</p>
        <h2>{L("In the heart of Soho.", "位於蘇豪區中心。")}</h2>
        <address>4th Floor, 36 Lexington Street<br>London W1F 0LJ</address>
        <dl>
          <dt>{L("Phone", "電話")}</dt><dd><a href="{TEL}">{PHONE}</a></dd>
          <dt>{L("Email", "電郵")}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          <dt>DX</dt><dd>44725 Soho Square</dd>
          <dt>{L("Tube", "地鐵")}</dt><dd>{L("Oxford Circus or Piccadilly Circus", "牛津圓環站（Oxford Circus）或皮卡迪利圓環站（Piccadilly Circus）")}</dd>
        </dl>
        <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=36+Lexington+Street+London+W1F+0LJ" target="_blank" rel="noopener">{L("Open in Maps", "在地圖開啟")} {icon("ext")}</a>
      </div>
      <div class="visit-map">{map_svg()}</div>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("index.html",
                  L("Lee &amp; Kan Solicitors | Solicitors in Soho, London", "Lee &amp; Kan Solicitors｜倫敦蘇豪律師行"),
                  L("Lee & Kan Solicitors in Soho, London: residential and commercial property, company, immigration, private client and litigation. Clear, published fees.",
                    "Lee & Kan Solicitors，倫敦蘇豪區律師行：住宅及商業物業、公司、移民、遺囑遺產及訴訟。收費清楚公開。"),
                  body)


def services():
    jump = "".join(f'<a href="#{slug}">{name}</a>' for slug, name, *_ in areas())
    blocks = []
    for i, (slug, name, blurb, items, price, link) in enumerate(areas(), 1):
        ticks = "".join(f"<li>{t}</li>" for t in items)
        price_html = f'<span class="price-tag">{price} · <a href="{link}">{L("see prices", "查看收費")}</a></span>' if price else \
            f'<span class="price-tag">{L("Quoted on enquiry, with an estimate before you instruct us", "按個案報價，委託前會先提供估算")}</span>'
        blocks.append(f"""<article class="svc reveal" id="{slug}">
  <div class="svc-side"><span class="area-num">{i:02d}</span><h2>{name}</h2></div>
  <div class="svc-body">
    <p>{blurb}</p>
    <ul class="ticks">{ticks}</ul>
    <div class="svc-foot">
      <a class="btn btn-primary" href="contact.html?matter={slug}#enquiry">{L("Ask about this", "就此查詢")} {icon("arrow")}</a>
      {price_html}
    </div>
  </div>
</article>""")
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">{L("Home", "主頁")}</a> / {L("Services", "服務範圍")}</p>
    <p class="eyebrow">{L("Services", "服務範圍")}</p>
    <h1>{L("A wide range of legal services, under one roof.", "一站式法律服務。")}</h1>
    <p class="lede">{L("From a first home to a company acquisition, we handle long and complex matters as carefully as short and straightforward ones.",
                        "由首次置業到公司收購，無論事務複雜還是簡單，我們都同樣用心處理。")}</p>
    <nav class="jump" aria-label="{L("Jump to a service", "跳到服務")}">{jump}</nav>
  </div>
</section>
<section class="section-tight">
  <div class="container">
{chr(10).join(blocks)}
  </div>
</section>
{cta_band()}
"""
    return layout("services.html", L("Services | Lee &amp; Kan Solicitors", "服務範圍｜Lee &amp; Kan Solicitors"),
                  L("Residential and commercial property, company and commercial, immigration, private client, and litigation and dispute resolution in Soho, London.",
                    "倫敦蘇豪區律師行：住宅及商業物業、公司及商業、移民、遺囑遺產及信託、訴訟及爭議解決。"),
                  body)


def rates(trainee=True):
    hour = L("/ hour", "／小時")
    t = f'<div class="rate"><span>{L("Trainee Solicitor / Paralegal", "見習律師／律師助理")}</span><strong>£200 <small>{hour}</small></strong></div>' if trainee else ""
    return f"""<div class="rates">
  <div class="rate"><span>{L("Partner", "合夥人")}</span><strong>£400 <small>{hour}</small></strong></div>
  <div class="rate"><span>{L("Assistant Solicitor", "助理律師")}</span><strong>£300 <small>{hour}</small></strong></div>
  {t}
</div>"""


def fees():
    sections = [
        ("policy", L("Our approach", "收費原則")), ("rates", L("Hourly rates", "時薪")),
        ("freehold", L("Freehold sale &amp; purchase", "永久業權買賣")),
        ("leasehold", L("Leasehold sale &amp; purchase", "租賃業權買賣")),
        ("mortgages", L("Mortgages &amp; remortgages", "按揭及轉按")),
        ("probate", L("Probate", "遺產承辦")), ("immigration", L("Immigration", "移民")),
        ("debt", L("Debt recovery", "追討欠款")),
    ]
    toc = "".join(f'<li><a href="#{a}">{b}</a></li>' for a, b in sections)

    hof = L("Home Office fee", "內政部申請費")
    ihs = L("Immigration Health Surcharge £1,035 per year", "移民健康附加費每年 £1,035")
    imm = [
        (L("Family visa (spouse / child), entry clearance", "家庭簽證（配偶／子女），入境申請"), "£2,000 – £2,200", f"{hof} £2,064<br>{ihs}"),
        (L("Family visa (spouse / child), extension", "家庭簽證（配偶／子女），續簽"), "£1,800 – £2,000", f"{hof} £1,407<br>{ihs}"),
        (L("Graduate and High Potential Individual visas", "畢業生簽證及高潛力人才簽證"), "£1,000", f"{hof} {L('£937 (Graduate) / £880 (HPI)', '£937（畢業生）／£880（高潛力人才）')}<br>{ihs}"),
        (L("10-year long residence ILR (settlement)", "十年長期居留永久居留（ILR）"), "£1,900 – £2,100", f"{hof} £3,226"),
        (L("Other Indefinite Leave to Remain (settlement)", "其他永久居留（ILR）"), "£1,800 – £2,000", f"{hof} £3,226"),
        (L("Naturalisation as a British citizen", "入籍英國"), "£1,200", f"{hof} {L('£1,839 (incl. £130 ceremony)', '£1,839（包括 £130 入籍儀式費）')}"),
        (L("British National (Overseas) visa", "BN(O) 簽證"), "£1,200",
         f"{hof} {L('£285 (5 years) / £206 (30 months)', '£285（5 年）／£206（30 個月）')}<br>{ihs}"),
        (L("Visitor visa (6 months)", "訪客簽證（6 個月）"), "£1,000", f"{hof} £135"),
        (L("Immigration appeal (First-tier Tribunal)", "移民上訴（初級審裁處）"), "£2,500 – £3,500",
         L("Tribunal fee £144 (with a hearing)<br>Barrister’s fee for complex cases, plus VAT", "審裁處費用 £144（設聆訊）<br>複雜案件另加大律師費及增值稅")),
        (L("Administrative review", "行政覆核"), "£600 – £800", f"{hof} £80"),
    ]
    imm_rows = "".join(f"<tr><td>{a}</td><td class=\"num\">{b}</td><td>{c}</td></tr>" for a, b, c in imm)

    plus = L("plus VAT and disbursements", "另加增值稅及代支費用")

    def conv_table(kind, low, start):
        purchase, sale = L(f"{kind} purchase", f"{kind}購買"), L(f"{kind} sale", f"{kind}出售")
        upto, band, top = L("Up to £500,000", "£500,000 以下"), L("£500,000 to £1,000,000", "£500,000 至 £1,000,000"), L("£1,000,000 and above", "£1,000,000 或以上")
        frm = L(f"From {start}", f"{start} 起")
        return f"""<div class="table-wrap"><table class="fee-table">
<thead><tr><th>{L("Matter", "事項")}</th><th>{L("Estimated fee", "估計收費")}</th></tr></thead>
<tbody>
<tr><td>{purchase}<small>{upto}</small></td><td class="num">{low}<small>{plus}</small></td></tr>
<tr><td>{purchase}<small>{band}</small></td><td class="num">{frm}<small>{plus}</small></td></tr>
<tr><td>{sale}<small>{upto}</small></td><td class="num">{low}<small>{plus}</small></td></tr>
<tr><td>{sale}<small>{band}</small></td><td class="num">{frm}<small>{plus}</small></td></tr>
<tr><td>{L("Purchase or sale", "買賣")}<small>{top}</small></td><td class="num">{L("Hourly rate", "按時收費")}<small>{L("all work by a Partner", "全部由合夥人處理")}</small></td></tr>
</tbody></table></div>"""

    factors = [
        L("the legal title is defective, or the title is unregistered", "業權有瑕疵，或業權未經註冊"),
        L("a management company must give a deed of covenant or consent", "需要管理公司提供契諾契據或同意書"),
        L("we need to comply with a restriction on the title", "需要遵守業權上的限制"),
        L("the correct consents were not obtained for alteration works", "改建工程未取得所需同意"),
        L("there is more than one mortgage secured on the property", "物業有多於一個按揭"),
        L("you are buying or selling at auction, from a lender under a power of sale, or have tight deadlines", "透過拍賣買賣、向行使出售權的貸款機構購買，或時間緊迫"),
        L("documents or information have to be requested more than once", "文件或資料需要重複索取"),
        L("the property is subject to a rent charge", "物業附有地租負擔（rent charge）"),
        L("you are receiving financial contributions from third parties, or using Help to Buy or a complex funding arrangement", "資金來自第三方，或使用 Help to Buy 或複雜的融資安排"),
        L("the property is a new build or is being transferred out of an existing title", "新建物業，或需從現有業權分拆轉讓"),
    ]
    cost_factors = '<ul class="bullets">' + "".join(f"<li>{f}</li>" for f in factors) + "</ul>"

    def steps(items):
        return '<ol class="steps">' + "".join(f"<li>{s}</li>" for s in items) + "</ol>"

    purchase_steps = steps([
        L("Once we have the memorandum of sale, we check your identity and source of funds and take money on account for searches.", "收到買賣備忘錄後，我們會核實你的身份及資金來源，並收取查冊費用。"),
        L("The seller’s solicitors send the contract pack: title, plan, protocol forms, contract and EPC.", "賣方律師寄來合約文件：業權、圖則、標準表格、合約及能源效益證書（EPC）。"),
        L("We investigate title, order searches, approve the contract, draft the transfer and raise enquiries.", "我們審查業權、安排查冊、審批合約、草擬轉讓契並提出查詢。"),
        L("With your mortgage offer, searches and replies in, we send you a written report on title.", "收齊按揭批核、查冊結果及回覆後，我們會給你書面業權報告。"),
        L("You sign the contract and transfer, by post or at our office.", "你以郵寄或親臨辦公室方式簽署合約及轉讓契。"),
        L("We exchange contracts. From this point the deal is binding.", "交換合約，交易自此具法律約束力。"),
        L("We draw down your mortgage, or ask for the balance needed to complete.", "我們提取按揭貸款，或請你支付完成交易所需餘款。"),
        L("On completion we send the funds and tell you and the agents so keys can be released.", "完成交易當日我們轉帳，並通知你及地產代理交收鎖匙。"),
        L("We file your SDLT return (or LTT in Wales) and register you as owner at HM Land Registry.", "我們代你申報印花稅（威爾斯為 LTT），並在土地註冊處登記你為業主。"),
    ])
    sale_steps = steps([
        L("We obtain your title from HM Land Registry, or ask for your deeds if it is unregistered.", "我們向土地註冊處取得業權文件；如業權未註冊，則需要你提供契據。"),
        L("We send you the property forms to complete.", "我們寄上物業資料表格讓你填寫。"),
        L("We prepare the contract pack for the buyer’s solicitors.", "我們為買方律師準備合約文件。"),
        L("We agree a completion date with you, the buyer and any related purchase.", "與你、買方及相關購買交易協定完成日期。"),
        L("We exchange contracts. You are then committed to completing on the agreed date.", "交換合約，你須在協定日期完成交易。"),
        L("On completion we pay off your mortgage and the estate agent, and send you the proceeds or use them for your purchase.", "完成交易時我們清還你的按揭及地產代理佣金，並把餘款交給你或用於你的購買交易。"),
    ])

    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">{L("Home", "主頁")}</a> / {L("Prices", "收費")}</p>
    <p class="eyebrow">{L("Prices &amp; service information", "收費及服務資料")}</p>
    <h1>{L("What our work costs, before you instruct us.", "委託之前，先知道費用。")}</h1>
    <p class="lede">{L("So there are no unwanted surprises, we will give you an estimate of likely costs and disbursements before you instruct us, and tell you straight away if we identify additional work.",
                        "為免出現意外開支，我們會在你委託前估算律師費及代支費用；如發現需要額外工作，會即時通知你。")}</p>
  </div>
</section>
<section class="section-tight">
  <div class="container fees-layout">
    <nav class="toc" aria-label="{L("On this page", "本頁內容")}"><p>{L("On this page", "本頁內容")}</p><ol>{toc}</ol>
      <a class="btn btn-primary" href="contact.html#enquiry">{L("Ask for a quote", "索取報價")}</a></nav>
    <div>
      <section class="fee-sec" id="policy">
        <h2>{L("Our approach", "收費原則")}</h2>
        <p>{L("We work within the estimated cost unless your matter turns out to be more complex, or it is difficult to know in advance what will be involved. In those cases we let you know in advance and agree an hourly rate with you.",
              "除非事務比預期複雜，或事前難以判斷所需工作，否則我們會在估算範圍內完成。遇到上述情況，我們會預先通知你，並與你協定按時收費。")}</p>
        <div class="callout">{L("<strong>VAT.</strong> All our fees, fixed or hourly, are subject to VAT at the current standard rate (20% at the time of publishing). Home Office fees, the Immigration Health Surcharge and HM Land Registry fees are not.",
                                "<strong>增值稅：</strong>所有律師費，不論定額或按時，均須另加現行標準增值稅（發佈時為 20%）。內政部申請費、移民健康附加費及土地註冊處費用不設增值稅。")}</div>
        <p>{L(f'Fixed fee work is carried out or supervised by a Partner or Assistant Solicitor, and any work by a Trainee Solicitor or Paralegal is supervised. You can check each fee earner’s details on the <a href="{SRA_REGISTER}" target="_blank" rel="noopener">SRA register</a>, or ask us.',
              f'定額收費工作由合夥人或助理律師處理或督導，見習律師及律師助理的工作亦會受督導。你可在 <a href="{SRA_REGISTER}" target="_blank" rel="noopener">SRA 律師名冊</a>查閱每位負責律師的資料，或直接問我們。')}</p>
      </section>

      <section class="fee-sec" id="rates">
        <h2>{L("Hourly rates", "時薪")}</h2>
        <p>{L("Where a fixed fee isn’t possible, we charge by the hour according to the qualification and experience of the person doing the work, and give you an estimate of the time involved first.",
              "未能定額收費的事務，會按處理人員的資歷按時收費，並會先估算所需時間。")}</p>
        {rates()}
        <p>{L("All rates are plus VAT.", "以上時薪另加增值稅。")}</p>
      </section>

      <section class="fee-sec" id="freehold">
        <h2>{L("Freehold sale &amp; purchase", "永久業權（Freehold）買賣")}</h2>
        <p>{L("The fee depends on the value of the property, the complexity of the title and whether third parties are involved. For transactions of £1,000,000 or more we charge hourly; a typical matter takes 10 to 15 hours.",
              "收費視乎樓價、業權複雜程度及是否涉及第三方。樓價 £1,000,000 或以上按時收費，一般需時 10 至 15 小時。")}</p>
        {conv_table(L("Freehold", "永久業權"), "£1,800 – £2,000", "£2,000")}
        <h3>{L("Disbursements", "代支費用")}</h3>
        <div class="table-wrap"><table class="fee-table">
          <thead><tr><th>{L("Item", "項目")}</th><th>{L("Cost", "費用")}</th></tr></thead>
          <tbody>
            <tr><td>{L("HM Land Registry official copies (sale)<small>Per document</small>", "土地註冊處正式副本（出售）<small>每份文件</small>")}</td><td class="num">£3<small>{L("no VAT", "不設增值稅")}</small></td></tr>
            <tr><td>{L("Telegraphic transfer fee", "電匯手續費")}</td><td class="num">£15<small>{L("plus VAT", "另加增值稅")}</small></td></tr>
            <tr><td>{L("Searches (purchase only)<small>Third-party fees vary by authority; any difference is adjusted on completion</small>", "查冊（只限購買）<small>第三方收費因地方政府而異，差額於完成交易時調整</small>")}</td><td class="num">£500<small>{L("minimum on account", "最少預付")}</small></td></tr>
            <tr><td>{L("Stamp Duty Land Tax (purchase only)", "印花稅 SDLT（只限購買）")}</td><td>{L('See <a href="https://www.gov.uk/stamp-duty-land-tax" target="_blank" rel="noopener">HMRC rates</a>', '參閱 <a href="https://www.gov.uk/stamp-duty-land-tax" target="_blank" rel="noopener">HMRC 稅率</a>')}</td></tr>
          </tbody>
        </table></div>
        <h3>{L("How long it takes", "需時多久")}</h3>
        <p>{L("A sale typically completes in four to eight weeks, depending on the buyer’s searches and the co-operation of all parties. In a chain, dates have to be agreed by everyone.",
              "出售一般需時四至八星期，視乎買方查冊進度及各方配合。如屬連鎖交易，日期須由所有人共同協定。")}</p>
        <details class="more-info"><summary>{L("What could change the cost?", "甚麼情況會令費用增加？")}</summary><div>{cost_factors}</div></details>
        <details class="more-info"><summary>{L("The purchase process, step by step", "購買流程")}</summary><div>{purchase_steps}</div></details>
        <details class="more-info"><summary>{L("The sale process, step by step", "出售流程")}</summary><div>{sale_steps}</div></details>
        <details class="more-info"><summary>{L("Exclusions", "不包括的情況")}</summary><div>
          <p>{L("These prices are for individuals selling or buying their own home. Extra work is likely if the property is tenanted, you are acting as a company director, the property is being transferred out of an existing title, or you are selling as an executor or attorney.",
                "以上收費適用於個人買賣自住物業。如物業已出租、你以公司董事身份行事、物業需從現有業權分拆轉讓，或你以遺囑執行人或受權人身份出售，很可能涉及額外工作。")}</p></div></details>
      </section>

      <section class="fee-sec" id="leasehold">
        <h2>{L("Leasehold sale &amp; purchase", "租賃業權（Leasehold）買賣")}</h2>
        <p>{L("Leasehold matters involve the freeholder or managing agent, so the work, and the fee, is a little higher. A typical £1,000,000+ matter takes 12 to 17 hours. Land Registry, bank transfer, search and SDLT costs are the same as freehold.",
              "租賃業權涉及業權人（freeholder）或管理代理，工作較多，收費亦稍高。£1,000,000 以上的交易一般需時 12 至 17 小時。土地註冊處、銀行轉帳、查冊及印花稅費用與永久業權相同。")}</p>
        {conv_table(L("Leasehold", "租賃業權"), "£2,000 – £2,200", "£2,200")}
        <h3>{L("Third-party charges", "第三方收費")}</h3>
        <p>{L("Freeholders, landlords and managing agents set their own charges, which may or may not carry VAT. We tell you what they are as soon as we know.",
              "業權人、業主及管理代理自行訂定收費，可能另加增值稅。我們一得知就會通知你。")}</p>
        <div class="split" style="gap:32px">
          <div><h4>{L("When selling", "出售時")}</h4><ul class="bullets"><li>{L("Management / pre-sale pack", "管理資料／售前文件")}</li><li>{L("Certificate of consent", "同意證明書")}</li><li>{L("Deed of covenant", "契諾契據")}</li><li>{L("Joining a management company", "加入管理公司")}</li><li>{L("Transfer of share certificate", "轉讓股票")}</li></ul></div>
          <div><h4>{L("When buying", "購買時")}</h4><ul class="bullets"><li>{L("Deed of covenant", "契諾契據")}</li><li>{L("Certificate of compliance", "合規證明書")}</li><li>{L("Notice of transfer and/or charge", "轉讓及／或押記通知")}</li><li>{L("Share certificate costs", "股票費用")}</li><li>{L("Ground rent and service charge apportionments", "地租及管理費分攤")}</li></ul></div>
        </div>
      </section>

      <section class="fee-sec" id="mortgages">
        <h2>{L("Mortgages &amp; remortgages", "按揭及轉按")}</h2>
        <p>{L("When we act only for the lender, the fee is based on the size of the advance. For a mortgage of £200,000:", "只代表貸款機構時，收費按貸款額計算。以 £200,000 按揭為例：")}</p>
        <div class="table-wrap"><table class="fee-table">
          <thead><tr><th>{L("Property", "物業")}</th><th>{L("Fee", "收費")}</th></tr></thead>
          <tbody>
            <tr><td>{L("Freehold", "永久業權")}</td><td class="num">£800<small>{plus}</small></td></tr>
            <tr><td>{L("Leasehold", "租賃業權")}</td><td class="num">£1,000<small>{plus}</small></td></tr>
            <tr><td>{L("Advances above £200,000", "貸款額超過 £200,000")}</td><td class="num">{L("Hourly quote", "按時報價")}</td></tr>
          </tbody>
        </table></div>
        <p>{L("Disbursements are as for a purchase, except that no Stamp Duty Land Tax is payable on a remortgage. Each lender may have its own requirements.",
              "代支費用與購買相同，但轉按不須繳付印花稅。個別貸款機構可能有額外要求。")}</p>
      </section>

      <section class="fee-sec" id="probate">
        <h2>{L("Probate", "遺產承辦")}</h2>
        <p>{L("Probate is the process of administering someone’s estate after they die: gathering their money, assets and possessions, paying taxes and debts, and passing on the inheritance. Where there is no Will, the estate is administered under a Grant of Administration and the rules of intestacy.",
              "遺產承辦是指在某人離世後管理其遺產：整理金錢、資產及財物，清繳稅項及債務，再分配遺產。如沒有遺囑，則須申請遺產管理書（Grant of Administration），並按無遺囑繼承規則分配。")}</p>
        <h3>{L("What we can do", "我們可以協助")}</h3>
        <ul class="bullets">
          <li>{L("Gather full details of the estate’s assets and debts, usually the longest stage", "整理遺產的全部資產及債務，通常是最費時的階段")}</li>
          <li>{L("Complete the inheritance tax return and pay any tax due", "填報遺產稅並繳付稅款")}</li>
          <li>{L("Apply for the Grant of Probate or Grant of Administration", "申請遺囑認證書或遺產管理書")}</li>
          <li>{L("Repay the deceased’s outstanding debts", "清還死者的未償債務")}</li>
          <li>{L("Advertise the Trustee Act notice", "刊登《受託人法》通告")}</li>
          <li>{L("Distribute the estate according to the Will", "按遺囑分配遺產")}</li>
        </ul>
        <p>{L("All probate work is supervised by our senior partner, Dominic Lee. Most estates take about a year. International estates, and disputes between executors, beneficiaries, creditors or HMRC, can take longer.",
              "所有遺產承辦工作由首席合夥人 Dominic Lee 督導。大部分遺產需時約一年；涉及海外資產，或遺囑執行人、受益人、債權人或稅務局之間有爭議，則需時更長。")}</p>
        <h3>{L("Cost", "收費")}</h3>
        {rates(trainee=False)}
        <p>{L("We estimate the hours from what you tell us about the estate. Alternatively, we may charge 0.2% of the gross value of the estate with a reduced hourly rate. Court fees and official copies of the grant are extra, as is any work after the grant is issued.",
              "我們會根據你提供的遺產資料估算時數。另一方案是收取遺產總值 0.2%，配合較低時薪。法院費用、認證書正式副本，以及發出認證書後的工作另計。")}</p>
      </section>

      <section class="fee-sec" id="immigration">
        <h2>{L("Immigration", "移民")}</h2>
        <p>{L("Work is carried out by a Partner or our Immigration Consultant, who has handled immigration matters since 2021 and has been a registered barrister in Hong Kong since 2012. We handle the application from start to finish: forms and covering letter, biometric appointment, paying UKVI and IHS fees, document checklists and review, uploading the bundle and chasing UKVI for updates.",
              "由合夥人或本行移民顧問處理。該顧問自 2021 年起處理移民事務，並自 2012 年起為香港註冊大律師。我們由頭到尾處理申請：填寫表格及附信、預約生物特徵登記、代繳 UKVI 及 IHS 費用、整理及審閱文件清單、上載申請文件，以及向 UKVI 跟進進度。")}</p>
        <div class="table-wrap"><table class="fee-table wide">
          <thead><tr><th>{L("Matter", "事項")}</th><th>{L("Our fee (+ VAT)", "律師費（另加增值稅）")}</th><th>{L("Expected disbursements", "預計代支費用")}</th></tr></thead>
          <tbody>{imm_rows}</tbody>
        </table></div>
        <p class="fee-note">{L("Home Office, tribunal and Immigration Health Surcharge amounts as listed on GOV.UK in October 2026; they change from time to time. They are not subject to VAT. Applications submitted from outside the UK may cost more because of exchange rates and card surcharges. Other possible costs: bank transfer £5–£15 + VAT, courier about £50 + VAT, postage at Post Office rates.",
                               "內政部申請費、審裁處費用及移民健康附加費以 2026 年 10 月 GOV.UK 所列為準，日後或會調整，均不設增值稅。在英國境外提交的申請，可能因匯率及信用卡附加費而費用較高。其他可能費用：銀行轉帳 £5–£15（另加增值稅）、速遞約 £50（另加增值稅）、郵費按郵局收費。")}</p>
      </section>

      <section class="fee-sec" id="debt">
        <h2>{L("Debt recovery", "追討欠款")}</h2>
        <p>{L("We review your contracts or leases, negotiate a settlement, write to the debtor in line with the Civil Procedure Rules, apply to court, attend hearings or instruct counsel, instruct bailiffs and enforce any court order.",
              "我們會審閱你的合約或租約、商討和解、按《民事訴訟程序規則》致函債務人、向法院提出申請、出席聆訊或委聘大律師、委託執達吏，以及執行法院命令。")}</p>
        {rates()}
        <p>{L('Court fees depend on the value and nature of the claim; see <a href="https://www.gov.uk/make-court-claim-for-money/court-fees" target="_blank" rel="noopener">GOV.UK court fees</a>. Other possible costs: bank transfer £5–£15 + VAT, courier about £50 + VAT, postage, bailiff fees and HM Land Registry fees.',
              '法院費用視乎申索金額及性質，詳見 <a href="https://www.gov.uk/make-court-claim-for-money/court-fees" target="_blank" rel="noopener">GOV.UK 法院費用</a>。其他可能費用：銀行轉帳 £5–£15（另加增值稅）、速遞約 £50（另加增值稅）、郵費、執達吏費用及土地註冊處費用。')}</p>
      </section>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("fees.html", L("Prices &amp; Service Information | Lee &amp; Kan Solicitors", "收費及服務資料｜Lee &amp; Kan Solicitors"),
                  L("Fixed fees for conveyancing, remortgages and visas, plus hourly rates for probate and debt recovery at Lee & Kan Solicitors, Soho.",
                    "Lee & Kan Solicitors 收費：物業轉讓、轉按及簽證定額收費，遺產承辦及追討欠款按時收費。"),
                  body)


def team():
    people = "\n".join(person(*p, show_bio=True) for p in team_members())
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">{L("Home", "主頁")}</a> / {L("Our team", "團隊")}</p>
    <p class="eyebrow">{L("Our team", "團隊")}</p>
    <h1>{L("The people who will look after your matter.", "負責你事務的人。")}</h1>
    <p class="lede">{L(f"A partner-led practice. Ask for anyone by name on {PHONE}, or check a fee earner’s details on the SRA register.",
                        f"由合夥人主理的律師行。致電 {PHONE} 可指名找任何一位，亦可在 SRA 律師名冊查閱資料。")}</p>
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
    <p class="pull">{L("We aim to understand your objectives and problems, and work with you in finding solutions.", "我們致力了解你的目標和難處，與你一起找出解決方法。")}</p>
    <div class="prose">
      <p>{L("We aim to give the best possible service to our clients, whether the matter is long and complex or short and straightforward.", "無論事務複雜冗長還是簡單直接，我們都致力為客戶提供最好的服務。")}</p>
      <p>{L("Alongside the competence and reliability you would expect from any law practice, we know you also expect speed, and we understand how important it is to avoid delays for you and your business.",
            "除了律師行應有的專業和可靠，我們知道你也期望效率，亦明白避免延誤對你和你的生意有多重要。")}</p>
      <p>{L("You will find us easy to work with and approachable, and with our wide range of connections we can often help beyond the matter in hand.",
            "我們容易溝通、平易近人，加上廣泛的業界網絡，往往能在案件以外提供更多協助。")}</p>
      <a class="text-link" href="{SRA_REGISTER}" target="_blank" rel="noopener">{L("Search the SRA register", "查閱 SRA 律師名冊")} {icon("ext")}</a>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("team.html", L("Our Team | Lee &amp; Kan Solicitors", "團隊｜Lee &amp; Kan Solicitors"),
                  L("Meet the partners, solicitors and consultants at Lee & Kan Solicitors, Lexington Street, Soho.",
                    "認識 Lee & Kan Solicitors 的合夥人、律師及顧問。"),
                  body)


def contact():
    options = "".join(f'<option value="{slug}">{name}</option>' for slug, name, *_ in areas())
    opt = L("(optional)", "（選填）")
    body = f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">{L("Home", "主頁")}</a> / {L("Contact", "聯絡我們")}</p>
    <p class="eyebrow">{L("Contact", "聯絡我們")}</p>
    <h1>{L("Tell us what you need.", "告訴我們你需要甚麼。")}</h1>
    <p class="lede">{L("Call us, or send a few details and we will come back to you with next steps and an estimate of costs.", "致電或留下資料，我們會回覆你下一步安排及費用估算。")}</p>
  </div>
</section>
<section class="section">
  <div class="container contact-grid">
    <div>
      <ul class="contact-list">
        <li><span class="ic-wrap">{icon("phone")}</span><div><small>{L("Telephone", "電話")}</small><a href="{TEL}"><strong>{PHONE}</strong></a><p>{L("The quickest way to reach the fee earner handling your matter.", "最快聯絡到負責律師的方法。")}</p></div></li>
        <li><span class="ic-wrap">{icon("mail")}</span><div><small>{L("Email", "電郵")}</small><a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a><p>{L("General enquiries only. For an existing matter, please email your fee earner directly or call us.", "只限一般查詢。現有案件請直接電郵負責律師或致電我們。")}</p></div></li>
        <li><span class="ic-wrap">{icon("pin")}</span><div><small>{L("Office", "辦公室")}</small><strong>4th Floor, 36 Lexington Street, London W1F 0LJ</strong><p>DX 44725 Soho Square</p></div></li>
        <li><span class="ic-wrap">{icon("train")}</span><div><small>{L("Getting here", "交通")}</small><strong>{L("Oxford Circus or Piccadilly Circus", "牛津圓環站或皮卡迪利圓環站")}</strong><p>{L("Both a short walk through Soho.", "兩個地鐵站都只需穿過蘇豪區步行一小段路。")}</p></div></li>
      </ul>
      <div class="visit-map" style="border-radius:14px;overflow:hidden;min-height:0;aspect-ratio:600/420">{map_svg()}</div>
    </div>
    <form class="form" id="enquiry-form" novalidate>
      <h2 id="enquiry">{L("Send an enquiry", "網上查詢")}</h2>
      <p>{L(f"This opens an email to {EMAIL} with your details filled in. Please don’t include confidential documents at this stage.",
            f"按下後會開啟一封寄往 {EMAIL} 的電郵，並已填好你的資料。此階段請勿附上機密文件。")}</p>
      <div class="field-row">
        <div class="field"><label for="name">{L("Name", "姓名")}</label><input id="name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="phone">{L("Phone", "電話")} <span style="font-weight:400;color:var(--ink-mute)">{opt}</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="email">{L("Email", "電郵")}</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="matter">{L("What is it about?", "查詢事項")}</label><select id="matter" name="matter">{options}<option value="other">{L("Something else", "其他")}</option></select></div>
      <div class="field"><label for="message">{L("Your message", "內容")}</label><textarea id="message" name="message" required placeholder="{L("A few lines about your matter, and any deadlines.", "簡述你的情況及任何期限。")}"></textarea></div>
      <button class="btn btn-primary" type="submit">{L("Write email", "撰寫電郵")} {icon("arrow")}</button>
      <p class="form-note">{L(f'Sending an enquiry doesn’t make you a client. We’ll confirm terms and costs in writing before any work begins. See our <a href="{PDF}LKPrivacy.pdf" target="_blank" rel="noopener">privacy policy</a>.',
                               f'提交查詢並不代表已委託本行。開始任何工作前，我們會以書面確認條款及費用。請參閱<a href="{PDF}LKPrivacy.pdf" target="_blank" rel="noopener">私隱政策（英文）</a>。')}</p>
    </form>
  </div>
</section>
"""
    return layout("contact.html", L("Contact | Lee &amp; Kan Solicitors", "聯絡我們｜Lee &amp; Kan Solicitors"),
                  L("Contact Lee & Kan Solicitors: 4th Floor, 36 Lexington Street, London W1F 0LJ. Telephone 020 7287 8888.",
                    "聯絡 Lee & Kan Solicitors：4th Floor, 36 Lexington Street, London W1F 0LJ。電話 020 7287 8888。"),
                  body)


if __name__ == "__main__":
    builders = {"index.html": home, "services.html": services, "fees.html": fees,
                "team.html": team, "contact.html": contact}
    for LANG, out in [("en", ROOT), ("zh", ROOT / "zh")]:
        out.mkdir(exist_ok=True)
        for name in PAGES:
            (out / name).write_text(builders[name](), encoding="utf-8")
            print("wrote", (out / name).relative_to(ROOT))
