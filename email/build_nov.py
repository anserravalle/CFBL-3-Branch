"""Builds the November Letters from the Practice email.

Each brand section sits on its dark brand color (navy, forest, oxblood) with
items set as light cards (cream, sand, paper, bone). Run: python3 build_nov.py
"""

CDN = "https://cdn.shopify.com/s/files/1/0861/1528/7346/files/"
SITE = "https://balancedlivingde.com"
WTDIR = SITE + "/#shopify-section-template--28119297098034__reading"
FONT = "Georgia,'Times New Roman',serif"


def img(src, alt, link=None):
    tag = (f'<img src="{src}" alt="{alt}" width="528" '
           f'style="display:block;width:100%;height:auto;border:0;border-radius:4px;margin:0 0 14px;">')
    return f'<a href="{link}">{tag}</a>' if link else tag


def card(body, bg, ink):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 18px;">'
            f'<tr><td style="background:{bg};border-radius:6px;padding:22px 24px;font-size:17px;line-height:1.6;color:{ink};">'
            f'{body}</td></tr></table>')


def h2(text, color):
    return f'<h2 style="margin:0 0 8px;font-weight:normal;font-size:22px;line-height:1.3;color:{color};">{text}</h2>'


def p(text, last=False):
    return f'<p style="margin:0{"" if last else " 0 14px"};">{text}</p>'


def a(text, href, color):
    return f'<a href="{href}" style="color:{color};font-weight:bold;">{text}</a>'


def section(bg, label, logo, label_color, cards, top_rule=None):
    rule = f"border-top:4px solid {top_rule};" if top_rule else ""
    head = ""
    if label:
        head = (f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 0 18px;"><tr>'
                f'<td valign="middle"><img src="{logo}" alt="" width="44" height="44" style="display:block;border:0;border-radius:4px;background:#FBF6F0;padding:3px;"></td>'
                f'<td valign="middle" style="padding-left:12px;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:{label_color};">{label}</td>'
                f'</tr></table>')
    return (f'<tr><td style="background:{bg};{rule}padding:32px 20px 18px;">'
            f'<div style="max-width:560px;margin:0 auto;">{head}{"".join(cards)}</div></td></tr>')


NAVY, SAND, CREAM, BROWN = "#2B5275", "#EED9C5", "#FBF6F0", "#3D2D29"
FOREST, PAPER, INK_G = "#3D5A52", "#F0EAE0", "#2A3530"
OX, BONE, INK = "#6E1F23", "#F1E8D8", "#1F1A16"
TREE = CDN + "CFBL_Logo.png?v=1791913956&width=200"
INST = CDN + "cfbl_intitute_logo.png?v=1782596648&width=200"
MUSA = CDN + "MUSA_logo.png?v=1782597722&width=200"

# ---------------- letter + website (navy, cream cards) ----------------
masthead = (
    f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 0 18px;"><tr>'
    f'<td valign="middle"><img src="{TREE}" alt="Center for Balanced Living" width="56" height="56" style="display:block;border:0;border-radius:4px;"></td>'
    f'<td valign="middle" style="padding-left:12px;"><p style="margin:0;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:{SAND};">Letters From The Practice</p>'
    f'<p style="margin:2px 0 0;font-size:13px;color:{SAND};">November 2026</p></td></tr></table>'
)
letter = card(
    f'<h1 style="margin:0 0 18px;font-weight:normal;font-size:30px;line-height:1.2;color:{NAVY};">A Month of Handoffs</h1>'
    + p("Dear friends,")
    + p("November is a month of handoffs here. The practice is changing the system that holds its records, and the Institute is planning next year.")
    + p("This letter goes to everyone in this community, clients and colleagues alike. Read the part that is yours and skip the rest. I won't mind.")
    + p("One more thing: the website is new. Here is what you will find there now.")
    + p("Niki", last=True),
    CREAM, "#2A2724")


