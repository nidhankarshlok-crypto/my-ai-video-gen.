import streamlit as st
import os
from moviepy import ImageClip, TextClip, CompositeVideoClip

# Cloud sathi ImageMagick Fix
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

st.title("🎬 AI Video Creator (Final Fix)")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
video_text = st.text_input("Text:", "My Sci-Fi Asset")

if st.button("Generate Video!"):
    if uploaded_file is not None:
        with st.spinner("Rendering suru aahe..."):
            try:
                # 1. Image save kar
                with open("temp_img.png", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # 2. Background (Simple Resize - No Lambda to avoid Error)
                bg_clip = ImageClip("temp_img.png").with_duration(5)
                # 'lambda' kadhun takla aahe mhanun '*' operand error yenar nahi
                bg_clip = bg_clip.resized(width=720, height=1280)

                # 3. Text with Manual Opacity (Fade-In)
                txt = TextClip(
                    text=video_text, 
                    font_size=60, 
                    color='yellow', 
                    size=(640, 300), 
                    method='caption'
                )
                txt = txt.with_duration(5).with_position(('center', 1000))
                
                # Opacity fix: Lambda function ऐवजी direct text dakhvuya jar error yet asel tar
                # Jar opacity mule error ala tar hi line delete kar
                txt = txt.with_opacity(0.8) 

                # 4. Combine & Write
                final_video = CompositeVideoClip([bg_clip, txt], size=(720, 1280))
                
                output = "final_fixed.mp4"
                final_video.write_videofile(output, fps=24, codec="libx264", logger=None)

                # 5. Preview
                st.video(output)
                st.success("🎉 Done! Error free video tayar aahe.")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pahile ek image upload kar bhau!")
