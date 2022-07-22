from pytube import YouTube

url='https://www.youtube.com/watch?v=7c3-Gei5j4w&list=RD7c3-Gei5j4w&start_radio=1'
my_video=YouTube(url)

print("*********************Video Title****************************")
print(my_video.title)
print("*********************thumbnail image****************************")
print(my_video.thumbnail_url)
print("*********************download video****************************")
my_video=my_video.streams.get_highest_resolution()
my_video.download()