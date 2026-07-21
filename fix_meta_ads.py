import re

with open("meta-ads-in-mumbai.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the massive duplicated paragraphs in section 3
# There are 5 identical sets of paragraphs. Let's just use regex to replace the content of that specific div.
# We'll extract the first unique instance of the paragraphs.

p1 = """Mumbai, the bustling metropolis of India, is an economic powerhouse where commerce, entertainment, and fashion converge. In this highly competitive landscape, relying solely on traditional marketing or organic reach is no longer sufficient. Meta Ads provide the critical leverage needed to penetrate this dense market. The city operates at a breakneck speed, and consumer attention spans are remarkably short. To capture and retain this fleeting attention, businesses must deploy highly targeted, visually arresting, and data-driven advertising campaigns across Facebook and Instagram. The algorithmic power of Meta allows us to dissect the vast Mumbai demographic—from the corporate executives in Nariman Point to the creative professionals in Bandra—ensuring your message reaches the precise individuals most likely to convert. This is not merely about accumulating 'likes' or superficial engagement; it is about engineering predictable, scalable revenue streams. By utilizing advanced pixel tracking, server-side APIs, and rigorous A/B testing frameworks, we transform ad spend into a measurable investment. Our methodologies bypass the noise of the Mumbai market, delivering your unique value proposition directly into the hands of high-intent prospects."""

p2 = """When you consider the sheer scale of digital consumption in Maharashtra's capital, the opportunity cost of ignoring Meta Ads is staggering. Millions of Mumbaikars commute daily via the local train network, spending hours engaged with their mobile devices. This captive audience is a goldmine for proactive demand generation. Through short-form video formats like Instagram Reels, businesses can inject their narratives seamlessly into the daily routines of their target market. The visual nature of these platforms is perfectly aligned with the aesthetic and lifestyle-driven consumer culture of Mumbai. Whether you are launching a luxury real estate project, a boutique fashion line, or a disruptive FinTech application, the ability to visually demonstrate value and build instant trust is unparalleled. Furthermore, the integration of conversational commerce, specifically through WhatsApp funnels, caters perfectly to the local preference for direct, immediate communication. By bridging the gap between an ad click and a personalized conversation, we significantly reduce friction in the sales process, leading to higher conversion rates and lower acquisition costs. Our approach is holistic, managing the entire customer journey from the initial visual hook to the final conversion, ensuring every rupee spent is optimized for maximum return on investment. The future of customer acquisition in Mumbai belongs to those who master the intricacies of the Meta advertising ecosystem."""

p3 = """The competitive density in Mumbai necessitates a marketing strategy that is not just visible, but unignorable. A simple boosted post will drown in the algorithmic noise. What is required is a sophisticated, multi-layered funnel architecture that systematically guides a stranger through the stages of awareness, consideration, and ultimately, conversion. We begin by defining the core unit economics of your business, understanding your margins, and setting realistic targets for Customer Acquisition Cost (CAC) and Lifetime Value (LTV). This data forms the bedrock of our strategy. We then deploy top-of-funnel (TOFU) campaigns designed to cast a wide net across specific Mumbai demographics, utilizing compelling video creatives to hook attention within the critical first three seconds. Those who engage with this content are then seamlessly transitioned into our middle-of-funnel (MOFU) retargeting sequences. Here, we address objections, build social proof through testimonials, and deepen the narrative. Finally, our bottom-of-funnel (BOFU) campaigns utilize aggressive, direct-response tactics—such as dynamic catalogue ads or limited-time offers—to drive the final purchase or lead submission. This systematic approach ensures that no potential customer falls through the cracks, maximizing the efficiency of your marketing budget."""

p4 = """Furthermore, the creative element cannot be overstated. In an era where AI handles the heavy lifting of bidding and optimization, the creative asset itself has become the primary targeting mechanism. The algorithm learns who your ideal customer is by analyzing who stops to interact with your videos or images. Therefore, we place an immense emphasis on creative testing and iteration. We do not rely on assumptions; we let the data dictate the winning aesthetics, copy, and formats. In Mumbai's trend-conscious environment, utilizing User-Generated Content (UGC), authentic founder stories, and culturally relevant messaging is vital for establishing trust and resonance. We continuously monitor ad fatigue, rapidly cycling in fresh creatives to maintain high engagement rates and prevent costs from spiraling. By combining this relentless creative engine with impeccable technical infrastructure—including robust pixel implementation and Conversion API integration—we create a marketing machine that is both highly resilient and immensely scalable, perfectly suited for the demands of the Mumbai market."""

replacement_content = f'''        <p style="margin-bottom: 25px;">
{p1}
        </p>
        <p style="margin-bottom: 25px;">
{p2}
        </p>
        <p style="margin-bottom: 25px;">
{p3}
        </p>
        <p>
{p4}
        </p>'''

# Replace the giant chunk
html = re.sub(r'<div class="content-text reveal"([^>]+)>\s*<p.*?</p>\s*</div>', f'<div class="content-text reveal"\\1>\n{replacement_content}\n      </div>', html, flags=re.DOTALL)

# Fix the trailing hallucinated text in all the grid cards
hallucination_str1 = """\nMumbai, the bustling metropolis of India, is an economic powerhouse where commerce, entertainment, and fashion converge. In this highly competitive landscape, relying solely on traditional marketing or organic reach is no longer sufficient. Meta Ads provide the critical leverage needed to penetrate"""
hallucination_str2 = """ Mumbai, the bustling metropolis of India, is an economic powerhouse where commerce, entertainment, and fashion converge. In this highly competitive landscape, relying solely on traditional marketing or organic reach is no longer sufficient. Meta Ads provide the critical leverage needed to penetrate"""
hallucination_str3 = """Mumbai, the bustling metropolis of India, is an economic powerhouse where commerce, entertainment, and fashion converge. In this highly competitive landscape, relying solely on traditional marketing or organic reach is no longer sufficient. Meta Ads provide the critical leverage needed to penetrate"""

html = html.replace(hallucination_str1, "")
html = html.replace(hallucination_str2, "")
html = html.replace(hallucination_str3, "")

with open("meta-ads-in-mumbai.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done fixing meta-ads-in-mumbai.html")
