# import streamlit as st
# import pandas as pd
# import spacy
# from spacy_langdetect import LanguageDetector
# from spacy.language import Language
# import speech_recognition as sr
# import io

# # Initialize Spacy and language detector
# nlp = spacy.load('en_core_web_sm')

# # Check if the factory is already registered before registering it
# if "language_detector" not in nlp.factories:
#     @Language.factory("language_detector")
#     def get_lang_detector(nlp, name):
#         return LanguageDetector()

# if "language_detector" not in nlp.pipe_names:
#     nlp.add_pipe("language_detector", last=True)  # Add the language detector to the pipeline

# # Load the dataset
# data_path = "Marathi Profanity.xlsx"  # Change this to the path of your Excel file
# df = pd.read_excel(data_path)

# # Create dictionaries for fast lookup
# profane_to_substitute = {}
# profane_to_substitute_translit = {}

# for _, row in df.iterrows():
#     profane_to_substitute[row['Profane Word']] = row['Substitute Word']
#     profane_to_substitute_translit[row['Profane Word (English Transliteration)']] = row[
#         'Substitute Word (English Transliteration)']

# def detect_language(text):
#     doc = nlp(text)
#     return doc._.language['language']

# def replace_profanity(text):
#     words = text.split()
#     for i, word in enumerate(words):
#         if word in profane_to_substitute:
#             words[i] = profane_to_substitute[word]
#         elif word in profane_to_substitute_translit:
#             words[i] = profane_to_substitute_translit[word]
#     return ' '.join(words)

# def process_text(text):
#     lang = detect_language(text)
#     doc = nlp(text)

#     # Lexical analysis
#     lexical_analysis = [(token.text, token.lemma_, token.pos_) for token in doc]

#     # Syntactic analysis and Dependency Parsing
#     syntactic_analysis = [(token.text, token.dep_, token.head.text) for token in doc]

#     # Tokenization and Sentence segmentation
#     tokens = [token.text for token in doc]
#     sentences = [sent.text for sent in doc.sents]

#     # Stemming and Lemmatization
#     lemmatization = [token.lemma_ for token in doc]

#     # Stop word analysis
#     stop_words = [token.text for token in doc if token.is_stop]

#     return {
#         'lang': lang,
#         'tokens': tokens,
#         'sentences': sentences,
#         'lexical_analysis': lexical_analysis,
#         'syntactic_analysis': syntactic_analysis,
#         'lemmatization': lemmatization,
#         'stop_words': stop_words
#     }

# def transcribe_audio(audio_file):
#     recognizer = sr.Recognizer()
#     try:
#         # Use the uploaded audio file as the audio source
#         with sr.AudioFile(audio_file) as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         # Recognize speech using Google Web Speech API
#         text = recognizer.recognize_google(audio, language='mr-IN')
#         return text
#     except sr.UnknownValueError:
#         return "Google Speech Recognition could not understand the audio"
#     except sr.RequestError as e:
#         return f"Could not request results from Google Speech Recognition service; {e}"

# # Streamlit app
# st.title("Marathi Text and Audio Processing")

# # Select input type
# input_type = st.radio("Choose input type:", ("Text", "Audio"))

# if input_type == "Text":
#     input_text = st.text_area("Enter your text here:", height=150)

#     if st.button("Filter Profanity"):
#         if input_text:
#             processed_text = process_text(input_text)
#             filtered_text = replace_profanity(input_text)

#             st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

#             st.subheader("NLP Analysis")
#             st.write(f"Detected Language: {processed_text['lang']}")
#             st.write("Tokens:", processed_text['tokens'])
#             st.write("Sentences:", processed_text['sentences'])
#             st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
#             st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
#             st.write("Lemmatization:", processed_text['lemmatization'])
#             st.write("Stop Words:", processed_text['stop_words'])
#         else:
#             st.warning("Please enter some text to filter.")

# elif input_type == "Audio":
#     st.write("Upload an audio file (in WAV format) to transcribe it into Marathi text:")

#     # Upload audio file
#     audio_file = st.file_uploader("Choose a WAV file", type="wav")

#     if audio_file is not None:
#         st.write("Processing...")
#         # Convert uploaded file to a byte stream
#         audio_bytes = io.BytesIO(audio_file.read())
        
