import streamlit as st

st.set_page_config(
    page_title="Grok Build macOS Guide",
    page_icon="🛠️",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: 700; color: #00D4FF;}
    .terminal {background-color: #1e2937; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; white-space: pre-wrap;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ Grok Build Guide")
st.sidebar.markdown("**Real macOS Walkthrough**")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", "✅ Prerequisites", "📥 Installation", 
    "🚀 Real Walkthrough", "✨ Features", "⌨️ Commands", 
    "🛠️ Troubleshooting", "🚀 Deploy This App"
])

# ====================== HOME ======================
if page == "🏠 Home":
    st.title("🛠️ Grok Build on macOS")
    st.subheader("Complete Real-User Walkthrough")
    st.info("This guide includes actual terminal steps from a successful macOS installation (June 2026).")

# ====================== INSTALLATION ======================
elif page == "📥 Installation":
    st.header("📥 Installation")
    st.code("curl -fsSL https://x.ai/cli/install.sh | bash", language="bash")
    st.success("Expected output: Grok 0.2.67 installed + PATH updated in ~/.zshrc")

# ====================== REAL WALKTHROUGH ======================
elif page == "🚀 Real Walkthrough":
    st.header("🚀 Real macOS Walkthrough (Your Steps)")
    
    st.subheader("1. Install Grok Build")
    st.markdown('<div class="terminal">user@MacBookAir ~ % curl -fsSL https://x.ai/cli/install.sh | bash\nFetching latest stable version...\nInstalling Grok 0.2.67 (macos-aarch64)...\nBinary linked to ~/.grok/bin/grok\nUpdated ~/.zshrc</div>', unsafe_allow_html=True)
    
    st.subheader("2. Restart Terminal")
    st.write("→ Type `exit` or close the Terminal window (red button top-left)")
    st.write("→ Re-open Terminal")
    
    st.subheader("3. Verify Installation")
    st.markdown('<div class="terminal">user@MacBookAir ~ % grok --version\ngrok 0.2.67 (03e13f99286)</div>', unsafe_allow_html=True)
    
    st.subheader("4. Start Grok Build in a Project")
    st.code("cd ~/my-project", language="bash")
    st.code("grok", language="bash")
    
    st.subheader("5. Sign In (Browser Flow)")
    st.write("Grok Build will show a code in the terminal:")
    st.markdown('<div class="terminal">Enter the code shown in your terminal.\nXXXX-YYYY\n\nOnly enter this code if you just initiated a sign-in from your device.</div>', unsafe_allow_html=True)
    
    st.write("→ Go to the browser window that opens")
    st.write("→ Sign in with your **x.com** account")
    st.write("→ Authorize the app")
    
    st.success("After authorization, Grok Build TUI should load with release notes!")

    st.subheader("What the TUI Looks Like")
    st.markdown('<div class="terminal">Grok Build 0.2.67 Beta\n\n┌─ Release Notes ────────────────────────┐\n│ 0.2.67 — 2026-06-25                    │\n└────────────────────────────────────────┘</div>', unsafe_allow_html=True)

# ====================== Other Pages (unchanged from previous) ======================
elif page == "✅ Prerequisites":
    st.header("✅ Prerequisites")
    st.write("- macOS (Apple Silicon recommended)")
    st.write("- SuperGrok or X Premium+ subscription")
    st.write("- Terminal (default or iTerm2)")

elif page == "✨ Features":
    st.header("✨ Key Features")
    st.write("- Plan Mode with approval")
    st.write("- Parallel sub-agents")
    st.write("- AGENTS.md & skill support")
    st.write("- Headless mode for scripts")

elif page == "⌨️ Commands":
    st.header("⌨️ Useful Commands")
    st.code("grok --version", language="bash")
    st.code("grok", language="bash")
    st.code("grok -p \"Explain this repo\"", language="bash")
    st.code("grok inspect", language="bash")

elif page == "🛠️ Troubleshooting":
    st.header("🛠️ Troubleshooting")
    st.write("• Run `source ~/.zshrc` after install")
    st.write("• Use API key for headless: `export XAI_API_KEY=...`")
    st.write("• Make sure project folder exists before `cd`")

elif page == "🚀 Deploy This App":
    st.header("🚀 Deploy This App")
    st.code("streamlit", language="text")
    st.write("requirements.txt content above.")

st.caption("Guide based on real macOS session • Grok Build 0.2.67 Beta • June 2026")
