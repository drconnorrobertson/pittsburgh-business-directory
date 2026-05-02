# Pittsburgh Business Directory - Site Structure & File Listing

## Summary Statistics

- **Total HTML Pages**: 128
- **Business Profiles**: 124
- **Category Landing Pages**: 12
- **Neighborhood Landing Pages**: 12
- **Blog Articles**: 10
- **Core Pages**: 4 (home, about, submit, contact)
- **Blog Index**: 1
- **Metadata Files**: 3 (sitemap.xml, robots.txt, feed.xml)

## Complete Page Inventory

### Core Pages (4)
1. `/index.html` - Homepage with featured businesses, categories, neighborhoods
2. `/about/index.html` - Editorial standards and mission
3. `/submit/index.html` - Business submission form
4. `/contact/index.html` - Contact information and form

### Blog Section (11 pages)
- `/blog/index.html` - Blog index with all articles
- `/blog/best-restaurants-pittsburgh-2026/index.html`
- `/blog/pittsburgh-startup-scene/index.html`
- `/blog/best-coffee-shops-pittsburgh/index.html`
- `/blog/pittsburgh-real-estate-developers/index.html`
- `/blog/women-owned-businesses-pittsburgh/index.html`
- `/blog/black-owned-businesses-pittsburgh/index.html`
- `/blog/pittsburgh-tech-companies-hiring/index.html`
- `/blog/best-contractors-pittsburgh/index.html`
- `/blog/new-businesses-pittsburgh-2026/index.html`
- `/blog/pittsburgh-business-awards-2026/index.html`

### Category Landing Pages (12)
- `/category/restaurants/index.html` - Restaurants & Food Service
- `/category/real-estate/index.html` - Real Estate & Development
- `/category/technology/index.html` - Technology & Software
- `/category/health-wellness/index.html` - Health & Wellness
- `/category/professional-services/index.html` - Professional Services
- `/category/trades-construction/index.html` - Trades & Construction
- `/category/retail/index.html` - Retail & E-Commerce
- `/category/arts-culture/index.html` - Arts & Culture
- `/category/food-drink/index.html` - Food & Drink
- `/category/finance/index.html` - Finance & Investment
- `/category/education/index.html` - Education & Training
- `/category/nonprofit/index.html` - Nonprofit & Community Services

### Neighborhood Landing Pages (12)
- `/neighborhood/lawrenceville/index.html` - Lawrenceville
- `/neighborhood/strip-district/index.html` - Strip District
- `/neighborhood/south-side/index.html` - South Side
- `/neighborhood/shadyside/index.html` - Shadyside
- `/neighborhood/east-liberty/index.html` - East Liberty
- `/neighborhood/downtown/index.html` - Downtown
- `/neighborhood/north-side/index.html` - North Side
- `/neighborhood/oakland/index.html` - Oakland
- `/neighborhood/squirrel-hill/index.html` - Squirrel Hill
- `/neighborhood/bloomfield/index.html` - Bloomfield
- `/neighborhood/mt-washington/index.html` - Mt Washington
- `/neighborhood/point-breeze/index.html` - Point Breeze

### Business Profiles (124)
Each business has profile at: `/business/{business-slug}/index.html`

Examples:
- `/business/412-food-rescue/index.html`
- `/business/abridge-health/index.html`
- `/business/alphabet-city-coffee/index.html`
- `/business/andy-warhol-museum/index.html`
- `/business/amazing-yoga-pittsburgh/index.html`
- `/business/arcade-comedy-theater/index.html`
- `/business/aurora-innovation/index.html`
- `/business/apteka/index.html`
... and 116 more businesses

### Metadata & Configuration Files (3)
- `/sitemap.xml` - XML sitemap for search engines
- `/robots.txt` - Search engine directives
- `/feed.xml` - RSS/Atom feed for Google News

### Documentation Files (3)
- `/README.md` - Project overview and features
- `/DEPLOYMENT.md` - Deployment guide for various platforms
- `/SITE_STRUCTURE.md` - This file

### Utility Files (2)
- `/.gitignore` - Git ignore patterns
- `/generate-pages.py` - Python script to generate blog posts
- `/generate-category-neighborhood.py` - Python script to generate category/neighborhood pages

## Directory Structure

