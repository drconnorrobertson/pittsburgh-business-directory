#!/usr/bin/env python3
import os
from pathlib import Path

base_url = "https://pittsburghbusinessdirectory.com"

# Template for blog pages
blog_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} - Pittsburgh Business Directory Blog</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{url}" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "{title}",
    "description": "{description}",
    "url": "{url}",
    "datePublished": "2026-05-02",
    "dateModified": "2026-05-02",
    "author": {{
      "@type": "Organization",
      "name": "Pittsburgh Business Directory"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Pittsburgh Business Directory",
      "logo": {{
        "@type": "ImageObject",
        "url": "{base_url}/logo.png"
      }}
    }}
  }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --charcoal: #1a1a1a;
      --gold: #C8A040;
      --steel-gray: #444;
      --light-gray: #f5f5f5;
      --border-gray: #ddd;
      --text-dark: #333;
      --text-light: #666;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      color: var(--text-dark);
      line-height: 1.6;
      background: #fff;
    }}

    a {{
      color: var(--gold);
      text-decoration: none;
      transition: color 0.3s ease;
    }}

    header {{
      background: var(--charcoal);
      border-bottom: 3px solid var(--gold);
      padding: 20px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .logo {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .logo-text {{
      color: var(--gold);
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 1px;
    }}

    .logo-tagline {{
      color: #aaa;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }}

    nav a {{
      color: #fff;
      margin: 0 20px;
      font-weight: 500;
      font-size: 14px;
      transition: color 0.3s ease;
    }}

    nav a:hover {{
      color: var(--gold);
    }}

    .post-header {{
      background: linear-gradient(135deg, var(--charcoal) 0%, var(--steel-gray) 100%);
      color: #fff;
      padding: 60px 20px;
      text-align: center;
    }}

    .post-header h1 {{
      font-family: 'Playfair Display', serif;
      font-size: 2.8rem;
      font-weight: 700;
      margin-bottom: 20px;
      line-height: 1.2;
    }}

    .post-header p {{
      font-size: 16px;
      color: #ddd;
    }}

    .post-content {{
      max-width: 800px;
      margin: 0 auto;
      padding: 60px 20px;
    }}

    .post-content h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 1.8rem;
      margin: 40px 0 20px 0;
      color: var(--charcoal);
    }}

    .post-content h3 {{
      font-family: 'Playfair Display', serif;
      font-size: 1.4rem;
      margin: 30px 0 15px 0;
      color: var(--charcoal);
    }}

    .post-content p {{
      margin-bottom: 20px;
      color: var(--text-light);
      line-height: 1.8;
    }}

    .post-content ul {{
      margin-left: 20px;
      margin-bottom: 20px;
    }}

    .post-content li {{
      margin-bottom: 12px;
      color: var(--text-light);
      line-height: 1.8;
    }}

    .cta-box {{
      background: var(--light-gray);
      padding: 30px;
      border-radius: 8px;
      border-left: 4px solid var(--gold);
      margin: 40px 0;
    }}

    .cta-box h3 {{
      margin-bottom: 10px;
      color: var(--charcoal);
    }}

    footer {{
      background: var(--charcoal);
      color: #ccc;
      padding: 40px 20px;
      border-top: 1px solid var(--steel-gray);
      font-size: 13px;
    }}

    footer a {{
      color: var(--gold);
    }}

    .footer-content {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 30px;
      margin-bottom: 30px;
    }}

    .footer-section h3 {{
      margin-bottom: 15px;
      color: #fff;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .footer-section ul {{
      list-style: none;
    }}

    .footer-section li {{
      margin-bottom: 10px;
    }}

    .footer-bottom {{
      border-top: 1px solid var(--steel-gray);
      padding-top: 20px;
      text-align: center;
      color: #888;
    }}

    @media (max-width: 768px) {{
      .post-header h1 {{
        font-size: 1.8rem;
      }}

      nav a {{
        margin: 0 10px;
        font-size: 12px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="container">
      <div class="header-inner">
        <div class="logo">
          <span class="logo-text">PGH BUSINESS</span>
          <span class="logo-tagline">Editorial Directory</span>
        </div>
        <nav>
          <a href="/">Home</a>
          <a href="/about/">About</a>
          <a href="/category/restaurants/">Categories</a>
          <a href="/neighborhood/lawrenceville/">Neighborhoods</a>
          <a href="/blog/">Blog</a>
          <a href="/submit/">Submit</a>
        </nav>
      </div>
    </div>
  </header>

  <section class="post-header">
    <div class="container">
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </div>
  </section>

  <article class="post-content">
    {content}

    <div class="cta-box">
      <h3>Discover More Businesses</h3>
      <p>Browse our full directory of Pittsburgh businesses, or submit your business for consideration.</p>
      <a href="/submit/" style="font-weight: 600;">Submit Your Business</a>
    </div>
  </article>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>Directory</h3>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/submit/">Submit Business</a></li>
            <li><a href="/contact/">Contact</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Categories</h3>
          <ul>
            <li><a href="/category/restaurants/">Restaurants</a></li>
            <li><a href="/category/technology/">Technology</a></li>
            <li><a href="/category/real-estate/">Real Estate</a></li>
            <li><a href="/category/health-wellness/">Health & Wellness</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Neighborhoods</h3>
          <ul>
            <li><a href="/neighborhood/lawrenceville/">Lawrenceville</a></li>
            <li><a href="/neighborhood/strip-district/">Strip District</a></li>
            <li><a href="/neighborhood/downtown/">Downtown</a></li>
            <li><a href="/neighborhood/shadyside/">Shadyside</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Resources</h3>
          <ul>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/feed.xml">RSS Feed</a></li>
            <li><a href="https://thepittsburghwire.com">Pittsburgh Wire</a></li>
            <li><a href="/sitemap.xml">Sitemap</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>Pittsburgh Business Directory. Founded by Dr. Connor Robertson. A sister publication of <a href="https://thepittsburghwire.com">The Pittsburgh Wire</a>.</p>
        <p style="margin-top: 10px;">&copy; 2026 Pittsburgh Business Directory. All rights reserved.</p>
      </div>
    </div>
  </footer>
</body>
</html>
'''

# Blog posts data
blog_posts = {
    "best-restaurants-pittsburgh-2026": {
        "title": "Best Restaurants in Pittsburgh 2026",
        "subtitle": "A curated guide to the city's most innovative dining establishments",
        "description": "Comprehensive guide to the best restaurants in Pittsburgh, featuring profiles of innovative chefs and dining establishments.",
        "content": """<h2>Pittsburgh's Culinary Renaissance</h2>
<p>Pittsburgh's restaurant scene has undergone a remarkable transformation in recent years. From casual neighborhood eateries to upscale fine dining establishments, the city now offers a diverse array of culinary experiences that showcase local ingredients, creative innovation, and the passion of Pittsburgh's chefs and restaurateurs.</p>

<h2>What Makes a Great Pittsburgh Restaurant</h2>
<p>The best restaurants in Pittsburgh share several characteristics: they source locally when possible, they reflect the character of their neighborhoods, and they demonstrate genuine commitment to culinary excellence and customer experience. Whether it is a Polish bakery in the Strip District, a contemporary restaurant in Lawrenceville, or a fine dining establishment in Shadyside, Pittsburgh's best restaurants tell the story of our city's culture and values.</p>

<h3>Notable Dining Establishments</h3>
<p>Our directory features comprehensive profiles of restaurants across genres, price points, and neighborhoods. Each profile includes the owner's story, the restaurant's philosophy, menu highlights, and details about how they contribute to Pittsburgh's culinary community.</p>

<h2>Supporting Local Restaurants</h2>
<p>Pittsburgh's restaurants are community gathering places that provide jobs, support local suppliers, and contribute to neighborhood vitality. Whether you are looking for a special occasion venue, a quick weeknight dinner, or a new neighborhood discovery, we encourage you to explore Pittsburgh's diverse and vibrant restaurant scene.</p>"""
    },
    "pittsburgh-startup-scene": {
        "title": "The Pittsburgh Startup Scene: Innovation and Growth",
        "subtitle": "Exploring the city's thriving entrepreneurial ecosystem",
        "description": "Analysis of Pittsburgh's growing startup ecosystem, funding trends, and emerging tech companies.",
        "content": """<h2>A City Reborn Through Innovation</h2>
<p>Pittsburgh's transformation from a steel-based economy to a technology and innovation hub represents one of America's greatest economic reinventions. Today, the city is home to hundreds of startups and emerging companies working across sectors including software, healthcare technology, autonomous vehicles, robotics, and artificial intelligence.</p>

<h2>Key Elements of Pittsburgh's Startup Ecosystem</h2>
<p>Several factors have contributed to Pittsburgh's emergence as a startup destination: a major research university (Carnegie Mellon), proximity to other innovation hubs, a recovering but affordable real estate market, and a culture of entrepreneurship that values practical innovation and hard work.</p>

<h3>Funding and Support</h3>
<p>Venture capital funding in Pittsburgh has increased substantially in recent years, with investors recognizing the talent pool and innovative potential of local entrepreneurs. Accelerators, incubators, and support organizations provide mentorship and resources for early-stage companies.</p>

<h2>The Entrepreneurs Leading the Way</h2>
<p>Our directory features profiles of Pittsburgh founders and startup leaders who are building companies, creating jobs, and establishing Pittsburgh as a technology destination. Their stories reflect the diversity, ambition, and resilience that characterize Pittsburgh's entrepreneurial community.</p>"""
    },
    "best-coffee-shops-pittsburgh": {
        "title": "Best Coffee Shops in Pittsburgh",
        "subtitle": "Specialty coffee roasters and cafes throughout the city",
        "description": "Guide to Pittsburgh's specialty coffee roasters and cafes.",
        "content": """<h2>Pittsburgh's Coffee Culture</h2>
<p>Pittsburgh has developed a vibrant specialty coffee culture, with independently-owned roasters and cafes now serving pour-over coffee, single-origin espresso, and carefully sourced beans from around the world. The city's coffee community reflects broader trends in American specialty beverage culture while maintaining a distinctly Pittsburgh character.</p>

<h2>What Defines Specialty Coffee</h2>
<p>Specialty coffee businesses are distinguished by their focus on quality sourcing, proper brewing techniques, and education about coffee. Many Pittsburgh roasters establish direct relationships with farmers, participate in the coffee community, and invest in training their baristas to achieve exceptional results.</p>

<h3>Notable Coffee Roasters</h3>
<p>From established roasters in Lawrenceville and the Strip District to newer cafes opening in neighborhoods across the city, Pittsburgh's coffee scene offers something for every taste and preference. Each establishment brings its own character and approach to coffee preparation and service.</p>

<h2>More Than Just Coffee</h2>
<p>Great coffee shops serve as community gathering places. Many feature art, host live music, provide workspace for remote workers, and contribute to their neighborhood's character and vitality. Visiting local coffee shops supports small business owners while enjoying exceptional beverages and community connection.</p>"""
    },
    "pittsburgh-real-estate-developers": {
        "title": "Pittsburgh Real Estate Developers Shaping the City's Future",
        "subtitle": "Profiles of developers transforming neighborhoods",
        "description": "Feature on Pittsburgh's leading real estate developers and their impact.",
        "content": """<h2>Development and Neighborhood Transformation</h2>
<p>Real estate developers shape cities through their decisions about what gets built, where, and how. Pittsburgh's most successful developers have demonstrated commitment to quality projects, neighborhood integration, and sustainable development that benefits existing residents while attracting new investment and activity.</p>

<h2>Current Development Trends</h2>
<p>Pittsburgh development activity concentrates in several key neighborhoods: Lawrenceville, the Strip District, East Liberty, and Downtown. Projects range from historic preservation and adaptive reuse to new construction, mixed-use development, and residential redevelopment.</p>

<h3>Developer Philosophy and Practice</h3>
<p>The best developers maintain long-term commitment to Pittsburgh, understand neighborhood context, and build projects that contribute positively to community character. They navigate complicated regulatory environments, work with community groups, and manage complex financing and construction.</p>

<h2>Impact on the City</h2>
<p>Quality development generates jobs, increases tax revenue, attracts residents and businesses, and improves neighborhood amenities. Our directory profiles developers and development companies contributing most meaningfully to Pittsburgh's evolution and growth.</p>"""
    },
    "women-owned-businesses-pittsburgh": {
        "title": "Women-Owned Businesses in Pittsburgh",
        "subtitle": "Celebrating female entrepreneurs and business leaders",
        "description": "Spotlight on successful women entrepreneurs in Pittsburgh.",
        "content": """<h2>Women Entrepreneurs in Pittsburgh</h2>
<p>Women-owned businesses contribute significantly to Pittsburgh's economy, job creation, and innovation. From service businesses to technology startups, manufacturing to retail, women entrepreneurs operate across all sectors and neighborhoods of the city.</p>

<h2>Challenges and Opportunities</h2>
<p>Women-owned businesses face particular challenges in accessing capital, navigating male-dominated industries, and balancing entrepreneurship with other responsibilities. However, women entrepreneurs also demonstrate remarkable resilience, creativity, and commitment to building sustainable, community-focused businesses.</p>

<h3>Support Resources</h3>
<p>Pittsburgh organizations support women entrepreneurs through mentorship, networking, funding programs, and business education. Women business owner associations provide community and collective advocacy.</p>

<h2>Leadership and Impact</h2>
<p>Women business owners in Pittsburgh lead across sectors, create employment, innovate, and contribute to their communities. Our directory celebrates their accomplishments and the positive impact their businesses have on Pittsburgh's economy and society.</p>"""
    },
    "black-owned-businesses-pittsburgh": {
        "title": "Black-Owned Businesses in Pittsburgh",
        "subtitle": "Entrepreneurs and business leaders strengthening communities",
        "description": "Feature on Black entrepreneurs and business owners in Pittsburgh.",
        "content": """<h2>Black Business Leadership in Pittsburgh</h2>
<p>Black-owned businesses are essential to Pittsburgh's economy, communities, and culture. From family businesses to innovative startups, Black entrepreneurs operate across all sectors and create employment, wealth, and community stability.</p>

<h2>Business Across Sectors</h2>
<p>Black business owners in Pittsburgh work in restaurants and food service, professional services, technology, real estate, retail, trades and construction, healthcare, and nonprofit sectors. Their diversity of focus reflects the diversity of the Black community and its economic participation.</p>

<h3>Community Impact</h3>
<p>Black-owned businesses often prioritize community service, employ local residents, and maintain deep roots in their neighborhoods. They provide economic opportunities, role models, and cultural anchoring for their communities.</p>

<h2>Supporting Black-Owned Businesses</h2>
<p>Consumers, investors, and community organizations increasingly recognize the importance of intentionally supporting Black-owned businesses through patronage, investment, and partnership. Such support strengthens communities and contributes to economic equity and opportunity.</p>"""
    },
    "pittsburgh-tech-companies-hiring": {
        "title": "Pittsburgh Tech Companies Actively Hiring",
        "subtitle": "Career opportunities in the city's growing tech sector",
        "description": "Guide to Pittsburgh tech companies with current job openings.",
        "content": """<h2>Tech Jobs in Pittsburgh</h2>
<p>Pittsburgh's technology sector offers diverse career opportunities in software development, data science, product management, design, sales, operations, and other roles. Companies range from established technology firms to early-stage startups and nonprofits.</p>

<h2>Skills in Demand</h2>
<p>Pittsburgh technology companies seek software engineers, data scientists, product managers, UX designers, sales professionals, and business operations specialists. Opportunities exist for both highly specialized technical roles and general business positions.</p>

<h3>Workplace Culture</h3>
<p>Pittsburgh technology companies often feature innovative workplace cultures that emphasize collaboration, continuous learning, and work-life balance. Many offer competitive compensation, benefits, professional development opportunities, and the chance to work on meaningful challenges.</p>

<h2>Breaking Into Tech</h2>
<p>If you are interested in technology careers, Pittsburgh offers numerous pathways including bootcamps, university programs, mentorship networks, and entry-level opportunities. Our directory profiles companies and provides details about career opportunities and company cultures.</p>"""
    },
    "best-contractors-pittsburgh": {
        "title": "Best Contractors in Pittsburgh",
        "subtitle": "Profiles of skilled tradespeople and construction firms",
        "description": "Guide to Pittsburgh's top contractors and tradespeople.",
        "content": """<h2>Quality Construction and Trades in Pittsburgh</h2>
<p>Pittsburgh's contractor and trades community provides essential services for residential and commercial projects. From general contractors to specialized trades like plumbing, electrical, HVAC, and masonry, skilled professionals keep the city's buildings, systems, and infrastructure functioning.</p>

<h2>What Makes a Good Contractor</h2>
<p>Quality contractors demonstrate technical expertise, reliability, clear communication, honest pricing, and commitment to customer satisfaction. The best contractors listen carefully to client needs, provide transparent estimates, maintain professional crews, and deliver quality work on time and on budget.</p>

<h3>Finding Qualified Contractors</h3>
<p>Quality references, proper licensing and insurance, and clear contracts protect both contractors and clients. Our directory provides profiles of respected contractors who have earned reputations for reliable, quality work.</p>

<h2>Supporting Local Trades</h2>
<p>Pittsburgh's contractor and trades community includes longtime established businesses and newer firms started by younger entrepreneurs. Supporting local contractors strengthens the community while ensuring quality service from people who are invested in Pittsburgh's success.</p>"""
    },
    "new-businesses-pittsburgh-2026": {
        "title": "New Businesses Opening in Pittsburgh 2026",
        "subtitle": "Recent launches and emerging ventures",
        "description": "Coverage of new and recently opened businesses across Pittsburgh.",
        "content": """<h2>Pittsburgh's Entrepreneurial Energy</h2>
<p>Every month, new businesses open across Pittsburgh, launched by entrepreneurs pursuing their visions and serving emerging community needs. These startups and new ventures represent the city's continuing evolution and the diverse opportunities available for business creation.</p>

<h2>Recent Openings Across Sectors</h2>
<p>New businesses in 2026 span restaurants, retail shops, professional services, technology companies, fitness studios, and service businesses. They open in established neighborhoods as well as in neighborhoods experiencing redevelopment and revitalization.</p>

<h3>First-Time Entrepreneurs</h3>
<p>Many new Pittsburgh businesses are founded by people starting their first company. Their diverse backgrounds, skill sets, and perspectives contribute to Pittsburgh's entrepreneurial diversity and dynamism.</p>

<h2>Supporting New Business</h2>
<p>New businesses need community support through patronage, referrals, positive reviews, and goodwill as they establish operations and build customer bases. Supporting new local businesses strengthens neighborhoods and the broader Pittsburgh economy.</p>"""
    },
    "pittsburgh-business-awards-2026": {
        "title": "Pittsburgh Business Awards 2026",
        "subtitle": "Recognition of outstanding businesses and leaders",
        "description": "Recognition of outstanding businesses and community leaders.",
        "content": """<h2>Celebrating Business Excellence</h2>
<p>Throughout the year, various organizations recognize Pittsburgh businesses, entrepreneurs, and leaders for their achievements, innovation, community service, and impact. These awards celebrate excellence and inspire others.</p>

<h2>Categories and Recognition</h2>
<p>Awards recognize business growth, innovation, community service, workplace culture, women leaders, minority-owned businesses, nonprofit excellence, and many other categories. Award programs are run by chambers of commerce, business journals, nonprofit organizations, and community groups.</p>

<h3>Award Winners and Their Impact</h3>
<p>Award winners represent the best of Pittsburgh's business community. Their successes and approaches to business serve as examples for other entrepreneurs and business leaders. Many award winners are featured in our directory.</p>

<h2>Recognition and Community</h2>
<p>Awards provide important recognition for business leaders and entrepreneurs who often work tirelessly with limited fanfare. Recognition ceremonies bring the business community together and celebrate shared values of excellence, innovation, and community contribution.</p>"""
    }
}

# Create blog post files
blog_dir = Path("blog")
blog_dir.mkdir(exist_ok=True)

for slug, data in blog_posts.items():
    post_dir = blog_dir / slug
    post_dir.mkdir(exist_ok=True)
    
    url = f"{base_url}/blog/{slug}/"
    content = blog_template.format(
        title=data["title"],
        subtitle=data["subtitle"],
        description=data["description"],
        url=url,
        base_url=base_url,
        content=data["content"]
    )
    
    with open(post_dir / "index.html", "w") as f:
        f.write(content)
    
    print(f"Created /blog/{slug}/")

# Create blog index
blog_index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pittsburgh Business Directory Blog</title>
  <meta name="description" content="Editorial articles about Pittsburgh businesses, entrepreneurs, and the city's business community." />
  <link rel="canonical" href="https://pittsburghbusinessdirectory.com/blog/" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --charcoal: #1a1a1a;
      --gold: #C8A040;
      --steel-gray: #444;
      --light-gray: #f5f5f5;
      --border-gray: #ddd;
      --text-dark: #333;
      --text-light: #666;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      color: var(--text-dark);
      line-height: 1.6;
      background: #fff;
    }

    a {
      color: var(--gold);
      text-decoration: none;
    }

    a:hover {
      color: var(--charcoal);
    }

    header {
      background: var(--charcoal);
      border-bottom: 3px solid var(--gold);
      padding: 20px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }

    .header-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .logo-text {
      color: var(--gold);
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 1px;
    }

    .logo-tagline {
      color: #aaa;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    nav a {
      color: #fff;
      margin: 0 20px;
      font-weight: 500;
      font-size: 14px;
    }

    nav a:hover {
      color: var(--gold);
    }

    .page-header {
      background: linear-gradient(135deg, var(--charcoal) 0%, var(--steel-gray) 100%);
      color: #fff;
      padding: 60px 20px;
      text-align: center;
    }

    .page-header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 15px;
    }

    .posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 30px;
      padding: 60px 20px;
    }

    .post-card {
      background: #fff;
      border: 1px solid var(--border-gray);
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.3s ease;
    }

    .post-card:hover {
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      border-color: var(--gold);
    }

    .post-card-body {
      padding: 30px;
    }

    .post-category {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold);
      margin-bottom: 10px;
    }

    .post-card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 22px;
      margin-bottom: 15px;
      color: var(--charcoal);
    }

    .post-card p {
      color: var(--text-light);
      margin-bottom: 20px;
      font-size: 14px;
      line-height: 1.7;
    }

    .read-more {
      display: inline-block;
      color: var(--gold);
      font-weight: 600;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    footer {
      background: var(--charcoal);
      color: #ccc;
      padding: 40px 20px;
      border-top: 1px solid var(--steel-gray);
      font-size: 13px;
    }

    footer a {
      color: var(--gold);
    }

    .footer-content {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 30px;
      margin-bottom: 30px;
    }

    .footer-section h3 {
      margin-bottom: 15px;
      color: #fff;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .footer-section ul {
      list-style: none;
    }

    .footer-section li {
      margin-bottom: 10px;
    }

    .footer-bottom {
      border-top: 1px solid var(--steel-gray);
      padding-top: 20px;
      text-align: center;
      color: #888;
    }

    @media (max-width: 768px) {
      .page-header h1 {
        font-size: 2rem;
      }

      nav a {
        margin: 0 10px;
        font-size: 12px;
      }

      .posts-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <header>
    <div class="container">
      <div class="header-inner">
        <div class="logo">
          <span class="logo-text">PGH BUSINESS</span>
          <span class="logo-tagline">Editorial Directory</span>
        </div>
        <nav>
          <a href="/">Home</a>
          <a href="/about/">About</a>
          <a href="/category/restaurants/">Categories</a>
          <a href="/neighborhood/lawrenceville/">Neighborhoods</a>
          <a href="/blog/">Blog</a>
          <a href="/submit/">Submit</a>
        </nav>
      </div>
    </div>
  </header>

  <section class="page-header">
    <div class="container">
      <h1>Latest Articles</h1>
      <p>Editorial insights about Pittsburgh businesses and the entrepreneurial community</p>
    </div>
  </section>

  <section class="posts-grid">
    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Dining</div>
        <h3>Best Restaurants in Pittsburgh 2026</h3>
        <p>A curated guide to the city's most innovative and impactful dining establishments, featuring profiles of chefs and restaurateurs.</p>
        <a href="/blog/best-restaurants-pittsburgh-2026/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Entrepreneurship</div>
        <h3>The Pittsburgh Startup Scene: Innovation and Growth</h3>
        <p>Exploring the city's thriving entrepreneurial ecosystem, funding trends, and emerging technology companies.</p>
        <a href="/blog/pittsburgh-startup-scene/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Food & Drink</div>
        <h3>Best Coffee Shops in Pittsburgh</h3>
        <p>Specialty coffee roasters and cafes throughout the city serving quality espresso, pour-over coffee, and community.</p>
        <a href="/blog/best-coffee-shops-pittsburgh/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Real Estate</div>
        <h3>Pittsburgh Real Estate Developers Shaping the City</h3>
        <p>Profiles of developers transforming neighborhoods and contributing to Pittsburgh's revitalization and growth.</p>
        <a href="/blog/pittsburgh-real-estate-developers/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Entrepreneurship</div>
        <h3>Women-Owned Businesses in Pittsburgh</h3>
        <p>Celebrating female entrepreneurs and business leaders across sectors, neighborhoods, and industries.</p>
        <a href="/blog/women-owned-businesses-pittsburgh/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Entrepreneurship</div>
        <h3>Black-Owned Businesses in Pittsburgh</h3>
        <p>Feature on Black entrepreneurs and business owners strengthening communities across Pittsburgh.</p>
        <a href="/blog/black-owned-businesses-pittsburgh/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Jobs</div>
        <h3>Pittsburgh Tech Companies Actively Hiring</h3>
        <p>Career opportunities in the city's growing technology sector across engineering, product, sales, and operations roles.</p>
        <a href="/blog/pittsburgh-tech-companies-hiring/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Trades</div>
        <h3>Best Contractors in Pittsburgh</h3>
        <p>Profiles of skilled tradespeople and construction firms providing quality services to Pittsburgh residents and businesses.</p>
        <a href="/blog/best-contractors-pittsburgh/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">News</div>
        <h3>New Businesses Opening in Pittsburgh 2026</h3>
        <p>Coverage of new and recently opened businesses across Pittsburgh, highlighting emerging ventures and entrepreneurship.</p>
        <a href="/blog/new-businesses-pittsburgh-2026/" class="read-more">Read Article</a>
      </div>
    </div>

    <div class="post-card">
      <div class="post-card-body">
        <div class="post-category">Awards</div>
        <h3>Pittsburgh Business Awards 2026</h3>
        <p>Recognition of outstanding businesses, entrepreneurs, and leaders receiving awards for excellence and community service.</p>
        <a href="/blog/pittsburgh-business-awards-2026/" class="read-more">Read Article</a>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>Directory</h3>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/submit/">Submit Business</a></li>
            <li><a href="/contact/">Contact</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Categories</h3>
          <ul>
            <li><a href="/category/restaurants/">Restaurants</a></li>
            <li><a href="/category/technology/">Technology</a></li>
            <li><a href="/category/real-estate/">Real Estate</a></li>
            <li><a href="/category/health-wellness/">Health & Wellness</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Neighborhoods</h3>
          <ul>
            <li><a href="/neighborhood/lawrenceville/">Lawrenceville</a></li>
            <li><a href="/neighborhood/strip-district/">Strip District</a></li>
            <li><a href="/neighborhood/downtown/">Downtown</a></li>
            <li><a href="/neighborhood/shadyside/">Shadyside</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Resources</h3>
          <ul>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/feed.xml">RSS Feed</a></li>
            <li><a href="https://thepittsburghwire.com">Pittsburgh Wire</a></li>
            <li><a href="/sitemap.xml">Sitemap</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>Pittsburgh Business Directory. Founded by Dr. Connor Robertson. A sister publication of <a href="https://thepittsburghwire.com">The Pittsburgh Wire</a>.</p>
        <p style="margin-top: 10px;">&copy; 2026 Pittsburgh Business Directory. All rights reserved.</p>
      </div>
    </div>
  </footer>
</body>
</html>
'''

with open(blog_dir / "index.html", "w") as f:
    f.write(blog_index_html)

print("\nCreated /blog/ index")
print("\nBlog generation complete!")
