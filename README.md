# thai-flashcard-audio-generator
Generates Thai audio for flashcards using Edge TTS

## What It Does
Takes my flashcard file and creates audio pronunciations for each Thai sentence.

## Setup
**Install edge-tts:**
```bash
pip install edge-tts
```

## How to Use
1. Make sure `flashcards.txt` is in the same folder as the script
   - Format: Thai text [TAB] English translation
   
2. Run it:
```bash
   python generate_thai_audio_edge.py
```

3. MP3 files appear in `thai_audio/` folder (001.mp3, 002.mp3, etc.)

## Voices
I'm using the male voice 'th-TH-NiwatNeural' (male). To switch:
- Open the script
- Line 6: Change `VOICE = "th-TH-NiwatNeural"` to:
  - `th-TH-PremwadeeNeural` (Female)
  - `th-TH-AcharaNeural` (Female)

## Notes
- Takes about 5 minutes for about 200 flashcards
- Flashcards must be tab-separated (not spaces!)

## Files in This Project
- `flashcards.txt` - Flashcards
- `generate_thai_audio_edge.py` - The script
- `thai_audio/` - Generated MP3s (193 files)
