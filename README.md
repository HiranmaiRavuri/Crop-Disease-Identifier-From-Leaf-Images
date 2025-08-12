# 🌱 Crop Disease Detection System 🌱

A simplified Flask-based web application that uses deep learning to detect plant diseases from images. This project focuses solely on disease detection functionality, making it easy to deploy and use.

## 🚀 Features

- **AI-Powered Disease Detection**: Uses a pre-trained ResNet9 model to identify 38 different plant diseases
- **User-Friendly Interface**: Simple web interface for uploading and analyzing plant images
- **Detailed Results**: Provides comprehensive disease information and treatment recommendations
- **Responsive Design**: Works on desktop and mobile devices
- **Fast Processing**: Quick image analysis and results

## 📋 Supported Crops and Diseases

The system can detect diseases in the following crops:
- **Apple**: Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry**: Healthy
- **Cherry**: Powdery Mildew, Healthy
- **Corn (Maize)**: Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Grape**: Black Rot, Black Measles, Leaf Blight, Healthy
- **Orange**: Citrus Greening
- **Peach**: Bacterial Spot, Healthy
- **Pepper**: Bacterial Spot, Healthy
- **Potato**: Early Blight, Late Blight, Healthy
- **Raspberry**: Healthy
- **Soybean**: Healthy
- **Squash**: Powdery Mildew
- **Strawberry**: Leaf Scorch, Healthy
- **Tomato**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy

## 📁 Project Structure

```
crop-disease-detection/
├── README.md                      # This documentation file
├── disease_detection_app.py       # Main Flask application
├── disease_requirements.txt       # Python dependencies
├── run_disease_detection.py       # Smart startup script
├── models/
│   └── plant_disease_model.pth    # Pre-trained disease detection model
├── utils/
│   ├── model.py                   # ResNet9 model architecture
│   └── disease.py                 # Disease information dictionary
├── templates/
│   ├── index_disease.html         # Home page
│   ├── disease.html               # Upload page
│   └── disease_result_simple.html # Results page
├── static/
│   ├── css/                       # Stylesheets
│   └── images/                    # Images
└── test_disease_images/           # Sample test images
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   # Make sure you have these files in your project directory:
   # - disease_detection_app.py
   # - disease_requirements.txt
   # - utils/ (folder with model.py and disease.py)
   # - models/ (folder with plant_disease_model.pth)
   # - templates/ (folder with HTML templates)
   ```

2. **Install dependencies**
   ```bash
   pip install -r disease_requirements.txt
   ```

3. **Run the application**
   ```bash
   python run_disease_detection.py
   ```

4. **Access the application**
   - Open your web browser
   - Go to `http://localhost:5000`
   - Start detecting plant diseases!

## 🎯 How to Use

1. **Home Page**: Visit the application homepage
2. **Upload Image**: Click "Start Detection" and upload a photo of your plant
3. **Analysis**: The AI will analyze the image and detect any diseases
4. **Results**: View detailed information about the detected disease and treatment recommendations

## 🔧 Technical Details

### Model Architecture
- **Model**: ResNet9 (Custom ResNet implementation)
- **Input**: RGB images (256x256 pixels)
- **Output**: 38-class classification (diseases + healthy)
- **Framework**: PyTorch

### Dependencies
- Flask 1.1.4 - Web framework
- PyTorch - Deep learning framework
- Torchvision - Computer vision utilities
- Pillow - Image processing
- NumPy - Numerical computing
- Markupsafe - HTML escaping

## 🚀 Deployment

### Local Development
```bash
python disease_detection_app.py
```

### Production Deployment
For production deployment, consider using:
- Gunicorn (WSGI server)
- Nginx (Reverse proxy)
- Docker (Containerization)

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 disease_detection_app:app
```

## 🐛 Troubleshooting

### Common Issues

1. **Model not found error**
   - Ensure `models/plant_disease_model.pth` exists in your project directory

2. **Import errors**
   - Make sure all dependencies are installed: `pip install -r disease_requirements.txt`

3. **Port already in use**
   - Change the port in `disease_detection_app.py` or kill the process using the port

4. **Memory issues**
   - The model requires sufficient RAM to load. Close other applications if needed.

### Performance Tips
- Use GPU if available for faster inference
- Optimize image size before upload
- Consider model quantization for deployment

## 📝 License

This project is for educational and research purposes. Please ensure you have proper licenses for any commercial use.

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding support for more crops/diseases

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section
2. Review the error messages
3. Ensure all dependencies are correctly installed

---

**Note**: This is a simplified version focused only on disease detection. The original project included crop recommendation and fertilizer suggestion features as well. 
