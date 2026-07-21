import re

filepath = '/Users/sidsmac/Documents/ADMAZIC/seo-in-surat.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header
header_match = re.search(r'(.*?</header>)', content, re.DOTALL)
header = header_match.group(1)

# Extract footer
footer_match = re.search(r'(<footer class="footer".*)', content, re.DOTALL)
footer = footer_match.group(1)

# Add custom CSS and FAQ Schema to the header
custom_head = """
<style>
  .surat-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
  .surat-grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; }
  @media (max-width: 992px) {
    .surat-grid-3 { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 768px) {
    .surat-grid-3, .surat-grid-2 { grid-template-columns: 1fr; }
  }
  .city-pill {
    background: var(--bg-primary); 
    padding: 12px 30px; 
    border-radius: 30px; 
    border: 1px solid var(--glass-border); 
    color: var(--accent-blue); 
    font-weight: 600;
    transition: all 0.3s ease;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  .city-pill:hover {
    background: var(--accent-blue);
    color: #fff;
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(31,83,151,0.3);
  }
  .faq-accordion {
    background: var(--bg-primary);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    margin-bottom: 15px;
    overflow: hidden;
  }
  .faq-question {
    width: 100%;
    text-align: left;
    padding: 20px 25px;
    background: none;
    border: none;
    color: var(--text-primary);
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.2s;
  }
  .faq-question:hover { background: rgba(255,255,255,0.02); }
  .faq-answer {
    padding: 0 25px;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding 0.3s ease;
    color: var(--text-secondary);
    line-height: 1.6;
  }
  .faq-accordion.active .faq-answer {
    padding: 0 25px 25px 25px;
    max-height: 500px;
  }
  .faq-accordion.active .faq-question i {
    transform: rotate(180deg);
  }
</style>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How long does it take to see SEO results in Surat?", "acceptedAnswer": {"@type": "Answer", "text": "Typically 3 to 6 months for noticeable improvements, depending on industry competitiveness like textiles or diamonds."}},
    {"@type": "Question", "name": "Do you provide local SEO for physical stores in Surat?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, we optimize Google Business Profiles for highly targeted local traffic in areas like Vesu, Adajan, and Piplod."}},
    {"@type": "Question", "name": "Can SEO help my diamond export business?", "acceptedAnswer": {"@type": "Answer", "text": "Absolutely. Enterprise B2B SEO ranks your website globally, connecting Surat manufacturers directly with international buyers."}},
    {"@type": "Question", "name": "What makes ADMAZIC different from other Surat SEO agencies?", "acceptedAnswer": {"@type": "Answer", "text": "We are revenue-driven. We focus on technical excellence and high-authority content, not spammy links or vanity metrics."}},
    {"@type": "Question", "name": "Do you help textile wholesalers rank pan-India?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, we optimize product and category pages to bypass B2B portals and capture direct wholesale inquiries nationally."}},
    {"@type": "Question", "name": "How much does SEO cost in Surat?", "acceptedAnswer": {"@type": "Answer", "text": "Pricing varies based on your current digital footprint and competitive landscape. We offer custom quotes after a free audit."}},
    {"@type": "Question", "name": "Is SEO better than Google Ads for my business?", "acceptedAnswer": {"@type": "Answer", "text": "SEO provides compounding long-term ROI and lowers acquisition costs, while Ads provide immediate but temporary traffic. We often recommend a hybrid approach."}},
    {"@type": "Question", "name": "Do you offer E-Commerce SEO for Surat brands?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, we specialize in Shopify and WooCommerce SEO for D2C ethnic wear, jewelry, and retail brands."}},
    {"@type": "Question", "name": "Why is my Surat business not ranking on Google Maps?", "acceptedAnswer": {"@type": "Answer", "text": "It usually comes down to inconsistent NAP data, lack of localized citations, poor review management, or an unoptimized Google Business Profile."}},
    {"@type": "Question", "name": "Can SEO generate B2B leads for heavy machinery?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. We target specific, high-intent industrial keywords that procurement managers use when searching for machinery manufacturers in GIDC areas."}},
    {"@type": "Question", "name": "Do you write content for the SEO campaigns?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, our team creates E-E-A-T optimized, semantic content that establishes your authority and ranks highly on Google."}},
    {"@type": "Question", "name": "What is Technical SEO and why do I need it?", "acceptedAnswer": {"@type": "Answer", "text": "Technical SEO ensures your site loads fast, is mobile-friendly, and has clean architecture so Google can crawl and index it flawlessly."}},
    {"@type": "Question", "name": "Do you build backlinks?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, we execute digital PR and manual outreach to secure high-authority, spam-free backlinks that drive real ranking power."}},
    {"@type": "Question", "name": "Will SEO work for real estate developers in Surat?", "acceptedAnswer": {"@type": "Answer", "text": "SEO is highly effective for real estate. Ranking for 'luxury flats in Vesu' or 'commercial spaces in Khajod' drives high-ticket investor leads."}},
    {"@type": "Question", "name": "How do we get started?", "acceptedAnswer": {"@type": "Answer", "text": "Claim your free SEO audit slot on our website. We'll analyze your site and present a customized growth roadmap."}}
  ]
}
</script>
</head>"""

