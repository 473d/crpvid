
import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip

# Function to crop the video
def crop_video(input_path, crop_x, crop_y, width, height):
    video = VideoFileClip(input_path)
    cropped_video = video.crop(x1=crop_x, y1=crop_y, x2=crop_x + width, y2=crop_y + height)
    output_path = input_path.replace(".mp4", "_cropped.mp4")
    cropped_video.write_videofile(output_path, codec="libx264")
    print(f"Cropped video saved to {output_path}")

# Function to let the user select the crop area
def select_crop_area(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Failed to read video")
        return None

    r = cv2.selectROI("Select Crop Area", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    cap.release()

    return r

# Function to handle file selection dialog
def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        main(file_path)

# Main function
def main(input_video_path):
    crop_area = select_crop_area(input_video_path)
    if crop_area:
        crop_x, crop_y, width, height = crop_area
        crop_video(input_video_path, crop_x, crop_y, width, height)

# Example usage
select_video_file()



"""



import cv2
from moviepy.editor import VideoFileClip
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.video import Video
from kivy.uix.popup import Popup
import os

class VideoCropperApp(App):
    def build(self):
        self.file_chooser = FileChooserListView()
        self.crop_button = Button(text="Crop Video", size_hint=(1, 0.1))
        self.crop_button.bind(on_press=self.crop_button_pressed)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.file_chooser)
        layout.add_widget(self.crop_button)

        return layout

    def crop_button_pressed(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            video_path = selected_file[0]
            crop_area = self.select_crop_area(video_path)
            if crop_area:
                crop_x, crop_y, width, height = crop_area
                self.crop_video(video_path, crop_x, crop_y, width, height)

    def select_crop_area(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        if not ret:
            print("Failed to read video")
            return None

        r = cv2.selectROI("Select Crop Area", frame, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()
        cap.release()

        return r

    def crop_video(self, input_path, crop_x, crop_y, width, height):
        video = VideoFileClip(input_path)
        cropped_video = video.crop(x1=crop_x, y1=crop_y, x2=crop_x + width, y2=crop_y + height)
        output_path = input_path.replace(os.path.basename(input_path), "") + "cropped_" + os.path.basename(input_path)
        cropped_video.write_videofile(output_path, codec="libx264")
        print(f"Cropped video saved to {output_path}")

        # Show a popup with the output path
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=f"Cropped video saved to:\n{output_path}"))

        popup = Popup(title='Video Cropped', content=popup_content, size_hint=(0.6, 0.6))
        popup.open()

if __name__ == '__main__':
    VideoCropperApp().run()

"""




