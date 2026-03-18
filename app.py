import streamlit as st
import os

# MoviePy v2.0 sathi navin import padhat
try:
    from moviepy import ColorClip, TextClip, CompositeVideoClip
except ImportError:
    from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

# Cloud var ImageMagick sathi hi line garjechi aahe
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"

st.title("🚀 AI Video Generator (Fixed)")

video_text = st.text_input("Video madhe kay lihayche aahe?", "Success! Mazya Starship cha Video.")

if st.button("Video Banav!"):
    with st.spinner("Rendering suru aahe..."):
        try:
            # 1. Background Clip (Black, 3 Seconds)
            bg = ColorClip(size=(720, 1280), color=(0, 0, 0), duration=3)

            # 2. Text Clip (MoviePy v2.0 parameters)
            txt = TextClip(
                text=video_text, 
                font_size=70, 
                color='white', 
                size=(720, 1280), 
                method='caption'
            )
            txt = txt.with_duration(3).with_position('center')

            # 3. Final Composite Video
            final_video = CompositeVideoClip([bg, txt])
            
            output_file = "result.mp4"
            # write_videofile madhe logger=None mule fast render hote
            final_video.write_videofile(output_file, fps=24, codec="libx264", logger=None)

            # 4. Display & Download
            st.video(output_file)
            with open(output_file, "rb") as file:
                st.download_button("Video Download Kar", file, file_name="ai_video.mp4")
            
            st.success("🎉 Bhau, video tayar jhala!")

        except Exception as e:
            st.error(f"Render Error: {e}")
            st.info("Jar ImageMagick error asel, tar apan method badluya.")
