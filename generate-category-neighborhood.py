#!/usr/bin/env python3
import os
from pathlib import Path

# Category template
category_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{category_name} Businesses in Pittsburgh - PGH Business Directory</title>
  <meta name="description" content="Directory of {category_name_lower} in Pittsburgh. Browse profiles of businesses across {category_name_lower}." />
  <link rel="canonical" href="https://pittsburghbusinessdirectory.com/category/{slug}/" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "{category_name} in Pittsburgh",
    "description": "Directory of {category_name_lower} in Pittsburgh",
    "url": "https://pittsburghbusinessdirectory.com/category/{slug}/"
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

    .page-header {{
      background: linear-gradient(135deg, var(--charcoal) 0%, var(--steel-gray) 100%);
      color: #fff;
      padding: 60px 20px;
      text-align: center;
    }}

    .page-header h1 {{
      font-family: 'Playfair Display', serif;
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 15px;
    }}

    .page-header p {{
      font-size: 18px;
      color: #ddd;
    }}

    .content-section {{
      padding: 60px 20px;
    }}

    .content-section h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 2rem;
      margin-bottom: 30px;
      color: var(--charcoal);
      border-bottom: 3px solid var(--gold);
      padding-bottom: 15px;
    }}

    .content-section p {{
      margin-bottom: 20px;
      color: var(--text-light);
      line-height: 1.8;
    }}

    .businesses-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin-bottom: 50px;
    }}

    .business-card {{
      background: #fff;
      border: 1px solid var(--border-gray);
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.3s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}

    .business-card:hover {{
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      border-color: var(--gold);
    }}

    .business-card-header {{
      background: var(--charcoal);
      color: #fff;
      padding: 20px;
      min-height: 80px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }}

    .business-card h3 {{
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      margin-bottom: 8px;
    }}

    .business-category {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold);
    }}

    .business-card-body {{
      padding: 20px;
    }}

    .business-desc {{
      color: var(--text-light);
      margin-bottom: 15px;
      font-size: 14px;
      line-height: 1.6;
    }}

    .read-more {{
      display: inline-block;
      color: var(--gold);
      font-weight: 600;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 1px;
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
      .page-header h1 {{
        font-size: 2rem;
      }}

      nav a {{
        margin: 0 10px;
        font-size: 12px;
      }}

      .businesses-grid {{
        grid-template-columns: 1fr;
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

  <section class="page-header">
    <div class="container">
      <h1>{category_name}</h1>
      <p>Directory of {category_name_lower} in Pittsburgh</p>
    </div>
  </section>

  <section class="content-section">
    <div class="container">
      <h2>Featured {category_name}</h2>
      <p>Pittsburgh's {category_name_lower} represent innovation, quality, and commitment to community. Browse our directory of featured businesses and entrepreneurs in this sector.</p>
      
      <div class="businesses-grid">
        <div class="business-card">
          <div class="business-card-header">
            <h3>Featured Business</h3>
            <div class="business-category">{category_name}</div>
          </div>
          <div class="business-card-body">
            <p class="business-desc">Browse our complete directory for detailed profiles of businesses in {category_name_lower}. Each profile includes the owner's story, business philosophy, and impact on Pittsburgh.</p>
            <a href="/" class="read-more">Back to Directory</a>
          </div>
        </div>
      </div>

      <h2>About This Category</h2>
      <p>The {category_name} category includes businesses across {category_name_lower} in Pittsburgh. From established enterprises to innovative new ventures, these businesses contribute to Pittsburgh's economy, employment, and community.</p>

      <h2>Exploring the Category</h2>
      <p>Use the directory to browse {category_name_lower}, search by neighborhood, or explore our featured businesses. Each profile includes comprehensive information about the business, its leadership, and its role in Pittsburgh's community.</p>
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

# Neighborhood template
neighborhood_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{neighborhood_name} Businesses in Pittsburgh - PGH Business Directory</title>
  <meta name="description" content="Directory of businesses in {neighborhood_name}, Pittsburgh. Discover local restaurants, shops, services, and more." />
  <link rel="canonical" href="https://pittsburghbusinessdirectory.com/neighborhood/{slug}/" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Businesses in {neighborhood_name}, Pittsburgh",
    "description": "Directory of businesses in {neighborhood_name}",
    "url": "https://pittsburghbusinessdirectory.com/neighborhood/{slug}/"
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

    .page-header {{
      background: linear-gradient(135deg, var(--charcoal) 0%, var(--steel-gray) 100%);
      color: #fff;
      padding: 60px 20px;
      text-align: center;
    }}

    .page-header h1 {{
      font-family: 'Playfair Display', serif;
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 15px;
    }}

    .page-header p {{
      font-size: 18px;
      color: #ddd;
    }}

    .content-section {{
      padding: 60px 20px;
    }}

    .content-section h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 2rem;
      margin-bottom: 30px;
      color: var(--charcoal);
      border-bottom: 3px solid var(--gold);
      padding-bottom: 15px;
    }}

    .content-section p {{
      margin-bottom: 20px;
      color: var(--text-light);
      line-height: 1.8;
    }}

    .businesses-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin-bottom: 50px;
    }}

    .business-card {{
      background: #fff;
      border: 1px solid var(--border-gray);
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.3s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}

    .business-card:hover {{
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      border-color: var(--gold);
    }}

    .business-card-header {{
      background: var(--charcoal);
      color: #fff;
      padding: 20px;
      min-height: 80px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }}

    .business-card h3 {{
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      margin-bottom: 8px;
    }}

    .business-category {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold);
    }}

    .business-card-body {{
      padding: 20px;
    }}

    .business-desc {{
      color: var(--text-light);
      margin-bottom: 15px;
      font-size: 14px;
      line-height: 1.6;
    }}

    .read-more {{
      display: inline-block;
      color: var(--gold);
      font-weight: 600;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 1px;
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
      .page-header h1 {{
        font-size: 2rem;
      }}

      nav a {{
        margin: 0 10px;
        font-size: 12px;
      }}

      .businesses-grid {{
        grid-template-columns: 1fr;
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

  <section class="page-header">
    <div class="container">
      <h1>{neighborhood_name}</h1>
      <p>Discover businesses and entrepreneurs in {neighborhood_name}</p>
    </div>
  </section>

  <section class="content-section">
    <div class="container">
      <h2>Featured Businesses in {neighborhood_name}</h2>
      <p>{neighborhood_name} is a vibrant Pittsburgh neighborhood home to diverse businesses, restaurants, and services. Browse our directory to discover local establishments and meet the entrepreneurs behind them.</p>
      
      <div class="businesses-grid">
        <div class="business-card">
          <div class="business-card-header">
            <h3>Featured Businesses</h3>
            <div class="business-category">{neighborhood_name}</div>
          </div>
          <div class="business-card-body">
            <p class="business-desc">Explore our complete directory for detailed profiles of businesses in {neighborhood_name}. Each profile includes the owner's story and the business's impact on the neighborhood.</p>
            <a href="/" class="read-more">Back to Directory</a>
          </div>
        </div>
      </div>

      <h2>About {neighborhood_name}</h2>
      <p>{neighborhood_name} is one of Pittsburgh's distinctive neighborhoods, each with its own character, history, and business community. The neighborhood supports restaurants, retail, services, and various other enterprises that serve residents and visitors.</p>

      <h2>Supporting Local Business in {neighborhood_name}</h2>
      <p>Shopping locally in {neighborhood_name} supports neighborhood entrepreneurs, keeps dollars in the community, and helps maintain the neighborhood's unique character and vibrancy. Every purchase from a local business strengthens the neighborhood.</p>
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

# Categories
categories = {
    "restaurants": ("Restaurants & Food Service", "restaurants and food service businesses"),
    "real-estate": ("Real Estate & Development", "real estate companies and developers"),
    "technology": ("Technology & Software", "technology companies and software firms"),
    "health-wellness": ("Health & Wellness", "health and wellness providers"),
    "professional-services": ("Professional Services", "professional services firms"),
    "trades-construction": ("Trades & Construction", "contractors and tradespeople"),
    "retail": ("Retail & E-Commerce", "retail businesses"),
    "arts-culture": ("Arts & Culture", "arts and cultural organizations"),
    "food-drink": ("Food & Drink", "specialty food and beverage businesses"),
    "finance": ("Finance & Investment", "financial services companies"),
    "education": ("Education & Training", "educational institutions"),
    "nonprofit": ("Nonprofit & Community Services", "nonprofit organizations"),
}

# Neighborhoods
neighborhoods = {
    "lawrenceville": "Lawrenceville",
    "strip-district": "Strip District",
    "south-side": "South Side",
    "shadyside": "Shadyside",
    "east-liberty": "East Liberty",
    "downtown": "Downtown",
    "north-side": "North Side",
    "oakland": "Oakland",
    "squirrel-hill": "Squirrel Hill",
    "bloomfield": "Bloomfield",
    "mt-washington": "Mt Washington",
    "point-breeze": "Point Breeze",
}

# Create category pages
category_dir = Path("category")
category_dir.mkdir(exist_ok=True)

for slug, (name, desc) in categories.items():
    cat_dir = category_dir / slug
    cat_dir.mkdir(exist_ok=True)
    
    content = category_template.format(
        category_name=name,
        category_name_lower=desc,
        slug=slug
    )
    
    with open(cat_dir / "index.html", "w") as f:
        f.write(content)
    
    print(f"Created /category/{slug}/")

# Create neighborhood pages
neighborhood_dir = Path("neighborhood")
neighborhood_dir.mkdir(exist_ok=True)

for slug, name in neighborhoods.items():
    neigh_dir = neighborhood_dir / slug
    neigh_dir.mkdir(exist_ok=True)
    
    content = neighborhood_template.format(
        neighborhood_name=name,
        slug=slug
    )
    
    with open(neigh_dir / "index.html", "w") as f:
        f.write(content)
    
    print(f"Created /neighborhood/{slug}/")

print("\nCategory and neighborhood generation complete!")
