import streamlit as st
import os
from moviepy import ImageClip, TextClip, CompositeVideoClip

# Cloud sathi ImageMagick Fix
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

st.title("🎬 Cinematic AI Video Creator")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
video_text = st.text_input("Text:", "My Sci-Fi Asset")

if st.button("Generate Motion Video!"):
    if uploaded_file is not None:
        with st.spinner("Cinematic rendering suru aahe..."):
            try:
                # 1. Image save kar
                with open("temp_img.png", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # 2. Background with SLOW ZOOM
                bg_clip = ImageClip("temp_img.png").with_duration(5)
                # Zoom effect: 1 second-la 4% zoom
                bg_clip = bg_clip.resized(lambda t: 1 + 0.04 * t)
                bg_clip = bg_clip.resized(width=720, height=1280)

                # 3. Text with MANUAL FADE-IN (v2.0 Safe)
                txt = TextClip(
                    text=video_text, 
                    font_size=60, 
                    color='yellow', 
                    size=(640, 300), 
                    method='caption'
                )
                txt = txt.with_duration(5).with_position(('center', 1000))
                
                # 'with_opacity' vapara, ha MoviePy v2.0 madhe perfect chalto
                txt = txt.with_opacity(lambda t: min(1.0, t / 1.0)) 

                # 4. Combine & Write
                final_video = CompositeVideoClip([bg_clip, txt], size=(720, 1280))
                
                output = "motion_render.mp4"
                final_video.write_videofile(output, fps=24, codec="libx264", logger=None)

                # 5. Preview & Download
                st.video(output)
                with open(output, "rb") as f:
                    st.download_button("Gallery madhe save kar", f, file_name="my_3d_video.mp4")
                
                st.success("🎉 Done! Ata bgh motion ani fade-in!")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pahile ek image upload kar bhau!")