def site_card(src, alt, href, title, text):
    return card(img(src, alt, href) + h2(title, NAVY) + p(f'{text} {a("Click here", href, NAVY)}', last=True), CREAM, "#2A2724")


website = [
    site_card(CDN + "Niki_Serravalle_intro_poster_v7.jpg?v=1793153956&width=1056", "Dr. Niki Serravalle in her video introduction",
              SITE + "/pages/team-introductions", "Meet the team", "Each of our clinicians in a short video, before your first appointment."),
    site_card(SITE + "/cdn/shop/files/CFBL_photo_testing_session.png?width=1056&amp;height=594&amp;crop=center", "The testing room at Center for Balanced Living",
              SITE + "/pages/psychological-evaluations", "What to expect from an evaluation", "A step-by-step guide, from gathering your information to the feedback session."),
    site_card(SITE + "/cdn/shop/files/CFBL_property_sunlit_path.jpg?width=1056&amp;height=594&amp;crop=center", "A sunlit path on the practice grounds",
              SITE + "/pages/community", "Community Reflections", "Our community scrapbook magazine."),
    site_card(CDN + "CFBL_leaves_wide.jpg?v=1791938817&width=1056", "Leaves on the meditation path",
              SITE + "/pages/preferences", "Choose what you hear from us", "Starting in January, this letter separates by interest, so you receive only the parts that are yours. Pick yours now."),
]

# ---------------- Center for Balanced Living (navy, sand cards) ----------------
clinical = [
    card(h2("A new client portal", NAVY)
         + p("This month we are moving our records and scheduling to TherapyNotes. If you are a current client, you will receive an email invitation to TherapyPortal, our new client portal. Your paperwork and appointment information will live there from now on.")
         + p("With the new portal, appointment reminders come by email only. Text message reminders are ending, so please make sure we have the email address you actually check. If your invitation has not arrived within a few days of your next appointment, call the office and we will send it again.", last=True),
         SAND, BROWN),
    card(h2("Around the holidays", NAVY)
         + p("Schedules shift between Thanksgiving and the new year. Check in with your therapist now about their availability so there are no surprise gaps in your care.", last=True),
         SAND, BROWN),
    card(h2("Meet Michael", NAVY)
         + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
           f'<td valign="top" width="128"><img src="{CDN}Michael_Szczechowski_Headshot.jpg?v=1793148953&width=360" alt="Michael Szczechowski" width="116" style="display:block;width:116px;height:auto;border:0;border-radius:4px;"></td>'
           f'<td valign="top" style="padding-left:14px;font-size:17px;line-height:1.6;color:{BROWN};">Michael Szczechowski is a pre-doctoral intern in psychological assessment at the practice. If you or your child comes in for an evaluation, you may meet him during testing.</td>'
           f'</tr></table>',
         SAND, BROWN),
    card(h2("Parenting With Purpose", NAVY)
         + p("Brianna Patton, LACMH, NCC, leads a free monthly workshop for parents and caregivers. It meets once a month online, and the next session is Friday, December 4. "
             "Registration is free, and the time and Zoom link go by email to everyone who signs up. "
             f'{a("Save your spot", SITE + "/products/parenting-with-purpose-monthly-virtual-parent-support-group", NAVY)}', last=True),
         SAND, BROWN),
]

# ---------------- CFBL Institute (forest, paper cards) ----------------
institute = [
    card(h2("Looking ahead to 2027", FOREST)
         + p(f'We are planning next year now, with clinical trainings for licensed clinicians one to two times a month. To hear dates first, choose "For Clinicians." '
             f'{a("Click here", SITE + "/pages/preferences?list=list-clinicians", FOREST)}', last=True),
         PAPER, INK_G),
    card(img(SITE + "/cdn/shop/files/WTDIR_tease_wk6_Dweck.png?width=1056", "What the Doctor Is Reading, week six: Mindset by Carol S. Dweck", WTDIR)
         + h2("What the Doctor Is Reading", FOREST)
         + p(f"Every week this month, one book for clinicians that makes you think: the kind that unsettles an assumption you didn't know you held. "
             f"A new title each week, with notes on why it earns a place on a clinician's shelf. {a('Follow along', WTDIR, FOREST)}", last=True),
         PAPER, INK_G),
]