#         # Transcribe audio
#         transcription = transcribe_audio(audio_bytes)
        
#         if transcription:
#             st.subheader("Transcription:")
#             st.write(transcription)
            
#             # Process the transcribed text
#             processed_text = process_text(transcription)
#             filtered_text = replace_profanity(transcription)

#             st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

#             st.subheader("NLP Analysis")
#             st.write(f"Detected Language: {processed_text['lang']}")
#             st.write("Tokens:", processed_text['tokens'])
#             st.write("Sentences:", processed_text['sentences'])
#             st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
#             st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
#             st.write("Lemmatization:", processed_text['lemmatization'])
#             st.write("Stop Words:", processed_text['stop_words'])
#         else:
#             st.warning("Failed to transcribe audio.")

# import streamlit as st
# import pandas as pd
# import spacy
# from spacy_langdetect import LanguageDetector
# from spacy.language import Language
# import speech_recognition as sr
# import io

# # Initialize Spacy and language detector
# nlp = spacy.load('en_core_web_sm')

# # Register language detector only if it's not already registered
# if "language_detector" not in nlp.pipe_names:
#     if not hasattr(Language.factories, 'language_detector'):
#         @Language.factory("language_detector")
#         def get_lang_detector(nlp, name):
#             return LanguageDetector()
#     nlp.add_pipe("language_detector", last=True)

# # Load the dataset
# data_path = "Marathi Profanity.xlsx"  # Change this to the path of your Excel file
# df = pd.read_excel(data_path)

# # Create dictionaries for fast lookup
# profane_to_substitute = {}
# profane_to_substitute_translit = {}

# for _, row in df.iterrows():
#     profane_to_substitute[row['Profane Word']] = row['Substitute Word']
#     profane_to_substitute_translit[row['Profane Word (English Transliteration)']] = row[
#         'Substitute Word (English Transliteration)']

# def detect_language(text):
#     doc = nlp(text)
#     return doc._.language['language']

# def replace_profanity(text):
#     words = text.split()
#     for i, word in enumerate(words):
#         if word in profane_to_substitute:
#             words[i] = profane_to_substitute[word]
#         elif word in profane_to_substitute_translit:
#             words[i] = profane_to_substitute_translit[word]
#     return ' '.join(words)

# def process_text(text):
#     lang = detect_language(text)
#     doc = nlp(text)

#     # Lexical analysis
#     lexical_analysis = [(token.text, token.lemma_, token.pos_) for token in doc]

#     # Syntactic analysis and Dependency Parsing
#     syntactic_analysis = [(token.text, token.dep_, token.head.text) for token in doc]

#     # Tokenization and Sentence segmentation
#     tokens = [token.text for token in doc]
#     sentences = [sent.text for sent in doc.sents]

#     # Stemming and Lemmatization
#     lemmatization = [token.lemma_ for token in doc]

#     # Stop word analysis
#     stop_words = [token.text for token in doc if token.is_stop]

#     return {
#         'lang': lang,
#         'tokens': tokens,
#         'sentences': sentences,
#         'lexical_analysis': lexical_analysis,
#         'syntactic_analysis': syntactic_analysis,
#         'lemmatization': lemmatization,
#         'stop_words': stop_words
#     }

# def transcribe_audio(audio_file):
#     recognizer = sr.Recognizer()
#     transcription = ""
#     try:
#         # Use the uploaded audio file as the audio source
#         with sr.AudioFile(audio_file) as source:
#             recognizer.adjust_for_ambient_noise(source)
#             # Determine the total duration of the audio file
#             total_duration = int(source.DURATION)
#             offset = 0
#             chunk_duration = 30  # Process 30 seconds at a time
            
#             while offset < total_duration:
#                 audio = recognizer.record(source, duration=chunk_duration, offset=offset)
#                 try:
#                     # Recognize speech using Google Web Speech API
#                     text = recognizer.recognize_google(audio, language='mr-IN')
#                     transcription += text + " "
#                 except sr.UnknownValueError:
#                     transcription += "[Unintelligible] "
#                 except sr.RequestError as e:
#                     transcription += f"[RequestError: {e}] "
                
