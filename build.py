# -*- coding: utf-8 -*-
"""Сборка страниц сайта."""
import json, os, re, datetime

OUT = os.path.dirname(os.path.abspath(__file__))
CDN = "https://static.tildacdn.com/"
SITE_URL = "https://traektoriya.pro"
YEAR_FOUNDED = 2013
YEARS = datetime.date.today().year - YEAR_FOUNDED

LOGO = CDN + "tild6462-3665-4865-b361-306134636137/____2_.svg"
LOGO_F = CDN + "tild3837-6438-4532-b265-663432396363/_1_.svg"


def u(idpath):
    return CDN + ("" if idpath.startswith("tild") else "tild") + idpath


def g(ids, fname):
    return [u(i) + "/" + fname for i in ids]


F213 = "IMAGE_2024-08-27_213.jpg"
F214 = "IMAGE_2024-08-27_214.jpg"

CHISTOE = g("""6136-3739-4662-a333-343863613162 3838-3565-4939-a666-393533663437
3635-6436-4437-b231-396334323262 3566-3062-4630-b862-343438373138
3762-3034-4539-b466-366261653066 3432-3665-4132-b831-396139346331
3930-3961-4738-b131-326633643536 3531-6266-4861-a633-613235333562
6130-3737-4566-a137-623830313062 6665-3537-4635-b931-666133396139
3533-3364-4733-a564-373661396362 3331-6437-4834-a166-643063363831""".split(), F213)

UNIVER = g("""3062-3963-4631-a264-636461303235 3031-3965-4166-a138-633537663431
6634-3465-4731-a561-326636383531 6432-6139-4639-a533-363430316565
3732-3837-4639-a532-323737656565 6331-3339-4731-b834-356631613337
3137-6262-4365-a137-386466376666 6139-3134-4065-b336-373139313330
3833-6436-4864-b939-333634353431 6666-6463-4632-a563-666665643963
3539-6465-4539-a563-363532303037 3639-3131-4839-a263-306334323337
6435-3335-4632-b463-326437303764 6631-3835-4662-b035-303639643931
6439-3934-4534-b234-376634336131 3939-3332-4437-a237-353935343462""".split(), F213)

SVETLANA2 = g("""3038-6139-4137-b965-396534393132 3530-6664-4333-a135-376139336661
3263-3661-4938-a662-323739333339 3066-3835-4235-a638-353637323261
6561-6166-4331-b238-386632663539 3734-6665-4561-a634-313130663061
6466-3235-4061-a138-356230623566 3239-3837-4463-b866-373334653739
6439-3431-4661-b165-303965396438 3139-6532-4830-a234-356365616565""".split(), F214)

PANORAMA = g("""3662-3539-4137-b534-643630373533 3865-3937-4439-b464-343736623064
3966-3961-4663-a161-623533353132 3034-3362-4833-b431-656262376261
3734-6535-4561-b366-633335333364 3830-3931-4964-a437-636436386539
3864-3565-4563-b962-356435316662 3030-3636-4233-a534-643362326162
3565-3162-4337-b964-323965356138 3438-6235-4433-a465-356166633139""".split(), F214)

SVETLANA1 = [
    u("3238-6338-4336-a435-653532656233") + "/IMAGE_2024-08-27_215.jpg",
    u("3965-3763-4839-b938-393134386362") + "/" + F214,
    u("6665-3630-4462-a664-663338383134") + "/" + F214,
    u("3866-3434-4538-b263-653337323431") + "/" + F214,
    u("3562-6663-4834-b865-343161613365") + "/IMAGE_2024-08-27_215.jpg",
    u("3461-3337-4063-b636-303363373938") + "/IMAGE_2024-08-27_215.jpg",
    u("3734-3766-4664-b535-343365636664") + "/" + F214,
    u("3761-3063-4530-b264-396131356565") + "/IMAGE_2024-08-27_215.jpg",
    u("3935-3937-4235-b266-373361313365") + "/IMAGE_2024-08-27_215.jpg",
    u("3535-3834-4436-b937-653761633965") + "/IMAGE_2024-08-27_215.jpg",
]

KORONA = g("""6466-3933-4365-b230-623464643266 6638-6434-4238-a366-376438356336
3839-3831-4366-a265-373764323063 3365-6138-4763-b632-656438363331
6538-6637-4263-b161-636537306131 3936-6630-4439-b934-323232386330
3730-3931-4537-a330-616134656430 6265-6466-4235-b762-366638623666
3832-6538-4531-a366-613964323539 6435-6365-4164-b932-653766353339""".split(), F213)

# Отделка квартир
OTD_UNIVER = [u("3264-3162-4438-a163-316364636534") + "/IMG_7814_resized.jpg"] + g(
    """3538-3965-4334-b530-333363383661 3365-3833-4331-a166-323333646233
    3738-3935-4365-b235-373836663733 6535-3163-4432-a266-383136356438
    3234-3735-4437-b562-663535616331 3962-3033-4134-a163-656664653736
    3833-6261-4132-b739-666365343636 3133-6234-4534-a638-663439396561
    6430-3833-4335-b164-646464613165 6130-3465-4039-b534-333563323461
    3338-3062-4562-a432-363336373534 6334-3331-4438-a232-393832633039
    6139-6664-4461-b565-373631616634""".split(), F213)

