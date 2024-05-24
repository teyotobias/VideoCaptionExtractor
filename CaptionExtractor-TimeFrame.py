from youtube_transcript_api import YouTubeTranscriptApi

def get_video_captions(video_id, start_time, end_time):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        filtered_transcript = [
            entry for entry in transcript 
            if start_time <= entry['start'] <= end_time
        ]
        combined_captions = []
        for i in range(0, len(filtered_transcript), 2):
            if i + 1 < len(filtered_transcript):
                combined_captions.append(filtered_transcript[i]['text'] + " " + filtered_transcript[i + 1]['text'])
            else:
                combined_captions.append(filtered_transcript[i]['text'])
        # Join the combined captions with a newline character
        captions = "\n".join(combined_captions)
        return captions
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    video_id = 'dOiA2nNJpc0'  # Replace with the actual video ID
    start_time = 60 * 0  # Start time in seconds (e.g., 2 minutes)
    end_time = 60 * 12  # End time in seconds (e.g., 5 minutes)
    captions = get_video_captions(video_id, start_time, end_time)
    file_path = 'captions.txt'

    try:
        with open(file_path, 'w') as file:
            file.write(captions)
        print(f"Captions saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")