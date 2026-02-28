import streamlit as st
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Jtech Media Portfolio", layout="wide")

# ------------------ HEADER ------------------
st.image("assets/logo.png", width=120)
st.title("🎬 Jtech Media Portfolio")
st.caption("Creative Media • Audio Production • Tech Solutions")

st.markdown("---")

# ------------------ HELPER FUNCTIONS ------------------
def get_mime(file_path):
    if file_path.endswith(".mp4"):
        return "video/mp4"
    elif file_path.endswith(".mp3"):
        return "audio/mpeg"
    elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
        return "image/jpeg"
    elif file_path.endswith(".png"):
        return "image/png"
    else:
        return "application/octet-stream"

def is_url(path):
    return path.startswith("http://") or path.startswith("https://")

# ------------------ PROJECT DATA ------------------
projects = [

#------------VIDEOS----------------
    {

        "title": "Come Alive (Dry Bones) by Lauren Diagle - cover",
        "type": "video",
        "file_path": "https://youtu.be/UFjOhBtC9Xc",
        "description": """
### Project Overview
High-definition promotional video for a tech startup.
"""
    },
    {

        "title": "Corporate Brand Video",
        "type": "video",
        "file_path": "https://youtu.be/KI2x19ppDFM",
        "description": """
### Project Overview
High-definition promotional video for a tech startup.
"""
    },
    {

        "title": "Corporate Brand Video",
        "type": "video",
        "file_path": "https://youtu.be/PUaMdAhe4Sc",
        "description": """
### Project Overview
High-definition promotional video for a tech startup.
"""
    },
    {

        "title": "Corporate Brand Video",
        "type": "video",
        "file_path": "https://youtu.be/GGLPXO-3fUo",
        "description": """
### Project Overview
High-definition promotional video for a tech startup.
"""
    },
    {

        "title": "Corporate Brand Video",
        "type": "video",
        "file_path": "https://youtu.be/MPcKtyNs42U",
        "description": """
### Project Overview
High-definition promotional video for a tech startup.
"""
    },

#--------------AUDIO----------------

#     {
#         "title": "Acoustic Session Audio",
#         "type": "audio",
#         "file_path": "uploads/studio_track.mp3",
#         "description": """
# ### Sound Engineering
# Multi-track recording and mastering for a local artist.
# """
#     },

#------------IMAGES----------------
    {
        "title": "Technical Documentation",
        "type": "image",
        "file_path": "uploads\\management.jpg",
        "description": """
### Tech Infrastructure
Detailed look at the server architecture implemented.
"""
    },
    {
        "title": "Technical Documentation",
        "type": "image",
        "file_path": "uploads\\Dlcf_welcome.jpg",
        "description": """
### Tech Infrastructure
Detailed look at the server architecture implemented.
"""
    },
    {
        "title": "Technical Documentation",
        "type": "image",
        "file_path": "uploads\\social_science.jpg",
        "description": """
### Tech Infrastructure
Detailed look at the server architecture implemented.
"""
    },
    {
        "title": "Technical Documentation",
        "type": "image",
        "file_path": "uploads\\sociology.jpg",
        "description": """
### Tech Infrastructure
Detailed look at the server architecture implemented.
"""
    },
    {
        "title": "Technical Documentation",
        "type": "image",
        "file_path": "uploads\\prayer_meeting.jpg",
        "description": """
### Tech Infrastructure
Detailed look at the server architecture implemented.
"""
    },
]

# ------------------ FILTER ------------------
category = st.selectbox(
    "Filter Projects",
    ["All", "video", "audio", "image"]
)

st.markdown("---")

# ------------------ DISPLAY PROJECTS ------------------
filtered_projects = [
    p for p in projects if category == "All" or p["type"] == category
]

if not filtered_projects:
    st.info("No projects found for this category.")
else:
    for project in filtered_projects:
        col1, col2 = st.columns([3, 2], gap="large")

        # ---------- MEDIA COLUMN ----------
        with col1:
            path = project["file_path"]

            if is_url(path):
                # Online media (YouTube, direct links)
                if project["type"] == "video":
                    st.video(path)
                elif project["type"] == "audio":
                    st.audio(path)
                elif project["type"] == "image":
                    st.image(path, use_container_width=True)
            else:
                # Local files
                if os.path.exists(path):
                    if project["type"] == "video":
                        with open(path, "rb") as f:
                            st.video(f.read())
                    elif project["type"] == "audio":
                        with open(path, "rb") as f:
                            st.audio(f.read())
                    elif project["type"] == "image":
                        st.image(path, use_container_width=True)
                else:
                    st.error(f"❌ File not found: {path}")

        # ---------- TEXT & DOWNLOAD COLUMN ----------
        with col2:
            st.subheader(project["title"])
            st.markdown(project["description"])

            # if is_url(path):
            #     st.link_button("▶ View / Download", path)
            # else:
            #     if os.path.exists(path):
            #         with open(path, "rb") as file:
            #             st.download_button(
            #                 label="📥 Download Project File",
            #                 data=file,
            #                 file_name=os.path.basename(path),
            #                 mime=get_mime(path)
            #             )
            #     else:
            #         st.warning("File not available")

        st.markdown("---")

# ------------------ CONTACT SECTION ------------------
st.markdown("## 📞 Work With Jtech Media")
st.write("Need video production, audio mastering, or tech solutions? Let's work together.")

st.link_button(
    "💬 Chat on WhatsApp",
    "https://wa.me/2348165750580"
)

st.link_button(
    "📧 Send Email",
    "mailto:jnwanya10@gmail.com"
)