FWA = "WhatsApp_Image_2024-.jpeg"
OTD_CHE = g("""3739-6634-4134-a462-346534333933 3131-6434-4330-b265-653464353662
3166-3735-4030-a230-323065633465 3439-6661-4762-a437-636562383165
6435-3831-4332-a635-386462616530 3139-3330-4332-b935-343434373331
3238-3164-4238-b636-653839636562 3663-3633-4263-a638-623166353439
6339-3937-4431-a534-346337653839 6461-6165-4732-b863-323765393637
6535-3235-4331-b134-633465643265 6134-3137-4334-a436-336466303865""".split(), FWA)

# Загородное строительство
VILLAGE = [
    u("6166-3036-4439-b262-643863323039") + "/1_.jpg",
    u("6132-3131-4134-a462-393662666662") + "/1_.jpg",
    u("3737-3361-4436-b763-393137323039") + "/2_.jpg",
    u("3234-6132-4332-b663-656630366132") + "/2_.jpg",
    u("6434-3634-4336-b030-663338663530") + "/1.jpg",
    u("3335-3261-4432-b263-353035383031") + "/2.jpg",
    u("6439-6539-4931-a135-646364353333") + "/3.jpg",
    u("6130-3130-4333-a463-393534363630") + "/4.jpg",
    u("6164-3534-4234-b738-643938323531") + "/5.jpg",
    u("3961-3666-4066-b631-623837356135") + "/1.jpg",
    u("6138-3361-4534-b037-626561303463") + "/2.jpg",
    u("3439-3938-4437-b763-396233383431") + "/3.jpg",
    u("3031-3963-4633-b037-613238313161") + "/4.jpg",
    u("3935-6362-4263-b366-653937633236") + "/5.jpg",
    u("6630-6630-4135-a339-306134316139") + "/6.jpg",
    u("3232-3838-4265-b536-306237323836") + "/3_copy.jpg",
    u("6136-3861-4966-b663-373033373037") + "/5_copy.jpg",
    u("3536-3463-4734-b733-363462653937") + "/4copy.jpg",
    u("3639-3933-4537-b765-663465366630") + "/2_copy.jpg",
    u("3437-3232-4364-b166-646161313834") + "/1_copy.jpg",
    u("3966-6234-4461-a631-653234383835") + "/5.jpg",
    u("3131-3661-4661-a532-316335356462") + "/3.jpg",
    u("6163-3064-4839-a664-633366303734") + "/2.jpg",
    u("3761-6135-4564-b239-363638386333") + "/1.jpg",
    u("3535-3630-4138-b735-373330333863") + "/4.jpg",
]

ABOUT_IMGS = [
    u("6439-3565-4431-b064-363161303837") + "/2_copy.jpg",
    u("3561-6539-4265-b333-623938613566") + "/3.jpg",
    u("3736-6661-4132-b831-336433323335") + "/2.jpg",
    u("3638-3738-4861-b363-366535343862") + "/5.jpg",
    u("3033-3832-4633-a462-353162386264") + "/6.jpg",
]

HOME_SHOTS = [
    u("3733-3063-4065-b263-653733653661") + "/1_copy.jpg",
    u("6438-3335-4937-b838-613437363862") + "/2_copy.jpg",
    u("6136-6262-4332-b664-363464396130") + "/3_copy.jpg",
    u("3561-3665-4162-a433-336230333861") + "/4copy.jpg",
    u("3737-6633-4465-a436-383930383433") + "/5_copy.jpg",
    u("6663-3531-4432-b030-633034646632") + "/1.jpg",
    u("3865-3465-4133-b830-353336653034") + "/2.jpg",
    u("6561-3039-4632-b730-356163653362") + "/3.jpg",
    u("3537-3962-4861-a362-373062663330") + "/4.jpg",
    u("3431-6561-4438-a632-356531323963") + "/5.jpg",
    u("3164-3662-4964-a136-393263336539") + "/1.jpg",
    u("3935-3963-4435-a338-393832653431") + "/2.jpg",
    u("3233-6438-4031-b939-663636343536") + "/3.jpg",
    u("3936-3765-4832-a432-306664656666") + "/4.jpg",
    u("3931-3932-4363-a663-316433626638") + "/5.jpg",
    u("3736-3130-4139-b930-383838333431") + "/6.jpg",
    u("3033-6433-4233-b564-346234333563") + "/1.jpg",
    u("3038-6666-4438-b838-376135623437") + "/2.jpg",
    u("3831-3837-4266-b535-363364646531") + "/3.jpg",
    u("3232-3334-4635-a236-613966383366") + "/4.jpg",
    u("3939-3033-4362-a164-353366356462") + "/5.jpg",
]


# Реестр изображений: каждому файлу назначается локальный путь.
MANIFEST = {}   # cdn_url -> local path
_used = set()


def local(url, folder, stem):
    """Возвращает локальный путь изображения."""
    if url in MANIFEST:
        return MANIFEST[url]
    ext = "." + url.rsplit(".", 1)[-1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".svg", ".webp"):
        ext = ".jpg"
    name = "%s/%s%s" % (folder, stem, ext)
    n = 2
    while name in _used:
        name = "%s/%s-%d%s" % (folder, stem, n, ext)
        n += 1
    _used.add(name)
    MANIFEST[url] = "assets/img/" + name
    return MANIFEST[url]


def reg_list(urls, folder, prefix):
    return [local(u_, folder, "%s-%02d" % (prefix, i + 1)) for i, u_ in enumerate(urls)]


def pair(url):
    """Локальный путь изображения."""
    return MANIFEST.get(url, url), url


