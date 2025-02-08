import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="A Special Question ❤️",
    page_icon="💍",
    layout="centered"
)

# Custom CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    /* Add a background color to the entire app */
    body {
        background-color: #f0f8ff; /* Light AliceBlue */
    }
    
    .main {
        background: linear-gradient(135deg, #ffb6c1, #e6e6fa);
        padding: 20px; /* Add padding around the content */
        border-radius: 10px; /* Optional: Add rounded corners */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional: Add a subtle shadow */
        margin-top: 20px; /* Add some top margin to separate from the very top */
        margin-bottom: 20px; /* Add some bottom margin */
    }

    .title {
        font-family: 'Dancing Script', cursive;
        font-size: 3rem;
        color: #ff1493;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }

    .message {
        font-size: 1.5rem;
        text-align: center;
        color: #4a4a4a;
        margin: 1rem 0;
    }

    /* Center all buttons */
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-size: 1.2rem;
        display: block;
        margin: 0 auto;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
    }

    div.stButton > button:hover {
        background-color: #ff1493;
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2); /* Enhance shadow on hover */
    }

    /* Style for the "No" button */
    .no-button > button {
        background-color: #808080 !important;
    }

    /* Ensure columns are centered */
    div.row-widget.stHorizontal {
        justify-content: center;
        gap: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'no_positions' not in st.session_state:
    st.session_state.no_positions = []
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

def get_new_position():
    # Generate a list of predefined positions for the "No" button
    positions = [
        "Maybe think again? 🤔",
        "Are you sure? 🥺",
        "Really? 😢",
        "Think about it! 💭",
        "One more time? 💝",
        "Pretty please? 🌹",
        "Last chance! ✨"
    ]
    return random.choice(positions)

# Content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">Hey Love... 💕</h1>', unsafe_allow_html=True)

if st.session_state.stage == 0:
    st.markdown('<p class="message">I have something special to ask you... 💌</p>', unsafe_allow_html=True)

    # Center the reveal button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Click to reveal 💝", key="reveal"):
            st.session_state.stage = 1
            st.rerun()

elif st.session_state.stage == 1:
    st.markdown('<p class="message">Will you be mine forever? 💍</p>', unsafe_allow_html=True)

    # Create centered columns for buttons
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("YES! 💖", key="yes"):
            st.session_state.stage = 2
            st.rerun()

    with col3:
        # Only show "No" button if we haven't exceeded our limit
        if st.session_state.no_count < 7:
            message = get_new_position()
            if st.button(message, key=f"no_{st.session_state.no_count}"):
                st.session_state.no_count += 1
                st.rerun()

elif st.session_state.stage == 2:
    st.markdown('<p class="message">YAAAAY! I\'m the happiest person alive! 🎉</p>', unsafe_allow_html=True)
    st.balloons()

    # Center the celebration emoji
    st.markdown("""
        <div style='text-align: center; font-size: 3rem; margin: 2rem;'>
            💑 💕 💍 🎉 🎊 💝
        </div>
        <p class="message">I love you forever! ❤️</p>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Hidden reset button in sidebar
if st.sidebar.button("Reset App"):
    st.session_state.stage = 0
    st.session_state.no_count = 0
    st.session_state.no_positions = []
    st.rerun()
