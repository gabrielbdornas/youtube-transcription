from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeTranscricao:

  def __init__(self, url):
    self.url = url
    self.idioma = 'pt'

  def __repr__(self):
    return f"YoutubeTranscricao('{self.url}')"

  def __str__(self):
    return f"Transcrição vídeos do Youtube url: {self.url}"

  def video_id(self):
    return self.url.split("watch?v=")[1]

  def transcricao_tempo(self):
    transcricao = YouTubeTranscriptApi.get_transcript(self.video_id(), languages=[self.idioma])
    transcricao_texto = ''
    for i in transcricao:
      transcricao_texto += f"{i['start']} - {i['text']}\n"
    return transcricao_texto

    def transcricao(self):
      transcricao = YouTubeTranscriptApi.get_transcript(self.video_id(), languages=[self.idioma])
      transcricao_texto = ''
      for i in transcricao:
        transcricao_texto += f"{i['text']}\n"
      return transcricao_texto


trans = YoutubeTranscricao('https://www.youtube.com/watch?v=Q8eajxcS6dQ')
print(trans)