LOGO_L = local(LOGO, "brand", "logo-dark")
LOGO_FL = local(LOGO_F, "brand", "logo-light")
CHISTOE_L = reg_list(CHISTOE, "jk", "chistoe-nebo")
UNIVER_L = reg_list(UNIVER, "jk", "univer-city")
SVETLANA2_L = reg_list(SVETLANA2, "jk", "svetlana-park-2")
PANORAMA_L = reg_list(PANORAMA, "jk", "panorama-park")
SVETLANA1_L = reg_list(SVETLANA1, "jk", "svetlana-park-1")
KORONA_L = reg_list(KORONA, "jk", "severnaya-korona")
OTD_UNIVER_L = reg_list(OTD_UNIVER, "otdelka", "univer-city")
OTD_CHE_L = reg_list(OTD_CHE, "otdelka", "che")
VILLAGE_L = reg_list(VILLAGE, "village", "obj")
ABOUT_L = reg_list(ABOUT_IMGS, "about", "about")
HOME_L = reg_list(HOME_SHOTS, "home", "shot")
FONT_URL = "https://static.tildacdn.com/tild6334-3065-4266-b863-353138363161/MagistralC-Bold.woff"

NAV = [
    ("villageprojects.html", "З-01", "Проекты домов"),
    ("villagerealization.html", "З-02", "Реализация"),
    ("projects.html", "Ж-01", "ЖК: входные группы"),
    ("otdelkajk.html", "Ж-02", "ЖК: отделка квартир"),
    ("partners.html", "П", "Партнёры"),
    ("about.html", "О", "О компании"),
    ("contacts.html", "К", "Контакты"),
]

TEL = "+7 911 923-09-03"
TELH = "tel:+79119230903"
MAIL = "info@traektoriya.pro"
ADDR = "Санкт-Петербург, Комендантский проспект, 43&nbsp;к3"


def head(title, desc, here, og=None):
    return f"""<!DOCTYPE html>
<html lang="ru" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e1216">
<link rel="icon" href="{LOGO}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}/{MANIFEST.get(og or HOME_SHOTS[0], "")}">
<meta property="og:locale" content="ru_RU">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<script>document.documentElement.classList.replace('no-js','js');</script>

<a class="skip" href="#main">Перейти к содержанию</a>
<div class="grain" aria-hidden="true"></div>
<div class="cur" id="cur" aria-hidden="true"><span class="cur__t">ТЯНИ</span></div>
<div class="cur-dot" id="curDot" aria-hidden="true"></div>

<div class="load" id="load" role="status" aria-live="polite" aria-label="Загрузка">
  <div class="load__half load__half--t"></div>
  <div class="load__half load__half--b"></div>
  <div class="load__in">
    <div class="load__mark">ТРАЕКТОРИЯ</div>
    <div class="load__line"><i id="loadLine"></i></div>
    <div class="load__meta">
      <span class="label">Санкт-Петербург · Ленинградская область</span>
      <span class="load__pct"><span id="loadPct">00</span><sup>%</sup></span>
    </div>
  </div>
</div>

<div class="gauge" id="gauge" aria-hidden="true"><b id="gaugeFill"></b></div>

<header class="hdr" id="hdr">
  <div class="hdr__in">
    <a class="hdr__logo" href="index.html" aria-label="Траектория, на главную">
      <img src="{LOGO}" alt="Траектория" width="160" height="38">
    </a>
    <nav class="hdr__nav" aria-label="Основное">
      <a class="hdr__tel mono" href="{TELH}">{TEL}</a>
      <a class="cta magnet" href="contacts.html">Обсудить проект</a>
      <button class="burger" id="burger" type="button" aria-label="Открыть меню" aria-expanded="false" aria-controls="sheet">
        <i></i><i></i>
      </button>
    </nav>
  </div>
</header>

<div class="sheet" id="sheet" aria-hidden="true">
  <nav class="sheet__nav" aria-label="Разделы сайта">
{sheet_rows(here)}
  </nav>
  <div class="sheet__foot">
    <a class="mono" href="{TELH}">{TEL}</a>
    <a href="mailto:{MAIL}">{MAIL}</a>
    <span>{ADDR}</span>
  </div>
</div>

<main id="main">
"""


def sheet_rows(here):
    rows = ['    <div class="sheet__row"><a class="sheet__link"%s href="index.html"><span>00</span>Главная</a></div>'
            % (' aria-current="page"' if here == "index.html" else "")]
    for href, idx, name in NAV:
        cur = ' aria-current="page"' if here == href else ""
        rows.append(f'    <div class="sheet__row"><a class="sheet__link"{cur} href="{href}"><span>{idx}</span>{name}</a></div>')
    return "\n".join(rows)


def contacts_block():
    return f"""
  <section class="contact" id="contact">
    <div class="wrap">
      <div class="contact__grid">
        <div class="contact__panel">
          <span class="label label--brand">Контакты</span>
          <h2 class="contact__title">
            <span class="l" style="--dl:0ms"><span>Свяжитесь с нами удобным</span></span>
            <span class="l" style="--dl:100ms"><span>для Вас способом</span></span>
          </h2>
          <div class="rows rv">
            <div class="row"><span class="label">Адрес</span><span class="row__v">{ADDR}</span></div>
            <div class="row"><span class="label">Телефон</span><span class="row__v mono"><a href="{TELH}">{TEL}</a></span></div>
            <div class="row"><span class="label">Почта</span><span class="row__v"><a href="mailto:{MAIL}">{MAIL}</a></span></div>
            <div class="row"><span class="label">Координаты</span><span class="row__v mono">60.027629 · 30.239709</span></div>
          </div>
          <div class="contact__cta rv" style="--dl:90ms">
            <a class="cta cta--solid magnet" href="{TELH}">Позвонить</a>
            <a class="cta magnet" href="mailto:{MAIL}">Написать письмо</a>
          </div>
        </div>
        <div class="contact__map">
          <iframe loading="lazy" title="Карта: Санкт-Петербург, Комендантский проспект, 43 к3"
            src="https://yandex.ru/map-widget/v1/?ll=30.239709%2C60.027629&amp;z=16&amp;pt=30.239709,60.027629,pm2blm"></iframe>
        </div>
      </div>
    </div>
  </section>
"""


