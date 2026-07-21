import re
import json

filepath = '/Users/sidsmac/Documents/ADMAZIC/seo-in-surat.html'
outpath = '/Users/sidsmac/Documents/ADMAZIC/google-ads-in-surat.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

header_match = re.search(r'(.*?</header>)', content, re.DOTALL)
header = header_match.group(1)
footer_match = re.search(r'(<footer class="footer".*)', content, re.DOTALL)
footer = footer_match.group(1)

# Modify the title and meta in header
header = re.sub(r'<title>.*?</title>', '<title>Google Ads Services in Surat | #1 PPC Agency | ADMAZIC</title>', header)
header = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Looking for the best Google Ads services in Surat? ADMAZIC helps Diamond, Textile, and Real Estate businesses in Surat generate high-intent leads and sales with data-driven PPC campaigns.">', header)

ads_faqs = [
    {"q": "How much should I spend on Google Ads in Surat?", "a": "For local businesses in Surat, we recommend a starting budget of ₹30,000 to ₹50,000 per month to gather enough data. For highly competitive B2B export campaigns (like CVD diamonds), budgets often exceed ₹1,000,000 monthly to capture international markets effectively."},
    {"q": "Is Google Ads suitable for my Surat-based manufacturing business?", "a": "Yes. Google Ads is extremely powerful for manufacturers. By targeting high-intent B2B keywords like 'wholesale saree manufacturer' or 'lab grown diamond supplier', you can bypass third-party portals and connect directly with global buyers."},
    {"q": "How quickly can I expect results from Google Ads?", "a": "Unlike SEO, Google Ads can drive traffic and leads within 24 to 48 hours of campaign launch. However, the machine learning algorithms typically take 14 to 30 days to optimize for the lowest cost-per-acquisition (CPA)."},
    {"q": "Do I need a landing page for my Google Ads campaigns?", "a": "Absolutely. Sending paid traffic to a generic homepage wastes budget. We design highly optimized, conversion-focused landing pages that perfectly match the search intent, drastically improving your conversion rates."},
    {"q": "Can I advertise outside of Surat?", "a": "Yes! Google Ads allows you to target any city, country, or specific radius in the world. Many of our Surat clients use Google Ads strictly to acquire customers in the USA, UK, UAE, and across India."},
    {"q": "Which campaign type is best for my industry?", "a": "It depends on your goal. Search Ads are best for high-intent lead generation (like real estate and B2B). Shopping Ads are ideal for D2C e-commerce. Performance Max is great for scaling conversions across all Google networks."},
    {"q": "Why am I getting clicks but no leads or sales?", "a": "This usually happens due to poor search intent alignment (bidding on broad keywords), a slow or confusing landing page, lack of trust signals, or not having proper conversion tracking set up."},
    {"q": "How is ADMAZIC different from other Google Ads agencies in Surat?", "a": "We are a revenue-driven growth agency. We don't just optimize for clicks or impressions; we integrate with your CRM and optimize for final sales and Return on Ad Spend (ROAS)."},
    {"q": "Do you handle Google Ads for Real Estate developers in Surat?", "a": "Yes. We run highly targeted Search and Display campaigns for real estate projects in Vesu, Adajan, and Khajod, driving qualified site-visit leads from HNIs and NRIs."},
    {"q": "What is Performance Max and should I use it?", "a": "Performance Max (PMax) uses Google's AI to serve ads across Search, Display, YouTube, and Maps from a single campaign. It is incredibly effective for E-commerce and lead generation if fed with high-quality creative assets and conversion data."},
    {"q": "Can Google Ads help my local retail store in Surat?", "a": "Yes. Using Local Campaigns and highly geo-targeted Search Ads, we can drive footfall to your physical store in areas like Piplod or Parle Point when users search for your products nearby."},
    {"q": "Do you setup conversion tracking and Google Tag Manager?", "a": "Yes, proper tracking is the foundation of our strategy. We setup GTM, GA4, offline conversion tracking, and CRM integrations to ensure every rupee spent is measured against actual business revenue."},
    {"q": "What is Remarketing and how does it help?", "a": "Remarketing targets users who have previously visited your website but didn't convert. It keeps your brand visible across the internet, highly increasing the chances of them returning to make a purchase or inquiry."},
    {"q": "Can you audit my existing Google Ads account?", "a": "Yes, we offer comprehensive Google Ads account audits. We review your campaign structure, keyword match types, negative keywords, ad copy, and bidding strategies to identify wasted spend and growth opportunities."},
    {"q": "How do you report on campaign performance?", "a": "We provide transparent, real-time Looker Studio dashboards. You will see exactly how much was spent, the cost per lead, total conversions, and the overall ROAS of your campaigns at any time."}
]

