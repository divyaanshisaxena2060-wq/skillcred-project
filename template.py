"""
Portfolio Template Engine
Generates self-contained, beautifully styled HTML portfolios across 5 unique standout templates:
1. Midnight Aurora (Deep Dark Glassmorphic & Neon Glow)
2. Neo-Brutalist Pop (Bold High-Contrast, Hard Shadows & Retro Vibe)
3. Nordic Bento Grid (Apple/Linear Clean Modern SaaS Aesthetic)
4. Retro Terminal CLI (Phosphor Hacker Console & Developer CLI)
5. Minimalist Editorial (Swiss / Vogue Luxury Magazine Style)
"""

from html import escape
import json

TEMPLATES = [
    {
        "id": "midnight_aurora",
        "name": "Midnight Aurora",
        "tag": "Most Popular",
        "badge": "Dev & Design",
        "description": "Deep dark canvas with luminous holographic glow, frosted glassmorphism cards, and modern glowing badges.",
        "accent_colors": ["#39ff9d", "#22d3ee", "#8b5cf6"],
        "bg_color": "#060911",
        "font_family": "Space Grotesk & Inter",
        "vibe": "Futuristic & Premium"
    },
    {
        "id": "neo_brutalist",
        "name": "Neo-Brutalist Pop",
        "tag": "Trendsetter",
        "badge": "Bold & High-Energy",
        "description": "High-contrast 3px solid borders, hard offset shadows, vibrant electric yellow/coral/lavender pops, and retro ticker badges.",
        "accent_colors": ["#FFE600", "#FF5E5B", "#6EE7B7"],
        "bg_color": "#FFFDF5",
        "font_family": "Lexend & JetBrains Mono",
        "vibe": "Punchy & Creative"
    },
    {
        "id": "nordic_bento",
        "name": "Nordic Bento Grid",
        "tag": "SaaS Standard",
        "badge": "Clean & Structured",
        "description": "Modern modular bento-box layout with multi-span cards, subtle inner borders, slate tones, and refined micro-metrics.",
        "accent_colors": ["#6366F1", "#38BDF8", "#A855F7"],
        "bg_color": "#0A0D14",
        "font_family": "Plus Jakarta Sans & Inter",
        "vibe": "Polished & Executive"
    },
    {
        "id": "terminal_hacker",
        "name": "Retro Terminal CLI",
        "tag": "Developer Favorite",
        "badge": "Cyberpunk & Hacker",
        "description": "Authentic phosphor CRT console with scanlines, bash prompts, interactive command tabs, and ASCII badge accents.",
        "accent_colors": ["#00FF66", "#00F0FF", "#FFAA00"],
        "bg_color": "#050B08",
        "font_family": "JetBrains Mono & Fira Code",
        "vibe": "Technical & Geek"
    },
    {
        "id": "minimal_editorial",
        "name": "Minimalist Editorial",
        "tag": "Luxury Design",
        "badge": "High Fashion & Luxe",
        "description": "Sophisticated Swiss editorial magazine layout with serif headlines, generous whitespace, numbered project archives, and hairline dividers.",
        "accent_colors": ["#C5A880", "#111111", "#8C827A"],
        "bg_color": "#FAF8F5",
        "font_family": "Playfair Display & Inter",
        "vibe": "Elegant & Timeless"
    }
]

def get_available_templates():
    return TEMPLATES

def get_sample_portfolio_data():
    return {
        "name": "Alex Rivera",
        "about": "Senior Full-Stack Engineer & Creative Developer specializing in scalable distributed systems, real-time architectures, and polished interactive web experiences.",
        "skills": [
            "Python", "TypeScript", "React", "Next.js", "Node.js", "PostgreSQL",
            "FastAPI", "Docker", "AWS", "GraphQL", "Tailwind CSS", "Redis", "GenAI / LLMs"
        ],
        "education": [
            {
                "degree": "B.S. in Computer Science",
                "institution": "University of California, Berkeley",
                "details": "Focus on Distributed Systems & Artificial Intelligence. Magna Cum Laude."
            },
            {
                "degree": "Specialization in Cloud Native Systems",
                "institution": "Stanford Online",
                "details": "Advanced microservices design, Kubernetes orchestration, and cloud architecture."
            }
        ],
        "projects": [
            {
                "title": "AuraFlow Real-time Engine",
                "description": "High-throughput telemetry & analytics pipeline processing 50K+ events/sec with sub-50ms latency using Rust, Kafka, and WebSockets.",
                "technologies": ["Rust", "Kafka", "WebSockets", "TimescaleDB", "React"],
                "link": "https://github.com"
            },
            {
                "title": "HyperSense AI Studio",
                "description": "Interactive collaborative canvas for prompt engineering, multimodal model evaluations, and synthetic dataset generation.",
                "technologies": ["TypeScript", "Next.js", "Python", "FastAPI", "Gemini API"],
                "link": "https://github.com"
            },
            {
                "title": "Prism Design System",
                "description": "Accessible, token-driven component library with zero runtime overhead, adopted across 14 production client applications.",
                "technologies": ["TypeScript", "Vanilla CSS", "Storybook", "Figma API"],
                "link": "https://github.com"
            }
        ],
        "experience": [
            {
                "role": "Lead Software Engineer",
                "company": "Vortex Cloud Technologies",
                "description": "Architected zero-downtime microservices infrastructure serving 1.2M monthly active users. Mentored 8 engineers and cut p99 latency by 42%."
            },
            {
                "role": "Senior Full-Stack Developer",
                "company": "Nexus Labs",
                "description": "Built core real-time collaboration engine and API platform. Integrated Gemini-powered AI workflows boosting developer velocity by 3x."
            },
            {
                "role": "Software Engineer",
                "company": "Starlight Studio",
                "description": "Developed high-performance web applications and internal observability tooling with modern TypeScript and Python backend services."
            }
        ],
        "certifications": [
            {
                "name": "AWS Certified Solutions Architect — Professional",
                "issuer": "Amazon Web Services"
            },
            {
                "name": "Google Cloud Professional Data Engineer",
                "issuer": "Google Cloud"
            }
        ],
        "contact": {
            "email": "alex.rivera@example.com",
            "phone": "+1 (555) 234-5678"
        },
        "social_links": {
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "portfolio": "https://example.com"
        }
    }


def _normalize_data(portfolio_data):
    """Safely extracts and formats fields from the raw portfolio dict."""
    if not isinstance(portfolio_data, dict):
        portfolio_data = {}

    name = escape(str(portfolio_data.get("name") or "My Portfolio"))
    about = escape(str(portfolio_data.get("about") or "Welcome to my portfolio. Explore my background, projects, and skills below."))
    
    raw_skills = portfolio_data.get("skills", [])
    skills = []
    if isinstance(raw_skills, list):
        for s in raw_skills:
            if isinstance(s, dict):
                skills.append(escape(str(s.get("name", s.get("skill", "")))))
            elif s:
                skills.append(escape(str(s)))
    
    raw_education = portfolio_data.get("education", [])
    education = []
    if isinstance(raw_education, list):
        for item in raw_education:
            if isinstance(item, dict):
                education.append({
                    "title": escape(str(item.get("degree", item.get("title", "Degree")))),
                    "details": escape(str(item.get("institution", item.get("details", ""))))
                })
            elif item:
                education.append({"title": escape(str(item)), "details": ""})

    raw_projects = portfolio_data.get("projects", [])
    projects = []
    if isinstance(raw_projects, list):
        for p in raw_projects:
            if isinstance(p, dict):
                title = escape(str(p.get("title", p.get("name", "Featured Project"))))
                desc = escape(str(p.get("description", "")))
                raw_tech = p.get("technologies", p.get("tech_stack", []))
                tech_list = []
                if isinstance(raw_tech, list):
                    tech_list = [escape(str(t)) for t in raw_tech if t]
                elif raw_tech:
                    tech_list = [escape(str(raw_tech))]
                link = escape(str(p.get("link", p.get("url", p.get("github", "")))))
                projects.append({
                    "title": title,
                    "description": desc,
                    "tech": tech_list,
                    "link": link
                })
            elif p:
                projects.append({"title": escape(str(p)), "description": "", "tech": [], "link": ""})

    raw_exp = portfolio_data.get("experience", [])
    experience = []
    if isinstance(raw_exp, list):
        for e in raw_exp:
            if isinstance(e, dict):
                role = escape(str(e.get("role", e.get("title", "Experience"))))
                company = escape(str(e.get("company", e.get("organization", ""))))
                desc = escape(str(e.get("description", "")))
                experience.append({"role": role, "company": company, "description": desc})
            elif e:
                experience.append({"role": escape(str(e)), "company": "", "description": ""})

    raw_certs = portfolio_data.get("certifications", [])
    certifications = []
    if isinstance(raw_certs, list):
        for c in raw_certs:
            if isinstance(c, dict):
                title = escape(str(c.get("name", c.get("title", "Certification"))))
                issuer = escape(str(c.get("issuer", "")))
                certifications.append({"title": title, "issuer": issuer})
            elif c:
                certifications.append({"title": escape(str(c)), "issuer": ""})

    contact = portfolio_data.get("contact", {}) if isinstance(portfolio_data.get("contact"), dict) else {}
    social_links = portfolio_data.get("social_links", {}) if isinstance(portfolio_data.get("social_links"), dict) else {}

    email = escape(str(contact.get("email", "")))
    phone = escape(str(contact.get("phone", "")))

    linkedin = escape(str(social_links.get("linkedin", "")))
    github = escape(str(social_links.get("github", "")))
    portfolio_url = escape(str(social_links.get("portfolio", social_links.get("website", ""))))

    initial = name[0].upper() if name else "P"

    return {
        "name": name,
        "about": about,
        "skills": skills,
        "education": education,
        "projects": projects,
        "experience": experience,
        "certifications": certifications,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "portfolio_url": portfolio_url,
        "initial": initial
    }