def nxt(href, kicker, title):
    return f"""
  <a class="next" href="{href}">
    <div class="wrap next__in">
      <div>
        <span class="label label--brand">{kicker}</span>
        <div class="next__t" style="margin-top:10px">{title}</div>
      </div>
      <span class="next__a" aria-hidden="true">
        <svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </span>
    </div>
  </a>
"""


def tail(galleries=None, shots=None, phrases=None):
    data = ""
    if galleries:
        data += "window.GALLERIES=" + json.dumps(galleries, ensure_ascii=False) + ";\n"
    if shots:
        data += "window.SHOTS=" + json.dumps(shots, ensure_ascii=False) + ";\n"
    if phrases:
        data += "window.PHRASES=" + json.dumps(phrases, ensure_ascii=False) + ";\n"
    return f"""</main>

<footer class="ftr">
  <div class="wrap">
    <div class="ftr__top">
      <a class="ftr__logo" href="index.html" aria-label="Траектория, на главную">
        <img src="{LOGO_F}" alt="Траектория" width="180" height="54" loading="lazy">
      </a>
      <div class="ftr__cols">
        <div class="ftr__col">
          <span class="label">Загородное</span>
          <a href="villageprojects.html">Проекты домов</a>
          <a href="villagerealization.html">Реализация</a>
        </div>
        <div class="ftr__col">
          <span class="label">Жилые комплексы</span>
          <a href="projects.html">Входные группы</a>
          <a href="otdelkajk.html">Отделка квартир</a>
        </div>
        <div class="ftr__col">
          <span class="label">Компания</span>
          <a href="about.html">О нас</a>
          <a href="partners.html">Партнёры</a>
          <a href="contacts.html">Контакты</a>
        </div>
      </div>
    </div>
    <div class="ftr__bot">
      <span>© <span id="yr">2026</span> Траектория · с {YEAR_FOUNDED} года</span>
      <span>Санкт-Петербург · Ленинградская область</span>
      <a class="mono" href="{TELH}">{TEL}</a>
    </div>
  </div>
</footer>

<div class="dock" id="dock">
  <div class="dock__in">
    <a class="cta cta--solid" href="{TELH}">Позвонить</a>
    <a class="cta" href="contacts.html">Контакты</a>
  </div>
</div>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Просмотр объекта">
  <div class="lb__bar">
    <span class="lb__title" id="lbTitle"></span>
    <button class="lb__x" id="lbX" type="button" aria-label="Закрыть">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
    </button>
  </div>
  <div class="lb__fig"><img id="lbImg" alt=""></div>
  <div class="lb__nav">
    <button class="arw" id="lbPrev" type="button" aria-label="Предыдущее фото">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 4 7 12l8 8"/></svg>
    </button>
    <span class="lb__idx" id="lbIdx">01 / 01</span>
    <button class="arw" id="lbNext" type="button" aria-label="Следующее фото">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4l8 8-8 8"/></svg>
    </button>
  </div>
</div>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"GeneralContractor","name":"Траектория",
"url":"https://traektoriya.pro/","telephone":"{TEL}","email":"{MAIL}","foundingDate":"{YEAR_FOUNDED}",
"address":{{"@type":"PostalAddress","streetAddress":"Комендантский проспект, 43 к3","addressLocality":"Санкт-Петербург","addressCountry":"RU"}},
"geo":{{"@type":"GeoCoordinates","latitude":60.027629,"longitude":30.239709}},
"areaServed":["Санкт-Петербург","Ленинградская область"]}}
</script>

<script>
{data}</script>
<script src="assets/site.js"></script>
</body>
</html>
"""


def page_header(kicker, title_lines, lead=None, bg=None, crumbs=None):
    lines = "\n".join(
        f'          <span class="l" style="--dl:{i*100}ms"><span>{t}</span></span>'
        for i, t in enumerate(title_lines))
    bg_html = ""
    cls = "phead"
    if bg:
        cls += " phead--img"
        bg_html = f'''    <div class="phead__bg" aria-hidden="true"><img src="{bg}" alt="" loading="eager" decoding="async" data-hero-img></div>\n'''
    crumb_html = ""
    if crumbs:
        parts = ['<a href="index.html">Главная</a>', '<i></i>'] + [f'<span>{crumbs}</span>']
        crumb_html = f'        <div class="crumbs rv">{"".join(parts)}</div>\n'
    lead_html = f'        <p class="phead__lead rv" style="--dl:120ms">{lead}</p>\n' if lead else ""
    return f"""  <section class="{cls}">
{bg_html}    <div class="phead__in wrap grid">
      <span class="label">{kicker}</span>
      <div>
{crumb_html}        <h1>
{lines}
        </h1>
{lead_html}      </div>
    </div>
  </section>
"""


def cards(items):
    out = ['      <div class="cards">']
    for i, (key, name, meta, cover) in enumerate(items):
        out.append(f"""        <button class="card rv" data-gal="{key}" type="button" style="--dl:{min(i,4)*70}ms">
          <span class="card__img"><img src="{cover}" alt="{name}" loading="lazy" decoding="async"></span>
          <span class="card__veil"></span>
          <span class="card__no">{i+1:02d}</span>
          <span class="card__body">
            <span class="card__name">{name}</span>
            <span class="card__meta">{meta}</span>
          </span>
        </button>""")
    out.append("      </div>")
    return "\n".join(out)



