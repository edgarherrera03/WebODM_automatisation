from PIL import Image
import os
import cv2 as cv
import numpy as np


def converter(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGBA mode (if not already)
        img = img.convert("RGBA")

        # Create a new image with a white background
        background = Image.new("RGBA", img.size, (255, 255, 255))

        # Composite the original image on top of the white background
        result = Image.alpha_composite(background, img)

        # Convert the image back to RGB mode (if needed)
        result = result.convert("RGB")
        jpeg_path = os.path.splitext(image_path)[0] + '.jpg'
        result.convert("RGB").save(jpeg_path, "JPEG")
        result.save(jpeg_path)
        return jpeg_path


def isPixelEqual(pixel1, pixel2):
    epsilon = 10
    if abs(pixel1[0]-pixel2[0])<=epsilon and abs(pixel1[1]-pixel2[1])<=epsilon and abs(pixel1[2]-pixel2[2])<=epsilon:
        return True
    else:
        return False


def crop_and_resize(image_path):
    # Open the image
    img = cv.imread(image_path)
    height, width = img.shape[:2]
    #crop the top
    found, y_top = False, 0
    for y in range(height):    
        for x in range(width):
            if not isPixelEqual(img[y,x], [255, 255, 255]):
                found = True
                break
        if found:
            y_top = y
            break
    #crop the bottom
    found, y_bottom = False, 0
    for y in range(height-1, -1, -1):    
        for x in range(width):
            if not isPixelEqual(img[y,x], [255, 255, 255]):
                found = True
                break
        if found:
            y_bottom = y
            break
    #crop the left
    found, x_left = False, 0
    for x in range(width):    
        for y in range(height): 
            if not isPixelEqual(img[y,x], [255, 255, 255]):
                found = True
                break
        if found:
            x_left = x
            break
    #crop the right
    found, x_right = False, 0
    for x in range(width-1, -1, -1):    
        for y in range(height): 
            if not isPixelEqual(img[y,x], [255, 255, 255]):
                found = True
                break
        if found:
            x_right = x
            break
    cropped_image = img[y_top+5:y_bottom-5, x_left+5:x_right-5]
    cv.imwrite('./Resultats/resultat_final.jpg', cropped_image)
    return('./Resultats/resultat_final.jpg')

def distance_between_pixels(pixel1, pixel2):
    x1, y1 = pixel1
    x2, y2 = pixel2
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def find_points(image):
    #Find left point
    point1= None
    height, width = image.shape[:2]
    for y in range(height):
        if isPixelEqual(image[y, 0], [255, 255, 255]):
            continue
        else: 
            point1 = (0, y)
            break
    #Find bottom left point 
    point2 = None
    for x in range(width):
        if isPixelEqual(image[height-1, x], [255, 255, 255]):
            continue
        else: 
            point2 = (x, height-1)
            break
    point3 = None
    for y in range(height-1, -1, -1):
        if isPixelEqual(image[y, width-1], [255, 255, 255]):
            continue
        else: 
            point3 = (width-1, y)
            break
    point4 = None
    for x in range(width):
        if isPixelEqual(image[0, x], [255, 255, 255]):
            continue
        else: 
            point4 = (x, 0)
            break

    width, height = distance_between_pixels(point1, point2), distance_between_pixels(point1, point4)

    # Calculer les dimensions du rectangle
    new_height, new_width = int(height), int(width)
    
    # Définir les coins du rectangle
    pts1 = np.float32([point1, point2, point3, point4])
    pts2 = np.float32([[0, 0], [new_width - 1, 0], [new_width - 1, new_height - 1], [0, new_height - 1]])

    # Calculer la matrice de transformation pour effectuer la perspective
    matrix = cv.getPerspectiveTransform(pts1, pts2)

    # Appliquer la transformation perspective
    result = cv.warpPerspective(image, matrix, (new_width, new_height))

    # Afficher le résultat
    cv.imwrite("./Resultats/resultat_final.jpg", result)

def draw_rectangle(image_path):
    path = converter(image_path)
    pathToStitch = crop_and_resize(path)
    image = cv.imread(pathToStitch)
    find_points(image)
    
if __name__ == "__main__":
    image_path = "orthophoto.png"
    draw_rectangle(image_path)
