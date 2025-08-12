#!/usr/bin/env python3
"""
Crop Disease Detection System - Startup Script
This script checks dependencies and starts the disease detection application.
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "disease_requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_model_file():
    """Check if the model file exists"""
    model_path = "models/plant_disease_model.pth"
    if not os.path.exists(model_path):
        print(f"❌ Error: Model file not found at {model_path}")
        print("Please ensure the model file is in the models/ directory")
        return False
    print("✅ Model file found")
    return True

def check_utils_files():
    """Check if required utility files exist"""
    required_files = [
        "utils/model.py",
        "utils/disease.py"
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"❌ Error: Required file not found: {file_path}")
            return False
    
    print("✅ Utility files found")
    return True

def check_templates():
    """Check if required template files exist"""
    required_templates = [
        "templates/index_disease.html",
        "templates/disease.html",
        "templates/disease_result_simple.html"
    ]
    
    for template in required_templates:
        if not os.path.exists(template):
            print(f"❌ Error: Template file not found: {template}")
            return False
    
    print("✅ Template files found")
    return True

def main():
    """Main startup function"""
    print("🌱 Crop Disease Detection System")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if requirements file exists
    if not os.path.exists("disease_requirements.txt"):
        print("❌ Error: disease_requirements.txt not found")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check model file
    if not check_model_file():
        sys.exit(1)
    
    # Check utility files
    if not check_utils_files():
        sys.exit(1)
    
    # Check templates
    if not check_templates():
        sys.exit(1)
    
    print("\n🚀 Starting Crop Disease Detection System...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 40)
    
    # Import and run the Flask app
    try:
        from disease_detection_app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError as e:
        print(f"❌ Error importing app: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 