IMG_SRC_RE = re.compile(r'src="(https://static\.tildacdn\.com/[^"]+)"')


def localize(html):
    """Подставляет локальные пути изображений."""
    def sub(m):
        cdn = m.group(1)
        loc = MANIFEST.get(cdn)
        return 'src="%s"' % loc if loc else m.group(0)
    html = IMG_SRC_RE.sub(sub, html)
    html = html.replace('<link rel="icon" href="%s">' % LOGO,
                        '<link rel="icon" href="%s">' % LOGO_L)
    # пути внутри данных галерей
    for cdn, loc in MANIFEST.items():
        html = html.replace('"%s"' % cdn, '"%s"' % loc)
    return html


def write(name, html):
    html = localize(html)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(name, len(html))


# ════════════════════════ ГЛАВНАЯ ════════════════════════
home = head("Траектория. Строительство и отделка",
            f"Траектория: загородное строительство и внутренняя отделка в Санкт-Петербурге и Ленинградской области. Полный цикл работ от проекта до завершения, с гарантией качества на каждом этапе. С {YEAR_FOUNDED} года.",
            "index.html")
home += f"""
  <section class="phead phead--img" style="min-height:clamp(600px,90svh,940px);display:flex;align-items:flex-end;padding-bottom:clamp(36px,4.6vw,72px)">
    <div class="phead__bg" data-parallax aria-hidden="true" style="inset:-8% 0">
      <img src="{HOME_SHOTS[0]}" alt="" data-hero-img fetchpriority="high" decoding="async" style="opacity:1">
    </div>
    <div class="phead__in wrap grid">
      <span class="label">Санкт-Петербург</span>
      <div>
        <h1 style="font-size:var(--d1);line-height:.94">
          <span class="l" style="--dl:0ms"><span style="color:var(--brand-lift)">Траектория</span></span>
          <span class="l" style="--dl:110ms"><span style="padding-left:.13em">в строительстве</span></span>
          <span class="l" style="--dl:220ms"><span style="padding-left:.13em">города</span></span>
        </h1>
        <div style="margin-top:clamp(30px,4vw,60px);display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px clamp(24px,4vw,64px)">
          <p class="phead__lead rv" style="--dl:120ms;margin:0;max-width:44ch">Загородное строительство и внутренняя отделка.
            Полный цикл работ от проекта до завершения, с гарантией качества на каждом этапе.</p>
          <div class="rv" style="--dl:220ms;display:flex;gap:clamp(16px,2vw,34px);align-items:flex-end">
            <div style="display:grid;gap:6px"><span class="label">Широта</span><b class="mono" style="font-family:var(--display);font-size:clamp(15px,1.15vw,19px)">60.027629</b></div>
            <div style="display:grid;gap:6px"><span class="label">Долгота</span><b class="mono" style="font-family:var(--display);font-size:clamp(15px,1.15vw,19px)">30.239709</b></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="ticker" aria-hidden="true">
    <div class="ticker__row">
      <div class="ticker__set"><span>Загородное строительство</span><span>Внутренняя отделка</span><span>Входные группы</span><span>Отделка квартир</span><span>Полный цикл работ</span></div>
      <div class="ticker__set"><span>Загородное строительство</span><span>Внутренняя отделка</span><span>Входные группы</span><span>Отделка квартир</span><span>Полный цикл работ</span></div>
    </div>
  </div>

  <section class="section">
    <div class="wrap grid">
      <span class="label">Подход</span>
      <p class="rv" style="margin:0;font-family:var(--display);font-weight:700;font-size:var(--d2);line-height:1.04;letter-spacing:-.028em">У&nbsp;нас <span style="position:relative;display:inline-block;vertical-align:top"><span id="ghost" style="visibility:hidden;display:block"></span><span id="typed" style="position:absolute;inset:0;display:block;color:var(--brand-lift)"></span></span></p>
    </div>
  </section>

  <section class="section section--paper">
    <div class="wrap grid">
      <span class="label">О компании</span>
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.86fr);gap:clamp(34px,5vw,90px);align-items:start">
        <div>
          <h2 style="margin:0 0 22px;font-family:var(--display);font-weight:700;font-size:var(--d3);line-height:1;letter-spacing:-.02em;color:var(--brand)"><span class="l"><span>Траектория</span></span></h2>
          <div class="article rv" style="--dl:90ms">
            <p>Ваш надежный партнер в загородном строительстве и внутренней отделке уже {YEARS} лет.
            Мы создаем дома с нуля и превращаем квартиры в новостройках в уютные и стильные пространства.
            <strong>Полный цикл работ от проекта до завершения</strong>, с гарантией качества на каждом этапе.</p>
          </div>
        </div>
        <div class="fig rv" style="justify-self:end">
          <span class="fig__n" data-count="{YEARS}">{YEARS}</span>
          <span class="fig__u">лет</span>
          <div class="fig__rule"></div>
          <span class="label">В строительстве и отделке · с {YEAR_FOUNDED}</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="works">
    <div class="wrap grid">
      <span class="label">Объекты</span>
      <div>
        <div class="works__head">
          <div>
            <span class="label label--brand">Портфолио</span>
            <h2 style="margin:12px 0 0;font-family:var(--display);font-weight:700;font-size:var(--d3);line-height:1.04;letter-spacing:-.02em">
              <span class="l" style="--dl:0ms"><span>Дома, квартиры,</span></span>
              <span class="l" style="--dl:100ms"><span>входные группы</span></span>
            </h2>
          </div>
          <div class="works__ctrl">
            <span class="works__idx" id="wIdx" aria-live="polite"><b>01</b><span> / {len(HOME_SHOTS)}</span></span>
            <button class="arw" id="wPrev" type="button" aria-label="Предыдущий объект"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 4 7 12l8 8"/></svg></button>
            <button class="arw" id="wNext" type="button" aria-label="Следующий объект"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4l8 8-8 8"/></svg></button>
          </div>
        </div>
        <div class="rail" id="rail" tabindex="0" role="region" aria-label="Лента объектов"></div>
        <div class="works__bar"><i id="wBar"></i></div>
      </div>
    </div>
  </section>

  <section class="section" style="border-top:1px solid var(--rule-soft)">
    <div class="wrap grid">
      <span class="label">Принцип</span>
      <h2 style="margin:0;font-family:var(--display);font-weight:700;font-size:var(--d2);line-height:1.04;letter-spacing:-.028em">
        <span class="l" style="--dl:0ms"><span>Ваша идея.</span></span>
        <span class="l" style="--dl:120ms"><span><em style="font-style:normal;color:var(--brand-lift)">Наша задача.</em></span></span>
      </h2>
    </div>
  </section>
"""
home += contacts_block()
home += nxt("projects.html", "Дальше", "Наши объекты")
home += tail(shots=HOME_SHOTS, phrases=[
    "полный цикл работ", "свой проект и своя бригада", "дома под ключ",
    "отделка квартир в новостройках", "гарантия на каждом этапе"])