schema_data = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{"@type": "Question", "name": faq["q"], "acceptedAnswer": {"@type": "Answer", "text": faq["a"]}} for faq in ads_faqs]
}
schema_json = json.dumps(schema_data, indent=2)

header = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: f'<script type="application/ld+json">\n{schema_json}\n</script>', header, flags=re.DOTALL)

new_body = f"""
  <!-- Section 1: Hero Section -->
  <section class="hero bg-grid" style="position: relative; padding-top: 180px; padding-bottom: 120px;">
    <div class="container" style="position: relative; z-index: 2; text-align: center; display: flex; flex-direction: column; align-items: center;">
      <div class="reveal text-reveal-up" style="margin-bottom: 20px;">
        <span class="section-tag" style="background: rgba(31,83,151,0.1); color: var(--accent-blue); border: 1px solid rgba(31,83,151,0.2);">Premium Google Ads Services in Surat</span>
      </div>
      <h1 class="hero-title reveal text-reveal-up delay-1" style="font-size: clamp(2.5rem, 5vw, 4.5rem); font-weight: 800; max-width: 950px; margin: 0 auto 24px auto; color: var(--text-primary); line-height: 1.1;">
        Turn Search Intent Into Revenue with <br><span class="text-highlight">Google Ads in Surat</span>
      </h1>
      <p class="hero-description reveal text-reveal-up delay-2" style="font-size: 1.2rem; max-width: 900px; margin: 0 auto 40px auto; color: var(--text-secondary); line-height: 1.8;">
        Surat's business ecosystem is fiercely competitive. From the diamonds polished in Mahidharpura to the luxury apartments rising in Vesu, your customers are searching for your exact services right now. We engineer hyper-targeted, high-ROAS Google Ads campaigns that capture high-intent buyers, eliminate wasted ad spend, and scale your business predictably. Stop relying on unpredictable referrals and start dominating the Google search results.
      </p>
      <div class="hero-buttons reveal text-reveal-up delay-3" style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 18px 40px; font-size: 1.1rem; background-color: #DC2626; color: #fff;">Get Your Free PPC Audit <i class="fas fa-arrow-right btn-icon"></i></a>
        <a href="tel:+917861910348" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem;"><i class="fas fa-phone-alt"></i> Call +91 78619 10348</a>
      </div>
    </div>
  </section>

  <!-- Section 2: Why Businesses in Surat Should Invest in Google Ads -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div style="max-width: 1400px; margin: 0 auto; padding: 0 20px;">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Why Surat Businesses Must Invest in Google Ads</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">The traditional referral network is no longer enough to scale rapidly.</p>
      </div>
      
      <div class="comparison-grid reveal surat-grid-3">
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px; border-radius: 12px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-bullseye"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Capturing High Commercial Intent</h3>
          <p style="color: var(--text-secondary); line-height: 1.8; font-size: 1.05rem;">
            Unlike social media where you interrupt users scrolling through feeds, Google Ads places your business directly in front of people actively searching for a solution. When a procurement manager searches for "wholesale textile manufacturers in Surat" or an NRI searches for "luxury 4BHK flats in Vesu," they have their credit cards ready. Google Ads ensures you are the first business they see, capturing peak commercial intent.
          </p>
        </div>
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px; border-radius: 12px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-chart-line"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Outpacing Growing Competition</h3>
          <p style="color: var(--text-secondary); line-height: 1.8; font-size: 1.05rem;">
            Surat is experiencing unprecedented economic expansion. With the influx of new agencies, real estate developers, and modernized manufacturing plants, the competition is fiercer than ever. Relying purely on traditional word-of-mouth or B2B directories like IndiaMART limits your growth and pits you in price wars. Google Ads allows you to bypass the noise, elevate your brand, and outbid competitors for the most valuable traffic.
          </p>
        </div>
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px; border-radius: 12px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-tachometer-alt"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Immediate Scalability and Speed</h3>
          <p style="color: var(--text-secondary); line-height: 1.8; font-size: 1.05rem;">
            While SEO is critical for long-term compounding growth, it takes months to rank. Google Ads provides immediate visibility. Within 48 hours of launching a structurally sound campaign, your business can start receiving highly qualified phone calls, form submissions, and sales. This speed of execution is critical for real estate project launches, seasonal e-commerce sales, and rapidly scaling B2B manufacturers.
          </p>
        </div>
      </div>
      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-secondary" style="padding: 15px 35px; display: inline-block;"><i class="fas fa-rocket"></i> Launch Your Ads Campaign Today</a>
      </div>
    </div>
  </section>

  <!-- Section 3: Business Landscape of Surat -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 40px;">
        <h2 class="section-title" style="color: var(--text-primary);">The Rapidly Evolving Business Landscape of Surat</h2>
        <p class="section-subtitle" style="color: var(--text-secondary); max-width: 800px; text-align: center; margin: 0 auto;">Understanding the economic engine driving South Gujarat.</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.15rem; line-height: 1.9; text-align: center; max-width: 1000px; margin: 0 auto;">
        <p style="margin-bottom: 25px;">
          Surat is widely celebrated as the "Diamond City of India" and the "Silk City," dominating the global diamond polishing industry and domestic synthetic textile manufacturing. However, this traditional narrative is rapidly expanding. Today, Surat is undergoing a massive corporate metamorphosis. With infrastructure marvels like the Surat Diamond Bourse (SDB) in Khajod and the sprawling DREAM City project, Surat is attracting massive national and international investments.
        </p>
        <p style="margin-bottom: 25px;">
          This economic boom has catalyzed a vibrant SME and startup ecosystem. We are seeing a significant generational shift—traditional family-run businesses are being inherited by a younger, tech-savvy generation. These modern leaders are pivoting away from heavy reliance on brokers and wholesale markets towards Direct-to-Consumer (D2C) e-commerce brands, digital B2B exports, and aggressive online brand building. The IT sector is also taking root, with numerous software development agencies and professional service providers setting up shop in premium commercial zones.
        </p>
        <p>
          Furthermore, the real estate sector is experiencing explosive growth, catering to the influx of corporate professionals and HNIs. In this high-stakes, fast-paced environment, having a dominant digital presence is mandatory. Businesses that fail to leverage targeted digital advertising like Google Ads risk being overshadowed by more aggressive, digitally-native competitors who are capitalizing on the millions of daily searches originating from and targeting Surat.
        </p>
      </div>
    </div>
  </section>

  <!-- Section 4: Major Commercial and Business Areas in Surat -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Major Commercial and Business Areas We Target</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Pinpoint geo-targeting for maximum localized ROI.</p>
      </div>
      <div class="grid-list reveal surat-grid-3">
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-building"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Vesu, Piplod & VIP Road</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">The epicenter of Surat's luxury real estate, high-end retail, elite healthcare clinics, and modern corporate IT parks. Google Ads here are highly effective for premium B2C services, D2C retail stores, and real estate lead generation targeting high-net-worth individuals.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-gem"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Mahidharpura, Varachha & Katargam</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">The traditional heartlands of the diamond manufacturing and trading industry. We deploy targeted B2B Google Ads to help Lab-Grown Diamond (CVD) manufacturers and traditional jewelers bypass brokers and secure lucrative international export contracts.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-tshirt"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Ring Road, Udhna & Sahara Darwaja</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">The bustling core of Surat's massive textile and apparel wholesale markets. Google Ads strategies here focus on national reach, helping wholesalers and saree manufacturers capture high-volume bulk orders from retailers across India.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-city"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Khajod (DREAM City)</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">Home to the Surat Diamond Bourse, Khajod is rapidly becoming a global corporate hub. This area requires aggressive, international-facing Search and Display campaigns to attract global investors, foreign diamond buyers, and multinational corporate tenants.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-industry"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Sachin, Pandesara & Hazira GIDC</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">The heavy industrial zones featuring textile dyeing mills, chemical plants, and heavy engineering. We leverage Google Ads to generate high-value RFQs and industrial equipment inquiries from national and international procurement managers.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2.2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-store"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Adajan, Pal & Rander</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">Rapidly expanding residential and commercial corridors that are perfect targets for Local Search Ads. We help local service providers, boutique clinics, educational institutes, and restaurants capture hyper-local "near me" search traffic effectively.</p>
        </div>
      </div>
      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-primary" style="padding: 15px 35px; background: var(--accent-blue); display: inline-block;">Target Your Exact Audience <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 5: Businesses That Can Benefit From Google Ads -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Who Needs Google Ads in Surat?</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Data-driven advertising drives growth across every major sector.</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
        <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px;">
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-building" style="color: var(--accent-blue); width: 30px;"></i> Real Estate Developers</strong>
            With high-ticket items like luxury apartments in Vesu or commercial spaces in Khajod, search intent is critical. We use precise Search and Display ads targeting NRIs and affluent locals, driving qualified site-visit leads directly to your CRM.
          </li>
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-gem" style="color: var(--accent-blue); width: 30px;"></i> Diamonds & Jewelry Exporters</strong>
            Surat is the global hub for Lab-Grown Diamonds (CVD). By bidding on keywords like "wholesale lab grown diamond suppliers," we connect your manufacturing unit directly with B2B buyers in the USA, UK, and UAE, bypassing middlemen.
          </li>
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-tshirt" style="color: var(--accent-blue); width: 30px;"></i> Textile Manufacturers & D2C Brands</strong>
            Whether you are a wholesaler in Ring Road looking for bulk pan-India orders or a modern D2C ethnic wear brand leveraging Performance Max and Google Shopping Ads, we ensure your products dominate the search engine results page.
          </li>
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-hospital" style="color: var(--accent-blue); width: 30px;"></i> Healthcare & Multi-Specialty Clinics</strong>
            Patients don't browse for doctors; they search when they need one. We run highly localized Search Ads for specific treatments (e.g., "best orthopedic surgeon in Surat" or "IVF clinic near me") ensuring you capture patients at their moment of highest need.
          </li>
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-industry" style="color: var(--accent-blue); width: 30px;"></i> Heavy Machinery & Industrial Manufacturers</strong>
            Businesses in Sachin and Pandesara GIDC manufacturing textile machinery, chemicals, or heavy engineering equipment rely on highly technical B2B Search Ads to generate high-value Request For Quotes (RFQs) and secure massive industrial tenders.
          </li>
          <li style="background: rgba(255,255,255,0.02); padding: 30px; border-left: 4px solid var(--accent-blue); border-radius: 8px;">
            <strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-bottom: 10px;"><i class="fas fa-graduation-cap" style="color: var(--accent-blue); width: 30px;"></i> Educational Institutes & Coaching Centers</strong>
            With intense competition in the education sector, we help schools, universities, and specialized coaching centers in Surat drive enrollments through targeted Search campaigns leading up to admission seasons, coupled with persistent YouTube remarketing.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Section 6: Google Ads Services We Offer -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Our Comprehensive Google Ads Services</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Full-funnel campaign management engineered for maximum ROAS.</p>
      </div>
      
      <div class="services-grid reveal surat-grid-3">
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Search Ads (PPC)</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">We build highly structured text ad campaigns targeting commercial intent keywords. By rigorously managing match types and negative keywords, we ensure you only pay for clicks that have a high probability of converting.</p>
        </div>
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Performance Max (PMax)</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">We leverage Google's most advanced AI-driven campaign type. By feeding PMax high-quality creative assets, precise audience signals, and flawless conversion data, we scale your results across Search, Display, YouTube, and Maps.</p>
        </div>
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Google Shopping Ads</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">Crucial for Surat's D2C apparel and jewelry brands. We optimize your Google Merchant Center product feed to display rich, visually appealing product ads directly at the top of the search results, driving high-converting e-commerce traffic.</p>
        </div>
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Advanced Remarketing</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">Don't lose the 95% of traffic that doesn't convert immediately. We design strategic remarketing campaigns across the Google Display Network and YouTube to nurture past visitors and bring them back to complete their purchase or inquiry.</p>
        </div>
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Conversion Tracking & GTM</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">Data is everything. We implement robust tracking using Google Tag Manager and GA4. We track form submissions, phone calls, WhatsApp clicks, and e-commerce purchases, providing the algorithms with the exact data needed to optimize.</p>
        </div>
        <div class="service-card" style="padding: 35px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Landing Page Optimization (CRO)</h3>
          <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">Sending expensive ad traffic to a slow, confusing homepage is a recipe for failure. We design, A/B test, and optimize dedicated landing pages that are laser-focused on converting your paid traffic into tangible business leads.</p>
        </div>
      </div>
      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-secondary" style="padding: 15px 35px; display: inline-block;"><i class="fas fa-search-plus"></i> Audit My Current Campaigns</a>
      </div>
    </div>
  </section>

  <!-- Section 7: Our Google Ads Strategy -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">The ADMAZIC Strategy: How We Win</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">A systematic, data-driven methodology that guarantees performance.</p>
      </div>
      
      <div class="process-timeline reveal" style="max-width: 900px; margin: 0 auto;">
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2.5rem; font-weight: 800; color: var(--accent-blue); margin-right: 30px; opacity: 0.8;">01</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.4rem;">Deep Business & Competitor Research</h3>
            <p style="color: var(--text-secondary); line-height: 1.7;">Before spending a single rupee, we dive deep into your business model, profit margins, and target audience. We analyze your top competitors in Surat to uncover gaps in their advertising strategies, allowing us to strike where they are weakest.</p>
          </div>
        </div>
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2.5rem; font-weight: 800; color: var(--accent-blue); margin-right: 30px; opacity: 0.8;">02</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.4rem;">Granular Keyword Strategy</h3>
            <p style="color: var(--text-secondary); line-height: 1.7;">We don't bid on vanity keywords. We identify highly specific, commercial-intent search terms that signify a user is ready to buy or inquire. We also build extensive negative keyword lists to prevent your ads from showing on irrelevant, budget-draining searches.</p>
          </div>
        </div>
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2.5rem; font-weight: 800; color: var(--accent-blue); margin-right: 30px; opacity: 0.8;">03</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.4rem;">Ad Copy & Landing Page Alignment</h3>
            <p style="color: var(--text-secondary); line-height: 1.7;">We write compelling, psychologically persuasive ad copy that drives high Click-Through Rates (CTR). We then ensure that the ad perfectly aligns with the messaging on the landing page, providing a seamless user experience that skyrockets conversion rates.</p>
          </div>
        </div>
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2.5rem; font-weight: 800; color: var(--accent-blue); margin-right: 30px; opacity: 0.8;">04</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.4rem;">Flawless Tracking & Integration</h3>
            <p style="color: var(--text-secondary); line-height: 1.7;">We set up intricate conversion tracking via Google Tag Manager. Whether it's a form fill, a phone call, a WhatsApp click, or an e-commerce purchase, we track it. We can even integrate offline conversions from your CRM back into Google Ads to train the bidding algorithms on actual closed sales.</p>
          </div>
        </div>
        <div style="display: flex; background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2.5rem; font-weight: 800; color: var(--accent-blue); margin-right: 30px; opacity: 0.8;">05</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.4rem;">Relentless Optimization & Scaling</h3>
            <p style="color: var(--text-secondary); line-height: 1.7;">A campaign launch is just the beginning. We perform daily and weekly optimizations—adjusting bids, split-testing ad creatives, pausing underperforming keywords, and reallocating budget to the most profitable campaigns. As your ROAS stabilizes, we aggressively scale your budget to dominate the market.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8: Google Ads Campaign Types -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Demystifying Google Ads Campaign Types</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">We deploy the right artillery for your specific business goals.</p>
      </div>
      <div class="surat-grid-2 reveal">
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px; font-size: 1.3rem;">Search Campaigns</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem; margin-bottom: 15px;">The foundation of lead generation. Text-based ads that appear exactly when a user types a relevant query. <br><strong>Best For:</strong> Real Estate, B2B Manufacturers, Healthcare, Professional Services.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px; font-size: 1.3rem;">Performance Max (PMax)</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem; margin-bottom: 15px;">Google's automated, goal-based campaign that serves ads across all Google channels from a single campaign to maximize conversions. <br><strong>Best For:</strong> E-commerce Brands, D2C Apparel, Scaled Lead Generation.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px; font-size: 1.3rem;">Google Shopping Campaigns</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem; margin-bottom: 15px;">Highly visual product listings (image, price, title) that appear at the very top of search results, driving users directly to the product page. <br><strong>Best For:</strong> Retail Jewelers, Online Textile Boutiques, Any Retail E-commerce.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px; font-size: 1.3rem;">Display & YouTube Remarketing</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem; margin-bottom: 15px;">Visual banners and video ads that follow your website visitors across millions of websites and YouTube, keeping your brand top-of-mind. <br><strong>Best For:</strong> High-ticket items (Real Estate, Diamonds) with long sales cycles.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9: Google Ads Opportunities in Surat -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="surat-grid-2">
        <div class="reveal">
          <h2 style="color: var(--text-primary); margin-bottom: 25px;">Untapped Advertising Opportunities in Surat</h2>
          <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; font-size: 1.1rem;">
            Surat sits at a unique intersection of heavy traditional manufacturing and rapid digital modernization. This creates massive, untapped advertising arbitrage opportunities for early adopters.
          </p>
          <p style="color: var(--text-secondary); line-height: 1.8; font-size: 1.1rem;">
            <strong>International Arbitrage:</strong> Lab-grown diamond (CVD) manufacturers in Varachha have the unique opportunity to run heavily targeted Search Ads directly in New York's Diamond District or Antwerp. By capturing high-value B2B buyers digitally, they bypass the immense costs of traditional international trade shows and middlemen.
          </p>
        </div>
        <div class="reveal">
          <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; font-size: 1.1rem;">
            <strong>National Domination:</strong> Textile wholesalers in Ring Road can completely bypass aggregate portals. By running pan-India Search and Performance Max campaigns targeting terms like "buy sarees wholesale online," they can build direct, loyal networks of retailers across the country.
          </p>
          <p style="color: var(--text-secondary); line-height: 1.8; font-size: 1.1rem;">
            <strong>Hyper-Local Dominance:</strong> With Surat's population wealth growing, local real estate developers and luxury service providers can utilize geo-fenced advertising to target affluent neighborhoods like Vesu, ensuring their high-end offerings are constantly visible to the city's top 1%.
          </p>
        </div>
      </div>
      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 15px 35px; background: #DC2626; display: inline-block;">Discover Your Market Opportunity <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 10: Recommended Advertising Budgets -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Recommended Advertising Budgets</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Realistic budget expectations for sustainable growth. We do not make false promises.</p>
      </div>
      <div class="grid-list reveal surat-grid-2">
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Small & Local Businesses</h3>
          <p style="color: var(--accent-blue); font-weight: 600; margin-bottom: 15px; font-size: 1.1rem;">Suggested Monthly Ad Spend: ₹30,000 - ₹50,000</p>
          <p style="color: var(--text-secondary); line-height: 1.6;">Ideal for local clinics, boutique restaurants, and professional service providers targeting a 10km radius within Surat. This budget allows Google's algorithms enough data to optimize for local lead generation effectively.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Medium Businesses & D2C Brands</h3>
          <p style="color: var(--accent-blue); font-weight: 600; margin-bottom: 15px; font-size: 1.1rem;">Suggested Monthly Ad Spend: ₹75,000 - ₹2,00,000</p>
          <p style="color: var(--text-secondary); line-height: 1.6;">Perfect for scaling e-commerce brands, mid-sized real estate projects, and regional B2B suppliers. Requires robust conversion tracking, dedicated landing pages, and active A/B testing.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">High Growth & B2B Exporters</h3>
          <p style="color: var(--accent-blue); font-weight: 600; margin-bottom: 15px; font-size: 1.1rem;">Suggested Monthly Ad Spend: ₹3,00,000 - ₹10,00,000+</p>
          <p style="color: var(--text-secondary); line-height: 1.6;">Essential for CVD Diamond exporters, massive textile mills, and enterprise real estate developers targeting national and international markets. Involves complex multi-channel strategies, CRM integrations, and aggressive market share acquisition.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Enterprise & Corporate</h3>
          <p style="color: var(--accent-blue); font-weight: 600; margin-bottom: 15px; font-size: 1.1rem;">Custom Built Strategies</p>
          <p style="color: var(--text-secondary); line-height: 1.6;">For multinational corporations operating out of the Surat Diamond Bourse or major industrial zones. Focuses on global brand dominance, advanced data attribution modeling, and maximizing overall pipeline revenue.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 11: Landing Page and Conversion Optimization -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Why Clicks Don't Always Equal Leads (The Power of CRO)</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Your ad campaign is only as good as the landing page it points to.</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8; max-width: 1000px; margin: 0 auto;">
        <p style="margin-bottom: 30px; text-align: center;">
          The biggest mistake businesses make with Google Ads is sending expensive, high-intent traffic to a slow, generic homepage. If a user searches for "2BHK flats in Adajan," they do not want to see your company's 'About Us' page; they want to see floor plans, pricing, and amenities for that specific project immediately. This is where Conversion Rate Optimization (CRO) changes the game.
        </p>
        <div class="surat-grid-3">
          <div style="background: rgba(255,255,255,0.02); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: var(--text-primary); margin-bottom: 15px;"><i class="fas fa-bolt" style="color: var(--accent-blue); margin-right: 10px;"></i> Dedicated Landing Pages</h4>
            <p style="font-size: 0.95rem;">We build custom, lightning-fast landing pages for every ad group, ensuring the messaging perfectly matches the user's search intent, drastically lowering bounce rates.</p>
          </div>
          <div style="background: rgba(255,255,255,0.02); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: var(--text-primary); margin-bottom: 15px;"><i class="fab fa-whatsapp" style="color: #25D366; margin-right: 10px;"></i> WhatsApp & Lead Integrations</h4>
            <p style="font-size: 0.95rem;">We integrate frictionless conversion points like WhatsApp chat widgets, floating lead forms, and direct click-to-call buttons tailored to how Indian consumers prefer to communicate.</p>
          </div>
          <div style="background: rgba(255,255,255,0.02); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: var(--text-primary); margin-bottom: 15px;"><i class="fas fa-database" style="color: var(--accent-blue); margin-right: 10px;"></i> CRM & Automation</h4>
            <p style="font-size: 0.95rem;">Every lead generated is automatically pushed into your CRM (like Salesforce, HubSpot, or Zoho) triggering instant email/SMS notifications to your sales team to strike while the lead is hot.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 12: Industries We Serve -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Industries We Serve in Surat</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Deep expertise across South Gujarat's core economic sectors.</p>
      </div>
      <div class="grid-list reveal surat-grid-3 text-center">
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Diamond Manufacturing & Export</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Textile & Apparel Wholesalers</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Luxury Real Estate & Commercial</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">D2C Fashion & Jewelry Brands</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Heavy Machinery & Engineering</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Hospitals & Healthcare Facilities</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Educational Institutes & Coaching</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Legal & Financial Professionals</h4>
        </div>
        <div style="padding: 20px; border: 1px solid var(--glass-border); border-radius: 12px; background: var(--bg-primary);">
          <h4 style="color: var(--text-primary); margin: 0;">Architecture & Interior Design</h4>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 13: Why Choose Us -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Why Partner With ADMAZIC?</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">We are not just media buyers; we are growth consultants.</p>
      </div>
      <div class="surat-grid-2 reveal">
        <div style="display: flex; align-items: flex-start; gap: 20px; background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <i class="fas fa-chart-pie" style="font-size: 2rem; color: var(--accent-blue); margin-top: 5px;"></i>
          <div>
            <h4 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.2rem;">Revenue-Centric, Not Click-Centric</h4>
            <p style="color: var(--text-secondary); line-height: 1.6;">We don't boast about impressions or cheap clicks. We optimize entirely for the metrics that keep your business alive: Cost Per Acquisition (CPA) and Return on Ad Spend (ROAS).</p>
          </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <i class="fas fa-search-dollar" style="font-size: 2rem; color: var(--accent-blue); margin-top: 5px;"></i>
          <div>
            <h4 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.2rem;">Transparent Live Reporting</h4>
            <p style="color: var(--text-secondary); line-height: 1.6;">No smoke and mirrors. You get access to a live, customized Looker Studio dashboard detailing exactly where every single rupee is spent and what it generated in return.</p>
          </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <i class="fas fa-cogs" style="font-size: 2rem; color: var(--accent-blue); margin-top: 5px;"></i>
          <div>
            <h4 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.2rem;">Full Automation Capabilities</h4>
            <p style="color: var(--text-secondary); line-height: 1.6;">We bridge the gap between marketing and sales. By integrating Google Ads directly with your CRM and WhatsApp APIs, we build automated pipelines that nurture leads instantly.</p>
          </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <i class="fas fa-chess-knight" style="font-size: 2rem; color: var(--accent-blue); margin-top: 5px;"></i>
          <div>
            <h4 style="color: var(--text-primary); margin-bottom: 10px; font-size: 1.2rem;">Strategic Business Approach</h4>
            <p style="color: var(--text-secondary); line-height: 1.6;">We act as an extension of your business. We analyze your profit margins, average order values, and customer lifetime value to build campaigns that are actually profitable to scale.</p>
          </div>
        </div>
      </div>
      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 15px 35px; background: var(--accent-blue); display: inline-block;">Consult With An Expert <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 14: Nearby Cities We Serve -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 80px 0;">
    <div class="container text-center reveal" style="text-align: center;">
      <h2 style="color: var(--text-primary); margin-bottom: 20px; text-align: center;">Nearby Cities We Serve</h2>
      <p style="color: var(--text-secondary); line-height: 1.8; max-width: 700px; margin: 0 auto; text-align: center;">
        Beyond Surat, our high-performance Google Ads and digital growth strategies support ambitious businesses across the entire South Gujarat industrial and commercial corridor:
      </p>
      <div style="display: flex; justify-content: center; gap: 20px; margin-top: 40px; flex-wrap: wrap;">
        <div class="city-pill">Navsari</div>
        <div class="city-pill">Vapi</div>
        <div class="city-pill">Bharuch</div>
        <div class="city-pill">Valsad</div>
        <div class="city-pill">Ankleshwar</div>
        <div class="city-pill">Dahej</div>
      </div>
    </div>
  </section>

  <!-- Section 15: Frequently Asked Questions -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin-bottom: 50px;">
        <h2 class="section-title" style="color: var(--text-primary);">Frequently Asked Questions</h2>
        <p class="section-subtitle" style="color: var(--text-secondary);">Everything you need to know about scaling with Google Ads.</p>
      </div>
      
      <div class="faq-container reveal" style="max-width: 800px; margin: 0 auto;" id="faq-list">
"""