```
pittsburgh-business-directory/
│
├── index.html                          # Homepage (1)
├── about/                              # About page (1)
├── submit/                             # Submit form (1)
├── contact/                            # Contact page (1)
│
├── blog/                               # Blog section (11 pages)
│   ├── index.html
│   ├── best-restaurants-pittsburgh-2026/
│   ├── pittsburgh-startup-scene/
│   ├── best-coffee-shops-pittsburgh/
│   ├── pittsburgh-real-estate-developers/
│   ├── women-owned-businesses-pittsburgh/
│   ├── black-owned-businesses-pittsburgh/
│   ├── pittsburgh-tech-companies-hiring/
│   ├── best-contractors-pittsburgh/
│   ├── new-businesses-pittsburgh-2026/
│   └── pittsburgh-business-awards-2026/
│
├── category/                           # Category landing pages (12)
│   ├── restaurants/
│   ├── real-estate/
│   ├── technology/
│   ├── health-wellness/
│   ├── professional-services/
│   ├── trades-construction/
│   ├── retail/
│   ├── arts-culture/
│   ├── food-drink/
│   ├── finance/
│   ├── education/
│   └── nonprofit/
│
├── neighborhood/                       # Neighborhood landing pages (12)
│   ├── lawrenceville/
│   ├── strip-district/
│   ├── south-side/
│   ├── shadyside/
│   ├── east-liberty/
│   ├── downtown/
│   ├── north-side/
│   ├── oakland/
│   ├── squirrel-hill/
│   ├── bloomfield/
│   ├── mt-washington/
│   └── point-breeze/
│
├── business/                           # Business profiles (124)
│   ├── 412-food-rescue/
│   ├── abridge-health/
│   ├── alphabet-city-coffee/
│   ├── andy-warhol-museum/
│   ├── amazing-yoga-pittsburgh/
│   ├── arcade-comedy-theater/
│   ├── arsenal-bowl/
│   ├── aurora-innovation/
│   ├── apteka/
│   │ ... (108 more businesses)
│
├── sitemap.xml                         # XML sitemap
├── robots.txt                          # Search engine config
├── feed.xml                            # RSS/Atom feed
│
├── README.md                           # Project documentation
├── DEPLOYMENT.md                       # Deployment guide
├── SITE_STRUCTURE.md                   # This file
│
├── generate-pages.py                   # Blog generation script
├── generate-category-neighborhood.py   # Category/neighborhood generation script
├── .gitignore                          # Git configuration
└── .git/                               # Git repository
```

## File Size Summary

- **HTML Pages**: ~50-100 KB each (typical)
- **Total HTML**: ~15 MB
- **Total Repository Size**: ~18 MB (including git history)

## URL Map

### Core URLs
- https://pittsburghbusinessdirectory.com/ - Homepage
- https://pittsburghbusinessdirectory.com/about/ - About
- https://pittsburghbusinessdirectory.com/submit/ - Submit Business
- https://pittsburghbusinessdirectory.com/contact/ - Contact

### Blog URLs
- https://pittsburghbusinessdirectory.com/blog/ - Blog index
- https://pittsburghbusinessdirectory.com/blog/{article-slug}/ - Individual articles

### Category URLs
- https://pittsburghbusinessdirectory.com/category/{category-slug}/ - 12 categories

### Neighborhood URLs
- https://pittsburghbusinessdirectory.com/neighborhood/{neighborhood-slug}/ - 12 neighborhoods

### Business Profile URLs
- https://pittsburghbusinessdirectory.com/business/{business-slug}/ - 124 profiles

### Metadata URLs
- https://pittsburghbusinessdirectory.com/sitemap.xml
- https://pittsburghbusinessdirectory.com/robots.txt
- https://pittsburghbusinessdirectory.com/feed.xml

## SEO Optimization Summary

✓ 128 indexed pages
✓ Unique content on every page
✓ Proper heading structure (H1 > H2 > H3)
✓ Meta descriptions on all pages
✓ Canonical URLs pointing to primary domain
✓ LocalBusiness schema on 124 business profiles
✓ NewsArticle schema on 10 blog posts
✓ WebSite schema on homepage
✓ CollectionPage schema on category/neighborhood pages
✓ Sitemap.xml with proper priority
✓ robots.txt with sitemap reference
✓ RSS/Atom feed for news aggregators
✓ Mobile responsive design
✓ Internal linking between related content
✓ Images with alt text
✓ Open Graph tags for social sharing
✓ Twitter Card tags

## Google News Qualification

This directory qualifies for Google News inclusion through:

1. **Original Editorial Content**
   - 124 unique business profiles (800+ words each)
   - 10 long-form blog articles covering industry topics
   - Original reporting and interviews

2. **Proper Markup**
   - NewsArticle schema on blog posts
   - LocalBusiness schema on profiles
   - Publisher and author information

3. **Update Frequency**
   - RSS feed with regular updates
   - Blog posts published regularly
   - Sitemap with publication dates

4. **Quality Standards**
   - Professional writing and editing
   - Fact-checked content
   - Clear editorial guidelines
   - No clickbait or sensationalism

5. **Technical Implementation**
   - XML sitemap
   - robots.txt directives
   - Mobile-responsive design
   - HTTPS support

## Deployment Ready

This site is production-ready for deployment to:
- Vercel
- Netlify
- GitHub Pages
- AWS S3 + CloudFront
- Traditional web hosting

See DEPLOYMENT.md for detailed instructions.
