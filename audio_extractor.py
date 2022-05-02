import moviepy.editor as mp 

my_clip = mp.VideoFileClip("vids/grumpieroldmen.mp4")

my_clip.audio.write_audiofile(r"my_result.mp3")

my_clip.audio.write_audiofile(r"my_result.wav")