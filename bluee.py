import time
import pygame
import tkinter as tk


class LyricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyrics Player")

        self.text = tk.Text(root, font=("Brass Mono Regular", 14), bg="black", fg="white", padx=20, pady=20)
        self.text.pack(expand=True, fill='both')
        self.text.config(state='disabled')

        self.lyrics = [
            (19.12, "Your morning eyes, I could stare like watching stars"),
            (26.55, "I could walk you by and I'll tell without a thought"),
            (33.00, "You'll be mine would you mind, If I took your hand tonight"),
            (40.56, "Know you're all that I want this life"),
            (45.00, ""),
            (46.00, ""),
            (48.46, "I'll imagine we fell in love"),
            (51.29, "I'll nap under moonlight skies with you"),
            (55.14, "I think I'll picture us, you with the waves"),
            (58.66, "The ocean's colors on your face"),
            (62.55, "I'll leave my heart with your air"),
            (66.94, "So let me fly with you"),
            (70.56, "Will you be forever with me?"),
            (71.00, ""),
            (76.72, ""),
            (107.42, "My love will always stay by you"),
            (113.34, "I'll keep it safe so, Don't you worry a thing"),
            (118.42, "I'll tell you I love you more"),
            (122.17, "It's stuck with you forever, So promise you won't let it go"),
            (128.93, "I'll trust the universe Will always bring me to you"),
            (129.00, ""),
            (135.00, ""),
            (136.82, "I'll imagine we fell in love"),
            (139.86, "I'll nap under moonlight skies with you"),
            (143.52, "I think I'll picture us, you with the waves"),
            (147.21, "The ocean's colors on your face"),
            (149.15, "I'll leave my heart with your air"),
            (151.94, "So let me fly with you"),
            (159.02, "Will you be forever with me?")
        ]
        self.lyric_index = 0
        self.song_start_time = None

        pygame.mixer.init()
        pygame.mixer.music.load("song.mp3")
        pygame.mixer.music.play()
        self.song_start_time = time.time()

        self.root.after(100, self.update_lyrics)

    def typewriter_effect(self, content, index=0, delay=70):
        if index == 0:
            self.text.config(state='normal')

        if index < len(content):
            self.text.insert('end', content[index])
            self.text.see('end')
            self.root.update()
            self.root.after(delay, self.typewriter_effect, content, index + 1)
        else:
            self.text.insert('end', '\n')
            self.text.config(state='disabled')
            self.lyric_index += 1
            self.root.after(100, self.update_lyrics)

    def update_lyrics(self):
        if self.lyric_index >= len(self.lyrics):
            self.root.after(1500, self.print_heart)
            return

        timestamp, line = self.lyrics[self.lyric_index]
        current_time = time.time() - self.song_start_time

        if current_time >= timestamp:
            self.typewriter_effect(line)
        else:
            self.root.after(100, self.update_lyrics)

    def print_heart(self, line_index=0):
        heart_shape = [
            "   ***     ***   ",
            " ******* ******* ",
            "*****************",
            "*****************",
            " ****************",
            "  ************** ",
            "   ************  ",
            "    **********   ",
            "     ********    ",
            "      ******     ",
            "       ****      ",
            "        **       "
        ]
        if line_index < len(heart_shape):
            self.typewriter_effect(heart_shape[line_index], delay=50)
            self.root.after(400, self.print_heart, line_index + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsApp(root)
    root.mainloop()
