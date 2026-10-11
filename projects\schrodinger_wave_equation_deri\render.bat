@echo off
REM Clipchat Multi-Track Compile Command
ffmpeg -y -i "shot_01.mp4" -i "shot_02.mp4" -i "assets/hyperframes/motion_overlay.mov" -i "voiceover_master.wav" -i "dark_ambient_pulse.wav" \
  -filter_complex "
  [0:v]trim=start=0.5:end=4.5,setpts=PTS-STARTPTS[v1_0];
  [1:v]trim=start=0.5:end=4.5,setpts=PTS-STARTPTS[v1_1];
  [v1_0][v1_1]concat=n=2:v=1:a=0[v1_base];
  [v1_base][2:v]overlay=0:0[v2_comp];
  [v2_comp]lut3d=file='C:/Users/user/Documents/VIDEO-EDIT-SKILL/references/PerplexityDarkSlate.cube'[v_graded];
  [4:a]volume=0.08[music_ducked];
  [3:a][music_ducked]amix=inputs=2:duration=first[a_master]
  " \
  -map "[v_graded]" -map "[a_master]" \
  -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 320k \
  "final_master_916.mp4"