header = header.replace('</head>', custom_head)

new_body = """
  <!-- Section 1: Hero Section -->
  <section class="hero bg-grid" style="position: relative; padding-top: 180px; padding-bottom: 120px;">
    <div class="container text-center" style="position: relative; z-index: 2;">
      <div class="reveal text-reveal-up" style="margin-bottom: 20px;">
        <span class="section-tag" style="background: rgba(31,83,151,0.1); color: var(--accent-blue); border: 1px solid rgba(31,83,151,0.2);">#1 Enterprise SEO Agency in Surat, Gujarat</span>
      </div>
      <h1 class="hero-title reveal text-reveal-up delay-1" style="font-size: clamp(2.5rem, 5vw, 4.5rem); font-weight: 800; max-width: 950px; margin: 0 auto 24px auto; color: var(--text-primary); line-height: 1.1;">
        Dominate Local & Global Markets with <br><span class="text-highlight">Data-Driven SEO in Surat</span>
      </h1>
      <p class="hero-description reveal text-reveal-up delay-2" style="font-size: 1.2rem; max-width: 800px; margin: 0 auto 40px auto; color: var(--text-secondary); line-height: 1.6;">
        Surat is no longer just the Diamond and Textile capital; it is a rapidly digitizing economic powerhouse. At ADMAZIC, we engineer highly technical, revenue-focused SEO strategies that help Surat-based businesses outrank competitors, attract high-paying clients, and build a compounding digital moat that generates leads on autopilot.
      </p>
      <div class="hero-buttons reveal text-reveal-up delay-3" style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 18px 40px; font-size: 1.1rem; background-color: #DC2626; color: #fff;">Get Your Free Surat SEO Audit <i class="fas fa-arrow-right btn-icon"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 2: Why Businesses in Surat Need SEO -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Why Businesses in Surat Need Strategic SEO</h2>
        <p class="section-subtitle">The traditional B2B handbook is changing. Your buyers are searching online.</p>
      </div>
      
      <div class="comparison-grid reveal surat-grid-3">
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-chart-line"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Transition from Offline to Online</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem;">
            Historically, business in Surat operated heavily on word-of-mouth and established trade networks in markets like Ring Road or Mahidharpura. Today, whether it's a global diamond buyer or a pan-India textile wholesaler, their first step is a Google search. If your business doesn't appear in the top 3 results, your competitor gets the contract.
          </p>
        </div>
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-globe-asia"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Capturing Export & National Markets</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem;">
            Surat is an export hub. Local SEO puts you on the map in Gujarat, but Enterprise SEO allows a diamond manufacturer in Surat to rank for high-intent queries from buyers in the US, UAE, and Europe. SEO breaks geographical limitations, turning a local manufacturing unit into a globally recognized supplier.
          </p>
        </div>
        <div class="glass-card" style="background: var(--bg-primary); border: 1px solid var(--glass-border); padding: 40px;">
          <div class="card-icon" style="color: var(--accent-blue); font-size: 2.5rem; margin-bottom: 20px;"><i class="fas fa-shield-alt"></i></div>
          <h3 class="card-title" style="color: var(--text-primary); font-size: 1.5rem; margin-bottom: 15px;">Lowering Blended Acquisition Costs</h3>
          <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1rem;">
            While Meta and Google Ads are powerful for immediate traction, Cost Per Click (CPC) is rising every year. SEO is the only marketing channel that compounds. The technical foundations and content silos we build today will continue to drive free, high-intent traffic for years, lowering your overall customer acquisition costs over time.
          </p>
        </div>
      </div>
      <div class="reveal text-center" style="margin-top: 50px;">
        <a href="free-audit" class="btn btn-secondary" style="padding: 15px 35px;"><i class="fas fa-rocket"></i> Scale Your Surat Business Today</a>
      </div>
    </div>
  </section>

  <!-- Section 3: Overview of the Business Landscape of Surat -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Overview of the Business Landscape of Surat</h2>
        <p class="section-subtitle" style="max-width: 800px; text-align: center; margin: 0 auto;">Understanding the economic engine of Gujarat.</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8; text-align: center; max-width: 1000px; margin: 0 auto;">
        <p style="margin-bottom: 20px;">
          Surat, often referred to as the "Diamond City of India" and the "Silk City of India," is one of the fastest-growing cities in the world. It is the economic powerhouse of South Gujarat, contributing massively to India's GDP. The city is globally renowned for polishing over 90% of the world's rough diamonds and producing a staggering volume of synthetic textiles.
        </p>
        <p style="margin-bottom: 20px;">
          However, the landscape is shifting. With the advent of the Surat Diamond Bourse (SDB) and the upcoming DREAM City project, Surat is transitioning from a purely manufacturing hub to a massive corporate and trading center. Furthermore, IT corridors are emerging, and real estate is booming. This shift from traditional "Lala companies" to professionally managed corporate entities means that digital branding, corporate identity, and Search Engine Optimization have suddenly become board-level priorities.
        </p>
        <p>
          As the younger generation takes over legacy businesses, there is a massive push towards D2C (Direct to Consumer) brands, online B2B portals, and global e-commerce. In this rapidly modernizing landscape, having a fast, optimized, and authoritative website is no longer optional—it is the baseline for survival and scalability.
        </p>
      </div>
    </div>
  </section>

  <!-- Section 4: Major Commercial and Business Areas in Surat -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Major Commercial and Business Areas in Surat</h2>
        <p class="section-subtitle">We optimize for local dominance across all major hubs.</p>
      </div>
      <div class="grid-list reveal surat-grid-3">
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-city"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Vesu & Piplod</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The premium commercial and IT hubs of Surat, housing modern agencies, real estate developers, and high-end retail brands.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-gem"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Varachha & Katargam</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The beating heart of the diamond manufacturing industry. Essential for B2B diamond SEO strategies.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-truck-loading"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Ring Road & Udhna</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The epicenter of Surat's textile markets, wholesalers, and logistics companies requiring pan-India visibility.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-building"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Khajod (DREAM City)</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The upcoming corporate megahub featuring the Surat Diamond Bourse. A critical target for global SEO positioning.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-industry"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Sachin & Pandesara GIDC</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The industrial zones housing massive textile dyeing, printing mills, and heavy engineering companies.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 30px; border-radius: 8px; border: 1px solid var(--glass-border); text-align: center;">
          <div style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 15px;"><i class="fas fa-store"></i></div>
          <h3 style="color: var(--text-primary); margin-bottom: 10px;">Adajan & Pal</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">A rapidly growing residential and commercial corridor, ideal for local businesses, clinics, and service providers.</p>
        </div>
      </div>
      <div class="reveal text-center" style="margin-top: 50px;">
        <a href="free-audit" class="btn btn-primary" style="padding: 15px 35px; background: var(--accent-blue);">Capture Your Target Area Now <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 5: Industries That Can Benefit From SEO -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Industries That Thrive on SEO in Surat</h2>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 20px; background: rgba(255,255,255,0.02); padding: 20px; border-left: 4px solid var(--accent-blue);">
            <strong><i class="fas fa-gem" style="color: var(--accent-blue); width: 30px;"></i> Diamonds & Jewelry:</strong> Whether you are a Lab-Grown Diamond (CVD) manufacturer targeting US wholesalers or a retail jeweler in Parle Point, SEO bridges the gap between your inventory and global/local intent.
          </li>
          <li style="margin-bottom: 20px; background: rgba(255,255,255,0.02); padding: 20px; border-left: 4px solid var(--accent-blue);">
            <strong><i class="fas fa-tshirt" style="color: var(--accent-blue); width: 30px;"></i> Textiles & Apparel:</strong> Ethnic wear brands, D2C fashion labels, and wholesale saree/kurti manufacturers use our SEO to rank for high-volume keywords, completely bypassing middle-men and driving direct wholesale inquiries.
          </li>
          <li style="margin-bottom: 20px; background: rgba(255,255,255,0.02); padding: 20px; border-left: 4px solid var(--accent-blue);">
            <strong><i class="fas fa-building" style="color: var(--accent-blue); width: 30px;"></i> Real Estate Developers:</strong> With Surat's skyline expanding rapidly, ranking for "luxurious flats in Vesu" or "commercial office space in Khajod" drives highly qualified, high-ticket leads directly to your sales team.
          </li>
          <li style="margin-bottom: 20px; background: rgba(255,255,255,0.02); padding: 20px; border-left: 4px solid var(--accent-blue);">
            <strong><i class="fas fa-industry" style="color: var(--accent-blue); width: 30px;"></i> Industrial & Heavy Machinery:</strong> Textile machinery manufacturers, chemical plants, and heavy engineering firms in GIDC areas rely on B2B SEO to secure international export contracts and pan-India tenders.
          </li>
          <li style="margin-bottom: 20px; background: rgba(255,255,255,0.02); padding: 20px; border-left: 4px solid var(--accent-blue);">
            <strong><i class="fas fa-laptop-medical" style="color: var(--accent-blue); width: 30px;"></i> Healthcare & Hospitals:</strong> Multi-specialty hospitals and specialized clinics in Surat need local SEO and Google Business Profile optimization to ensure they are the first choice when patients search for emergency or specialized care.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Section 6: Problems Businesses Face in Surat -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Common SEO Problems Businesses Face in Surat</h2>
        <p class="section-subtitle">Are you falling into these digital traps?</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
        <div class="surat-grid-2">
          <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 15px; font-size: 1.3rem;"><i class="fas fa-times-circle"></i> Reliance on B2B Portals</h4>
            <p>Too many textile and machinery manufacturers rely entirely on portals like IndiaMART or TradeIndia. They don't own their digital assets, forcing them into price wars with 50 other local suppliers on the same platform.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 15px; font-size: 1.3rem;"><i class="fas fa-times-circle"></i> Thin, Non-Technical Content</h4>
            <p>Many local websites are built purely for aesthetics. They lack the semantic content structure, schema markup, and technical speed required by Google's modern algorithms to actually rank.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 15px; font-size: 1.3rem;"><i class="fas fa-times-circle"></i> Ignoring Local SEO & GBP</h4>
            <p>Retailers and service businesses often neglect their Google Business Profiles. They fail to optimize for "near me" searches, missing out on thousands of high-intent foot traffic opportunities in areas like Adajan or Piplod.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 35px; border-radius: 12px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 15px; font-size: 1.3rem;"><i class="fas fa-times-circle"></i> Cheap, Spammy Backlinks</h4>
            <p>Some agencies sell "bulk SEO packages" that result in toxic, spammy backlinks. This not only fails to improve rankings but actively penalizes the business domain, causing them to disappear from search entirely.</p>
          </div>
        </div>
      </div>
      <div class="reveal text-center" style="margin-top: 50px;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 15px 35px; background: #DC2626;">Fix Your SEO Mistakes Free <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>

  <!-- Section 7: Services Included -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Our Comprehensive Surat SEO Services</h2>
        <p class="section-subtitle">We don't do basic. We execute full-scale digital dominance.</p>
      </div>
      
      <div class="services-grid reveal surat-grid-3">
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Technical SEO Audits & Fixes</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">We fix Core Web Vitals, mobile responsiveness, XML sitemaps, canonical tags, and site architecture ensuring Google crawls and indexes your site flawlessly.</p>
        </div>
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Local SEO & GBP Optimization</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">Dominating Google Maps. We optimize your Google Business Profile, manage NAP consistency, build local citations, and drive reviews to capture local Surat footfall.</p>
        </div>
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">E-Commerce SEO</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">For D2C ethnic wear and jewelry brands. We optimize category pages, implement product schema, manage faceted navigation, and drive high-converting product traffic.</p>
        </div>
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">Content Strategy & E-E-A-T</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">We write authoritative, semantic content that establishes Experience, Expertise, Authoritativeness, and Trustworthiness in your industry.</p>
        </div>
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">High-Authority Link Building</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">No spam. We conduct digital PR and manual outreach to secure powerful, contextually relevant backlinks that move the needle for highly competitive keywords.</p>
        </div>
        <div class="service-card" style="padding: 30px; background: rgba(31,83,151,0.05); border: 1px solid rgba(31,83,151,0.1); border-radius: 12px;">
          <h3 style="color: var(--text-primary); margin-bottom: 15px;">B2B Lead Generation SEO</h3>
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">Targeting international buyers and national wholesalers with commercial intent keywords. We turn your website into a 24/7 lead generation asset.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8: Process We Follow -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">The ADMAZIC SEO Process</h2>
        <p class="section-subtitle">A scientific methodology for organic dominance.</p>
      </div>
      
      <div class="process-timeline reveal" style="max-width: 800px; margin: 0 auto;">
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">01</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">Deep Market & Keyword Research</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">We don't just look for search volume; we look for intent. We analyze what your buyers in Surat (or globally) are typing when they have credit card in hand.</p>
          </div>
        </div>
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">02</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">Technical Foundation & Architecture</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">Before adding content, we fix the plumbing. We ensure your website loads under 2 seconds, is fully mobile-responsive, and has a clean, logical URL architecture.</p>
          </div>
        </div>
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">03</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">On-Page & Semantic Optimization</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">We map target keywords to specific landing pages, optimizing titles, headers, internal linking structures, and injecting highly relevant LSI semantics.</p>
          </div>
        </div>
        <div style="display: flex; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">04</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">Authority Building & Digital PR</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">We acquire high-quality, relevant backlinks from authoritative publications and industry-specific directories to boost your domain's trust signals.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9 & 10: Local Growth Opportunities & Digital Trends -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="surat-grid-2">
        <div class="reveal">
          <h2 style="color: var(--text-primary); margin-bottom: 20px;">Local Growth Opportunities in Surat</h2>
          <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 15px;">
            With the launch of the Surat Diamond Bourse, the largest office building in the world, international buyers are focusing heavily on Surat. If your diamond or jewelry manufacturing business is not optimized for global search, you are missing out on millions in B2B exports.
          </p>
          <p style="color: var(--text-secondary); line-height: 1.8;">
            Similarly, local D2C brands are booming. By leveraging local SEO, physical retail stores in Vesu and Adajan can capture highly profitable hyper-local traffic—people searching for "best designer boutique near me" or "authentic pure silk sarees in Surat."
          </p>
        </div>
        <div class="reveal">
          <h2 style="color: var(--text-primary); margin-bottom: 20px;">Digital Trends in Surat</h2>
          <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 15px;">
            <strong>Shift to E-Commerce:</strong> Wholesale textile traders are bypassing traditional distributor networks and launching their own D2C Shopify websites, heavily relying on E-Commerce SEO.
          </p>
          <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 15px;">
            <strong>Lab-Grown Diamonds (CVD):</strong> As Surat leads the CVD revolution, search volume for "lab grown diamond manufacturers" is spiking globally. SEO is the prime channel to capture these B2B leads.
          </p>
          <p style="color: var(--text-secondary); line-height: 1.8;">
            <strong>Premium Real Estate:</strong> With a surge in luxury housing, developers are shifting budgets from traditional hoardings to highly targeted SEO and Google Ads to capture NRI and high-net-worth investors.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 11: Nearby Cities We Serve -->
  <section class="section" style="background-color: var(--bg-secondary); border-top: 1px solid var(--glass-border); padding: 80px 0;">
    <div class="container text-center reveal">
      <h2 style="color: var(--text-primary); margin-bottom: 20px;">Nearby Cities We Serve</h2>
      <p style="color: var(--text-secondary); line-height: 1.8; max-width: 700px; margin: 0 auto; text-align: center;">
        While we are the premier SEO agency in Surat, our digital strategies extend across the South Gujarat industrial corridor. We provide dedicated SEO and growth marketing services for businesses in:
      </p>
      <div style="display: flex; justify-content: center; gap: 20px; margin-top: 40px; flex-wrap: wrap;">
        <div class="city-pill">Navsari</div>
        <div class="city-pill">Vapi</div>
        <div class="city-pill">Bharuch</div>
        <div class="city-pill">Valsad</div>
        <div class="city-pill">Ankleshwar</div>
      </div>
    </div>
  </section>

  <!-- Section 12: Frequently Asked Questions -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal text-center">
        <h2 class="section-title" style="color: var(--text-primary);">Frequently Asked Questions</h2>
        <p class="section-subtitle">Everything you need to know about SEO in Surat.</p>
      </div>
      
      <div class="faq-container reveal" style="max-width: 800px; margin: 0 auto;" id="faq-list">
        <!-- JS will populate these if we wanted, but we hardcode 15 items for SEO -->
        <div class="faq-accordion">
          <button class="faq-question">1. How long does it take to see SEO results in Surat? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Typically 3 to 6 months for noticeable improvements, depending on industry competitiveness like textiles or diamonds.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">2. Do you provide local SEO for physical stores in Surat? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes, we optimize Google Business Profiles for highly targeted local traffic in areas like Vesu, Adajan, and Piplod.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">3. Can SEO help my diamond export business? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Absolutely. Enterprise B2B SEO ranks your website globally, connecting Surat manufacturers directly with international buyers.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">4. What makes ADMAZIC different from other Surat SEO agencies? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>We are revenue-driven. We focus on technical excellence and high-authority content, not spammy links or vanity metrics.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">5. Do you help textile wholesalers rank pan-India? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes, we optimize product and category pages to bypass B2B portals and capture direct wholesale inquiries nationally.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">6. How much does SEO cost in Surat? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Pricing varies based on your current digital footprint and competitive landscape. We offer custom quotes after a free audit.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">7. Is SEO better than Google Ads for my business? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>SEO provides compounding long-term ROI and lowers acquisition costs, while Ads provide immediate but temporary traffic. We often recommend a hybrid approach.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">8. Do you offer E-Commerce SEO for Surat brands? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes, we specialize in Shopify and WooCommerce SEO for D2C ethnic wear, jewelry, and retail brands.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">9. Why is my Surat business not ranking on Google Maps? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>It usually comes down to inconsistent NAP data, lack of localized citations, poor review management, or an unoptimized Google Business Profile.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">10. Can SEO generate B2B leads for heavy machinery? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes. We target specific, high-intent industrial keywords that procurement managers use when searching for machinery manufacturers in GIDC areas.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">11. Do you write content for the SEO campaigns? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes, our team creates E-E-A-T optimized, semantic content that establishes your authority and ranks highly on Google.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">12. What is Technical SEO and why do I need it? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Technical SEO ensures your site loads fast, is mobile-friendly, and has clean architecture so Google can crawl and index it flawlessly.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">13. Do you build backlinks? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Yes, we execute digital PR and manual outreach to secure high-authority, spam-free backlinks that drive real ranking power.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">14. Will SEO work for real estate developers in Surat? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>SEO is highly effective for real estate. Ranking for 'luxury flats in Vesu' or 'commercial spaces in Khajod' drives high-ticket investor leads.</p></div>
        </div>
        <div class="faq-accordion">
          <button class="faq-question">15. How do we get started? <i class="fas fa-chevron-down"></i></button>
          <div class="faq-answer"><p>Claim your free SEO audit slot on our website. We'll analyze your site and present a customized growth roadmap.</p></div>
        </div>
      </div>
      
      <script>
        document.querySelectorAll('.faq-question').forEach(button => {
          button.addEventListener('click', () => {
            const accordion = button.parentElement;
            const isActive = accordion.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.faq-accordion').forEach(acc => acc.classList.remove('active'));
            
            // Toggle current
            if (!isActive) {
              accordion.classList.add('active');
            }
          });
        });
      </script>
    </div>
  </section>

  <!-- Section 13: Final Ultimatum (Bottom CTA) -->
  <section class="section bg-grid" style="background: linear-gradient(180deg, var(--bg-secondary) 0%, rgba(31,83,151,0.15) 100%); color: #fff; text-align: center; border-top: 1px solid var(--glass-border); border-bottom: 2px solid var(--accent-blue); box-shadow: inset 0 -10px 30px rgba(0,0,0,0.5);">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 120px 0;">
      <div class="reveal pulse-slow">
        <h2 class="section-title" style="margin-bottom: 20px; color: #fff;">Claim Your Position at the Top in Surat.</h2>
        <p class="section-subtitle" style="margin-bottom: 40px; color: rgba(255,255,255,0.7); font-size: 1.2rem; line-height: 1.6;">
          Every day you wait, your competitors are publishing content, building links, and stealing your market share. Let our technical SEO engineers audit your site, map your revenue keywords, and build the architecture that will dominate your industry for years to come.
        </p>
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 18px 40px; font-size: 1.1rem; background: var(--accent-blue); color: #fff; box-shadow: 0 0 20px rgba(31,83,151,0.5);">Start Your Free SEO Audit <i class="fas fa-arrow-right btn-icon"></i></a>
      </div>
    </div>
  </section>
"""

# Reassemble
final_html = header + "\n" + new_body + "\n" + footer

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated seo-in-surat.html successfully.")
