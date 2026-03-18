import streamlit as st
import os
from moviepy import ImageClip, TextClip, CompositeVideoClip

# Cloud sathi ImageMagick Fix
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

st.title("🎬 Pro AI Video Creator")

# 1. Image Upload Option
uploaded_file = st.file_uploader("Tujha 3D Render (Image) upload kar", type=["png", "jpg", "jpeg"])

# 2. Text Input
video_text = st.text_input("Video var kay lihayche aahe?", "My Sci-Fi Starship")

if st.button("Video Generate Kar!"):
    if uploaded_file is not None:
        with st.spinner("Video render hotoय..."):
            try:
                # Image la Temporary file mhanun save kar
                with open("temp_img.png", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # --- MOVIEPY LOGIC ---
                # 1. Image Clip (5 Seconds)
                # Note: Navin MoviePy madhe ImageClip nantar .with_duration vaprtat
                bg_clip = ImageClip("temp_img.png").with_duration(5)
                
                # Image chi size 720x1280 (Portrait) madhe adjust karne
               bg_clip = bg_clip.resized(width=720, height=1280)

                # 2. Text Clip (Khali Subtitle sarkhe)
                txt = TextClip(
                    text=video_text, 
                    font_size=50, 
                    color='yellow', 
                    size=(600, 200), 
                    method='caption'
                )
                # Text la khali (bottom) set karne
                txt = txt.with_duration(5).with_position(('center', 1000))

                # 3. Combine karne
                final_video = CompositeVideoClip([bg_clip, txt], size=(720, 1280))
                
                output = "final_render.mp4"
                final_video.write_videofile(output, fps=24, codec="libx264", logger=None)

                # 4. Result
                st.video(output)
                with open(output, "rb") as f:
                    st.download_button("Gallery madhe save kar", f, file_name="my_3d_video.mp4")
                
                st.success("🎉 Done! VN madhe edit karayla tayar aahe.")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pahile ek image upload kar bhau!")
