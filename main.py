from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeTranscricao:

  def __init__(self, url):
    self.url = url
    self.idioma = 'pt'

  def video_id(self):
    return self.url.split('watch?v=')[1]

  def transcricao(self):
    transcricao = YouTubeTranscriptApi.get_transcript("Q8eajxcS6dQ", languages=['pt'])
    print(transcricao[0]['text'])
    print(transcricao[1]['text'])
    print(transcricao[2]['text'])

trans = YoutubeTranscricao('https://www.youtube.com/watch?v=Q8eajxcS6dQ')
print(trans)
print(trans.video_id())
