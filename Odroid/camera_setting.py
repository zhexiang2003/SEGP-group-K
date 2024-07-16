import cv2
import glob
import os

test = {'close':'too close', 'far':'too far', 'normal':'nomal', 'setup':'setup problem'}

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
    for key, value in similarity_list.items() :
        max_values[key] = max(value)

    max_similarity_key = max(max_values, key=max_values.get)

    # Get the value from the test dictionary using the key
    return test[max_similarity_key]