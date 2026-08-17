from html import escape


def build_portfolio_html(portfolio_data):

    name = escape(str(portfolio_data.get("name", "My Portfolio")))
    about = escape(str(portfolio_data.get("about", "")))

    skills = portfolio_data.get("skills", [])
    education = portfolio_data.get("education", [])
    projects = portfolio_data.get("projects", [])
    experience = portfolio_data.get("experience", [])
    certifications = portfolio_data.get("certifications", [])

    contact = portfolio_data.get("contact", {})
    social_links = portfolio_data.get("social_links", {})

    email = escape(str(contact.get("email", "")))
    phone = escape(str(contact.get("phone", "")))

    linkedin = escape(str(social_links.get("linkedin", "")))
    github = escape(str(social_links.get("github", "")))
    portfolio = escape(str(social_links.get("portfolio", "")))

    # ---------------- SKILLS ----------------

    skills_html = ""

    for skill in skills:
        skills_html += f"""
        <span class="skill-pill">{escape(str(skill))}</span>
        """

    # ---------------- EDUCATION ----------------

    education_html = ""

    for item in education:

        if isinstance(item, dict):
            title = escape(str(item.get("degree", item.get("title", ""))))
            details = escape(str(item.get("institution", item.get("details", ""))))
        else:
            title = escape(str(item))
            details = ""

        education_html += f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>

            <div class="timeline-content">
                <h3>{title}</h3>
                <p>{details}</p>
            </div>
        </div>
        """

    # ---------------- PROJECTS ----------------

    projects_html = ""

    for project in projects:

        if isinstance(project, dict):

            title = escape(
                str(project.get("title", project.get("name", "Project")))
            )

            description = escape(
                str(project.get("description", ""))
            )

            technologies = project.get(
                "technologies",
                project.get("tech_stack", [])
            )

            if isinstance(technologies, list):
                tech_html = "".join(
                    f'<span class="tech-tag">{escape(str(t))}</span>'
                    for t in technologies
                )
            else:
                tech_html = (
                    f'<span class="tech-tag">{escape(str(technologies))}</span>'
                )

        else:
            title = escape(str(project))
            description = ""
            tech_html = ""

        projects_html += f"""
        <article class="project-card">

            <div class="project-number">
                PROJECT
            </div>

            <h3>{title}</h3>

            <p>{description}</p>

            <div class="tech-stack">
                {tech_html}
            </div>

        </article>
        """

    # ---------------- EXPERIENCE ----------------

    experience_html = ""

    for item in experience:

        if isinstance(item, dict):

            role = escape(
                str(item.get("role", item.get("title", "Experience")))
            )

            company = escape(
                str(item.get("company", item.get("organization", "")))
            )

            description = escape(
                str(item.get("description", ""))
            )

        else:
            role = escape(str(item))
            company = ""
            description = ""

        experience_html += f"""
        <div class="experience-card">

            <h3>{role}</h3>

            <div class="company">
                {company}
            </div>

            <p>{description}</p>

        </div>
        """

    # ---------------- CERTIFICATIONS ----------------

    certifications_html = ""

    for certification in certifications:

        if isinstance(certification, dict):

            title = escape(
                str(certification.get("name", certification.get("title", "")))
            )

            issuer = escape(
                str(certification.get("issuer", ""))
            )

        else:
            title = escape(str(certification))
            issuer = ""

        certifications_html += f"""
        <div class="certification-card">

            <div class="certificate-icon">
                ✓
            </div>

            <div>
                <h3>{title}</h3>
                <p>{issuer}</p>
            </div>

        </div>
        """

    # ---------------- SOCIAL LINKS ----------------

    social_html = ""

    if github:
        social_html += f"""
        <a href="{github}" target="_blank">GitHub ↗</a>
        """

    if linkedin:
        social_html += f"""
        <a href="{linkedin}" target="_blank">LinkedIn ↗</a>
        """

    if portfolio:
        social_html += f"""
        <a href="{portfolio}" target="_blank">Website ↗</a>
        """

    # ---------------- FINAL HTML ----------------

    return f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>{name} — Portfolio</title>

<style>

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html {{
    scroll-behavior: smooth;
}}

body {{

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    background: #0b0d12;

    color: #f5f5f5;

    line-height: 1.6;
}}

/* ================= NAVBAR ================= */

.navbar {{

    position: sticky;

    top: 0;

    z-index: 100;

    backdrop-filter: blur(18px);

    background: rgba(11,13,18,0.82);

    border-bottom: 1px solid rgba(255,255,255,0.08);

}}

.nav-inner {{

    max-width: 1200px;

    margin: auto;

    padding: 18px 30px;

    display: flex;

    justify-content: space-between;

    align-items: center;

}}

.logo {{

    font-size: 20px;

    font-weight: 800;

    letter-spacing: -0.5px;

}}

.logo span {{

    color: #7c5cff;

}}

.nav-links {{

    display: flex;

    gap: 28px;

}}

.nav-links a {{

    color: #aaa;

    text-decoration: none;

    font-size: 14px;

    transition: 0.25s;

}}

.nav-links a:hover {{

    color: white;

}}

/* ================= HERO ================= */

.hero {{

    max-width: 1200px;

    margin: auto;

    padding: 130px 30px 110px;

    display: grid;

    grid-template-columns: 1.4fr 0.6fr;

    gap: 80px;

    align-items: center;

}}

.badge {{

    display: inline-block;

    padding: 7px 14px;

    border-radius: 100px;

    background: rgba(124,92,255,0.12);

    border: 1px solid rgba(124,92,255,0.3);

    color: #a995ff;

    font-size: 13px;

    margin-bottom: 24px;

}}

.hero h1 {{

    font-size: clamp(52px, 7vw, 90px);

    line-height: 0.95;

    letter-spacing: -5px;

    margin-bottom: 30px;

}}

.hero h1 span {{

    color: #7c5cff;

}}

.hero p {{

    color: #a8a8ad;

    font-size: 19px;

    max-width: 650px;

}}

.hero-card {{

    height: 340px;

    border-radius: 28px;

    background:
        radial-gradient(circle at 30% 30%, #7c5cff55, transparent 35%),
        radial-gradient(circle at 70% 70%, #3a7bd555, transparent 35%),
        #12151d;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0 30px 80px rgba(0,0,0,0.4);

    display: flex;

    align-items: center;

    justify-content: center;

}}

.hero-initial {{

    width: 150px;

    height: 150px;

    border-radius: 50%;

    background: linear-gradient(135deg,#7c5cff,#4b8cff);

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 64px;

    font-weight: 800;

}}

/* ================= SECTIONS ================= */

section {{

    max-width: 1200px;

    margin: auto;

    padding: 100px 30px;

}}

.section-label {{

    color: #7c5cff;

    font-size: 13px;

    text-transform: uppercase;

    letter-spacing: 2px;

    font-weight: 700;

    margin-bottom: 12px;

}}

.section-title {{

    font-size: 42px;

    letter-spacing: -2px;

    margin-bottom: 45px;

}}

.about-text {{

    max-width: 800px;

    color: #aaa;

    font-size: 20px;

}}

/* ================= SKILLS ================= */

.skills-container {{

    display: flex;

    flex-wrap: wrap;

    gap: 12px;

}}

.skill-pill {{

    padding: 11px 18px;

    border-radius: 100px;

    background: #151820;

    border: 1px solid #272b36;

    color: #ddd;

    transition: 0.25s;

}}

.skill-pill:hover {{

    border-color: #7c5cff;

    transform: translateY(-2px);

}}

/* ================= PROJECTS ================= */

.projects-grid {{

    display: grid;

    grid-template-columns:
        repeat(auto-fit,minmax(300px,1fr));

    gap: 22px;

}}

.project-card {{

    padding: 32px;

    min-height: 280px;

    background: #11141b;

    border: 1px solid #252934;

    border-radius: 22px;

    transition: 0.3s;

}}

.project-card:hover {{

    transform: translateY(-8px);

    border-color: #7c5cff;

    box-shadow: 0 20px 50px rgba(0,0,0,0.35);

}}

.project-number {{

    font-size: 11px;

    color: #7c5cff;

    letter-spacing: 2px;

    margin-bottom: 35px;

}}

.project-card h3 {{

    font-size: 25px;

    margin-bottom: 15px;

}}

.project-card p {{

    color: #999;

}}

.tech-stack {{

    margin-top: 22px;

    display: flex;

    gap: 8px;

    flex-wrap: wrap;

}}

.tech-tag {{

    font-size: 11px;

    padding: 5px 10px;

    border-radius: 5px;

    background: #1c2029;

    color: #bbb;

}}

/* ================= TIMELINE ================= */

.timeline-item {{

    position: relative;

    padding-left: 35px;

    padding-bottom: 45px;

    border-left: 1px solid #292d38;

}}

.timeline-dot {{

    position: absolute;

    left: -5px;

    top: 5px;

    width: 9px;

    height: 9px;

    border-radius: 50%;

    background: #7c5cff;

}}

.timeline-content h3 {{

    font-size: 22px;

}}

.timeline-content p {{

    color: #999;

}}

/* ================= EXPERIENCE ================= */

.experience-card {{

    padding: 28px;

    margin-bottom: 16px;

    background: #11141b;

    border: 1px solid #252934;

    border-radius: 18px;

}}

.experience-card h3 {{

    font-size: 22px;

}}

.company {{

    color: #7c5cff;

    margin: 5px 0 12px;

}}

.experience-card p {{

    color: #999;

}}

/* ================= CERTIFICATIONS ================= */

.certification-card {{

    display: flex;

    gap: 18px;

    align-items: center;

    padding: 22px;

    margin-bottom: 14px;

    background: #11141b;

    border: 1px solid #252934;

    border-radius: 16px;

}}

.certificate-icon {{

    width: 45px;

    height: 45px;

    border-radius: 12px;

    background: #7c5cff22;

    color: #a995ff;

    display: flex;

    align-items: center;

    justify-content: center;

    font-weight: 800;

}}

.certification-card p {{

    color: #888;

}}

/* ================= CONTACT ================= */

.contact-section {{

    text-align: center;

}}

.contact-section p {{

    color: #999;

    margin-bottom: 30px;

}}

.social-links {{

    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 12px;

}}

.social-links a {{

    color: white;

    text-decoration: none;

    padding: 12px 20px;

    border-radius: 10px;

    background: #151820;

    border: 1px solid #292d38;

    transition: 0.25s;

}}

.social-links a:hover {{

    background: #7c5cff;

    border-color: #7c5cff;

}}

/* ================= FOOTER ================= */

footer {{

    text-align: center;

    padding: 50px 20px;

    color: #666;

    border-top: 1px solid #1d2028;

}}

/* ================= RESPONSIVE ================= */

@media(max-width: 800px) {{

    .hero {{

        grid-template-columns: 1fr;

        padding-top: 80px;

    }}

    .hero-card {{

        display: none;

    }}

    .nav-links {{

        display: none;

    }}

    .hero h1 {{

        font-size: 60px;

    }}

}}

</style>

</head>

<body>

<!-- NAVBAR -->

<nav class="navbar">

<div class="nav-inner">

<div class="logo">
{name}<span>.</span>
</div>

<div class="nav-links">

<a href="#about">About</a>

<a href="#skills">Skills</a>

<a href="#projects">Projects</a>

<a href="#experience">Experience</a>

<a href="#contact">Contact</a>

</div>

</div>

</nav>


<!-- HERO -->

<header class="hero">

<div>

<div class="badge">
Available for opportunities
</div>

<h1>
Hi, I'm <span>{name}</span>
</h1>

<p>
{about}
</p>

</div>

<div class="hero-card">

<div class="hero-initial">
{name[0] if name else "P"}
</div>

</div>

</header>


<!-- ABOUT -->

<section id="about">

<div class="section-label">
01 — About
</div>

<h2 class="section-title">
A little about me
</h2>

<p class="about-text">
{about}
</p>

</section>


<!-- SKILLS -->

<section id="skills">

<div class="section-label">
02 — Expertise
</div>

<h2 class="section-title">
Skills & Technologies
</h2>

<div class="skills-container">

{skills_html}

</div>

</section>


<!-- PROJECTS -->

<section id="projects">

<div class="section-label">
03 — Selected Work
</div>

<h2 class="section-title">
Projects
</h2>

<div class="projects-grid">

{projects_html}

</div>

</section>


<!-- EXPERIENCE -->

<section id="experience">

<div class="section-label">
04 — Experience
</div>

<h2 class="section-title">
Experience
</h2>

{experience_html}

</section>


<!-- EDUCATION -->

<section>

<div class="section-label">
05 — Education
</div>

<h2 class="section-title">
Education
</h2>

{education_html}

</section>


<!-- CERTIFICATIONS -->

<section>

<div class="section-label">
06 — Certifications
</div>

<h2 class="section-title">
Certifications
</h2>

{certifications_html}

</section>


<!-- CONTACT -->

<section id="contact" class="contact-section">

<div class="section-label">
07 — Contact
</div>

<h2 class="section-title">
Let's connect.
</h2>

<p>
{email}
{phone}
</p>

<div class="social-links">

{social_html}

</div>

</section>


<footer>

© {name} — Built with AI

</footer>

</body>

</html>
"""