# ---------------- Blog and Essays (oxblood, bone cards) ----------------
anx = SITE + "/blogs/balanced-living-blog-make-it-make-sense/social-anxiety-vs-ptsd"
court = SITE + "/blogs/essays/we-should-not-need-a-courtroom-part-1"
essays = [
    card(img(SITE + "/cdn/shop/articles/an-open-doorway-seen-from-inside-a-quiet-room.png?width=800&amp;height=450&amp;crop=center", "An open doorway seen from inside a quiet room", anx)
         + h2("Is It Social Anxiety, or Is It What Already Happened to You?", OX)
         + p(f'New this month on Make It Make Sense. {a("Read it", anx, OX)}', last=True),
         BONE, INK),
    card(img(SITE + "/cdn/shop/articles/Three_dawn_bands_beside_an_empty_bassinet.png?width=1056", "Three bands of dawn light beside an empty bassinet", court)
         + h2("We Should Not Need a Courtroom", OX)
         + p(f'An essay in four parts, all four out this month. {a("Start with Part One", court, OX)}', last=True),
         BONE, INK),
]

# ---------------- this month (navy, cream card) ----------------
light = [card(
    img(CDN + "CFBL_hero_path_tree_wide.jpg?v=1792083459&width=1056", "Morning light on the meditation path")
    + h2("This month: ten minutes of morning light", NAVY)
    + p("Now that the clocks have fallen back, the evenings go dark early, and many people notice their sleep and mood shift with them. One of the simplest things to try is light early in the day. Ten to twenty minutes outdoors in the first hour after waking gives the body's internal clock a clear signal about when the day begins. Even on an overcast morning, outdoor light is many times brighter than a lit room, so the window is no substitute for the porch.")
    + p("Attach it to something you already do: coffee outside, or the long way to the car.")
    + '<p style="margin:0;font-size:14px;font-style:italic;color:#666;">This is general education, not clinical care. If you have bipolar disorder, talk with your prescriber before adding light exposure. If changes in sleep or mood last, or get in the way of your life, talk with your doctor or a licensed clinician.</p>',
    CREAM, "#2A2724")]

rows = [
    section(NAVY, None, None, None, [masthead, letter] + website),
    section(NAVY, "Center for Balanced Living", TREE, SAND, clinical, top_rule=SAND),
    section(FOREST, "CFBL Institute", INST, PAPER, institute),
    section(OX, "From the Blog and Essays", MUSA, BONE, essays),
    section(NAVY, None, None, None, light),
    f'<tr><td style="background:#1F2F40;padding:22px 20px;font-size:14px;line-height:1.6;color:{CREAM};">'
    f'<div style="max-width:560px;margin:0 auto;"><p style="margin:0 0 6px;">If you are in crisis, call or text 988.</p>'
    f'<p style="margin:0;color:{SAND};">Center for Balanced Living · 5879 Summit Bridge Road, Townsend, DE 19734</p></div></td></tr>',
]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Letters from the Practice | November 2026</title>
<!--
  Letters from the Practice, November 2026. Generated by build_nov.py.
  Subject: Letters from the Practice | November
  Preview: A new client portal, holiday schedules, and a new website.
  Goes to clients and colleagues alike: no book promotion in this letter.
-->
</head>
<body style="margin:0;padding:0;background:{NAVY};">
<div style="display:none;max-height:0;overflow:hidden;">A new client portal, holiday schedules, and a new website.</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;font-family:{FONT};text-align:left;">
{chr(10).join(rows)}
</table>
</body>
</html>
"""

if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).with_name("2026-11_letters-from-the-practice.html")
    out.write_text(html)
    print(out)
