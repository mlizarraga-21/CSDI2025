import os
import soundfile as sf

def convert_ogg_to_mp3(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all .ogg files in the input folder
    ogg_files = [f for f in os.listdir(input_folder) if f.endswith('.ogg')]

    if not ogg_files:
        print("No .ogg files found in the input folder.")
        return

    for ogg_file in ogg_files:
        try:
            # Define full input and output file paths
            ogg_path = os.path.join(input_folder, ogg_file)
            mp3_file_name = os.path.splitext(ogg_file)[0] + ".mp3"
            mp3_path = os.path.join(output_folder, mp3_file_name)

            # Read and write audio data using soundfile
            data, samplerate = sf.read(ogg_path)
            sf.write(mp3_path, data, samplerate, format="MP3")
            print(f"Converted: {ogg_file} -> {mp3_file_name}")

        except Exception as e:
            print(f"Failed to convert {ogg_file}: {e}")

if __name__ == "__main__":
    input_folder = r'C:\Users\lizar\OneDrive\Escritorio\Audio'
    output_folder = r'C:\Users\lizar\OneDrive\Escritorio\Audiomp3'

    convert_ogg_to_mp3(input_folder, output_folder)