#                 offset += chunk_duration
#         return transcription
#     except sr.UnknownValueError:
#         return "Google Speech Recognition could not understand the audio"
#     except sr.RequestError as e:
#         return f"Could not request results from Google Speech Recognition service; {e}"

# # Streamlit app
# st.title("Marathi Text and Audio Processing")

# # Select input type
# input_type = st.radio("Choose input type:", ("Text", "Audio"))

# if input_type == "Text":
#     input_text = st.text_area("Enter your text here:", height=150)

#     if st.button("Filter Profanity"):
#         if input_text:
#             processed_text = process_text(input_text)
#             filtered_text = replace_profanity(input_text)

#             st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

#             st.subheader("NLP Analysis")
#             st.write(f"Detected Language: {processed_text['lang']}")
#             st.write("Tokens:", processed_text['tokens'])
#             st.write("Sentences:", processed_text['sentences'])
#             st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
#             st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
#             st.write("Lemmatization:", processed_text['lemmatization'])
#             st.write("Stop Words:", processed_text['stop_words'])
#         else:
#             st.warning("Please enter some text to filter.")

# elif input_type == "Audio":
#     st.write("Upload an audio file (in WAV format) to transcribe it into Marathi text:")

#     # Upload audio file
#     audio_file = st.file_uploader("Choose a WAV file", type="wav")

#     if audio_file is not None:
#         st.write("Processing...")
#         # Convert uploaded file to a byte stream
#         audio_bytes = io.BytesIO(audio_file.read())
        
#         # Transcribe audio
#         transcription = transcribe_audio(audio_bytes)
        
#         if transcription:
#             st.subheader("Transcription:")
#             st.write(transcription)
            
#             # Process the transcribed text
#             processed_text = process_text(transcription)
#             filtered_text = replace_profanity(transcription)

#             st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

#             st.subheader("NLP Analysis")
#             st.write(f"Detected Language: {processed_text['lang']}")
#             st.write("Tokens:", processed_text['tokens'])
#             st.write("Sentences:", processed_text['sentences'])
#             st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
#             st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
#             st.write("Lemmatization:", processed_text['lemmatization'])
#             st.write("Stop Words:", processed_text['stop_words'])
#         else:
#             st.warning("Failed to transcribe audio.")


import streamlit as st
import pandas as pd
import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language
import speech_recognition as sr
import io
import pyaudio

# Initialize Spacy and language detector
nlp = spacy.load('en_core_web_sm')

# Check if the 'language_detector' is already in the pipeline or if the factory exists
if "language_detector" not in nlp.pipe_names:
    if not Language.has_factory("language_detector"):
        @Language.factory("language_detector")
        def get_lang_detector(nlp, name):
            return LanguageDetector()
    nlp.add_pipe("language_detector", last=True)

# Load the dataset
data_path = "Marathi Profanity.xlsx"  # Change this to the path of your Excel file
df = pd.read_excel(data_path)

# Create dictionaries for fast lookup
profane_to_substitute = {}
profane_to_substitute_translit = {}

for _, row in df.iterrows():
    profane_to_substitute[row['Profane Word']] = row['Substitute Word']
    profane_to_substitute_translit[row['Profane Word (English Transliteration)']] = row[
        'Substitute Word (English Transliteration)']

def detect_language(text):
    doc = nlp(text)
    return doc._.language['language']

def replace_profanity(text):
    words = text.split()
    for i, word in enumerate(words):
        if word in profane_to_substitute:
            words[i] = profane_to_substitute[word]
        elif word in profane_to_substitute_translit:
            words[i] = profane_to_substitute_translit[word]
    return ' '.join(words)