write("index.html", home)

# ════════════════════════ ВХОДНЫЕ ГРУППЫ ════════════════════════
JK = [
    ("chistoenebo", "ЖК Чистое небо", CHISTOE),
    ("univercity", "ЖК Univer City", UNIVER),
    ("svetlanapark2", "ЖК Светлана Парк 2", SVETLANA2),
    ("panorama", "ЖК Панорама Парк Сосновка", PANORAMA),
    ("svetlanapark1", "ЖК Светлана Парк 1", SVETLANA1),
    ("severnayakorona", "Северная Корона", KORONA),
]
gal = {k: {"title": n, "imgs": im} for k, n, im in JK}
p = head("Входные группы | Траектория",
         "Входные группы в жилых комплексах Санкт-Петербурга: Чистое небо, Univer City, Светлана Парк, Панорама Парк Сосновка, Северная Корона.",
         "projects.html", og=CHISTOE[0])
p += page_header("Жилые комплексы", ["Входные", "группы"],
                 "Отделка входных групп в жилых комплексах Санкт-Петербурга. Нажмите на объект, чтобы посмотреть галерею.",
                 bg=KORONA[0], crumbs="Входные группы")
p += '  <section class="section">\n    <div class="wrap grid">\n      <span class="label">Объекты</span>\n      <div>\n'
p += cards([(k, n, f"{len(im)} фото", im[0]) for k, n, im in JK])
p += "\n      </div>\n    </div>\n  </section>\n"
p += contacts_block()
p += nxt("otdelkajk.html", "Дальше", "Отделка квартир в ЖК")
p += tail(galleries=gal)
write("projects.html", p)

# ════════════════════════ ОТДЕЛКА КВАРТИР ════════════════════════
OT = [
    ("otd_univer", "ЖК Univer City", OTD_UNIVER),
    ("otd_che", "ЖК «CHE»", OTD_CHE),
]
gal = {k: {"title": n, "imgs": im} for k, n, im in OT}
p = head("Отделка квартир в ЖК | Траектория",
         "Внутренняя отделка квартир в новостройках Санкт-Петербурга: ЖК Univer City, ЖК «CHE». Полный цикл работ.",
         "otdelkajk.html", og=OTD_UNIVER[0])
p += page_header("Жилые комплексы", ["Внутренняя отделка", "квартир"],
                 "Превращаем квартиры в новостройках в уютные и стильные пространства: от чернового состояния до готового интерьера.",
                 bg=OTD_UNIVER[1], crumbs="Отделка квартир")
p += '  <section class="section">\n    <div class="wrap grid">\n      <span class="label">Объекты</span>\n      <div>\n'
p += cards([(k, n, f"{len(im)} фото", im[0]) for k, n, im in OT])
p += "\n      </div>\n    </div>\n  </section>\n"
p += contacts_block()
p += nxt("partners.html", "Дальше", "Наши партнёры")
p += tail(galleries=gal)
write("otdelkajk.html", p)

# ════════════════════════ ЗАГОРОДНОЕ: ПРОЕКТЫ ════════════════════════
TR = [("tr0%d" % (i + 1), '«ТР» 0%d' % (i + 1), VILLAGE[i * 6:(i + 1) * 6]) for i in range(4)]
gal = {k: {"title": n, "imgs": im} for k, n, im in TR}
p = head("Проекты загородных домов | Траектория",
         "Проекты загородных домов «Траектория». Строительство домов с нуля в Санкт-Петербурге и Ленинградской области.",
         "villageprojects.html", og=VILLAGE[0])
p += page_header("Загородное строительство", ["Проекты", "загородных домов"],
                 "Типовые решения «ТР». Адаптируем каждое под участок, состав семьи и бюджет.",
                 bg=VILLAGE[4], crumbs="Проекты домов")
p += '  <section class="section">\n    <div class="wrap grid">\n      <span class="label">Серии</span>\n      <div>\n'
p += cards([(k, n, f"{len(im)} фото", im[0]) for k, n, im in TR])
p += "\n      </div>\n    </div>\n  </section>\n"
p += contacts_block()
p += nxt("villagerealization.html", "Дальше", "Реализация")
p += tail(galleries=gal)
write("villageprojects.html", p)

