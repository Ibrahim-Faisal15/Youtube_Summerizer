from youtube_transcript_api import YouTubeTranscriptApi

def generate_tranScript(id):
   transScript = YouTubeTranscriptApi.get_transcript(id,  languages=('en',))
   return transScript



