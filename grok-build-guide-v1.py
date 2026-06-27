import streamlit as st

st.set_page_config(
    page_title="Grok Build macOS Guide",
    page_icon="🛠️",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: 700; color: #00D4FF;}
    .terminal {background-color: #1e2937; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; white-space: pre-wrap; line-height: 1.4;}
    .release-notes {background-color: #0f172a; color: #94a3b8; padding: 1.2rem; border-radius: 10px; border: 1px solid #334155;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ Grok Build Guide")
st.sidebar.markdown("**Real macOS Walkthrough • v0.2.67**")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", "✅ Prerequisites", "📥 Installation", 
    "🚀 Real Walkthrough", "📋 Release Notes", "✨ Features", 
    "⌨️ Commands", "🛠️ Troubleshooting", "🚀 Deploy This App"
])

# ====================== HOME ======================
if page == "🏠 Home":
    st.title("🛠️ Grok Build on macOS")
    st.subheader("Complete Real-User Guide (v0.2.67)")
    st.info("Includes actual terminal output from a successful installation on June 27, 2026.")

# ====================== INSTALLATION ======================
elif page == "📥 Installation":
    st.header("📥 Installation")
    st.code("curl -fsSL https://x.ai/cli/install.sh | bash", language="bash")

# ====================== REAL WALKTHROUGH ======================
elif page == "🚀 Real Walkthrough":
    st.header("🚀 Your Real macOS Walkthrough")
    
    st.subheader("1. Install")
    st.markdown('<div class="terminal">user@MacBookAir ~ % curl -fsSL https://x.ai/cli/install.sh | bash\nFetching latest stable version...\nInstalling Grok 0.2.67 (macos-aarch64)...\nGrok 0.2.67 installed successfully.\nUpdated ~/.zshrc</div>', unsafe_allow_html=True)
    
    st.subheader("2. Restart Terminal & Verify")
    st.markdown('<div class="terminal">user@MacBookAir ~ % grok --version\ngrok 0.2.67 (03e13f99286)</div>', unsafe_allow_html=True)
    
    st.subheader("3. Launch in Project")
    st.code("cd ~/my-project", language="bash")
    st.code("grok", language="bash")
    
    st.subheader("4. Authentication")
    st.write("Enter the code displayed in the terminal into the browser (dummy placeholder):")
    st.markdown('<div class="terminal">Enter the code shown in your terminal.\nXXXX-YYYY</div>', unsafe_allow_html=True)

# ====================== RELEASE NOTES ======================
elif page == "📋 Release Notes":
    st.header("📋 Current Release Notes — Grok Build 0.2.67")
    st.caption("2026-06-25")
    
    st.markdown("""
<div class="release-notes">
<pre>
        ┌─ Release Notes ──────────────────────────────────────── [✗] ─┐        
        │                                                              │        
        │  0.2.67 — 2026-06-25                                         │        
        │                                                              │        
        │  Features                                                    │        
        │                                                              │        
        │  • Added --json-schema flag for headless mode to constrain   │        
        │  model output to a supplied JSON Schema.                     │        
        │  • Idle detection can now ignore background tasks when the   │        
        │  env flag is set (off by default).                           │        
        │                                                              │        
        │  Bug Fixes                                                   │        
        │                                                              │        
        │                                                              │        
  ╭─────│                   ↑/↓ scroll  |  Esc back                    │─────╮  
  │ ❯   └──────────────────────────────────────────────────────────────┘     │  
  ╰───────────────────────────────────────────────────────────── Grok Build ─╯  
                                                       Grok Build  0.2.67 Beta
</pre>
</div>
""", unsafe_allow_html=True)
    
    st.success("**New in 0.2.67**")
    st.markdown("""
    - `--json-schema` flag for headless mode (structured output)
    - Improved idle detection with background task support
    """)

# ====================== Other Sections ======================
elif page == "✅ Prerequisites":
    st.header("✅ Prerequisites")
    st.write("• macOS (Apple Silicon or Intel)")
    st.write("• SuperGrok or X Premium+ subscription")
    st.write("• Terminal app")

elif page == "✨ Features":
    st.header("✨ Key Features")
    st.write("• Plan Mode with approval gates")
    st.write("• Parallel sub-agents")
    st.write("• AGENTS.md + MCP server support")
    st.write("• Headless mode + JSON Schema output (new in 0.2.67)")

elif page == "⌨️ Commands":
    st.header("⌨️ Useful Commands")
    st.code("grok --version", language="bash")
    st.code("grok", language="bash")
    st.code("grok -p \"Your task here\" --json-schema schema.json   # New in 0.2.67", language="bash")

elif page == "🛠️ Troubleshooting":
    st.header("🛠️ Troubleshooting")
    st.write("• After install: `source ~/.zshrc`")
    st.write("• Project folder must exist before `cd`")

elif page == "🚀 Deploy This App":
    st.header("🚀 Deploy This App")
    st.code("streamlit", language="text")

st.caption("Guide updated with Grok Build 0.2.67 • Real session from June 27, 2026")
