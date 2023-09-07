# SCANet: Real-Time_Face_Parsing_Using_Spatial_and_Channel_Attention
The official repository of [__"SCANet: Real-Time Face Parsing Using Spatial and Channel Attention"__](https://ieeexplore.ieee.org/document/10202537/metrics#metrics), presented at the 2023 20th International Conference on Ubiquitous Robots (UR).

<br>
<hr>

## Abstract
This paper presents a real-time face parsing method that is efficient and robust to small facial components. The proposed approach utilizes two separate attention networks, namely the Spatial and Channel Attention Networks (SCANet), to integrate local features with global dependencies and focus on the most critical contextual features. Specifically, the Spatial attention module (SAM) captures the spatial relationships between different facial features, while the Channel attention module (CAM) identifies important features within each channel of the feature map, such as skin texture or eye color. Moreover, an edge detection branch, which helps differentiate edge and non-edge pixels, is added to improve segmentation precision along edges. To address class imbalance issues, which arise from limited data on accessories such as necklaces and earrings, we utilize a weighted cross-entropy loss function that assigns higher weights to rare classes. The proposed method outperforms state-of-the-art methods on the CelebAMask-HQ dataset, especially in small facial classes like necklaces and earrings. Additionally, the model is designed to operate in real-time, making it a promising solution for various face recognition and analysis applications.

<br>

![그림1](https://github.com/Seungeun-Han/SCANet_Real-Time_Face_Parsing_Using_Spatial_and_Channel_Attention/assets/101082685/1707c784-812d-42cf-84fd-5e0a91ca6572)

<br>
<hr>

## ✨ Demo coming soon! ✨
We will be with you as quickly as possible! 
 
<br>
<hr>

## Visualization
The comparison of our face parsing results to those of the previous state-of-the-art model, DML CSR, which was developed by [Zheng et al.](https://arxiv.org/pdf/2203.14448.pdf). (a) is the original image, (b) is the ground-truth of the corresponding image., (c) is the result of DML CSR, and (d) is result of our models. Our approach effectively enables more detailed segmentation of rare facial components, particularly in the case of necklaces.

![10202537-fig-2-source-small](https://github.com/Seungeun-Han/SCANet_Real-Time_Face_Parsing_Using_Spatial_and_Channel_Attention/assets/101082685/b7537719-26d8-4669-b990-e8303cbc0ed6)

<br>
<hr>

## ✨ Application ✨
We have developed a Face Parsing network that operates in __real-time__ on desktop and Android devices.

### DeskTop
coming soon ..

### Android
coming soon ..

<br>
<hr>

## Dataset
### CelebAMask-HQ

You can download this dataset at [here](https://github.com/switchablenorms/CelebAMask-HQ).

And make that folder construct as below:

```
./CelebAMask
    |---test
    |---train
        |---images
            |---00000.jpg
            |---00001.jpg
        |---labels
            |---00000.png
            |---00001.png
        |---edges
            |---00000.png
            |---00001.png
    |---valid
    |---label_names.txt
    |---test_list.txt
    |---train_list.txt
        |---'images/00000.jpg labels/00000.png'
        |---'images/00001.jpg labels/00001.png'
    |---valid_list.txt
```

You can make train/valid/test_list.txt file through [this](https://github.com/Seungeun-Han/Face-Parsing-Preprocessing/blob/main/Write_TXT_List.py) code.

<br>
<hr>

## Pre-Processing
### 1. Make Label Images

You can make labels of CelebAMask-HQ Dataset through [this](https://github.com/Seungeun-Han/Face-Parsing-Preprocessing/blob/main/make_groundtruth_fast.py) code.
And you have to change below "Path".

```
IMAGE_PATH = '$Your Data path$/CelebAMask-HQ/CelebA-HQ-img/'
ANNOTATIOM_PATH = '$Your Data path$/CelebAMask-HQ/CelebAMask-HQ-mask-anno_acc'
SAVE_PATH = "$The path where you want to save$"
INPUT_SIZE = $input size$
```

### 2. Make Edge Images

You can make edges of CelebAMask-HQ Dataset through [this](https://github.com/Seungeun-Han/Face-Parsing-Preprocessing/blob/main/generate_edges_agrnet_2.py) code.
And you have to change below "Path".

```
generate_edge("$Your Label Path$", "The path where you want to save")
```

And the other extra pre-processing codes are [here](https://github.com/Seungeun-Han/Face-Parsing-Preprocessing).

### Example

<img width="363" alt="2" src="https://github.com/Seungeun-Han/SCANet_Real-Time_Face_Parsing_Using_Spatial_and_Channel_Attention/assets/101082685/c724f802-d1b1-4865-bfa0-db6db7433e45">

The labels and edge images seen here have been multiplied by 10 and 255, respectively, for easier viewing.

<br>
<hr>

## Result
We've got the state-of-the-art methods on the CelebAMask-HQ dataset, especially in small facial classes like necklaces and earrings.

![10202537-table-1-source-large](https://github.com/Seungeun-Han/SCANet_Real-Time_Face_Parsing_Using_Spatial_and_Channel_Attention/assets/101082685/24042146-1b9b-452a-aec5-9d24668b7a4a)

<br>
<hr>

## Citation
```
@INPROCEEDINGS{10202537,
  author={Han, Seungeun and Yoon, Hosub},
  booktitle={2023 20th International Conference on Ubiquitous Robots (UR)}, 
  title={SCANet: Real-Time Face Parsing Using Spatial and Channel Attention}, 
  year={2023},
  volume={},
  number={},
  pages={13-18},
  doi={10.1109/UR57808.2023.10202537}}
```

