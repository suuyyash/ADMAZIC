import re

filepath = '/Users/sidsmac/Documents/ADMAZIC/seo-in-surat.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header (everything up to closing </header>)
header_match = re.search(r'(.*?</header>)', content, re.DOTALL)
header = header_match.group(1)

# Extract footer (everything from <footer class="footer"...)
footer_match = re.search(r'(<footer class="footer".*)', content, re.DOTALL)
footer = footer_match.group(1)

# Modify title and meta description in header
header = re.sub(r'<title>.*?</title>', '<title>SEO Services in Surat | #1 Local SEO Agency | ADMAZIC</title>', header)
header = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Looking for the best SEO services in Surat? ADMAZIC helps Diamond, Textile, and Real Estate businesses in Surat dominate local search and scale revenue.">', header)

# New Body Content
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
        <a href="tel:+917861910348" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem;"><i class="fas fa-phone-alt"></i> Call +91 78619 10348</a>
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
      
      <div class="comparison-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
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
    </div>
  </section>

  <!-- Section 3: Overview of the Business Landscape of Surat -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title" style="color: var(--text-primary);">Overview of the Business Landscape of Surat</h2>
        <p class="section-subtitle" style="max-width: 800px; text-align: left;">Understanding the economic engine of Gujarat.</p>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
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
      <div class="grid-list reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Vesu & Piplod</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The premium commercial and IT hubs of Surat, housing modern agencies, real estate developers, and high-end retail brands.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Varachha & Katargam</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The beating heart of the diamond manufacturing industry. Essential for B2B diamond SEO strategies.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Ring Road & Udhna</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The epicenter of Surat's textile markets, wholesalers, and logistics companies requiring pan-India visibility.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Khajod (DREAM City)</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The upcoming corporate megahub featuring the Surat Diamond Bourse. A critical target for global SEO positioning.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Sachin & Pandesara GIDC</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">The industrial zones housing massive textile dyeing, printing mills, and heavy engineering companies.</p>
        </div>
        <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
          <h3 style="color: var(--accent-blue); margin-bottom: 10px;">Adajan & Pal</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">A rapidly growing residential and commercial corridor, ideal for local businesses, clinics, and service providers.</p>
        </div>
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
      <div class="section-header reveal">
        <h2 class="section-title" style="color: var(--text-primary);">Common SEO Problems Businesses Face in Surat</h2>
      </div>
      <div class="content-text reveal" style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
        <p style="margin-bottom: 20px;">Despite the rapid adoption of digital marketing, many businesses in Surat struggle with fundamental digital roadblocks:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
          <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 10px;"><i class="fas fa-times-circle"></i> Reliance on B2B Portals</h4>
            <p>Too many textile and machinery manufacturers rely entirely on portals like IndiaMART or TradeIndia. They don't own their digital assets, forcing them into price wars with 50 other local suppliers on the same platform.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 10px;"><i class="fas fa-times-circle"></i> Thin, Non-Technical Content</h4>
            <p>Many local websites are built purely for aesthetics. They lack the semantic content structure, schema markup, and technical speed required by Google's modern algorithms to actually rank.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 10px;"><i class="fas fa-times-circle"></i> Ignoring Local SEO & GBP</h4>
            <p>Retailers and service businesses often neglect their Google Business Profiles. They fail to optimize for "near me" searches, missing out on thousands of high-intent foot traffic opportunities in areas like Adajan or Piplod.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 25px; border-radius: 8px; border: 1px solid var(--glass-border);">
            <h4 style="color: #DC2626; margin-bottom: 10px;"><i class="fas fa-times-circle"></i> Cheap, Spammy Backlinks</h4>
            <p>Some agencies sell "bulk SEO packages" that result in toxic, spammy backlinks. This not only fails to improve rankings but actively penalizes the business domain, causing them to disappear from search entirely.</p>
          </div>
        </div>
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
      
      <div class="services-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
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
          <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6;">We write authoritative, semantic content that establishes Experience, Expertise, Authoritativeness, and Trustworthiness in your industry, signaling to Google that you are the market leader.</p>
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
        <div style="display: flex; margin-bottom: 30px; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">04</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">Authority Building & Digital PR</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">We acquire high-quality, relevant backlinks from authoritative publications and industry-specific directories to boost your domain's trust signals.</p>
          </div>
        </div>
        <div style="display: flex; background: var(--bg-primary); padding: 30px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue); margin-right: 25px;">05</div>
          <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">Analytics, Reporting & Iteration</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">SEO is an ongoing war. We monitor GA4, Search Console, and rank trackers to constantly tweak our strategy, ensuring we not only achieve Rank 1 but defend it.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9 & 10: Local Growth Opportunities & Digital Trends -->
  <section class="section" style="padding: 100px 0;">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 50px;">
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
      <p style="color: var(--text-secondary); line-height: 1.8; max-width: 700px; margin: 0 auto;">
        While we are the premier SEO agency in Surat, our digital strategies extend across the South Gujarat industrial corridor. We provide dedicated SEO and growth marketing services for businesses in:
      </p>
      <div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px; flex-wrap: wrap;">
        <span style="background: var(--bg-primary); padding: 10px 25px; border-radius: 30px; border: 1px solid var(--glass-border); color: var(--accent-blue); font-weight: 600;">Navsari</span>
        <span style="background: var(--bg-primary); padding: 10px 25px; border-radius: 30px; border: 1px solid var(--glass-border); color: var(--accent-blue); font-weight: 600;">Vapi</span>
        <span style="background: var(--bg-primary); padding: 10px 25px; border-radius: 30px; border: 1px solid var(--glass-border); color: var(--accent-blue); font-weight: 600;">Bharuch</span>
        <span style="background: var(--bg-primary); padding: 10px 25px; border-radius: 30px; border: 1px solid var(--glass-border); color: var(--accent-blue); font-weight: 600;">Valsad</span>
        <span style="background: var(--bg-primary); padding: 10px 25px; border-radius: 30px; border: 1px solid var(--glass-border); color: var(--accent-blue); font-weight: 600;">Ankleshwar</span>
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
      
      <div class="faq-container reveal" style="max-width: 800px; margin: 0 auto;">
        <div class="faq-item" style="background: var(--bg-secondary); border: 1px solid var(--glass-border); padding: 25px; border-radius: 12px; margin-bottom: 20px;">
          <h3 style="color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px;">How long does it take to see SEO results in Surat?</h3>
          <p style="color: var(--text-secondary); line-height: 1.6;">SEO is a mid-to-long-term investment. Depending on the competitiveness of your industry (e.g., highly competitive markets like textiles vs. niche B2B machinery), you can expect to see noticeable ranking improvements and traffic growth within 3 to 6 months.</p>
        </div>
        <div class="faq-item" style="background: var(--bg-secondary); border: 1px solid var(--glass-border); padding: 25px; border-radius: 12px; margin-bottom: 20px;">
          <h3 style="color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px;">Do you provide local SEO for physical stores?</h3>
          <p style="color: var(--text-secondary); line-height: 1.6;">Absolutely. We optimize your Google Business Profile (GBP) so that when a customer in Vesu or Adajan searches for your services "near me," your store appears in the coveted Google Maps 3-Pack, driving immediate footfall.</p>
        </div>
        <div class="faq-item" style="background: var(--bg-secondary); border: 1px solid var(--glass-border); padding: 25px; border-radius: 12px; margin-bottom: 20px;">
          <h3 style="color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px;">Can SEO help me get international buyers for my diamond export business?</h3>
          <p style="color: var(--text-secondary); line-height: 1.6;">Yes. Enterprise B2B SEO is specifically designed to rank your website globally. By targeting high-intent commercial keywords and optimizing for international search engines, we connect your Surat manufacturing unit directly with global wholesalers.</p>
        </div>
        <div class="faq-item" style="background: var(--bg-secondary); border: 1px solid var(--glass-border); padding: 25px; border-radius: 12px; margin-bottom: 20px;">
          <h3 style="color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px;">How is ADMAZIC different from other SEO agencies in Surat?</h3>
          <p style="color: var(--text-secondary); line-height: 1.6;">We don't focus on vanity metrics or sell cheap, spammy link packages. We are a revenue-driven growth agency. Our focus is strictly on technical excellence, authoritative content, and ultimately, how many qualified leads and sales our SEO efforts generate for your bottom line.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 13: Final Ultimatum (Bottom CTA) -->
  <section class="section bg-grid" style="background-color: #0F172A; color: #fff; text-align: center; border-top: 1px solid var(--glass-border);">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 120px 0;">
      <div class="reveal pulse-slow">
        <h2 class="section-title" style="margin-bottom: 20px; color: #fff;">Claim Your Position at the Top in Surat.</h2>
        <p class="section-subtitle" style="margin-bottom: 40px; color: rgba(255,255,255,0.7); font-size: 1.2rem; line-height: 1.6;">
          Every day you wait, your competitors are publishing content, building links, and stealing your market share. Let our technical SEO engineers audit your site, map your revenue keywords, and build the architecture that will dominate your industry for years to come.
        </p>
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 18px 40px; font-size: 1.1rem; background: #DC2626; color: #fff;">Start Your Free SEO Audit <i class="fas fa-arrow-right btn-icon"></i></a>
      </div>
    </div>
  </section>
"""

# Reassemble
final_html = header + "\n" + new_body + "\n" + footer

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated seo-in-surat.html successfully.")
