import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw
import tensorflow as tf
import matplotlib.pyplot as plt

# Tải mô hình đã lưu
model = tf.keras.models.load_model("mnist_digit_model.h5")

# Hàm dự đoán chữ viết tay từ ảnh vẽ
def predict_digit(img):
    img = img.resize((28, 28)).convert("L")  # Chuyển ảnh về 28x28 pixel và thang xám
    img = np.array(img) / 255.0              # Chuẩn hóa giá trị pixel
    img = img.reshape(1, 28, 28)             # Chuyển thành định dạng phù hợp cho mô hình
    prediction = model.predict(img)
    print(prediction)
    return np.argmax(prediction)

# Lớp ứng dụng Tkinter
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dự đoán chữ viết tay")
        self.geometry("400x400")

        self.canvas = tk.Canvas(self, width=280, height=280, bg="white")
        self.canvas.pack(pady=20)

        self.button_predict = tk.Button(self, text="Dự đoán", command=self.predict)
        self.button_predict.pack()

        self.button_clear = tk.Button(self, text="Xóa", command=self.clear_canvas)
        self.button_clear.pack()

        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)

    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        r = 8  # Kích thước bút vẽ
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="black")

    def predict(self):
        # Hiển thị ảnh input
        self.show_image()

        # Dự đoán
        digit = predict_digit(self.image)
        messagebox.showinfo("Kết quả", f"Số được dự đoán: {digit}")

    def show_image(self):
        img_array = np.array(self.image.resize((28, 28)).convert("L"))
        plt.imshow(img_array, cmap="gray")
        plt.title("Ảnh người dùng vẽ")
        plt.axis("off")
        plt.show()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    app = App()
    app.mainloop()
