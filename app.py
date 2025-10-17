# app.py  (Home / Landing)
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="LongLive — Tahmini Yaşam Süreniz",
    page_icon="⌛",
    layout="wide",
)

# ---------- Minimal CSS (clean & compact) ----------
st.markdown("""
<style>
/* page background & font */
html, body, [class*="css"]  { font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

/* headline */
.hero-title { font-size: 2.1rem; line-height: 1.2; font-weight: 700; margin: 0 0 .6rem 0; }
.hero-sub { font-size: 1.05rem; color: #4b5563; margin-bottom: 1.2rem; }

/* card */
.card { border: 1px solid #e5e7eb; border-radius: 16px; padding: 1.25rem 1.25rem; background: #ffffffcc; backdrop-filter: blur(3px); }

/* inputs compact */
.compact input, .compact textarea { max-width: 320px !important; }
.compact label { font-weight: 600; }

/* primary button */
div.stButton>button { border-radius: 10px; padding: .55rem 1rem; font-weight: 600; }

/* footer note */
.footer-note { font-size: .78rem; color:#6b7280; margin-top: .75rem; }

/* left rail */
.left-rail { border: 2px solid #111827; border-radius: 8px; padding: 1.2rem; }
.left-title { font-size: 1.1rem; font-weight: 700; margin-bottom: .6rem; }
.left-item { font-size: 1rem; margin: .35rem 0; }

/* hourglass SVG animation */
.hourglass { width: 140px; height: 140px; }
@keyframes sand {
  0% { transform: translateY(-28%); }
  100% { transform: translateY(28%); }
}
.sand { animation: sand 3.5s ease-in-out infinite alternate; }
</style>
""", unsafe_allow_html=True)

# ---------- Layout ----------
left, mid, right = st.columns([1.1, 1.6, 1.1])

with left:
    st.markdown('<div class="left-rail">', unsafe_allow_html=True)
    st.markdown('<div class="left-title">Bölümler</div>', unsafe_allow_html=True)
    st.markdown('<div class="left-item">• <b>Fiziksel</b> — Sağlık & alışkanlıklar</div>', unsafe_allow_html=True)
    st.markdown('<div class="left-item">• <b>Yaşamsal</b> — Anlam & etki</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with mid:
    # Header + hourglass side-by-side
    hcol, icocol = st.columns([2.2, 1])
    with hcol:
        st.markdown('<div class="hero-title">Tahmini yaşam sürenizi görün. Küçük değişikliklerle daha uzun ve kaliteli yaşama yolculuğuna başlayın.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-sub">LongLive, verdiğiniz bilgilere göre <b>tahmini</b> süreyi hesaplar ve “fiziksel” ile “yaşamsal” alanlarda iyileştirme fikirleri sunar.</div>', unsafe_allow_html=True)
    with icocol:
        # Simple inline SVG hourglass (no external assets)
        st.markdown("""
        <svg class="hourglass" viewBox="0 0 120 180" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#06b6d4"/>
              <stop offset="100%" stop-color="#10b981"/>
            </linearGradient>
          </defs>
          <path d="M20 20h80v16c0 18-22 36-40 44C42 72 20 54 20 36V20z" stroke="#111827" stroke-width="3" />
          <path d="M20 160h80v-16c0-18-22-36-40-44c-18 8-40 26-40 44v16z" stroke="#111827" stroke-width="3" />
          <rect x="18" y="18" width="84" height="20" rx="3" fill="#111827"/>
          <rect x="18" y="142" width="84" height="20" rx="3" fill="#111827"/>
          <ellipse class="sand" cx="60" cy="90" rx="16" ry="12" fill="url(#g)" opacity="0.9"/>
        </svg>
        """, unsafe_allow_html=True)

    # Login card
    st.markdown('<div class="card compact">', unsafe_allow_html=True)
    st.markdown("#### Giriş yap / Kaydol")
    email = st.text_input("E-posta", placeholder="ornek@eposta.com", help="E-postanızı yazın (ör. ornek@eposta.com)")
    pwd = st.text_input("Parola", type="password", placeholder="En az 9 karakter", help="Min 9 karakter; büyük, küçük, rakam ve sembol içermesi önerilir.")
    st.button("Devam et")  # sadece görsel amaçlı; henüz işlev eklemiyoruz
    st.markdown('<div class="footer-note">Bu uygulama tamamen ücretsizdir. Verilerinizi satmıyoruz.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    # Placeholder for small highlights
    st.markdown("##### Neler Göreceksiniz")
    st.write("• Tahmini kalan süre (yıl/gün/saniye)")
    st.write("• Kişiselleştirilmiş iyileştirme fikirleri")
    st.write("• Simülatör: Değiştir ve etkisini gör")
