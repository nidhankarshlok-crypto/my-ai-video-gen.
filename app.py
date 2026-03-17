import streamlit as st
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

st.title("🚀 AI Video Generator (Cloud Render)")

# User Input
video_text = st.text_input("Video madhe kay lihayche aahe?", "Mazya Starship che Render!")
duration = st.slider("Video kiti seconds cha pahije?", 1, 10, 5)

if st.button("Video Banav!"):
    with st.spinner("Cloud var rendering suru aahe..."):
        try:
            # 1. Background banav (Black color)
            bg = ColorClip(size=(720, 1280), color=(0, 0, 0), duration=duration)

            # 2. Text Clip banav
            txt = TextClip(video_text, fontsize=70, color='white', size=(720, 1280), method='caption')
            txt = txt.set_duration(duration).set_position('center')

            # 3. Merge kar
            final_video = CompositeVideoClip([bg, txt])
            
            # 4. Save to temp file
            output_file = "generated_video.mp4"
            final_video.write_videofile(output_file, fps=24, codec="libx264")

            # 5. Display & Download
            st.video(output_file)
            with open(output_file, "rb") as file:
                st.download_button("Video Download Kar", file, file_name="ai_video.mp4")
            
            st.success("Done! 🎉")
        except Exception as e:
            st.error(f"Error: {e}")