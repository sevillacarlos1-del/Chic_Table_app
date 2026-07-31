# ── Tab: INICIO ───────────────────────────────────────────────────────────────
def render_inicio():
    st.markdown("""
    <section style="text-align:center;padding:48px 16px 20px;">
      <p class="ornament">✦ LUXURY BOUTIQUE ✦</p>
      <h1 class="hero-title" style="font-family:'Playfair Display',serif;font-size:clamp(2.5rem,6vw,4rem);color:#8B0000;margin:16px 0 20px;font-weight:700;">+CHIC</h1>
      <p class="hero-subtitle" style="font-family:'Montserrat',sans-serif;font-size:1rem;color:#6B6B6B;margin:0 auto 24px;letter-spacing:0.05em;">
        Luxury gifts for unforgettable moments.
      </p>
    </section>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.2, 1.6, 1.2])
    with c2:
        st.markdown(wa_button(
            "Hi! I'd love to learn more about +CHIC gifts.",
            "✦ Contact Us"
        ), unsafe_allow_html=True)

    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:40px 0 24px;">
      <p class="ornament">✦ OUR ESSENCE ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.6rem,5vw,2.4rem);
                 color:#1A1A1A;margin:12px 0 8px;">The +CHIC Experience</h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;
                color:#6B6B6B;max-width:600px;margin:0 auto;line-height:1.6;">
        We believe gifting is an art. Every detail is carefully designed to convey elegance, exclusivity, and love.
      </p>
    </div>
    """, unsafe_allow_html=True)

    essence = [
        ("inicio1.jpg", "", ""), 
        ("inicio2.jpg", "Impeccable Presentation", "Luxury boxes, silk ribbons, and a flawless finish."),
        ("inicio3.jpg", "Unique Moments", "We don't just deliver gifts, we deliver emotions.")
    ]

    cards = ""
    for img, title, desc in essence:
        src = img_b64(img)
        alt_text = title if title else "+CHIC"
        img_tag = (
            f'<div class="product-img-wrap" style="position:relative;overflow:hidden;aspect-ratio:4/3;">'
            f'<img src="{src}" alt="{alt_text}" style="width:100%;height:100%;display:block;margin:0;object-fit:cover;">'
            f'</div>'
            if src else ""
        )
        
        if title:
            cards += f"""
            <div class="glass-card">
              {img_tag}
              <div class="product-info">
                <p class="product-name">{title}</p>
                <p class="product-caption">{desc}</p>
              </div>
            </div>"""
        else:
            cards += f"""
            <div class="glass-card" style="background:transparent !important; display:block !important; height:auto !important;">
              {img_tag}
            </div>"""
            
    st.markdown(f'<div class="essence-grid">{cards}</div>', unsafe_allow_html=True)

    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card" style="text-align:center;padding:48px 32px;max-width:640px;margin:0 auto 60px;">
      <p class="ornament">✦ READY TO IMPRESS? ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:2rem;color:#1A1A1A;margin:16px 0 12px;">
        Create a moment<br>no one will forget
      </h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;color:#6B6B6B;margin-bottom:0;">
        Explore our exclusive catalog or contact us for a personalized service.
      </p>
    </div>
    """, unsafe_allow_html=True)