# ==============================================================================
# 1. MIDNIGHT AURORA TEMPLATE
# ==============================================================================
def render_midnight_aurora(d):
    skills_html = "".join(f'<span class="skill-pill">{s}</span>' for s in d["skills"])
    
    projects_html = ""
    for idx, p in enumerate(d["projects"], 1):
        tech_tags = "".join(f'<span class="tech-tag">{t}</span>' for t in p["tech"])
        link_markup = f'<a href="{p["link"]}" target="_blank" class="proj-link">View Project ↗</a>' if p["link"] else ""
        projects_html += f"""
        <article class="project-card">
            <div class="project-header">
                <span class="project-num">PROJECT {idx:02d}</span>
                {link_markup}
            </div>
            <h3>{p["title"]}</h3>
            <p>{p["description"]}</p>
            <div class="tech-stack">{tech_tags}</div>
        </article>
        """

    experience_html = ""
    for e in d["experience"]:
        experience_html += f"""
        <div class="experience-card">
            <div class="exp-role-row">
                <h3>{e["role"]}</h3>
                {f'<span class="company-badge">{e["company"]}</span>' if e["company"] else ''}
            </div>
            <p>{e["description"]}</p>
        </div>
        """

    education_html = ""
    for edu in d["education"]:
        education_html += f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h3>{edu["title"]}</h3>
                {f'<p class="inst">{edu["details"]}</p>' if edu["details"] else ''}
            </div>
        </div>
        """

    certs_html = ""
    for c in d["certifications"]:
        certs_html += f"""
        <div class="certification-card">
            <div class="certificate-icon">✦</div>
            <div>
                <h3>{c["title"]}</h3>
                {f'<p>{c["issuer"]}</p>' if c["issuer"] else ''}
            </div>
        </div>
        """

    social_html = ""
    if d["github"]:
        social_html += f'<a href="{d["github"]}" target="_blank" class="social-btn">GitHub ↗</a>'
    if d["linkedin"]:
        social_html += f'<a href="{d["linkedin"]}" target="_blank" class="social-btn">LinkedIn ↗</a>'
    if d["portfolio_url"]:
        social_html += f'<a href="{d["portfolio_url"]}" target="_blank" class="social-btn">Website ↗</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["name"]} — Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: #060911;
    color: #f5f7fa;
    line-height: 1.6;
    overflow-x: hidden;
}}
.aurora-bg {{
    position: fixed; inset: 0; z-index: 0; overflow: hidden; pointer-events: none;
}}
.aurora-ribbon {{
    position: absolute; border-radius: 50%; filter: blur(90px); opacity: 0.35; mix-blend-mode: screen;
}}
.ribbon-1 {{ width: 55vw; height: 55vw; top: -15vw; left: -10vw; background: radial-gradient(circle, #39ff9d, transparent 65%); animation: drift1 24s ease-in-out infinite alternate; }}
.ribbon-2 {{ width: 45vw; height: 45vw; top: 15vw; right: -10vw; background: radial-gradient(circle, #22d3ee, transparent 65%); animation: drift2 28s ease-in-out infinite alternate; }}
.ribbon-3 {{ width: 50vw; height: 50vw; bottom: -10vw; left: 30vw; background: radial-gradient(circle, #8b5cf6, transparent 65%); opacity: 0.25; }}
@keyframes drift1 {{ 0% {{ transform: translate(0,0) scale(1); }} 100% {{ transform: translate(8vw,6vw) scale(1.1); }} }}
@keyframes drift2 {{ 0% {{ transform: translate(0,0) scale(1); }} 100% {{ transform: translate(-7vw,8vw) scale(1.08); }} }}

.navbar {{
    position: sticky; top: 0; z-index: 100;
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    background: rgba(6, 9, 17, 0.75);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}}
.nav-inner {{
    max-width: 1140px; margin: auto; padding: 18px 24px;
    display: flex; justify-content: space-between; align-items: center;
}}
.logo {{
    font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 700;
    display: flex; align-items: center; gap: 8px; color: #fff; text-decoration: none;
}}
.logo span {{ color: #39ff9d; }}
.nav-links {{ display: flex; gap: 24px; }}
.nav-links a {{
    color: #9aa4b2; text-decoration: none; font-size: 14px; font-weight: 500; transition: color 0.2s;
}}
.nav-links a:hover {{ color: #39ff9d; }}
.container {{ max-width: 1140px; margin: auto; padding: 0 24px; position: relative; z-index: 1; }}

.hero {{
    padding: 110px 0 80px;
    display: grid; grid-template-columns: 1.4fr 0.6fr; gap: 60px; align-items: center;
}}
.badge {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 6px 14px; border-radius: 100px;
    background: rgba(57,255,157,0.08); border: 1px solid rgba(57,255,157,0.3);
    color: #39ff9d; font-size: 13px; font-family: 'JetBrains Mono', monospace;
    margin-bottom: 24px;
}}
.hero h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(40px, 6vw, 68px); font-weight: 700; line-height: 1.05;
    letter-spacing: -0.03em; margin-bottom: 24px;
}}
.hero h1 .grad {{
    background: linear-gradient(100deg, #39ff9d, #22d3ee 50%, #8b5cf6);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.hero p {{
    color: #9aa4b2; font-size: 18px; line-height: 1.65; max-width: 620px;
}}
.hero-card {{
    height: 320px; border-radius: 24px;
    background: radial-gradient(circle at 30% 30%, rgba(57,255,157,0.15), transparent 60%),
                radial-gradient(circle at 70% 70%, rgba(139,92,246,0.2), transparent 60%),
                rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 30px 60px rgba(0,0,0,0.5);
    display: flex; align-items: center; justify-content: center;
}}
.hero-initial {{
    width: 140px; height: 140px; border-radius: 50%;
    background: linear-gradient(135deg, #39ff9d, #22d3ee, #8b5cf6);
    display: flex; align-items: center; justify-content: center;
    font-size: 60px; font-weight: 800; color: #060911;
    box-shadow: 0 0 40px rgba(57,255,157,0.4);
}}

section {{ padding: 80px 0; border-top: 1px solid rgba(255,255,255,0.06); }}
.section-label {{
    color: #22d3ee; font-family: 'JetBrains Mono', monospace;
    font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px;
}}
.section-title {{
    font-family: 'Space Grotesk', sans-serif; font-size: 36px; font-weight: 700;
    letter-spacing: -0.02em; margin-bottom: 36px;
}}

.skills-container {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.skill-pill {{
    padding: 10px 18px; border-radius: 100px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
    color: #e2e8f0; font-size: 14px; transition: all 0.25s ease;
}}
.skill-pill:hover {{
    border-color: #39ff9d; background: rgba(57,255,157,0.1);
    transform: translateY(-2px); box-shadow: 0 0 15px rgba(57,255,157,0.2);
}}

.projects-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;
}}
.project-card {{
    padding: 30px; border-radius: 18px;
    background: rgba(255,255,255,0.025); border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease; display: flex; flex-direction: column;
}}
.project-card:hover {{
    transform: translateY(-6px); border-color: rgba(57,255,157,0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 25px rgba(57,255,157,0.1);
}}
.project-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }}
.project-num {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #39ff9d; letter-spacing: 1px; }}
.proj-link {{ color: #22d3ee; text-decoration: none; font-size: 13px; font-weight: 600; }}
.proj-link:hover {{ text-decoration: underline; }}
.project-card h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 22px; margin-bottom: 12px; }}
.project-card p {{ color: #9aa4b2; font-size: 14.5px; line-height: 1.6; margin-bottom: 20px; flex-grow: 1; }}
.tech-stack {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: auto; }}
.tech-tag {{
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    padding: 4px 10px; border-radius: 6px; background: rgba(255,255,255,0.05); color: #cbd5e1;
}}

.experience-card {{
    padding: 26px; border-radius: 16px; margin-bottom: 16px;
    background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07);
}}
.exp-role-row {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px; }}
.exp-role-row h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 20px; }}
.company-badge {{
    padding: 4px 12px; border-radius: 100px; font-size: 12px; font-family: 'JetBrains Mono', monospace;
    background: rgba(34,211,238,0.1); border: 1px solid rgba(34,211,238,0.3); color: #22d3ee;
}}
.experience-card p {{ color: #9aa4b2; font-size: 14.5px; }}

.timeline-item {{
    position: relative; padding-left: 32px; padding-bottom: 36px;
    border-left: 2px solid rgba(255,255,255,0.1);
}}
.timeline-dot {{
    position: absolute; left: -6px; top: 4px; width: 10px; height: 10px;
    border-radius: 50%; background: #39ff9d; box-shadow: 0 0 10px #39ff9d;
}}
.timeline-content h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 18px; }}
.timeline-content .inst {{ color: #9aa4b2; font-size: 14px; margin-top: 4px; }}

.certification-card {{
    display: flex; align-items: center; gap: 16px; padding: 20px; border-radius: 14px;
    background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); margin-bottom: 12px;
}}
.certificate-icon {{
    width: 42px; height: 42px; border-radius: 10px; flex-shrink: 0;
    background: rgba(139,92,246,0.15); border: 1px solid rgba(139,92,246,0.3);
    color: #c4b5fd; display: flex; align-items: center; justify-content: center; font-size: 18px;
}}
.certification-card h3 {{ font-size: 16px; }}
.certification-card p {{ color: #9aa4b2; font-size: 13px; }}

.contact-section {{ text-align: center; }}
.contact-info {{ font-size: 18px; color: #cbd5e1; margin-bottom: 24px; }}
.social-links {{ display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; }}
.social-btn {{
    padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 14px; font-weight: 600;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.12); color: #fff;
    transition: all 0.2s;
}}
.social-btn:hover {{
    background: #39ff9d; color: #060911; border-color: #39ff9d;
    box-shadow: 0 0 20px rgba(57,255,157,0.3); transform: translateY(-2px);
}}

footer {{
    text-align: center; padding: 50px 24px; color: #64748b; font-size: 13px;
    border-top: 1px solid rgba(255,255,255,0.06); font-family: 'JetBrains Mono', monospace;
}}

@media(max-width: 768px) {{
    .hero {{ grid-template-columns: 1fr; padding-top: 60px; }}
    .hero-card {{ display: none; }}
    .nav-links {{ display: none; }}
}}
</style>
</head>
<body>
<div class="aurora-bg">
    <div class="aurora-ribbon ribbon-1"></div>
    <div class="aurora-ribbon ribbon-2"></div>
    <div class="aurora-ribbon ribbon-3"></div>
</div>

<nav class="navbar">
    <div class="nav-inner">
        <a href="#" class="logo">{d["name"]}<span>.</span></a>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#experience">Experience</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
</nav>

<main class="container">
    <header class="hero" id="about">
        <div>
            <div class="badge">● Ready for Opportunities</div>
            <h1>Hi, I'm <span class="grad">{d["name"]}</span></h1>
            <p>{d["about"]}</p>
        </div>
        <div class="hero-card">
            <div class="hero-initial">{d["initial"]}</div>
        </div>
    </header>

    {"<section id='skills'><div class='section-label'>Skills</div><h2 class='section-title'>Core Technologies</h2><div class='skills-container'>" + skills_html + "</div></section>" if skills_html else ""}
    {"<section id='projects'><div class='section-label'>Work</div><h2 class='section-title'>Selected Projects</h2><div class='projects-grid'>" + projects_html + "</div></section>" if projects_html else ""}
    {"<section id='experience'><div class='section-label'>Career</div><h2 class='section-title'>Work Experience</h2>" + experience_html + "</section>" if experience_html else ""}
    {"<section id='education'><div class='section-label'>Background</div><h2 class='section-title'>Education</h2>" + education_html + "</section>" if education_html else ""}
    {"<section id='certifications'><div class='section-label'>Accreditations</div><h2 class='section-title'>Certifications</h2>" + certs_html + "</section>" if certs_html else ""}

    <section id="contact" class="contact-section">
        <div class="section-label">Connect</div>
        <h2 class="section-title">Let's Build Something Together</h2>
        <div class="contact-info">
            {f'<div>Email: <a href="mailto:{d["email"]}" style="color:#22d3ee;text-decoration:none;">{d["email"]}</a></div>' if d["email"] else ''}
            {f'<div>Phone: {d["phone"]}</div>' if d["phone"] else ''}
        </div>
        <div class="social-links">
            {social_html}
        </div>
    </section>
</main>

<footer>
    © {d["name"]} — Built with AI Portfolio Generator
</footer>
</body>
</html>"""


