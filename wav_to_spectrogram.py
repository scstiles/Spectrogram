import scipy.io.wavfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Load audio
audio_file = '/Users/Jo/Desktop/Python codes/Spectrogram/Stick_shifts.wav'
sr, data = sf.read(audio_file)

# Ensure data is a numpy array
if not isinstance(data, np.ndarray):
    raise TypeError(f"Expected numpy array, got {type(data).__name__}. Audio file may be corrupted or in an unsupported format.")

print(f"Audio loaded: Sample rate = {sr} Hz, Duration = {len(data)/sr:.2f} seconds")

# Handle stereo audio (convert to mono if needed)
if len(data.shape) > 1:
    data = np.mean(data, axis=1)
    print("Converted stereo audio to mono")

# Create spectrogram
f, t, Sxx = signal.spectrogram(data, sr)
plt.figure(figsize=(12, 6))
plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='viridis')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram')
plt.colorbar(label='Power [dB]')

# Save as PDF
pdf_file = 'spectrogram.pdf'
plt.savefig(pdf_file, format='pdf', dpi=300, bbox_inches='tight')
print(f"Spectrogram saved as {pdf_file}")

# Display the plot
plt.show()