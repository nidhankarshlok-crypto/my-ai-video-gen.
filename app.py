import streamlit as st
import os
from moviepy import ImageClip, TextClip, CompositeVideoClip

os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

st.title("🎬 Cinematic AI Video Creator")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
video_text = st.text_input("Text:", "My Sci-Fi Asset")

if st.button("Generate Motion Video!"):
    if uploaded_file is not None:
        with st.spinner("Cinematic rendering suru aahe..."):
            try:
                with open("temp_img.png", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # 1. Background with SLOW ZOOM MOTION
                bg_clip = ImageClip("temp_img.png").with_duration(5)
                # Zoom Effect (lambda t: 1 + 0.04 * t)
                bg_clip = bg_clip.resized(lambda t: 1 + 0.04 * t)
                bg_clip = bg_clip.resized(width=720, height=1280)

                # 2. Text with Fade-In (Using crossfadein for v2.0)
                txt = TextClip(
                    text=video_text, 
                    font_size=60, 
                    color='yellow', 
                    size=(640, 300), 
                    method='caption'
                )
                txt = txt.with_duration(5).with_position(('center', 1000))
                txt = txt.crossfadein(1.0) # <--- HA BADAL KELA AAHE

                # 3. Combine
                final_video = CompositeVideoClip([bg_clip, txt], size=(720, 1280))
                
                output = "motion_render.mp4"
                # Logger None thevla mhanje server var fast kaam karel
                final_video.write_videofile(output, fps=24, codec="libx264", logger=None)

                st.video(output)
                st.success("🎉 Ata bgh, motion ani fade-in donhi kaam kartil!")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pahile ek image upload kar bhau!")