# ==============================================================================
# 2. NEO-BRUTALIST POP TEMPLATE
# ==============================================================================
def render_neo_brutalist(d):
    skills_html = "".join(f'<span class="brutal-pill">{s}</span>' for s in d["skills"])

    projects_html = ""
    colors = ["#FFE600", "#FF5E5B", "#6EE7B7", "#C4B5FD", "#38BDF8"]
    for idx, p in enumerate(d["projects"], 1):
        bg_col = colors[(idx - 1) % len(colors)]
        tech_tags = "".join(f'<span class="brutal-tech">{t}</span>' for t in p["tech"])
        link_markup = f'<a href="{p["link"]}" target="_blank" class="brutal-link">OPEN ↗</a>' if p["link"] else ""
        projects_html += f"""
        <article class="brutal-card project-card" style="--card-accent: {bg_col};">
            <div class="project-header">
                <span class="project-tag">PROJ #{idx:02d}</span>
                {link_markup}
            </div>
            <h3>{p["title"]}</h3>
            <p>{p["description"]}</p>
            <div class="tech-stack">{tech_tags}</div>
        </article>
        """

    experience_html = ""
    for idx, e in enumerate(d["experience"], 1):
        experience_html += f"""
        <div class="brutal-card exp-card">
            <div class="exp-head">
                <h3>{e["role"]}</h3>
                {f'<span class="brutal-badge">{e["company"]}</span>' if e["company"] else ''}
            </div>
            <p>{e["description"]}</p>
        </div>
        """

    education_html = ""
    for edu in d["education"]:
        education_html += f"""
        <div class="brutal-card edu-card">
            <h3>{edu["title"]}</h3>
            {f'<p class="edu-inst">{edu["details"]}</p>' if edu["details"] else ''}
        </div>
        """

    certs_html = ""
    for c in d["certifications"]:
        certs_html += f"""
        <div class="brutal-card cert-card">
            <div class="cert-star">★</div>
            <div>
                <h3>{c["title"]}</h3>
                {f'<p>{c["issuer"]}</p>' if c["issuer"] else ''}
            </div>
        </div>
        """

    social_html = ""
    if d["github"]:
        social_html += f'<a href="{d["github"]}" target="_blank" class="brutal-btn">GITHUB ↗</a>'
    if d["linkedin"]:
        social_html += f'<a href="{d["linkedin"]}" target="_blank" class="brutal-btn" style="background:#38BDF8;">LINKEDIN ↗</a>'
    if d["portfolio_url"]:
        social_html += f'<a href="{d["portfolio_url"]}" target="_blank" class="brutal-btn" style="background:#FFE600;">WEBSITE ↗</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["name"]} — Neo-Brutalist Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend+Mega:wght@500;700;900&family=JetBrains+Mono:wght@500;700&family=Public+Sans:wght@500;600;700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    background-color: #FFFDF5;
    background-image: radial-gradient(#000000 1.2px, transparent 1.2px);
    background-size: 24px 24px;
    color: #111;
    font-family: 'Public Sans', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
}}

/* Neo-Brutalist Utility */
.brutal-card {{
    background: #FFF;
    border: 3px solid #000;
    box-shadow: 6px 6px 0px #000;
    border-radius: 12px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}}
.brutal-card:hover {{
    transform: translate(-3px, -3px);
    box-shadow: 9px 9px 0px #000;
}}
.brutal-btn {{
    display: inline-flex; align-items: center; justify-content: center;
    background: #FFE600; color: #000;
    font-family: 'Lexend Mega', sans-serif; font-size: 13px; font-weight: 700;
    padding: 14px 24px; border: 3px solid #000;
    box-shadow: 4px 4px 0px #000; border-radius: 8px;
    text-decoration: none; cursor: pointer;
    transition: all 0.15s ease;
}}
.brutal-btn:hover {{
    transform: translate(-2px, -2px);
    box-shadow: 6px 6px 0px #000;
}}
.brutal-btn:active {{
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0px #000;
}}

