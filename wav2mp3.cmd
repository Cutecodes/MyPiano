for /R %v IN (./source/*.wav) do ( ffmpeg -i "mp3source/\%~na.mp3")
