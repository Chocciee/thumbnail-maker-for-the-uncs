# Thumbnail Studio

## Manage the shared library (what everyone sees)
- Backgrounds: put image files in `bank/backgrounds/`
- Images: put files in `bank/images/<Category name>/` (make a new folder for a new category)
- Then run `python3 make-manifest.py` and re-upload the site.

Visitors can also add their own backgrounds and images; those stay in their own browser and are never shared.

## Put it online with your own .host name
1. Upload this folder to a static host. Easiest: drag the folder onto app.netlify.com/drop, or use Cloudflare Pages or GitHub Pages (all free).
2. Buy your name (e.g. mythumbs.host) at a registrar such as Namecheap, Porkbun or Cloudflare.
3. In the host's "Custom domain" settings, add that name and copy the DNS records it shows into your registrar.
