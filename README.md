# Project Pipeline

Goal: The goal of these code segments is to replciate the data pipeline process that was in the "MMGCN: Multi-modal Graph Convolution Network for Personalized Recommendation of Micro-video" paper. 

Programs: 

- ml-20m-youtube.zip: Download .zip to access ml-youtube-20.csv, which contains the csv of all 20M movies and their YoutubeIDs

- yt3.py: Program that takes Youtube ID's and locally downloads youtube videos in a 'vids' folder

- keyFrames.py: Program which grabs key frames from previsouly downloaded videos and same them in a 'save' folder with individually named video folders containing key frames. 

- resnet.py: Accesses keyframes and produces classification 

- audio_extractor.py: Extracts audio from previously donwloaded videos and saves audio in a 'audio' folder

- vggish_feature_extractor.py: Accesses audio and produces a 128x128 audio embedding 

