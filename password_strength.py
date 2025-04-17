import streamlit as st
import re
import string

# Custom CSS styling
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
        padding: 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stProgress>div>div>div {
        background-color: #4CAF50;
    }
    .stMarkdown {
        font-family: 'Arial', sans-serif;
    }
    .password-strength {
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .weak {
        background-color: #ffcdd2;
        color: #d32f2f;
    }
    .medium {
        background-color: #fff9c4;
        color: #f57f17;
    }
    .strong {
        background-color: #c8e6c9;
        color: #388e3c;
    }
    .suggestion {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .title {
        color: #1976d2;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter")
    
    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number")
    
    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character")
    
    # Common patterns check
    common_patterns = ['123', 'abc', 'password', 'qwerty']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
    else:
        feedback.append("Avoid using common patterns or sequences")
    
    return score, feedback

def get_strength_level(score):
    if score <= 2:
        return "Weak", "red", "weak"
    elif score <= 4:
        return "Medium", "orange", "medium"
    else:
        return "Strong", "green", "strong"

def main():
    st.markdown('<h1 class="title">🔒 Password Strength Meter</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Enter a password to check its strength</p>', unsafe_allow_html=True)
    
    password = st.text_input("", type="password", placeholder="Enter your password here...")
    
    if password:
        score, feedback = check_password_strength(password)
        strength_level, color, css_class = get_strength_level(score)
        
        st.markdown(f'<div class="password-strength {css_class}">Password Strength: {strength_level}</div>', unsafe_allow_html=True)
        st.progress(score/6)
        
        if feedback:
            st.markdown('<h3 style="color: #1976d2;">Suggestions to improve your password:</h3>', unsafe_allow_html=True)
            for suggestion in feedback:
                st.markdown(f'<div class="suggestion">🔹 {suggestion}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
