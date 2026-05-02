# Pittsburgh Business Directory - Deployment Guide

## Quick Start

This is a static HTML site with no backend requirements. It can be deployed to any web hosting platform.

## Recommended Deployment Options

### Option 1: Vercel (Recommended)

**Pros:** Fast, free tier, automatic HTTPS, excellent for static sites

1. Create Vercel account at https://vercel.com
2. Connect GitHub repository
3. Configure build settings:
   - Framework: None (static)
   - Build Command: (leave empty)
   - Output Directory: . (root)
4. Deploy
5. Custom domain setup:
   - Add domain at Vercel dashboard
   - Configure DNS at domain registrar

### Option 2: Netlify

**Pros:** Drag-and-drop deploy, free tier, excellent static site hosting

1. Create Netlify account at https://netlify.com
2. Option A - Connect GitHub repository:
   - Authorize Netlify
   - Select repository
   - Build command: (leave empty)
   - Publish directory: . (root)
3. Option B - Drag and drop:
   - Drag entire site folder to Netlify
4. Custom domain setup in Netlify dashboard

### Option 3: GitHub Pages

**Pros:** Free, integrated with GitHub

1. Push code to GitHub repository
2. Go to repository Settings > Pages
3. Set source to main branch
4. Add custom domain in Pages settings
5. Update DNS records at domain registrar

### Option 4: AWS S3 + CloudFront

**Pros:** Scalable, cost-effective for high traffic

1. Create S3 bucket
2. Enable static website hosting
3. Upload files with appropriate MIME types
4. Create CloudFront distribution
5. Update DNS to CloudFront domain
6. Add SSL certificate

### Option 5: Traditional Web Hosting

**Pros:** Familiar interface, easy management

1. Log in to cPanel or hosting control panel
2. Create/select public_html folder
3. Upload all files via FTP or file manager
4. Set proper file permissions (644 for files, 755 for directories)
5. Configure custom domain DNS

## Domain Setup

### Before Deployment

1. Register domain (e.g., pittsburghbusinessdirectory.com)
2. Choose domain registrar (GoDaddy, Namecheap, etc.)

### DNS Configuration

Update DNS records at your domain registrar:

**For Vercel:**
```
CNAME: www -> cname.vercel-dns.com
A: @ -> Vercel IP (check Vercel dashboard)
```

**For Netlify:**
```
CNAME: www -> [your-site].netlify.app
A: @ -> Netlify IP (check Netlify dashboard)
```

**For GitHub Pages:**
```
CNAME: www -> [username].github.io
A: @ -> GitHub Pages IP (1.1.1.1 or from docs)
```

## Pre-Deployment Checklist

Before going live:

- [ ] Test all pages render correctly
- [ ] Verify responsive design on mobile
- [ ] Check all links work (internal and external)
- [ ] Validate HTML with W3C validator
- [ ] Test form submissions (if backend added)
- [ ] Verify sitemap.xml is accessible
- [ ] Check robots.txt is accessible
- [ ] Test RSS feed in feed reader
- [ ] Verify schema markup with Google Rich Results Test
- [ ] Check Open Graph tags appear in social shares
- [ ] Ensure favicon/logo displays correctly
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)

## SSL/HTTPS

All modern hosting platforms provide free SSL/HTTPS:

- **Vercel**: Automatic
- **Netlify**: Automatic
- **GitHub Pages**: Automatic
- **AWS S3**: Add CloudFront (automatic)
- **Traditional hosting**: Check if included, or use Let's Encrypt

## Performance Optimization

### Image Optimization

All images should be optimized before deployment:

```bash
# Using ImageOptim (Mac) or similar tool
# Or use online tools like TinyPNG

# Ensure images are appropriately sized
# Homepage hero: ~1200x600px
# Business card images: ~400x300px
# Thumbnails: ~200x150px
```

### Caching Headers

Set HTTP caching headers for static assets:

```
# For static files (CSS, JS, images)
Cache-Control: public, max-age=31536000

# For HTML files
Cache-Control: public, max-age=3600

# For frequently updated feeds
Cache-Control: public, max-age=3600
```

### CDN Configuration

For high-traffic sites, use a CDN:

- **Cloudflare** (free tier available)
- **CloudFront** (AWS)
- **Netlify Edge** (built-in with Netlify)

## Google Search Console Setup

1. Create Google Search Console account
2. Add property (pittsburghbusinessdirectory.com)
3. Verify domain ownership (DNS record or HTML file)
4. Submit sitemap.xml
5. Monitor indexing status
6. Check for crawl errors
7. Review search performance

## Google News Publisher Center

To qualify for Google News inclusion:

1. Ensure site has been live for 1+ month
2. Go to https://news.google.com/news/publication/add
3. Submit publication details
4. Verify ownership
5. Submit site in Google Search Console
6. Wait for review (2-4 weeks)

