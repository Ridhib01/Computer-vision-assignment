# Computer Vision Assignment
> **Sample image:** The assignment outputs in this repository were generated from the provided real-world `sample.jpg` (mountain forest photograph).

Complete solutions for the **25 Python + OpenCV coding questions** in the provided assignment.

## Topics covered
- Basic image handling
- Pixel and image representation
- Sampling and quantization
- Geometric operations

## Requirements
```bash
pip install -r requirements.txt
```
Recommended: Python 3.10+.

## Project structure
```text
computer-vision-day1-assignment/
├── README.md
├── requirements.txt
├── sample.jpg
├── run_all.py
├── solutions/
│   ├── q01.py
│   ├── ...
│   └── q25.py
└── outputs/
    ├── q01_output.png
    ├── ...
    └── q25_output.png
```

## Q1–Q25
1. Read and display image using OpenCV.
2. Check whether an image loaded successfully.
3. Print height, width, and number of channels.
4. Calculate total number of pixels.
5. Print image matrix data type.
6. Save image with another filename.
7. Read image directly in grayscale.
8. Convert a color image to grayscale.
9. Display image using Matplotlib and hide axis.
10. Resize image to 50% width and height.
11. Access a pixel at a coordinate.
12. Modify a selected pixel and save.
13. Print B, G, R values of a selected pixel.
14. Split image into B, G, R channels.
15. Merge three image channels.
16. Find minimum and maximum grayscale intensity.
17. Calculate mean grayscale intensity.
18. Calculate mean and standard deviation.
19. Create a 256×256 grayscale image with intensity 128.
20. Create a grayscale intensity ramp from 0 to 255.
21. Convert an 8-bit grayscale image to 4-bit quantization.
22. Convert an 8-bit grayscale image to 2-bit quantization.
23. Downsample image by factor 2.
24. Crop a rectangular ROI.
25. Rotate image by 90 degrees and save.

## Viva quick points
- OpenCV normally reads images in **BGR** order.
- `image.shape` for a color image is `(height, width, channels)`.
- A grayscale image normally has one intensity value per pixel from 0 to 255.
- NumPy image indexing is `[row, column]`, equivalent to `[y, x]`.
- 4-bit quantization gives 16 intensity levels; 2-bit gives 4.
- Downsampling reduces spatial resolution; quantization reduces intensity resolution.
- Cropping is performed efficiently using NumPy slicing.
