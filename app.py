import streamlit as st
import os

# --- MOVIEPY FIX START ---
try:
    # Navin version sathi (v2.0+)
    from moviepy.video.VideoClip import ColorClip, TextClip
    from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
except ImportError:
    try:
        # Junya version sathi (v1.0.3)
        from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
    except ImportError:
        # Direct import try
        from moviepy import ColorClip, TextClip, CompositeVideoClip
# --- MOVIEPY FIX END ---

st.title("🚀 AI Video Generator (Fixed)")

video_text = st.text_input("Video Text:", "Success! Setup Done.")

if st.button("Video Banav!"):
    with st.spinner("Rendering..."):
        try:
            # Simple 3-second black clip
            bg = ColorClip(size=(720, 1280), color=(0,0,0), duration=3)
            
            # Text Clip
            # Note: Cloud var fonts cha issue yeto, mhanun 'method=caption' vaprat ahot
            txt = TextClip(video_text, fontsize=50, color='white', size=(720, 1280), method='caption')
            txt = txt.set_duration(3).set_position('center')
            
            final = CompositeVideoClip([bg, txt])
            output = "result.mp4"
            
            # Logger=None mule extra errors yet nahit
            final.write_videofile(output, fps=24, codec="libx264", audio=False, logger=None)
            
            st.video(output)
            st.success("Bhau, video banla! 🎉")
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Jar ImageMagick cha error asel tar sang, to last step asel.")
