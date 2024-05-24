from youtube_transcript_api import YouTubeTranscriptApi

def get_video_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    video_id = '0HZPyhnErFo'  # Replace with the actual video ID
    captions = get_video_captions(video_id)
    file_path = 'captions.txt'

    try:
        with open(file_path, 'w') as file:
            file.write(captions)
        print(f"Captions saved to {file_path}")
    # handling exceptions
    except Exception as e:
        print(f"An error ocurred while saving the file {str(e)}")