from PIL import Image
import os


def check_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except Exception as e:
        print(f"损坏文件: {file_path} - {str(e)}")
        return False


data_dir = r"D:\A_Projects\0_Thesis_Programs\LLIE\EnlightenGAN\raw_train_dataset\trainA"
for root, _, files in os.walk(data_dir):
    for file in files:
        check_image(os.path.join(root, file))
