from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeTranscricao:

  def __init__(self, url):
    self.url = url
    self.idioma = 'pt'

  def __repr__(self):
    return f"YoutubeTranscricao('{self.video_id()}')"

  def __str__(self):
    return f"Transcrição do vídeo YouTube de url: {self.url}"

  def video_id(self):
    return self.url.split('watch?v=')[1]

  def transcricao(self):
    transcricao_texto = ''
    transcricao = YouTubeTranscriptApi.get_transcript(self.video_id(), languages=['pt'])
    for i in transcricao:
      transcricao_texto += f"{i['text']}\n"
    return transcricao_texto

  def cria_arquivo_transcricao(self):
    with open('transcricao.txt', 'w', encoding='utf-8') as file:
      file.write(self.transcricao())

trans = YoutubeTranscricao('https://www.youtube.com/watch?v=Q8eajxcS6dQ')
print(trans)
print(trans.video_id())
print(trans.cria_arquivo_transcricao())


