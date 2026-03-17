import streamlit as st
import os

# MoviePy Import karnyachi safe padhat
try:
    from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
except ImportError:
    from moviepy import ColorClip, TextClip, CompositeVideoClip

st.title("🚀 AI Video Generator")

# User Input
video_text = st.text_input("Video Text:", "Testing Cloud Render")

if st.button("Video Banav!"):
    with st.spinner("Processing..."):
        try:
            # 1. Simple Clip
            bg = ColorClip(size=(720, 1280), color=(0,0,0), duration=3)
            
            # 2. Text Clip (Method badalli aahe)
            txt = TextClip(video_text, fontsize=50, color='white', size=(720, 1280))
            txt = txt.set_duration(3).set_position('center')
            
            # 3. Final Video
            final = CompositeVideoClip([bg, txt])
            output = "test.mp4"
            final.write_videofile(output, fps=24, codec="libx264")
            
            st.video(output)
            st.success("Yesss! Banla Video.")
        except Exception as e:
            st.error(f"Error: {e}")