# ════════════════════════ ЗАГОРОДНОЕ: РЕАЛИЗАЦИЯ ════════════════════════
REAL = [("real%d" % (i + 1), "Объект %02d" % (i + 1), VILLAGE[i * 5:(i + 1) * 5]) for i in range(5)]
gal = {k: {"title": n, "imgs": im} for k, n, im in REAL}
p = head("Реализация загородного строительства | Траектория",
         "Построенные загородные дома «Траектория» в Санкт-Петербурге и Ленинградской области.",
         "villagerealization.html", og=VILLAGE[9])
p += page_header("Загородное строительство", ["Реализация"],
                 "Дома, построенные с нуля: от проекта и фундамента до чистовой отделки и благоустройства.",
                 bg=VILLAGE[9], crumbs="Реализация")
p += '  <section class="section">\n    <div class="wrap grid">\n      <span class="label">Объекты</span>\n      <div>\n'
p += cards([(k, n, f"{len(im)} фото", im[0]) for k, n, im in REAL])
p += "\n      </div>\n    </div>\n  </section>\n"
p += contacts_block()
p += nxt("about.html", "Дальше", "О компании")
p += tail(galleries=gal)
write("villagerealization.html", p)

# ════════════════════════ О КОМПАНИИ ════════════════════════
p = head("О компании | Траектория",
         f"«Траектория»: строительная компания, основанная в {YEAR_FOUNDED} году. Реализует проекты в Санкт-Петербурге и Ленинградской области.",
         "about.html", og=ABOUT_IMGS[0])
p += page_header("Компания", ["Траектория"],
                 "Строительная компания, которая реализует свои проекты в Санкт-Петербурге и Ленинградской области.",
                 bg=ABOUT_IMGS[0], crumbs="О компании")
p += f"""
  <section class="section section--paper">
    <div class="wrap grid">
      <span class="label">Кто мы</span>
      <div style="display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:clamp(34px,5vw,90px);align-items:start">
        <div class="article">
          <p class="lede rv">С {YEAR_FOUNDED} года мы специализируемся на внутренней отделке домов и квартир,
            строительстве домов, превращая ваши идеи в реальность.</p>
          <p class="rv" style="--dl:80ms">Наша компания гордится богатым опытом и высоким качеством выполнения работ,
            предлагая широкий выбор материалов для создания уникальных интерьеров.</p>
          <p class="rv" style="--dl:140ms">Наша команда понимает, что каждый проект для нас не просто работа,
            а возможность реализовать ваши мечты о комфортном и стильном жилье. Мы предлагаем
            <strong>индивидуальный подход к каждому клиенту</strong>, гарантируя, что наши решения
            соответствуют вашим ожиданиям и требованиям.</p>
        </div>
        <div class="fig rv" style="justify-self:end">
          <span class="fig__n" data-count="{YEARS}">{YEARS}</span>
          <span class="fig__u">лет</span>
          <div class="fig__rule"></div>
          <span class="label">Основана в {YEAR_FOUNDED} году</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid">
      <span class="label">Коротко</span>
      <div class="facts">
        <div class="fact rv"><span class="label">Основана</span><span class="fact__v">{YEAR_FOUNDED} год</span></div>
        <div class="fact rv"><span class="label">География</span><span class="fact__v">Санкт-Петербург и Ленинградская область</span></div>
        <div class="fact rv"><span class="label">Направления</span><span class="fact__v">Загородное строительство · внутренняя отделка домов и квартир · входные группы в ЖК</span></div>
        <div class="fact rv"><span class="label">Объём работ</span><span class="fact__v">Полный цикл: от проекта до завершения, с гарантией качества на каждом этапе</span></div>
      </div>
    </div>
  </section>

  <section class="section" style="border-top:1px solid var(--rule-soft)">
    <div class="wrap grid">
      <span class="label">Работы</span>
      <div>
        <div class="shead"><span class="label label--brand">Галерея</span>
          <h2><span class="l"><span>Из наших объектов</span></span></h2></div>
{cards([("about_gal", "Объекты компании", "%d фото" % len(ABOUT_IMGS + VILLAGE[:8]), ABOUT_IMGS[1])])}
      </div>
    </div>
  </section>
"""
p += contacts_block()
p += nxt("partners.html", "Дальше", "Наши партнёры")
p += tail(galleries={"about_gal": {"title": "Объекты Траектории", "imgs": ABOUT_IMGS + VILLAGE[:8]}})
write("about.html", p)

# ════════════════════════ ПАРТНЁРЫ ════════════════════════
SETL = ("«Траектория» гордится надежными партнерскими отношениями с SetlGroup, ведущим застройщиком "
        "в регионе. Это сотрудничество подтверждает нашу способность выполнять проекты на высшем уровне "
        "и обеспечивать высокое качество внутренней отделки для жилых комплексов SetlGroup. Мы совместно "
        "стремимся создать комфортные и стильные пространства для ваших будущих домов.")
PARTNERS = [
    ("SetlGroup", "Застройщик", SETL, None),
    ("КРЕПС", "Производитель сухих строительных смесей", None,
     None),
    ("ТД «Стройтраст»", "Поставщик строительных материалов", None, None),
    ("ТД «Петрович»", "Строительный торговый дом", None, None),
]
p = head("Партнёры | Траектория",
         "Партнёры компании «Траектория»: SetlGroup, КРЕПС, ТД «Стройтраст», ТД «Петрович».",
         "partners.html", og=VILLAGE[2])
