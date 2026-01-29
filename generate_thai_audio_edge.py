import asyncio
import edge_tts  # Microsoft Edge text-to-speech library
import os

# Voice options: th-TH-NiwatNeural (Male) (used for this project), th-TH-PremwadeeNeural (Female), th-TH-AcharaNeural (Female)
VOICE = "th-TH-NiwatNeural"

FLASHCARDS_FILE = "flashcards.txt"  # Tab-separated: Thai text \t English translation
OUTPUT_DIR = "thai_audio"  # Folder where MP3 files will be saved

async def generate_audio(text, output_file, voice):
    """Generate MP3 audio from Thai text using Edge TTS"""
    try:
        communicate = edge_tts.Communicate(text, voice) 
        await communicate.save(output_file) 
        await asyncio.sleep(0.5)  # Small delay to avoid rate limiting
        return True
    except Exception as e:
        print(f"    Error details: {str(e)}")
        return False

async def main():
    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created folder: {OUTPUT_DIR}")
    
    print("\n" + "=" * 60) 
    print(f"Using Thai Voice: {VOICE}")
    print("=" * 60)
    
    # Read flashcards from file
    print("\nReading flashcards...")
    with open(FLASHCARDS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total = len(lines)
    print(f"Found {total} flashcards.\n")
    print("=" * 60)
    print("Starting audio generation...")
    print("This may take a few minutes...")
    print("=" * 60)
    
    success_count = 0 
    error_count = 0 
    
    # Process each flashcard line
    for i, line in enumerate(lines, 1): 
        parts = line.strip().split('\t')  # Split by tab: [Thai, English]
        if len(parts) < 2:  # Skip malformed lines without both columns
            continue
        
        thai_text = parts[0].strip()  # Extract only the Thai text for audio generation
        
        if not thai_text:  # Skip empty lines
            continue
            
        filename = f"{i:03d}.mp3"  # 001.mp3, 002.mp3, etc.
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Show progress every 10 files
        if i % 10 == 0:
            print(f"\nProgress: {i}/{total} files...")
        
        try:
            success = await generate_audio(thai_text, filepath, VOICE)
            if success:
                success_count += 1
                if i % 10 == 1:  # Show first of each batch of 10
                    print(f"✓ [{i:03d}] {thai_text[:50]}...")
            else:
                error_count += 1
                print(f"✗ [{i:03d}] Failed: {thai_text[:50]}...")
            
        except KeyboardInterrupt:
            print("\n\nStopped by user!")
            break
        except Exception as e:
            print(f"✗ [{i:03d}] Error: {str(e)[:100]}")
            error_count += 1
            continue
    
    # Print final summary
    print("\n" + "=" * 60)
    print(f"✓ COMPLETE!")
    print(f"✓ Success: {success_count} files")
    if error_count > 0:
        print(f"✗ Errors: {error_count} files")
    print(f"✓ Location: {OUTPUT_DIR}/ folder")
    print("=" * 60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nScript stopped by user.")