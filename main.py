import streamlit as st
from app import PasswordStrengthMeter

# Set page configuration and style
st.set_page_config(page_title="Password Checker", page_icon="🔒")

# Custom CSS for background and styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #134e5e, #71b280);
        color: white;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton button:hover {
        background-color: #27ae60;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #134e5e;
        background-color: rgba(255,255,255,0.9);
    }
    .stSlider div[data-baseweb="slider"] {
        background-color: #2ecc71 !important;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Password Strength Checker 🔒")
    
    meter = PasswordStrengthMeter()
    
    st.subheader("Check Your Password")
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, feedback, strength = meter.check_password_strength(password)
        
        # Show strength with color
        colors = {
            "Strong": "#2ecc71",
            "Moderate": "#f1c40f",
            "Weak": "#e74c3c",
            "Very Weak": "#c0392b"
        }
        
        st.markdown(f"### Strength: <span style='color: {colors[strength]}'>{strength}</span>", unsafe_allow_html=True)
        st.markdown(f"**Score:** {score}/4")
        
        if feedback:
            st.subheader("Feedback:")
            for msg in feedback:
                st.error(msg)
    
    st.markdown("---")
    
    # Password generator section
    st.subheader("Generate Strong Password")
    length = st.slider("Password Length", 8, 32, 12)
    
    if st.button("Generate Password"):
        password = meter.generate_strong_password(length)
        st.code(password, language=None)
        st.success("✅ Password generated successfully! Copy and keep it safe!")

if __name__ == "__main__":
    main() 