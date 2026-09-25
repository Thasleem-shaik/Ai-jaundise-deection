import streamlit as st
from PIL import Image


# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------

st.set_page_config(
    page_title="AI Jaundice Screening",
    page_icon="👁️",
    layout="wide"
)


# -----------------------------------------
# TITLE
# -----------------------------------------

st.title("👁️ AI Jaundice Screening")

st.write(
    "Look at the camera and capture an image of your eye "
    "for preliminary screening."
)

st.warning(
    "⚠️ This is an educational screening project and "
    "is not a medical diagnosis."
)


# -----------------------------------------
# SIDEBAR
# -----------------------------------------

st.sidebar.title("📋 Instructions")

st.sidebar.write(
    """
    1. Allow camera access.
    2. Look directly at the camera.
    3. Make sure your eye is clearly visible.
    4. Capture the image.
    5. The AI will analyze the image.
    """
)


# -----------------------------------------
# CAMERA
# -----------------------------------------

st.subheader("📷 Camera")

camera_image = st.camera_input(
    "Take a picture of your eye"
)


# -----------------------------------------
# DISPLAY IMAGE
# -----------------------------------------

if camera_image is not None:

    image = Image.open(
        camera_image
    ).convert("RGB")


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Captured Image")

        st.image(
            image,
            use_container_width=True
        )


    with col2:

        st.subheader("AI Screening")

        if st.button(
            "🔍 Analyze Eye",
            use_container_width=True
        ):

            # Temporary result
            # Real AI model will be connected later.

            result = "normal"


            if result == "normal":

                st.success(
                    "🟢 NO JAUNDICE DETECTED"
                )


            else:

                probability = 87

                st.warning(
                    "🟡 POSSIBLE JAUNDICE"
                )

                st.metric(
                    "Screening Probability",
                    f"{probability}%"
                )


# -----------------------------------------
# FOOTER
# -----------------------------------------

st.markdown("---")

st.caption(
    "AI Jaundice Screening • Educational Project"
)