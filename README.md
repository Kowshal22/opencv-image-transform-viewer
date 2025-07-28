# Image Processing Viewer - OpenCV
This project demonstrates basic image transformations using OpenCV, with support for both static image processing and real-time webcam feeds. It uses a custom image-stacking utility for easy visualization of multiple processing stages.
## Features
- Read and process static images or live webcam feed.
- Apply key transformations:
  - Grayscale
  - Gaussian Blur
  - Canny Edge Detection
  - Dilation
  - Erosion
- Stack multiple image outputs into a single display for comparison.
- Modular `util1.py` with a flexible `stackImages()` utility function.
## File Structure
- version1_static_image.py
- version2_webcam.py
- util1.py
## Requirements
- Python 3.13
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
## Credits
Built with ❤️ using OpenCV and NumPy.







