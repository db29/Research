from pytube import YouTube


with open("/Users/daraius/Desktop/ndClasses/Research/urls.txt", "r") as f:
    ytids = f.read().splitlines()



for i in ytids:
    #print(i)
    print("Donwloading: " + i)

    
    try:
        YouTube('https://www.yt-download.org/api/button/videos/'+i).streams.first().download('/Users/daraius/Desktop/ndClasses/Research/vids2')
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download('/Users/daraius/Desktop/ndClasses/Research/audio') 
    except:
        print("no video found" + i )
    #audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    #audio.download('/Users/daraius/Desktop/ndClasses/Research/audio')