Key requirements we've met:
- Original editorial content
- NewsArticle schema markup
- RSS feed
- Regular content updates
- Quality standards

## Google Analytics

1. Create Google Analytics account
2. Add tracking code to header (if needed):
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```
3. Monitor traffic and user behavior
4. Track conversions (business submissions, email signups)

## Monitoring and Maintenance

### Regular Checks

- Weekly: Monitor website uptime
- Daily: Check error logs
- Monthly: Review analytics
- Monthly: Test contact forms
- Quarterly: Update blog content
- Quarterly: Add new business profiles
- Annually: Review and update outdated information

### Uptime Monitoring

Use uptime monitoring service:

- **Uptime Robot** (free)
- **Pingdom** (paid)
- **Datadog** (paid)
- **New Relic** (paid)

## Email Setup

For contact forms and business submissions:

### Option 1: Third-Party Form Service

Use services that handle form submission:

- **Formspree** - Free tier available
- **Getform** - Simple form backend
- **Basin** - Email form submissions
- **Netlify Forms** - If using Netlify

### Option 2: Email Service Provider

Set up transactional emails:

- **SendGrid** - Transactional email
- **Mailgun** - Email API
- **AWS SES** - Low-cost email
- **Postmark** - Developer-friendly

### Domain Email

Set up email at domain:

- **Google Workspace** - $6/user/month
- **Namecheap Email** - $0.50-1/month
- **Zoho Mail** - Free tier available

## SSL Certificate

Most hosting platforms provide free SSL:

- **Vercel**: Automatic Let's Encrypt
- **Netlify**: Automatic Let's Encrypt
- **GitHub Pages**: Automatic HTTPS
- **Cloudflare**: Free SSL

If needed, purchase from:

- **Let's Encrypt**: Free
- **Comodo**: Budget-friendly
- **DigiCert**: Premium
- **GoDaddy**: Easy integration

## Subdomain Setup (Optional)

To host subdomains:

- **blog.pittsburghbusinessdirectory.com**: Point to same hosting
- **www.pittsburghbusinessdirectory.com**: Recommended (set up in DNS)
- **directory.pittsburghbusinessdirectory.com**: Optional for specific sections

## Backup Strategy

Regular backups are essential:

- **Daily**: Automated backups (hosting provider)
- **Weekly**: Manual backup download
- **Version Control**: Keep code in Git

For Git repository backup:

```bash
git clone https://github.com/connorrobertson/pittsburgh-business-directory.git backup-$(date +%Y%m%d)
```

## Git Workflow for Updates

### Updating Business Profiles

```bash
# Pull latest changes
git pull origin main

# Create feature branch
git checkout -b add/new-business-name

# Make changes
# Add new business directory and profile

# Stage and commit
git add business/new-business-slug/
git commit -m "Add profile: New Business Name"

# Update metadata
git add sitemap.xml feed.xml
git commit -m "Update sitemap and feed for new business"

# Push and create pull request
git push origin add/new-business-name
```

### Blog Post Updates

```bash
git checkout -b blog/article-title
# Create blog post
git add blog/article-slug/
git add blog/index.html
git commit -m "Add blog post: Article Title"
git push origin blog/article-title
```

## Performance Benchmarks

Target metrics:

- **Page Load**: < 2 seconds (desktop), < 3 seconds (mobile)
- **First Contentful Paint**: < 1 second
- **Time to Interactive**: < 3 seconds
- **Core Web Vitals**: All green on PageSpeed Insights

Test with:

- Google PageSpeed Insights
- GTmetrix
- Lighthouse
- WebPageTest

## Security

Security best practices:

- [ ] Enable HTTPS everywhere
- [ ] Set Security Headers (HSTS, CSP)
- [ ] Regular security audits
- [ ] Keep software updated
- [ ] Monitor for vulnerabilities
- [ ] Regular backups
- [ ] DDoS protection (Cloudflare)

## Troubleshooting

### Common Issues

**404 errors:**
- Check file paths are correct
- Verify index.html files in directories
- Check .htaccess rules (if using Apache)

**Slow loading:**
- Optimize images
- Enable caching headers
- Use CDN
- Minimize CSS/JS

**Form submission issues:**
- Verify form backend is configured
- Check email settings
- Test with simple form first

**Mobile display issues:**
- Test viewport meta tag
- Check media queries
- Verify responsive breakpoints

## Support Resources

- Vercel Docs: https://vercel.com/docs
- Netlify Docs: https://docs.netlify.com
- GitHub Pages: https://pages.github.com
- Cloudflare: https://support.cloudflare.com

## Next Steps

After deployment:

1. Submit to Google Search Console
2. Set up Google Analytics
3. Add to Bing Webmaster Tools
4. Set up Google News Publisher Center
5. Monitor performance
6. Collect feedback
7. Plan content updates
