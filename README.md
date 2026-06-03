# Spectrogram
Quick tool that converts a .wav file to a spectrogram. 
# WAV Spectrogram Generator

## Overview
This Python script generates spectrograms from WAV audio files and saves them as high-quality PDF images. A spectrogram is a visual representation of the frequency spectrum of a signal as it varies with time, useful for analyzing audio characteristics and patterns.

## Features
- **Audio Loading**: Reads WAV files using SciPy's audio I/O capabilities
- **Stereo to Mono Conversion**: Automatically converts stereo audio to mono for analysis
- **Spectrogram Generation**: Creates a spectrogram using SciPy's signal processing
- **Power Visualization**: Displays power levels in decibels (dB) using a color-coded visualization
- **High-Quality Output**: Saves spectrograms as PDF files at 300 DPI resolution
- **Error Handling**: Includes validation to detect corrupted or unsupported audio formats

## Requirements
- Python 3.14.3+
- Required Libraries:
  - `scipy`: For WAV file I/O and signal processing
  - `matplotlib`: For data visualization and plotting
  - `numpy`: For numerical array operations

## Installation
1. Ensure you have Python 3.14.3 installed
2. Install required packages using pip:
   ```bash
   pip install scipy matplotlib numpy
   ```

## Usage
1. Update the `audio_file` path in the script to point to your WAV file:
   ```python
   audio_file = '/path/to/your/audio.wav'
   ```

2. Run the script:
   ```bash
   python wav_spectrogram.py
   ```

3. The script will:
   - Load the audio file and display sample rate and duration
   - Convert stereo audio to mono if needed
   - Generate a spectrogram visualization
   - Save the spectrogram as `spectrogram.pdf`
   - Display the plot in a window

## Output
- **PDF File**: `spectrogram.pdf` - High-resolution spectrogram image
- **Console Output**: Sample rate, duration, and processing status messages

## How It Works
1. **Audio Loading**: Reads the WAV file and extracts sample rate and audio data
2. **Data Validation**: Checks that data is a valid NumPy array
3. **Channel Conversion**: Converts stereo to mono by averaging channels if necessary
4. **Spectrogram Calculation**: Uses Short-Time Fourier Transform (STFT) to compute frequency content over time
5. **Visualization**: Creates a color-coded plot where:
   - X-axis represents time (seconds)
   - Y-axis represents frequency (Hz)
   - Color intensity represents power in decibels (dB)
6. **File Export**: Saves the visualization as a PDF with high resolution

## Visualization Details
- **Color Map**: Uses 'viridis' colormap (perceptually uniform, colorblind-friendly)
- **Power Scale**: Logarithmic scale (dB) with noise floor at -40 dB for clarity
- **Resolution**: 300 DPI for crisp, publication-quality output
- **Figure Size**: 12x6 inches for optimal visualization

## Troubleshooting
- **TypeError - Audio file corrupted**: The audio file may be in an unsupported format or corrupted. Try converting it to WAV format.
- **FileNotFoundError**: Verify the audio file path is correct and the file exists.
- **Module import errors**: Ensure all required packages are installed in your Python environment.
