import cv2
import glob
import os
import tkinter as tk
from tkinter import messagebox


def snapshot():
    '''set to 2 to use external camera'''
    cam = cv2.VideoCapture(0)
    img_format = '.jpg'
    img_quality = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    ret, image = cam.read()
    filename = f"captured_image.jpg"
    cv2.imwrite(filename, image)
    return filename

test = {'close':'too close', 'far':'too far', 'normal':'normal', 'setup':'setup_problem' }

def image_similarity(folder_path, compare_image_path):
    image_paths = {}
    for key in test:
        image_paths[key] = glob.glob(os.path.join(folder_path, key, "*.jpg"))

    template_images = {}
    for key in test:
        template_images[key] = []
        for path in image_paths[key]:
            template_images[key].append(cv2.imread(path))

    gray_image_list = {}
    hist_list = {}
    for key in test:
        gray_image_list[key] = []
        hist_list[key] = []
        for image in template_images[key]:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_image_list[key].append(gray_image)
            hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
            hist_list[key].append(hist)

    compare_image_path = snapshot()
    compare_image = cv2.imread(compare_image_path)
    gray_compare_image = cv2.cvtColor(compare_image, cv2.COLOR_BGR2GRAY)
    hist_compare = cv2.calcHist([gray_compare_image], [0], None, [256], [0, 256])

    similarity_list = {}
    for key in test:
        similarity_list[key] = []
        for hist in hist_list[key]:
            similarity = cv2.compareHist(hist, hist_compare, cv2.HISTCMP_CORREL)
            similarity_list[key].append(similarity)

    max_values = {}
    for key, value in similarity_list.items():
        if value:
            max_values[key] = max(value)

    if not max_values:
        return "No images found for similarity comparison"

    max_similarity_key = max(max_values, key=max_values.get)

    # Get the value from the test dictionary using the key
    return test[max_similarity_key]


def check_similarity():
    global most_similar_label
    most_similar_label = image_similarity(r"C:\Users\USER\Desktop\ex\original", "captured_image.jpg")
    if most_similar_label == 'too close':
        messagebox.showerror("Camera Setup : too close", "Please adjust camera settings and try again.")

    elif most_similar_label == 'far':
        messagebox.showerror("Camera Setup : too far", "Please adjust camera settings and try again.")

    elif most_similar_label == 'normal':
        messagebox.showinfo("Camera Setup Success", "Camera setup is successful.")

    elif most_similar_label == 'setup_problem':
        messagebox.showerror("Camera Setup Problem", "Please adjust camera settings and try again.")

    else:
        messagebox.showerror("No similarity found.", "No similarity found.")


root = tk.Tk()
root.title("Set Up")
root.geometry("400x300")
root.configure(bg='#9ABDA7')

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))



check_button = tk.Button(root, text="Check Current Setup Status", command=check_similarity)
check_button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
