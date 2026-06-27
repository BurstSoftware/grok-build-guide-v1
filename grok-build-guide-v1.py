import streamlit as st

st.set_page_config(
    page_title="Grok Build macOS Guide",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better look
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: 700; color: #00D4FF;}
    .section-header {font-size: 1.6rem; margin-top: 1.5rem; color: #1E3A8A;}
    .step-box {background-color: #f0f4f8; padding: 1rem; border-radius: 10px; margin: 0.5rem 0;}
    .command-box {background-color: #1e2937; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace;}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🛠️ Grok Build Guide")
st.sidebar.markdown("**macOS Edition** — June 2026")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "✅ Prerequisites", "📥 Installation", "🚀 Getting Started", 
     "✨ Key Features", "⌨️ Commands & Usage", "🛠️ Troubleshooting"]
)

st.sidebar.markdown("---")
st.sidebar.info("Grok Build is in **early beta** (as of June 2026). Feedback welcome via `/feedback` inside the CLI.")

# ====================== HOME ======================
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">🛠️ Grok Build on macOS</h1>', unsafe_allow_html=True)
    st.subheader("The Ultimate Interactive Guide")
    
    st.markdown("""
    **Grok Build** is xAI’s powerful **terminal-native AI coding agent**.  
    It runs directly in your Mac’s Terminal and helps you plan, code, review, test, and deploy complex projects with natural language.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Access Required", "SuperGrok or X Premium+")
    with col2:
        st.metric("Install Time", "~10 seconds")
    with col3:
        st.metric("Best For", "Professional coding workflows")
    
    st.markdown("---")
    st.info("This guide compiles official xAI documentation + real-world macOS usage tips.")

# ====================== PREREQUISITES ======================
elif page == "✅ Prerequisites":
    st.header("✅ Prerequisites")
    
    st.markdown("Before installing Grok Build on macOS:")
    
    checklist = [
        "macOS (Apple Silicon or Intel supported)",
        "Terminal app (built-in or iTerm2/WezTerm recommended)",
        "Active **SuperGrok** or **X Premium+** subscription",
        "Internet connection (for install + auth)",
        "A project folder with code (recommended)"
    ]
    
    for item in checklist:
        st.checkbox(item, value=True, disabled=True)
    
    st.warning("Grok Build is currently in **early beta**. Only available to SuperGrok / X Premium+ users.")

# ====================== INSTALLATION ======================
elif page == "📥 Installation":
    st.header("📥 Installation on macOS")
    
    st.markdown("### Step 1: Run the official installer")
    
    st.code("curl -fsSL https://x.ai/cli/install.sh | bash", language="bash")
    
    st.markdown("### Step 2: Verify installation")
    st.code("grok --version", language="bash")
    
    st.markdown("### Step 3: (Optional) Add to PATH if needed")
    st.code("""
# If 'grok' command not found after install:
echo 'export PATH="$HOME/.grok/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
""", language="bash")
    
    st.success("Installation usually completes in under 10 seconds.")

# ====================== GETTING STARTED ======================
elif page == "🚀 Getting Started":
    st.header("🚀 Getting Started on macOS")
    
    st.markdown("### 1. Navigate to your project")
    st.code("cd ~/Projects/my-awesome-app", language="bash")
    
    st.markdown("### 2. Start Grok Build")
    st.code("grok", language="bash")
    
    st.info("On first launch, Grok Build will open your browser for **OAuth authentication** with your xAI account.")
    
    st.markdown("### Alternative: Use API Key (headless/non-browser)")
    st.code("""
export XAI_API_KEY="xai-your-key-here"
grok
""", language="bash")
    
    st.markdown("### Quick first commands inside Grok Build")
    st.code("""
Explain this repo.
@src/main.py Walk me through this file.
grok inspect          # See what config/skills it detected
""", language="bash")

# ====================== KEY FEATURES ======================
elif page == "✨ Key Features":
    st.header("✨ Key Features")
    
    features = [
        ("🗺️ Plan Mode", "Propose a full plan first. Review, comment, or rewrite before any code changes are made. Changes appear as clean diffs."),
        ("🤖 Parallel Sub-agents", "Break large tasks into multiple specialized agents that work simultaneously."),
        ("📋 Skills & AGENTS.md", "Automatically picks up your project conventions, skills, hooks, and MCP servers."),
        ("🖱️ Rich TUI", "Mouse support, fullscreen experience, beautiful diffs, and interactive plan viewer."),
        ("🔄 Headless Mode", "Run in scripts/CI with `grok -p \"your task\"`."),
        ("🔗 Git & Terminal Integration", "Stage, commit, run builds/tests with live output."),
        ("🧠 Memory & Context", "Remembers decisions across sessions."),
    ]
    
    for title, desc in features:
        with st.expander(title, expanded=False):
            st.write(desc)

# ====================== COMMANDS & USAGE ======================
elif page == "⌨️ Commands & Usage":
    st.header("⌨️ Useful Commands")
    
    st.markdown("### Core Commands")
    commands = {
        "Start interactive session": "grok",
        "Headless mode (one-shot)": "grok -p \"your task here\"",
        "Inspect current project": "grok inspect",
        "Use specific model": "grok -p \"task\" -m model-name",
        "Switch model inside TUI": "/model <name>",
    }
    
    for cmd, desc in commands.items():
        st.markdown(f"**{cmd}**")
        st.code(desc, language="bash")
    
    st.markdown("### Recommended First Prompts")
    st.code("""
Explain this entire codebase.
Create a plan to add user authentication with JWT.
Refactor the checkout flow for better performance.
Review this PR and suggest improvements.
""", language="bash")

# ====================== TROUBLESHOOTING ======================
elif page == "🛠️ Troubleshooting":
    st.header("🛠️ Common Issues & Fixes (macOS)")
    
    with st.expander("`grok: command not found`"):
        st.code("""
echo 'export PATH="$HOME/.grok/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
# or restart Terminal
""", language="bash")
    
    with st.expander("Authentication / Access Denied"):
        st.write("Make sure you have **SuperGrok** or **X Premium+**.")
        st.write("Try setting the API key manually:")
        st.code("export XAI_API_KEY=\"xai-...\"", language="bash")
    
    with st.expander("Installer fails or hangs"):
        st.write("Run the command again or check your internet/firewall.")
    
    with st.expander("Want to update Grok Build?"):
        st.write("Just re-run the install command — it will update automatically.")

# Footer
st.markdown("---")
st.caption("Compiled from official xAI documentation (docs.x.ai) • June 2026 • Grok Build is in early beta")
st.caption("Made with ❤️ using Streamlit • Works perfectly on Python 3.14.6")