def process_text(text):
    lang = detect_language(text)
    doc = nlp(text)

    # Lexical analysis
    lexical_analysis = [(token.text, token.lemma_, token.pos_) for token in doc]

    # Syntactic analysis and Dependency Parsing
    syntactic_analysis = [(token.text, token.dep_, token.head.text) for token in doc]

    # Tokenization and Sentence segmentation
    tokens = [token.text for token in doc]
    sentences = [sent.text for sent in doc.sents]

    # Stemming and Lemmatization
    lemmatization = [token.lemma_ for token in doc]

    # Stop word analysis
    stop_words = [token.text for token in doc if token.is_stop]

    return {
        'lang': lang,
        'tokens': tokens,
        'sentences': sentences,
        'lexical_analysis': lexical_analysis,
        'syntactic_analysis': syntactic_analysis,
        'lemmatization': lemmatization,
        'stop_words': stop_words
    }

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    transcription = ""
    try:
        # Use the uploaded audio file as the audio source
        with sr.AudioFile(audio_file) as source:
            recognizer.adjust_for_ambient_noise(source)
            # Determine the total duration of the audio file
            total_duration = int(source.DURATION)
            offset = 0
            chunk_duration = 30  # Process 30 seconds at a time
            
            while offset < total_duration:
                audio = recognizer.record(source, duration=chunk_duration, offset=offset)
                try:
                    # Recognize speech using Google Web Speech API
                    text = recognizer.recognize_google(audio, language='mr-IN')
                    transcription += text + " "
                except sr.UnknownValueError:
                    transcription += "[Unintelligible] "
                except sr.RequestError as e:
                    transcription += f"[RequestError: {e}] "
                
                offset += chunk_duration
        return transcription
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def record_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.write("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            st.write("Processing...")
            transcription = recognizer.recognize_google(audio, language='mr-IN')
            return transcription
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Streamlit app
st.title("Marathi Text and Audio Processing")

# Select input type
input_type = st.radio("Choose input type:", ("Text", "Upload Audio File", "Record Audio in Real-time"))

if input_type == "Text":
    input_text = st.text_area("Enter your text here:", height=150)

    if st.button("Filter Profanity"):
        if input_text:
            processed_text = process_text(input_text)
            filtered_text = replace_profanity(input_text)

            st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

            st.subheader("NLP Analysis")
            st.write(f"Detected Language: {processed_text['lang']}")
            st.write("Tokens:", processed_text['tokens'])
            st.write("Sentences:", processed_text['sentences'])
            st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
            st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
            st.write("Lemmatization:", processed_text['lemmatization'])
            st.write("Stop Words:", processed_text['stop_words'])
        else:
            st.warning("Please enter some text to filter.")

elif input_type == "Upload Audio File":
    st.write("Upload an audio file (in WAV format) to transcribe it into Marathi text:")

    # Upload audio file
    audio_file = st.file_uploader("Choose a WAV file", type="wav")

    if audio_file is not None:
        st.write("Processing...")
        # Convert uploaded file to a byte stream
        audio_bytes = io.BytesIO(audio_file.read())
        
        # Transcribe audio
        transcription = transcribe_audio(audio_bytes)
        
        if transcription:
            st.subheader("Transcription:")
            st.write(transcription)
            
            # Process the transcribed text
            processed_text = process_text(transcription)
            filtered_text = replace_profanity(transcription)

            st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

            st.subheader("NLP Analysis")
            st.write(f"Detected Language: {processed_text['lang']}")
            st.write("Tokens:", processed_text['tokens'])
            st.write("Sentences:", processed_text['sentences'])
            st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
            st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
            st.write("Lemmatization:", processed_text['lemmatization'])
            st.write("Stop Words:", processed_text['stop_words'])
        else:
            st.warning("Failed to transcribe audio.")

elif input_type == "Record Audio in Real-time":
    if st.button("Start Recording"):
        transcription = record_audio()

        if transcription:
            st.subheader("Transcription:")
            st.write(transcription)

            # Process the transcribed text
            processed_text = process_text(transcription)
            filtered_text = replace_profanity(transcription)

            st.text_area("Filtered Text:", value=filtered_text, height=150, disabled=True)

            st.subheader("NLP Analysis")
            st.write(f"Detected Language: {processed_text['lang']}")
            st.write("Tokens:", processed_text['tokens'])
            st.write("Sentences:", processed_text['sentences'])
            st.write("Lexical Analysis (Token, Lemma, POS):", processed_text['lexical_analysis'])
            st.write("Syntactic Analysis (Token, Dependency, Head):", processed_text['syntactic_analysis'])
            st.write("Lemmatization:", processed_text['lemmatization'])
            st.write("Stop Words:", processed_text['stop_words'])
        else:
            st.warning("Failed to transcribe audio.")
