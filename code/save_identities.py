import numpy as np
import argparse
import json
from scipy.misc import imread
import cv2

def main(desc_path):
    json_str_messages = np.load(desc_path)
    json_messages = [json.loads(message) for message in json_str_messages]
    images = []
    digit_classes = []
    for video_message in json_messages:
        digit_messages = filter(lambda x: x['type'] == 'digit', video_message)
        if len(digit_messages) != 1:
            print('Number of digits in %s is not one, skipping' % desc_path)
            return
        digit_image = imread(digit_messages[0]['meta']['image_path'])
        # Pad the image to make it 64x64
        digit_image_padded = cv2.copyMakeBorder(digit_image, 18, 18, 18, 18, cv2.BORDER_CONSTANT, value=0)
        digit_class = digit_messages[0]['meta']['label']
        images.append(digit_image_padded)
        digit_classes.append(digit_class)
    images = np.stack(images, axis=0)
    digit_classes = np.array(digit_classes, dtype=np.uint8)
    out_path = desc_path.replace('_messages.npy', '_identities')
    np.savez(out_path, images=images, digit_classes=digit_classes)
    print('Saved identities to %s' % desc_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('desc_path', type=str, help='Path to the *_messages.npy file')
    args = parser.parse_args()

    main(**vars(args))