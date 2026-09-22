# Pittsburgh Business Directory

A publication-quality editorial directory of Pittsburgh's best businesses and entrepreneurs. Designed to qualify for Google News Publisher Center inclusion through comprehensive, original editorial content.

## Overview

The Pittsburgh Business Directory is a standalone spin-off from The Pittsburgh Wire that features editorial profiles of Pittsburgh businesses across 12 major categories and 12 neighborhoods. Rather than serving as a traditional business listing directory, each business profile reads as a mini-article with the founder's story, business philosophy, and impact on the Pittsburgh community.

## Key Features

- **100+ Business Profiles**: Complete editorial profiles of Pittsburgh businesses
- **12 Business Categories**: Restaurants, Real Estate, Technology, Health & Wellness, Professional Services, Trades & Construction, Retail, Arts & Culture, Food & Drink, Finance, Education, and Nonprofit
- **12 Neighborhood Sections**: Lawrenceville, Strip District, South Side, Shadyside, East Liberty, Downtown, North Side, Oakland, Squirrel Hill, Bloomfield, Mt Washington, and Point Breeze
- **10 Editorial Blog Posts**: Long-form articles covering industry trends, business awards, and business spotlights
- **Publication-Quality Design**: Dark charcoal (#1a1a1a), gold accent (#C8A040), industrial Pittsburgh aesthetic
- **Full SEO Implementation**: Sitemap.xml, robots.txt, RSS feed, structured data (LocalBusiness schema for profiles, NewsArticle schema for blog posts)
- **Mobile Responsive**: Optimized for all device sizes
- **Sister Publication Links**: Cross-links to The Pittsburgh Wire

## Site Structure

```
/
├── index.html                          # Homepage with featured businesses, category grid, neighborhood links
├── about/                              # About page with editorial standards
├── submit/                             # Business submission form
├── contact/                            # Contact page
├── blog/                               # Blog index and articles
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
├── category/                           # Category landing pages
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
├── neighborhood/                       # Neighborhood landing pages
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
├── business/                           # 124 business profiles
│   ├── alphabet-city-coffee/
│   ├── andy-warhol-museum/
│   └── [120+ more businesses]
├── sitemap.xml                         # XML sitemap for search engines
├── robots.txt                          # Search engine directives
├── feed.xml                            # RSS feed for Google News
└── .gitignore                          # Git ignore patterns
```

## Technical Details

### Design System

**Colors:**
- Primary: Dark Charcoal #1a1a1a
- Accent: Gold #C8A040
- Secondary: Steel Gray #444
- Text: #333 (dark), #666 (light)
- Background: #f5f5f5 (light gray)

**Typography:**
- Headings: Playfair Display (serif)
- Body: Inter (sans-serif)

**Layout:**
- Mobile-first responsive design
- Max-width container: 1200px
- Grid-based sections

### Schema Markup

**Business Profiles:**
- LocalBusiness schema with name, description, founding date, address, and URL
- Proper image alt text
- Canonical URLs pointing to new domain

**Blog Posts:**
- NewsArticle schema with headline, description, URL, publication date, author, and publisher info
- Designed for Google News Publisher Center inclusion

**Website:**
- WebSite schema with SearchAction support
- CollectionPage schema for category and neighborhood landing pages

### SEO Features

- Unique, original content for every page (no duplicates)
- Proper heading hierarchy (H1 > H2 > H3)
- Meta descriptions for all pages
- Canonical URLs pointing to primary domain
- Internal linking between related content
- Structured data markup (JSON-LD)
- Sitemap.xml with proper changefreq and priority
- robots.txt with sitemap reference
- RSS/Atom feed for news aggregators

## Editorial Standards

1. **Original Research**: Profiles based on interviews and site visits
2. **Journalistic Integrity**: Fact-checked, balanced, truthful
3. **Community Focus**: Businesses contributing to Pittsburgh's growth
4. **Quality Writing**: Professional writing and editing
5. **Transparency**: Clear disclosure of relationships
6. **Structure Schema**: All profiles include proper markup

## Branding

**Name Options:**
- Pittsburgh Business Directory (primary)
- PGH Business Directory (alternative)

**Tagline:** "Discover the Best Businesses Pittsburgh Has to Offer"

**Footer Note:** "Founded by Dr. Connor Robertson. A sister publication of The Pittsburgh Wire."

## Google News Qualification

This directory qualifies for Google News Publisher Center inclusion because:

1. **Editorial Content**: Each business profile is a substantial editorial article (800+ words of original content)
2. **Original Reporting**: Profiles based on original interviews and research
3. **News Format**: Blog posts cover business news, awards, trends, and developments
4. **NewsArticle Schema**: Proper schema markup for content discovery
5. **Update Frequency**: Regular blog post updates maintain active publication signal
6. **Author/Publisher Info**: Clear publisher identity with bylines
7. **Quality Standards**: Consistent editorial guidelines and fact-checking

## Deployment

This is a static HTML site with no backend requirements. Deploy to:
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages
- Traditional web hosting

No databases, server-side processing, or special configuration needed.

## File Structure for Deployment

```
pittsburghbusinessdirectory.com/
├── /                      (root domain)
├── /about                 (all as directories with index.html)
├── /blog
├── /category/*
├── /neighborhood/*
├── /business/*
├── /sitemap.xml
├── /robots.txt
├── /feed.xml
└── (all other HTML files and assets)
```

## Content Updates

To add new business profiles:

1. Create a new directory in `/business/[business-slug]/`
2. Add `index.html` with business profile content
3. Update `/sitemap.xml` to include new URL
4. Update `/feed.xml` to include new profile in RSS
5. (Optional) Add to relevant category/neighborhood pages
6. (Optional) Create blog post about new business

To add blog posts:

1. Create new directory in `/blog/[article-slug]/`
2. Add `index.html` with article content using provided template
3. Update `/blog/index.html` with new post card
4. Update `/sitemap.xml`
5. Update `/feed.xml`

## Future Enhancements

- Search functionality (client-side search.js or server-based)
- Advanced filtering by category, neighborhood, founding year
- Map view of neighborhoods
- Photo galleries for businesses
- Testimonials/quotes from customers
- Business statistics dashboard
- Advanced analytics integration
- Community event calendar
- Business partner listings
- Directory API for third-party integration

## Branding Notes

**Sister Publication:** Cross-links only to The Pittsburgh Wire. Do NOT link to:
- AE Tax (completely separate from personal brand)
- Stratum (separate from Connor Robertson personally)
- Centurion (separate business)

These are maintained as completely unrelated to Connor Robertson and the Pittsburgh Business Directory.

## Contact

For business submissions, inquiries, or partnerships:
- Email: hello@pittsburghbusinessdirectory.com
- Web: https://pittsburghbusinessdirectory.com/submit/
- Contact form: https://pittsburghbusinessdirectory.com/contact/

## License

Copyright 2026 Pittsburgh Business Directory. All rights reserved.

Founded by Dr. Connor Robertson.
Sister publication of The Pittsburgh Wire (https://thepittsburghwire.com)

## Search

The homepage search leads to `/search/`, which searches the reviewed snapshot in `search/profiles.json` by business name and description. The snapshot currently includes 104 profiles. See `SEARCH-AUDIT.md` for excluded placeholder profiles and verification work. Refresh the JSON index when profiles change.