for i, faq in enumerate(ads_faqs):
    new_body += f"""
        <div class="faq-accordion">
          <button class="faq-question">{i+1}. {faq['q']} <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>{faq['a']}</p></div>
        </div>
"""

new_body += """
      </div>
      
      <script>
        document.querySelectorAll('.faq-question').forEach(button => {
          button.addEventListener('click', () => {
            const accordion = button.parentElement;
            const isActive = accordion.classList.contains('active');
            
            document.querySelectorAll('.faq-accordion').forEach(acc => acc.classList.remove('active'));
            
            if (!isActive) {
              accordion.classList.add('active');
            }
          });
        });
      </script>
    </div>
  </section>

  <!-- Final Call to Action -->
  <section class="section bg-grid" style="background-color: #0F172A; color: #fff; text-align: center; border-top: 1px solid var(--glass-border);">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 120px 0;">
      <div class="reveal pulse-slow">
        <h2 class="section-title" style="margin-bottom: 20px; color: #fff;">Stop Wasting Ad Spend. Start Scaling Revenue.</h2>
        <p class="section-subtitle" style="margin-bottom: 40px; color: rgba(255,255,255,0.7); font-size: 1.2rem; line-height: 1.6;">
          Your competitors in Surat are already bidding on your most profitable keywords. Let our Google Ads specialists perform a deep-dive audit on your market, map your revenue potential, and build a campaign architecture designed purely for growth.
        </p>
        <div style="display: flex; justify-content: center; gap: 20px; width: 100%; flex-wrap: wrap;">
          <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 18px 40px; font-size: 1.1rem; background: #DC2626; color: #fff; box-shadow: 0 0 20px rgba(220, 38, 38, 0.5); display: inline-block;">Request Your Free Ad Audit <i class="fas fa-arrow-right btn-icon"></i></a>
          <a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem; display: inline-block;">Strategy Consultation</a>
        </div>
      </div>
    </div>
  </section>
"""

final_html = header + "\n" + new_body + "\n" + footer

with open(outpath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated google-ads-in-surat.html successfully.")
