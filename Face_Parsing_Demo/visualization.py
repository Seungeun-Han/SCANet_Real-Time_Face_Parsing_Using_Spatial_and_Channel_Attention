import os
import cv2
import numpy as np

"""LABELS = {'bg': 0, 'skin': 1, 'nose': 2, 'eye_g': 3, 'l_eye': 4, 'r_eye': 5,
        'l_brow': 6, 'r_brow': 7, 'l_ear': 8, 'r_ear': 9, 'mouth': 10, 'u_lip': 11,
        'l_lip': 12, 'hair': 13, 'hat': 14, 'ear_r': 15, 'neck_l': 16, 'neck': 17, 'cloth': 18, 'mask': 19}"""
LABELS = {'bg': 0, 'skin': 1, 'nose': 2, 'eye_g': 3, 'l_eye': 4, 'r_eye': 5,
        'l_brow': 6, 'r_brow': 7, 'l_ear': 8, 'r_ear': 9, 'mouth': 10, 'u_lip': 11,
        'l_lip': 12, 'hair': 13, 'hat': 14, 'ear_r': 15, 'neck': 16, 'cloth': 17, 'neck_l': 18, 'mask': 19, 'hand': 20, 'scarf': 21}

#def vis_parsing_maps(im, parsing_anno, stride, save_im=False, save_path='vis_results/parsing_map_on_im.jpg'):
def visualization(im, parsing_anno, stride=1, save_im=False, save_path = None, num_of_class = 20):
    # Colors for all 20 parts
    """part_colors = [[0, 0, 0, 150], [255, 85, 0, 150], [255, 170, 0, 150],  # background, skin, nose
                   [255, 0, 85, 150], [255, 0, 170, 150],  # glasses, left_eye
                   [0, 255, 0, 150], [204, 255, 0, 150], [0, 102, 153, 150],  # right_eye, left_brow, r_brow
                   [0, 255, 85, 150], [255, 190, 190, 150], # left_ear, right_ear
                   [0, 0, 255, 150], [85, 10, 255, 150], [255, 0, 255, 150],  # mouth, upper_lip, lower_lip
                   [0, 85, 255, 150], [0, 170, 255, 150], # hair, hat
                   [255, 255, 0, 150], [255, 255, 85, 150], [255, 255, 170, 150], # ear_ring, necklace, neck
                   [255, 0, 255, 150],[153, 255, 0, 150]] #23개=>19개로 수정    # cloth, mask """

    part_colors = [[0, 0, 0, 150], [255, 0, 0, 150], [255, 170, 0, 150],  # background, skin, nose
                   [0, 0, 255, 150], [255, 255, 0, 150], [0, 255, 255, 150],  # glasses, left_eye, right_eye
                   [255, 0, 255, 150], [255, 255, 170, 150],  # left_brow, r_brow
                   [255, 170, 255, 150], [170, 255, 255, 150],  # left_ear, right_ear
                   [170, 170, 255, 150], [170, 255, 170, 150], [255, 170, 170, 150],  # mouth, upper_lip, lower_lip
                   [0, 85, 255, 150], [0, 102, 153, 150],  # hair, hat
                   [85, 255, 0, 150], [85, 0, 255, 150], [85, 255, 255, 150],  # ear_ring, necklace, neck
                   [255, 0, 85, 150], [153, 255, 0, 150], [255, 190, 190, 150], [204, 255, 0, 150]]  # cloth, mask


    im = np.array(im)
    vis_im = im.copy().astype(np.uint8)
    vis_parsing_anno = parsing_anno.copy().astype(np.uint8)
    vis_parsing_anno = cv2.resize(vis_parsing_anno, None, fx=stride, fy=stride, interpolation=cv2.INTER_NEAREST)
    vis_parsing_anno_color = np.zeros((vis_parsing_anno.shape[0], vis_parsing_anno.shape[1], 4)) + 255 #473,473,3 흰색 바탕


    for pi in range(0, num_of_class):
        index = np.where(vis_parsing_anno == pi) #각 클래스에 해당하는 부분 추가.
        vis_parsing_anno_color[index[0], index[1], :] = part_colors[pi]

    vis_parsing_anno_color = vis_parsing_anno_color.astype(np.uint8)

    vis_im = cv2.addWeighted(cv2.cvtColor(vis_im, cv2.COLOR_BGR2BGRA), 0.6, vis_parsing_anno_color, 0.4, 0,dtype=cv2.CV_32F) #원본이미지에 합성
    vis_parsing_anno_num = vis_parsing_anno.max(axis=0)
    #cv2.imshow('vis_im',vis_im)
    #cv2.waitkey(0)
    # Save result or not
    if save_im:
        cv2.imwrite(save_path[:-4] +'.png', vis_parsing_anno_num)
        cv2.imwrite(save_path, vis_im, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    # print(vis_im.shape)  # (256, 256, 4)
    vis_im = cv2.cvtColor(vis_im, cv2.COLOR_BGRA2RGB)
    vis_im = np.uint8(vis_im)
    # print(vis_im.shape)
    return vis_im