/* Navbar */
.nav-wrap {{
    position: sticky; top: 0; z-index: 100;
    background: #FFFDF5; border-bottom: 3px solid #000;
}}
.nav-inner {{
    max-width: 1140px; margin: auto; padding: 18px 24px;
    display: flex; justify-content: space-between; align-items: center;
}}
.logo {{
    font-family: 'Lexend Mega', sans-serif; font-size: 20px; font-weight: 900;
    background: #FFE600; padding: 6px 14px; border: 3px solid #000;
    box-shadow: 3px 3px 0px #000; border-radius: 6px; text-decoration: none; color: #000;
}}
.nav-links {{ display: flex; gap: 16px; }}
.nav-link {{
    font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700;
    color: #000; text-decoration: none; padding: 6px 12px; border: 2px solid transparent;
    transition: all 0.15s;
}}
.nav-link:hover {{
    border-color: #000; background: #C4B5FD; box-shadow: 3px 3px 0px #000;
}}

/* Ticker Bar */
.ticker-bar {{
    background: #000; color: #FFE600; padding: 10px 0;
    font-family: 'Lexend Mega', sans-serif; font-size: 12px; font-weight: 700;
    overflow: hidden; white-space: nowrap; border-bottom: 3px solid #000;
}}
.ticker-inner {{
    display: inline-block; animation: marquee 25s linear infinite;
}}
@keyframes marquee {{
    0% {{ transform: translateX(0%); }}
    100% {{ transform: translateX(-50%); }}
}}

.container {{ max-width: 1140px; margin: auto; padding: 0 24px; }}

/* Hero */
.hero {{
    padding: 70px 0 50px;
    display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 40px; align-items: center;
}}
.status-pill {{
    display: inline-block; background: #6EE7B7; border: 3px solid #000;
    box-shadow: 4px 4px 0px #000; padding: 6px 16px; border-radius: 100px;
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    margin-bottom: 24px;
}}
.hero h1 {{
    font-family: 'Lexend Mega', sans-serif; font-size: clamp(38px, 5.5vw, 62px);
    font-weight: 900; line-height: 1.1; margin-bottom: 24px; letter-spacing: -0.03em;
}}
.hero-highlight {{
    background: #FFE600; padding: 0 10px; border: 3px solid #000; display: inline-block;
    box-shadow: 4px 4px 0px #000;
}}
.hero p {{
    font-size: 19px; font-weight: 500; color: #222; margin-bottom: 28px;
    max-width: 600px;
}}
.hero-avatar-box {{
    background: #C4B5FD; border: 4px solid #000; box-shadow: 8px 8px 0px #000;
    border-radius: 16px; height: 320px; display: flex; align-items: center; justify-content: center;
    position: relative; overflow: hidden;
}}
.hero-avatar-inner {{
    width: 140px; height: 140px; border-radius: 20px;
    background: #FFE600; border: 4px solid #000; box-shadow: 6px 6px 0px #000;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Lexend Mega', sans-serif; font-size: 64px; font-weight: 900;
}}

/* Sections */
section {{ padding: 60px 0; }}
.section-tag {{
    display: inline-block; background: #FF5E5B; color: #FFF;
    border: 2px solid #000; box-shadow: 3px 3px 0px #000;
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    padding: 4px 12px; border-radius: 4px; margin-bottom: 12px;
}}
.section-title {{
    font-family: 'Lexend Mega', sans-serif; font-size: 32px; font-weight: 900;
    letter-spacing: -0.02em; margin-bottom: 32px;
}}

