# PT - Your Personal Transcriber
    ### Are you tired of sifting through long audio recordings just to find that one important snippet of information you need? This Python program offers a solution by allowing you to record audio, play it back, and automatically transcribe it into a text file. With user-friendly input collection, real-time countdowns, and options to customize filenames, this program simplifies the process of capturing and accessing spoken content.

Key Features:

User-Friendly Input Collection: The program begins by prompting you to specify the duration of your audio recording in seconds. It ensures that you input a valid integer for the recording duration.
Real-Time Countdown: As you start recording, a visual countdown is displayed, showing you exactly how much time remains for your recording session.
Audio Recording and Playback: The program uses the sounddevice library to capture audio from your microphone. After recording, it plays back the audio so you can review it immediately.
Customizable Filenames: You have the option to customize the name of the audio file. If you prefer, the program can generate filenames using the current date and time.
Transcription: If you choose to save the recording, the program utilizes the Google Web Speech API through the speech_recognition library to transcribe the audio into text.
Text File Creation: The transcription is saved as a text file with the same name as the audio recording. This makes it easy to find and review the content later.

How It Works:

Input Collection: The program initiates by asking you for the duration (in seconds) of your recording. It continues to prompt until a valid integer is provided.
Recording: Using a sample rate of 48,000 Hz and two audio channels, the program records your voice for the specified duration. A visual countdown informs you of the remaining time.
Playback: After recording, the program plays back the audio, allowing you to listen to your recording immediately.
Save or Discard: You decide whether to save the recording. If you choose to save it, you can opt for a custom filename or use the default naming format based on the date and time.
Transcription: If saved, the audio is transcribed into text using the Google Web Speech API. This text is then ready for further use or reference.
Text File Creation: The transcription is saved as a text file with the same name as the audio recording, making it easy to locate and review.

Use Cases:

Note Taking: Quickly capture your spoken thoughts and ideas, and access them as text files for reference or organization.
Interviews and Meetings: Record interviews, meetings, or lectures and convert them into text transcripts for easy searching and summarization.
Voice Memo Management: Keep a library of voice memos, all neatly transcribed and accessible as text documents.
Language Learning: Practice speaking a new language, and have your pronunciation and speech automatically converted to text for review.
Accessibility: Assist individuals with hearing impairments by providing text versions of spoken content.

    

    [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

    