p += page_header("Компания", ["Наши партнёры"],
                 "С кем мы работаем на объектах и у кого закупаем материалы.",
                 crumbs="Партнёры")
p += '  <section class="section">\n    <div class="wrap grid">\n      <span class="label">Партнёрство</span>\n      <div class="partners">\n'
for i, (name, role, txt, todo) in enumerate(PARTNERS):
    body = f'        <p class="partner__txt">{txt}</p>\n' if txt else ""
    note = f'        <p class="partner__todo">{todo}</p>\n' if todo else ""
    p += f"""      <article class="partner rv" style="--dl:{min(i,4)*70}ms">
        <span class="label label--brand">{role}</span>
        <h2 class="partner__name">{name}</h2>
{body}{note}      </article>
"""
p += "      </div>\n    </div>\n  </section>\n"
p += contacts_block()
p += nxt("contacts.html", "Дальше", "Контакты")
p += tail()
write("partners.html", p)

# ════════════════════════ КОНТАКТЫ ════════════════════════
p = head("Контакты | Траектория",
         f"Контакты «Траектории»: {ADDR}, телефон {TEL}, почта {MAIL}.",
         "contacts.html")
p += page_header("Связь", ["Свяжитесь с нами", "удобным способом"],
                 "Позвоните, напишите на почту или приезжайте в офис на Комендантском проспекте.",
                 crumbs="Контакты")
p += f"""
  <section class="section section--tight">
    <div class="wrap grid">
      <span class="label">Реквизиты связи</span>
      <div class="facts">
        <div class="fact rv"><span class="label">Адрес</span><span class="fact__v">{ADDR}</span></div>
        <div class="fact rv"><span class="label">Телефон</span><span class="fact__v mono"><a href="{TELH}">{TEL}</a></span></div>
        <div class="fact rv"><span class="label">Почта</span><span class="fact__v"><a href="mailto:{MAIL}">{MAIL}</a></span></div>
        <div class="fact rv"><span class="label">Координаты</span><span class="fact__v mono">60.027629 · 30.239709</span></div>
        <div class="fact rv"><span class="label">География</span><span class="fact__v">Санкт-Петербург и Ленинградская область</span></div>
      </div>
    </div>
  </section>
"""
p += contacts_block()
p += nxt("projects.html", "Дальше", "Наши объекты")
p += tail()
write("contacts.html", p)

print("years:", YEARS)


# Манифест изображений.
MANIFEST[FONT_URL] = "assets/MagistralC-Bold.woff"
items = sorted(MANIFEST.items(), key=lambda kv: kv[1])

with open(os.path.join(OUT, "images.tsv"), "w", encoding="utf-8") as f:
    f.write("# локальный путь<TAB>адрес на CDN Тильды\n")
    for cdn, loc in items:
        f.write(loc + "\t" + cdn + "\n")

py = ['#!/usr/bin/env python3',
      '# -*- coding: utf-8 -*-',
      '"""Скачивает все фотографии и шрифт сайта «Траектория» в папку assets/.',
      '',
      'Запуск из папки сайта:   python3 download-assets.py',
      'Ничего не спрашивает, ничего не удаляет, уже скачанное пропускает."""',
      'import os, sys, time',
      'from urllib.request import urlopen, Request',
      '',
      'HERE = os.path.dirname(os.path.abspath(__file__))',
      'FILES = [']
for cdn, loc in items:
    py.append('    (%r, %r),' % (loc, cdn))
py += [']',
       '',
       'ok = skip = bad = 0',
       'for i, (loc, url) in enumerate(FILES, 1):',
       '    dest = os.path.join(HERE, *loc.split("/"))',
       '    if os.path.exists(dest) and os.path.getsize(dest) > 0:',
       '        skip += 1; continue',
       '    os.makedirs(os.path.dirname(dest), exist_ok=True)',
       '    for attempt in range(3):',
       '        try:',
       '            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})',
       '            with urlopen(req, timeout=40) as r, open(dest, "wb") as out:',
       '                out.write(r.read())',
       '            ok += 1',
       '            print("%4d/%d  %s" % (i, len(FILES), loc))',
       '            break',
       '        except Exception as e:',
       '            if attempt == 2:',
       '                bad += 1',
       '                print("%4d/%d  ОШИБКА %s: %s" % (i, len(FILES), loc, e), file=sys.stderr)',
       '            else:',
       '                time.sleep(1.5)',
       '',
       'print()',
       'print("Скачано: %d   пропущено (уже были): %d   с ошибкой: %d" % (ok, skip, bad))',
       'if bad:',
       '    print("Запустите скрипт ещё раз, он докачает недостающее.")',
       'else:',
       '    print("Готово. Сайт больше не зависит от CDN Тильды.")',
       '']
with open(os.path.join(OUT, "download-assets.py"), "w", encoding="utf-8") as f:
    f.write("\n".join(py))

sh = ['#!/bin/sh',
      '# Скачивает фотографии и шрифт сайта «Траектория» (macOS / Linux).',
      '# Запуск из папки сайта:  sh download-assets.sh',
      'cd "$(dirname "$0")" || exit 1',
      'n=0']
for cdn, loc in items:
    d = os.path.dirname(loc)
    sh.append('mkdir -p "%s"; [ -s "%s" ] || { curl -fsSL -o "%s" "%s" && n=$((n+1)) && echo "%s"; }' % (d, loc, loc, cdn, loc))
sh += ['echo ""', 'echo "Скачано файлов: $n"']
with open(os.path.join(OUT, "download-assets.sh"), "w", encoding="utf-8") as f:
    f.write("\n".join(sh) + "\n")

print("манифест:", len(items), "файлов")