/* Skills */
.skills-wrap {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.brutal-pill {{
    background: #FFF; border: 3px solid #000; box-shadow: 4px 4px 0px #000;
    padding: 10px 18px; border-radius: 8px;
    font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700;
    transition: all 0.15s ease;
}}
.brutal-pill:hover {{
    background: #FFE600; transform: translate(-2px, -2px); box-shadow: 6px 6px 0px #000;
}}

/* Projects */
.projects-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px;
}}
.project-card {{
    padding: 30px; border-top: 10px solid var(--card-accent, #FFE600);
    display: flex; flex-direction: column;
}}
.project-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
.project-tag {{
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    background: #000; color: #FFF; padding: 2px 8px; border-radius: 4px;
}}
.brutal-link {{
    font-family: 'Lexend Mega', sans-serif; font-size: 11px; font-weight: 700;
    color: #000; text-decoration: none; border-bottom: 2px solid #000;
}}
.project-card h3 {{ font-family: 'Lexend Mega', sans-serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; }}
.project-card p {{ font-size: 15px; color: #333; margin-bottom: 20px; flex-grow: 1; }}
.tech-stack {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.brutal-tech {{
    font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700;
    background: #F1F1F1; border: 2px solid #000; padding: 3px 8px; border-radius: 4px;
}}

/* Experience */
.exp-card {{ padding: 26px; margin-bottom: 20px; }}
.exp-head {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px; }}
.exp-head h3 {{ font-family: 'Lexend Mega', sans-serif; font-size: 18px; font-weight: 700; }}
.brutal-badge {{
    background: #6EE7B7; border: 2px solid #000; box-shadow: 2px 2px 0px #000;
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
    padding: 4px 10px; border-radius: 4px;
}}
.exp-card p {{ color: #333; font-size: 15px; }}

/* Education & Certs */
.edu-card, .cert-card {{ padding: 22px; margin-bottom: 14px; }}
.edu-card h3, .cert-card h3 {{ font-family: 'Lexend Mega', sans-serif; font-size: 17px; font-weight: 700; }}
.edu-inst {{ color: #555; font-size: 14px; margin-top: 4px; font-family: 'JetBrains Mono', monospace; }}
.cert-card {{ display: flex; align-items: center; gap: 16px; }}
.cert-star {{
    width: 44px; height: 44px; background: #FFE600; border: 3px solid #000;
    box-shadow: 3px 3px 0px #000; border-radius: 8px; display: flex; align-items: center;
    justify-content: center; font-size: 20px; flex-shrink: 0; font-weight: 900;
}}

/* Contact */
.contact-box {{
    background: #FFE600; border: 4px solid #000; box-shadow: 8px 8px 0px #000;
    border-radius: 16px; padding: 50px 30px; text-align: center;
}}
.contact-box h2 {{ font-family: 'Lexend Mega', sans-serif; font-size: 32px; font-weight: 900; margin-bottom: 16px; }}
.contact-info-p {{ font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 700; margin-bottom: 28px; }}
.social-row {{ display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }}

footer {{
    border-top: 3px solid #000; padding: 40px 24px; text-align: center;
    font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700;
    background: #FFFDF5;
}}

@media(max-width: 768px) {{
    .hero {{ grid-template-columns: 1fr; }}
    .hero-avatar-box {{ display: none; }}
    .nav-links {{ display: none; }}
}}
</style>
</head>
<body>

<div class="ticker-bar">
    <div class="ticker-inner">
        ⚡ AVAILABLE FOR HIRE ✦ FULL STACK / CREATIVE ✦ OPEN TO COLLABORATION ✦ DESIGN & CODE ✦ READY TO BUILD ✦ HIGH PERFORMANCE ✦
        ⚡ AVAILABLE FOR HIRE ✦ FULL STACK / CREATIVE ✦ OPEN TO COLLABORATION ✦ DESIGN & CODE ✦ READY TO BUILD ✦ HIGH PERFORMANCE ✦
    </div>
</div>

<div class="nav-wrap">
    <div class="nav-inner">
        <a href="#" class="logo">{d["name"]}</a>
        <div class="nav-links">
            <a href="#about" class="nav-link">ABOUT</a>
            <a href="#skills" class="nav-link">SKILLS</a>
            <a href="#projects" class="nav-link">PROJECTS</a>
            <a href="#experience" class="nav-link">EXPERIENCE</a>
            <a href="#contact" class="nav-link">CONTACT</a>
        </div>
    </div>
</div>

<main class="container">
    <header class="hero" id="about">
        <div>
            <div class="status-pill">★ AVAILABLE FOR NEW PROJECTS</div>
            <h1>HEY, I'M <span class="hero-highlight">{d["name"]}</span></h1>
            <p>{d["about"]}</p>
            <div>
                <a href="#contact" class="brutal-btn">GET IN TOUCH ↘</a>
            </div>
        </div>
        <div class="hero-avatar-box">
            <div class="hero-avatar-inner">{d["initial"]}</div>
        </div>
    </header>

    {"<section id='skills'><span class='section-tag'>STACK</span><h2 class='section-title'>SKILLS & TOOLS</h2><div class='skills-wrap'>" + skills_html + "</div></section>" if skills_html else ""}
    {"<section id='projects'><span class='section-tag'>WORK</span><h2 class='section-title'>SELECTED PROJECTS</h2><div class='projects-grid'>" + projects_html + "</div></section>" if projects_html else ""}
    {"<section id='experience'><span class='section-tag'>CAREER</span><h2 class='section-title'>EXPERIENCE</h2>" + experience_html + "</section>" if experience_html else ""}
    {"<section id='education'><span class='section-tag'>STUDIES</span><h2 class='section-title'>EDUCATION</h2>" + education_html + "</section>" if education_html else ""}
    {"<section id='certifications'><span class='section-tag'>BADGES</span><h2 class='section-title'>CERTIFICATIONS</h2>" + certs_html + "</section>" if certs_html else ""}

    <section id="contact">
        <div class="contact-box">
            <h2>LET'S MAKE SOMETHING EPIC</h2>
            <p class="contact-info-p">
                {f'EMAIL: {d["email"]}<br>' if d["email"] else ''}
                {f'PHONE: {d["phone"]}' if d["phone"] else ''}
            </p>
            <div class="social-row">
                {social_html}
            </div>
        </div>
    </section>
</main>

<footer>
    © {d["name"]} ✦ BUILT WITH AI PORTFOLIO GENERATOR
</footer>

</body>
</html>"""


# ==============================================================================
# 3. NORDIC BENTO GRID TEMPLATE
# ==============================================================================
def render_nordic_bento(d):
    skills_chips = "".join(f'<span class="bento-chip">{s}</span>' for s in d["skills"])

    projects_bento = ""
    for idx, p in enumerate(d["projects"], 1):
        tech_tags = "".join(f'<span class="bento-tech">{t}</span>' for t in p["tech"])
        link_markup = f'<a href="{p["link"]}" target="_blank" class="bento-arrow">↗</a>' if p["link"] else '<span class="bento-arrow">✦</span>'
        span_class = "bento-span-2" if idx == 1 else ""
        projects_bento += f"""
        <div class="bento-box project-box {span_class}">
            <div class="bento-top-row">
                <span class="bento-num">PROJ {idx:02d}</span>
                {link_markup}
            </div>
            <h3>{p["title"]}</h3>
            <p>{p["description"]}</p>
            <div class="bento-tech-wrap">{tech_tags}</div>
        </div>
        """

    experience_bento = ""
    for e in d["experience"]:
        experience_bento += f"""
        <div class="bento-box exp-bento">
            <div class="bento-top-row">
                <h3>{e["role"]}</h3>
                {f'<span class="bento-badge">{e["company"]}</span>' if e["company"] else ''}
            </div>
            <p>{e["description"]}</p>
        </div>
        """

    edu_bento = ""
    for edu in d["education"]:
        edu_bento += f"""
        <div class="bento-box edu-bento">
            <h3>{edu["title"]}</h3>
            {f'<p class="edu-sub">{edu["details"]}</p>' if edu["details"] else ''}
        </div>
        """

    cert_bento = ""
    for c in d["certifications"]:
        cert_bento += f"""
        <div class="bento-box cert-bento">
            <div class="cert-icon-bento">✓</div>
            <div>
                <h3>{c["title"]}</h3>
                {f'<p>{c["issuer"]}</p>' if c["issuer"] else ''}
            </div>
        </div>
        """

    social_links_bento = ""
    if d["github"]:
        social_links_bento += f'<a href="{d["github"]}" target="_blank" class="bento-btn">GitHub ↗</a>'
    if d["linkedin"]:
        social_links_bento += f'<a href="{d["linkedin"]}" target="_blank" class="bento-btn">LinkedIn ↗</a>'
    if d["portfolio_url"]:
        social_links_bento += f'<a href="{d["portfolio_url"]}" target="_blank" class="bento-btn">Website ↗</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["name"]} — Bento Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    background: #090C15;
    color: #F8FAFC;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
}}

/* Bento Grid System */
.container {{ max-width: 1160px; margin: auto; padding: 40px 24px; }}
.bento-grid {{
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
}}
.bento-box {{
    background: #111625;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 32px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}}
.bento-box:hover {{
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 30px rgba(99, 102, 241, 0.08);
    transform: translateY(-3px);
}}

/* Header Navigation */
.nav-box {{
    grid-column: span 12;
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 32px;
    background: rgba(17, 22, 37, 0.75);
    backdrop-filter: blur(20px);
}}
.logo {{
    font-size: 18px; font-weight: 800; color: #FFF; text-decoration: none;
    display: flex; align-items: center; gap: 10px;
}}
.logo-dot {{ width: 10px; height: 10px; border-radius: 50%; background: #6366F1; box-shadow: 0 0 12px #6366F1; }}
.nav-links {{ display: flex; gap: 24px; }}
.nav-links a {{ color: #94A3B8; font-size: 14px; font-weight: 600; text-decoration: none; transition: color 0.2s; }}
.nav-links a:hover {{ color: #F8FAFC; }}

/* Hero Boxes */
.hero-main {{
    grid-column: span 8;
    display: flex; flex-direction: column; justify-content: center;
    min-height: 380px;
}}
.hero-tag {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 6px 14px; border-radius: 100px;
    background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818CF8; font-size: 12.5px; font-weight: 600;
    width: fit-content; margin-bottom: 20px;
}}
.hero-main h1 {{
    font-size: clamp(36px, 4.5vw, 56px); font-weight: 800; line-height: 1.1;
    letter-spacing: -0.03em; margin-bottom: 18px;
}}
.hero-main h1 span {{
    background: linear-gradient(135deg, #818CF8, #38BDF8);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.hero-main p {{ font-size: 17px; color: #94A3B8; max-width: 580px; }}

.hero-side {{
    grid-column: span 4;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    background: radial-gradient(circle at center, rgba(99, 102, 241, 0.15), transparent 70%), #111625;
    text-align: center;
}}
.avatar-bento {{
    width: 120px; height: 120px; border-radius: 50%;
    background: linear-gradient(135deg, #6366F1, #38BDF8);
    display: flex; align-items: center; justify-content: center;
    font-size: 52px; font-weight: 800; color: #FFF;
    box-shadow: 0 15px 35px rgba(99, 102, 241, 0.35); margin-bottom: 18px;
}}
.hero-side-title {{ font-size: 16px; font-weight: 700; }}
.hero-side-sub {{ font-size: 13px; color: #94A3B8; margin-top: 4px; }}

/* Section Titles */
.section-span {{ grid-column: span 12; margin-top: 20px; margin-bottom: -6px; }}
.section-label {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #818CF8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }}
.section-title {{ font-size: 28px; font-weight: 800; letter-spacing: -0.02em; }}

/* Skills Bento */
.skills-box {{ grid-column: span 12; }}
.bento-chips-wrap {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }}
.bento-chip {{
    padding: 9px 18px; border-radius: 12px;
    background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 13.5px; font-weight: 600; color: #E2E8F0; transition: all 0.2s;
}}
.bento-chip:hover {{
    background: rgba(99, 102, 241, 0.15); border-color: #6366F1; color: #FFF;
}}

/* Projects */
.project-box {{
    grid-column: span 6; display: flex; flex-direction: column;
}}
.bento-span-2 {{ grid-column: span 12; }}
.bento-top-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
.bento-num {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #818CF8; font-weight: 600; }}
.bento-arrow {{
    width: 32px; height: 32px; border-radius: 50%;
    background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
    display: flex; align-items: center; justify-content: center;
    color: #FFF; text-decoration: none; font-size: 13px; transition: all 0.2s;
}}
.bento-box:hover .bento-arrow {{ background: #6366F1; border-color: #6366F1; }}
.project-box h3 {{ font-size: 21px; font-weight: 700; margin-bottom: 10px; }}
.project-box p {{ color: #94A3B8; font-size: 14.5px; margin-bottom: 20px; flex-grow: 1; }}
.bento-tech-wrap {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.bento-tech {{
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    padding: 4px 10px; border-radius: 8px;
    background: rgba(255, 255, 255, 0.03); color: #CBD5E1;
}}

/* Experience & Edu */
.exp-bento {{ grid-column: span 6; }}
.exp-bento h3 {{ font-size: 18px; font-weight: 700; }}
.bento-badge {{
    padding: 4px 12px; border-radius: 100px;
    background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38BDF8; font-size: 12px; font-weight: 600;
}}
.exp-bento p {{ color: #94A3B8; font-size: 14px; margin-top: 10px; }}

.edu-bento {{ grid-column: span 6; }}
.edu-bento h3 {{ font-size: 17px; font-weight: 700; }}
.edu-sub {{ color: #94A3B8; font-size: 13.5px; margin-top: 6px; }}

.cert-bento {{
    grid-column: span 6; display: flex; align-items: center; gap: 16px;
}}
.cert-icon-bento {{
    width: 44px; height: 44px; border-radius: 14px;
    background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818CF8; display: flex; align-items: center; justify-content: center;
    font-size: 18px; font-weight: 700; flex-shrink: 0;
}}
.cert-bento h3 {{ font-size: 16px; font-weight: 700; }}
.cert-bento p {{ color: #94A3B8; font-size: 13px; }}

/* Contact */
.contact-bento {{
    grid-column: span 12; text-align: center; padding: 60px 32px;
    background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15), transparent 70%), #111625;
}}
.contact-bento h2 {{ font-size: 32px; font-weight: 800; margin-bottom: 12px; }}
.contact-bento p {{ color: #94A3B8; font-size: 16px; margin-bottom: 24px; }}
.contact-btn-row {{ display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; }}
.bento-btn {{
    padding: 12px 24px; border-radius: 14px; text-decoration: none;
    background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
    color: #FFF; font-size: 14px; font-weight: 600; transition: all 0.2s;
}}
.bento-btn:hover {{
    background: #6366F1; border-color: #6366F1; transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
}}

.footer-box {{
    grid-column: span 12; text-align: center; padding: 24px;
    font-size: 13px; color: #64748B;
}}

@media(max-width: 900px) {{
    .hero-main {{ grid-column: span 12; }}
    .hero-side {{ display: none; }}
    .project-box, .exp-bento, .edu-bento, .cert-bento {{ grid-column: span 12; }}
}}
</style>
</head>
<body>

<div class="container">
    <div class="bento-grid">
        <!-- Navigation -->
        <div class="bento-box nav-box">
            <a href="#" class="logo"><span class="logo-dot"></span>{d["name"]}</a>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#experience">Experience</a>
                <a href="#contact">Contact</a>
            </div>
        </div>

        <!-- Hero -->
        <div class="bento-box hero-main" id="about">
            <div class="hero-tag">● Available for Work</div>
            <h1>Building with precision &amp; <span>vision</span>.</h1>
            <p>{d["about"]}</p>
        </div>
        <div class="bento-box hero-side">
            <div class="avatar-bento">{d["initial"]}</div>
            <div class="hero-side-title">{d["name"]}</div>
            <div class="hero-side-sub">Portfolio &amp; Showcase</div>
        </div>

        <!-- Skills -->
        {"<div class='section-span' id='skills'><div class='section-label'>Stack</div><div class='section-title'>Core Technologies</div></div><div class='bento-box skills-box'><div class='bento-chips-wrap'>" + skills_chips + "</div></div>" if skills_chips else ""}

        <!-- Projects -->
        {"<div class='section-span' id='projects'><div class='section-label'>Showcase</div><div class='section-title'>Featured Work</div></div>" + projects_bento if projects_bento else ""}

        <!-- Experience -->
        {"<div class='section-span' id='experience'><div class='section-label'>History</div><div class='section-title'>Work Experience</div></div>" + experience_bento if experience_bento else ""}

        <!-- Education -->
        {"<div class='section-span' id='education'><div class='section-label'>Academics</div><div class='section-title'>Education</div></div>" + edu_bento if edu_bento else ""}

        <!-- Certifications -->
        {"<div class='section-span' id='certifications'><div class='section-label'>Credentials</div><div class='section-title'>Certifications</div></div>" + cert_bento if cert_bento else ""}

        <!-- Contact -->
        <div class="bento-box contact-bento" id="contact">
            <h2>Let's connect</h2>
            <p>{f'Email: {d["email"]} &nbsp;·&nbsp; ' if d["email"] else ''}{f'Phone: {d["phone"]}' if d["phone"] else ''}</p>
            <div class="contact-btn-row">
                {social_links_bento}
            </div>
        </div>

        <div class="footer-box">
            © {d["name"]} — Built with AI Portfolio Generator
        </div>
    </div>
</div>

</body>
</html>"""


# ==============================================================================
# 4. RETRO TERMINAL CLI TEMPLATE
# ==============================================================================
def render_terminal_hacker(d):
    skills_json = json.dumps(d["skills"], indent=2)

    projects_cli = ""
    for idx, p in enumerate(d["projects"], 1):
        tech_str = ", ".join(p["tech"])
        link_str = f'<a href="{p["link"]}" target="_blank" class="term-link">[LAUNCH_URL ↗]</a>' if p["link"] else ""
        projects_cli += f"""
        <div class="term-block">
            <div class="term-cmd"><span class="prompt">$</span> git log --project="{idx}"</div>
            <div class="term-output">
                <div class="proj-title">commit #{idx:03d}: {p["title"]} {link_str}</div>
                <div class="proj-desc">{p["description"]}</div>
                <div class="proj-stack"><span class="cyan">STACK:</span> [{tech_str}]</div>
            </div>
        </div>
        """

    experience_cli = ""
    for e in d["experience"]:
        experience_cli += f"""
        <div class="term-block">
            <div class="term-cmd"><span class="prompt">$</span> cat /experience/{e["company"].lower().replace(' ', '_') or 'role'}.txt</div>
            <div class="term-output">
                <div class="role-name">> {e["role"]} {f'@ [{e["company"]}]' if e["company"] else ''}</div>
                <p>{e["description"]}</p>
            </div>
        </div>
        """

    education_cli = ""
    for edu in d["education"]:
        education_cli += f"""
        <div class="term-row">
            <span class="yellow">></span> <b>{edu["title"]}</b> {f'— {edu["details"]}' if edu["details"] else ''}
        </div>
        """

    certs_cli = ""
    for c in d["certifications"]:
        certs_cli += f"""
        <div class="term-row">
            <span class="green">[CERT_VERIFIED]</span> <b>{c["title"]}</b> {f'({c["issuer"]})' if c["issuer"] else ''}
        </div>
        """

    social_cli = ""
    if d["github"]:
        social_cli += f'<a href="{d["github"]}" target="_blank" class="term-btn">./github.sh</a>'
    if d["linkedin"]:
        social_cli += f'<a href="{d["linkedin"]}" target="_blank" class="term-btn">./linkedin.sh</a>'
    if d["portfolio_url"]:
        social_cli += f'<a href="{d["portfolio_url"]}" target="_blank" class="term-btn">./website.sh</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["name"]} — Terminal CLI Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=VT323&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    background: #050B08;
    color: #00FF66;
    font-family: 'JetBrains Mono', monospace;
    line-height: 1.6;
    overflow-x: hidden;
    padding: 30px 16px;
}}

/* CRT Scanline Effect */
body::before {{
    content: " ";
    display: block;
    position: fixed;
    top: 0; left: 0; bottom: 0; right: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
    z-index: 999;
    background-size: 100% 3px, 6px 100%;
    pointer-events: none;
    opacity: 0.6;
}}

.terminal-window {{
    max-width: 1040px; margin: 0 auto;
    background: rgba(8, 18, 12, 0.95);
    border: 1px solid #00FF66;
    border-radius: 12px;
    box-shadow: 0 0 30px rgba(0, 255, 102, 0.18), inset 0 0 20px rgba(0, 255, 102, 0.05);
    overflow: hidden;
}}

/* Terminal Title Bar */
.term-bar {{
    background: #0D2418;
    border-bottom: 1px solid #00FF66;
    padding: 12px 20px;
    display: flex; justify-content: space-between; align-items: center;
}}
.term-dots {{ display: flex; gap: 8px; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; display: inline-block; }}
.dot-red {{ background: #FF5F56; }}
.dot-yellow {{ background: #FFBD2E; }}
.dot-green {{ background: #27C93F; }}
.term-title {{ font-size: 13px; font-weight: 700; color: #88FFAA; }}

.term-body {{ padding: 36px 30px; }}

/* Text & Colors */
.prompt {{ color: #00F0FF; font-weight: 700; margin-right: 8px; }}
.green {{ color: #00FF66; }}
.cyan {{ color: #00F0FF; }}
.yellow {{ color: #FFCC00; }}
.gray {{ color: #5C826C; }}
.dim {{ color: #88B89C; }}

.ascii-header {{
    font-size: 12px; line-height: 1.2; color: #00F0FF; margin-bottom: 24px;
    overflow-x: auto; white-space: pre; text-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
}}

.cursor {{
    display: inline-block; width: 8px; height: 16px; background: #00FF66;
    animation: blink 1s step-end infinite; vertical-align: middle; margin-left: 4px;
}}
@keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}

/* Navigation Tabs */
.term-nav {{
    display: flex; gap: 14px; flex-wrap: wrap; margin: 24px 0 36px;
    border-bottom: 1px dashed #00FF66; padding-bottom: 16px;
}}
.term-nav a {{
    color: #00F0FF; text-decoration: none; font-size: 13px;
    padding: 4px 10px; border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 4px;
    transition: all 0.2s;
}}
.term-nav a:hover {{ background: #00F0FF; color: #050B08; }}

/* Content Blocks */
.term-section {{ margin-bottom: 40px; }}
.term-sec-head {{
    font-size: 18px; font-weight: 700; color: #00F0FF; margin-bottom: 16px;
    text-transform: uppercase; letter-spacing: 1px;
}}
.term-block {{
    background: rgba(0, 255, 102, 0.03); border-left: 2px solid #00FF66;
    padding: 16px 20px; margin-bottom: 16px; border-radius: 0 8px 8px 0;
}}
.term-cmd {{ color: #88FFAA; font-weight: 600; margin-bottom: 8px; font-size: 13.5px; }}
.term-output {{ padding-left: 10px; }}
.proj-title {{ font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 6px; }}
.proj-desc {{ color: #A0D8B6; font-size: 14px; margin-bottom: 10px; }}
.proj-stack {{ font-size: 12.5px; color: #88B89C; }}
.term-link {{ color: #00F0FF; text-decoration: none; font-size: 12px; margin-left: 10px; }}
.term-link:hover {{ text-decoration: underline; }}

.role-name {{ font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 6px; }}
.term-output p {{ color: #A0D8B6; font-size: 13.5px; }}

.term-row {{ margin-bottom: 10px; font-size: 14px; color: #D0F8E0; }}

/* Skills JSON display */
.json-display {{
    background: #030805; padding: 18px; border-radius: 6px;
    border: 1px solid rgba(0, 255, 102, 0.3); font-size: 13px; color: #88FFAA;
    overflow-x: auto;
}}

/* Contact & Buttons */
.term-btn {{
    display: inline-block; padding: 8px 18px; border-radius: 4px;
    border: 1px solid #00FF66; color: #00FF66; text-decoration: none;
    font-size: 13px; font-weight: 700; transition: all 0.2s;
}}
.term-btn:hover {{
    background: #00FF66; color: #050B08; box-shadow: 0 0 15px #00FF66;
}}
.btn-group {{ display: flex; gap: 12px; flex-wrap: wrap; margin-top: 14px; }}

footer {{
    text-align: center; margin-top: 40px; color: #5C826C; font-size: 12px;
}}
</style>
</head>
<body>

<div class="terminal-window">
    <div class="term-bar">
        <div class="term-dots">
            <span class="dot dot-red"></span>
            <span class="dot dot-yellow"></span>
            <span class="dot dot-green"></span>
        </div>
        <div class="term-title">user@{d["name"].lower().replace(' ', '')}: ~ (zsh)</div>
        <div class="gray">UTF-8</div>
    </div>

    <div class="term-body">
        <div class="ascii-header">
+-------------------------------------------------------+
|  SYSTEM INITIALIZED: AI PORTFOLIO TERMINAL v2.5.0     |
|  HOST: {d["name"].upper()} // STATUS: READY_TO_DEPLOY |
+-------------------------------------------------------+</div>

        <div class="term-nav">
            <a href="#about">[01_ABOUT]</a>
            <a href="#skills">[02_SKILLS]</a>
            <a href="#projects">[03_PROJECTS]</a>
            <a href="#experience">[04_EXPERIENCE]</a>
            <a href="#contact">[05_CONTACT]</a>
        </div>

        <div class="term-section" id="about">
            <div class="term-cmd"><span class="prompt">$</span> whoami --verbose</div>
            <div class="term-output">
                <p class="green" style="font-size:18px; font-weight:700;">{d["name"]}<span class="cursor"></span></p>
                <p class="dim" style="margin-top:8px;">{d["about"]}</p>
            </div>
        </div>

        {"<div class='term-section' id='skills'><div class='term-sec-head'>STACK &amp; CAPABILITIES</div><div class='term-cmd'><span class='prompt'>$</span> cat ./skills.json</div><pre class='json-display'>" + skills_json + "</pre></div>" if d["skills"] else ""}

        {"<div class='term-section' id='projects'><div class='term-sec-head'>REPOSITORIES &amp; PROJECTS</div>" + projects_cli + "</div>" if projects_cli else ""}

        {"<div class='term-section' id='experience'><div class='term-sec-head'>EXPERIENCE LOGS</div>" + experience_cli + "</div>" if experience_cli else ""}

        {"<div class='term-section' id='education'><div class='term-sec-head'>ACADEMIC RECORDS</div>" + education_cli + "</div>" if education_cli else ""}

        {"<div class='term-section' id='certifications'><div class='term-sec-head'>CERTIFICATIONS</div>" + certs_cli + "</div>" if certs_cli else ""}

        <div class="term-section" id="contact">
            <div class="term-sec-head">TRANSMIT MESSAGE</div>
            <div class="term-cmd"><span class="prompt">$</span> ./ping_contact.sh</div>
            <div class="term-output">
                {f'<p class="cyan">EMAIL: {d["email"]}</p>' if d["email"] else ''}
                {f'<p class="yellow">PHONE: {d["phone"]}</p>' if d["phone"] else ''}
                <div class="btn-group">
                    {social_cli}
                </div>
            </div>
        </div>

        <footer>
            [PROCESS COMPLETED WITH EXIT CODE 0] &nbsp;·&nbsp; © {d["name"]}
        </footer>
    </div>
</div>

</body>
</html>"""


# ==============================================================================
# 5. MINIMALIST EDITORIAL TEMPLATE
# ==============================================================================
def render_minimal_editorial(d):
    skills_html = "".join(f'<span class="edit-pill">{s}</span>' for s in d["skills"])

    projects_html = ""
    for idx, p in enumerate(d["projects"], 1):
        tech_tags = " · ".join(p["tech"])
        link_markup = f'<a href="{p["link"]}" target="_blank" class="edit-proj-link">Read Archive ↗</a>' if p["link"] else ""
        projects_html += f"""
        <article class="edit-project-row">
            <div class="edit-proj-num">({idx:02d})</div>
            <div class="edit-proj-content">
                <div class="edit-proj-head">
                    <h3>{p["title"]}</h3>
                    {link_markup}
                </div>
                <p>{p["description"]}</p>
                {f'<div class="edit-tech">{tech_tags}</div>' if tech_tags else ''}
            </div>
        </article>
        """

    experience_html = ""
    for e in d["experience"]:
        experience_html += f"""
        <div class="edit-exp-row">
            <div class="edit-exp-role">
                <h3>{e["role"]}</h3>
                {f'<span class="edit-company">{e["company"]}</span>' if e["company"] else ''}
            </div>
            <div class="edit-exp-desc">
                <p>{e["description"]}</p>
            </div>
        </div>
        """

    education_html = ""
    for edu in d["education"]:
        education_html += f"""
        <div class="edit-edu-row">
            <h3>{edu["title"]}</h3>
            {f'<p>{edu["details"]}</p>' if edu["details"] else ''}
        </div>
        """

    certs_html = ""
    for c in d["certifications"]:
        certs_html += f"""
        <div class="edit-cert-item">
            <span class="cert-bullet">◆</span>
            <div>
                <h3>{c["title"]}</h3>
                {f'<p>{c["issuer"]}</p>' if c["issuer"] else ''}
            </div>
        </div>
        """

    social_html = ""
    if d["github"]:
        social_html += f'<a href="{d["github"]}" target="_blank" class="edit-social-link">GitHub ↗</a>'
    if d["linkedin"]:
        social_html += f'<a href="{d["linkedin"]}" target="_blank" class="edit-social-link">LinkedIn ↗</a>'
    if d["portfolio_url"]:
        social_html += f'<a href="{d["portfolio_url"]}" target="_blank" class="edit-social-link">Website ↗</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["name"]} — Selected Works</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    background: #FAF8F5;
    color: #1A1A1A;
    font-family: 'Newsreader', serif;
    line-height: 1.7;
    overflow-x: hidden;
    padding: 0;
}}

.editorial-wrap {{
    max-width: 980px;
    margin: 0 auto;
    padding: 0 32px;
}}

/* Navbar */
nav {{
    border-bottom: 1px solid #E2DCD5;
    padding: 28px 0;
    display: flex; justify-content: space-between; align-items: baseline;
}}
.nav-name {{
    font-family: 'Cinzel', serif; font-size: 20px; font-weight: 700;
    letter-spacing: 0.1em; text-transform: uppercase; color: #1A1A1A; text-decoration: none;
}}
.nav-links {{ display: flex; gap: 32px; font-family: 'Inter', sans-serif; font-size: 13px; text-transform: uppercase; letter-spacing: 0.08em; }}
.nav-links a {{ color: #7A726A; text-decoration: none; transition: color 0.2s; }}
.nav-links a:hover {{ color: #1A1A1A; }}

/* Hero */
.hero {{
    padding: 100px 0 70px;
    border-bottom: 1px solid #E2DCD5;
}}
.hero-issue {{
    font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase;
    letter-spacing: 0.18em; color: #9E958C; margin-bottom: 24px;
}}
.hero h1 {{
    font-family: 'Newsreader', serif; font-weight: 400;
    font-size: clamp(44px, 7vw, 76px); line-height: 1.05; letter-spacing: -0.02em;
    margin-bottom: 32px; color: #111;
}}
.hero h1 em {{ font-style: italic; font-weight: 300; }}
.hero-narrative {{
    font-size: 23px; color: #4A443E; font-weight: 400;
    max-width: 720px; line-height: 1.55;
}}

/* Sections */
section {{
    padding: 70px 0;
    border-bottom: 1px solid #E2DCD5;
}}
.section-meta {{
    display: flex; justify-content: space-between; align-items: baseline;
    margin-bottom: 40px;
}}
.section-tag {{
    font-family: 'Inter', sans-serif; font-size: 11.5px; text-transform: uppercase;
    letter-spacing: 0.15em; color: #9E958C;
}}
.section-title {{
    font-family: 'Newsreader', serif; font-size: 36px; font-weight: 400;
    font-style: italic;
}}

/* Skills */
.skills-list {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.edit-pill {{
    font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500;
    padding: 8px 18px; border: 1px solid #DCD5CC; border-radius: 100px;
    background: #FFF; color: #2B2621; transition: all 0.2s;
}}
.edit-pill:hover {{
    border-color: #1A1A1A; background: #1A1A1A; color: #FFF;
}}

/* Projects */
.edit-project-row {{
    display: grid; grid-template-columns: 80px 1fr; gap: 24px;
    padding: 36px 0; border-top: 1px solid #EDE7DF;
}}
.edit-project-row:first-of-type {{ border-top: none; padding-top: 0; }}
.edit-proj-num {{
    font-family: 'Newsreader', serif; font-size: 20px; font-style: italic; color: #9E958C;
}}
.edit-proj-head {{
    display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;
}}
.edit-proj-head h3 {{
    font-family: 'Newsreader', serif; font-size: 28px; font-weight: 500; letter-spacing: -0.01em;
}}
.edit-proj-link {{
    font-family: 'Inter', sans-serif; font-size: 12px; text-transform: uppercase;
    letter-spacing: 0.1em; color: #1A1A1A; text-decoration: none; border-bottom: 1px solid #1A1A1A;
}}
.edit-proj-content p {{
    font-size: 17px; color: #5C544C; margin-bottom: 14px; max-width: 680px;
}}
.edit-tech {{
    font-family: 'Inter', sans-serif; font-size: 12px; color: #8C8278; text-transform: uppercase;
    letter-spacing: 0.05em;
}}

/* Experience */
.edit-exp-row {{
    display: grid; grid-template-columns: 280px 1fr; gap: 32px;
    padding: 30px 0; border-top: 1px solid #EDE7DF;
}}
.edit-exp-row:first-of-type {{ border-top: none; padding-top: 0; }}
.edit-exp-role h3 {{ font-family: 'Newsreader', serif; font-size: 22px; font-weight: 500; }}
.edit-company {{
    font-family: 'Inter', sans-serif; font-size: 12.5px; text-transform: uppercase;
    letter-spacing: 0.08em; color: #8C8278; display: block; margin-top: 4px;
}}
.edit-exp-desc p {{ font-size: 17px; color: #5C544C; }}

/* Education & Certs */
.edit-edu-row {{ padding: 20px 0; border-top: 1px solid #EDE7DF; }}
.edit-edu-row:first-of-type {{ border-top: none; }}
.edit-edu-row h3 {{ font-family: 'Newsreader', serif; font-size: 21px; }}
.edit-edu-row p {{ font-family: 'Inter', sans-serif; font-size: 13.5px; color: #7A726A; margin-top: 4px; }}

.edit-cert-item {{ display: flex; align-items: baseline; gap: 14px; padding: 14px 0; }}
.cert-bullet {{ font-size: 10px; color: #9E958C; }}
.edit-cert-item h3 {{ font-family: 'Newsreader', serif; font-size: 19px; }}
.edit-cert-item p {{ font-family: 'Inter', sans-serif; font-size: 13px; color: #8C8278; }}

/* Contact */
.contact-edit {{
    padding: 90px 0 60px; text-align: center;
}}
.contact-edit h2 {{
    font-family: 'Newsreader', serif; font-size: 46px; font-weight: 400;
    font-style: italic; margin-bottom: 20px;
}}
.contact-info-text {{
    font-family: 'Inter', sans-serif; font-size: 15px; color: #5C544C; margin-bottom: 32px;
}}
.social-edit-row {{ display: flex; justify-content: center; gap: 24px; }}
.edit-social-link {{
    font-family: 'Inter', sans-serif; font-size: 13px; text-transform: uppercase;
    letter-spacing: 0.1em; color: #1A1A1A; text-decoration: none;
    border-bottom: 1px solid #1A1A1A; padding-bottom: 2px;
}}

footer {{
    padding: 40px 0; text-align: center;
    font-family: 'Inter', sans-serif; font-size: 12px; color: #9E958C;
    letter-spacing: 0.05em;
}}

@media(max-width: 768px) {{
    .edit-project-row {{ grid-template-columns: 1fr; }}
    .edit-exp-row {{ grid-template-columns: 1fr; gap: 10px; }}
    .nav-links {{ display: none; }}
}}
</style>
</head>
<body>

<div class="editorial-wrap">
    <nav>
        <a href="#" class="nav-name">{d["name"]}</a>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#skills">Expertise</a>
            <a href="#projects">Archive</a>
            <a href="#experience">History</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <header class="hero" id="about">
        <div class="hero-issue">PORTFOLIO EDITION // VOL. I</div>
        <h1>Selected Works of <em>{d["name"]}</em></h1>
        <div class="hero-narrative">{d["about"]}</div>
    </header>

    {"<section id='skills'><div class='section-meta'><span class='section-tag'>01 — Disciplines</span><h2 class='section-title'>Core Competencies</h2></div><div class='skills-list'>" + skills_html + "</div></section>" if skills_html else ""}

    {"<section id='projects'><div class='section-meta'><span class='section-tag'>02 — Selected Works</span><h2 class='section-title'>Project Archive</h2></div>" + projects_html + "</div></section>" if projects_html else ""}

    {"<section id='experience'><div class='section-meta'><span class='section-tag'>03 — Career</span><h2 class='section-title'>Work History</h2></div>" + experience_html + "</section>" if experience_html else ""}

    {"<section id='education'><div class='section-meta'><span class='section-tag'>04 — Academics</span><h2 class='section-title'>Education</h2></div>" + education_html + "</section>" if education_html else ""}

    {"<section id='certifications'><div class='section-meta'><span class='section-tag'>05 — Accreditations</span><h2 class='section-title'>Certifications</h2></div>" + certs_html + "</section>" if certs_html else ""}

    <section id="contact" class="contact-edit">
        <h2>Inquiries &amp; Collaboration</h2>
        <div class="contact-info-text">
            {f'<span>{d["email"]}</span><br>' if d["email"] else ''}
            {f'<span>{d["phone"]}</span>' if d["phone"] else ''}
        </div>
        <div class="social-edit-row">
            {social_html}
        </div>
    </section>

    <footer>
        © {d["name"]} — CURATED VIA AI PORTFOLIO GENERATOR
    </footer>
</div>

</body>
</html>"""


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def build_portfolio_html(portfolio_data, theme="midnight_aurora"):
    """
    Builds a standalone portfolio HTML page based on the selected theme template.
    Supported themes:
    - 'midnight_aurora' (Default)
    - 'neo_brutalist'
    - 'nordic_bento'
    - 'terminal_hacker'
    - 'minimal_editorial'
    """
    normalized = _normalize_data(portfolio_data)

    theme_renderers = {
        "midnight_aurora": render_midnight_aurora,
        "neo_brutalist": render_neo_brutalist,
        "nordic_bento": render_nordic_bento,
        "terminal_hacker": render_terminal_hacker,
        "minimal_editorial": render_minimal_editorial
    }

    renderer = theme_renderers.get(theme, render_midnight_aurora)
    return renderer(normalized)