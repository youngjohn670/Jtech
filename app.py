import streamlit as st
# from auth import auth_page
# from auth_db import create_user, create_user, init_db
# init_db()  # ensures users.db exists
# from db import add_project, get_projects, init_db as init_project_db

# st.set_page_config(page_title="Jtech Media", layout="wide")
# init_db()

# #create default admin (wrapped in a try/check is better, but this works)
# create_user("admin", "admin123", role="admin")

# 2. Initialize Session States
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = None

# ------------------ LOGO AND HEADER ------------------
col1, col2 = st.columns([1, 6])
with col1:
    st.image("assets/logo.png", width=80)
with col2:
    st.markdown("## JTECH MEDIA")

st.markdown("MULTIMEDIA AND TECH SERVICES.")
st.image("assets/tech.jpg", use_container_width=True)

# # ------------------ CENTERED AUTH BUTTONS ------------------
# if "auth_mode" not in st.session_state:
#     st.session_state.auth_mode = None

# if not st.session_state.get("authenticated", False) and st.session_state.auth_mode is None:
#     # Columns to centralize buttons
#     col_left, col_center, col_right = st.columns([1, 2, 1])
#     with col_center:
#         col_login, col_signup = st.columns(2)  # inline buttons in the center column
#         with col_login:
#             if st.button("🔐 Login", use_container_width=True):
#                 st.session_state.auth_mode = "login"
#         with col_signup:
#             if st.button("📝 Sign Up", use_container_width=True):
#                 st.session_state.auth_mode = "signup"

# # ------------------ LOGOUT BUTTON ------------------
# if st.session_state.get("authenticated", False):
#     with st.sidebar:
#         if st.button("🚪 Logout"):
#             st.session_state.authenticated = False
#             st.session_state.username = None
#             st.session_state.role = None
#             st.session_state.auth_mode = None
#             st.experimental_rerun()  # reload app to homepage

# # ------------------ MAIN FLOW ------------------
# if not st.session_state.get("authenticated", False):
#     auth_page()  # shows login/signup forms based on auth_mode
# else:
#     main_app()  # your main app after login

# if pages == "Upload Project":
#     if st.session_state.role != "admin":
#         st.error("Access Denied. Only admins can upload projects.")
#         st.stop()