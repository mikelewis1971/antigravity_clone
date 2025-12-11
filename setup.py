"""Setup script for Antigravity Local."""
import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Ensure Python 3.9+ is installed."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("[ERROR] Python 3.9 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"[OK] Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_model_exists():
    """Check if the GGUF model file exists."""
    model_path = "G:/Jan/llamacpp/models/lmstudio-community/Qwen3-8B-GGUF/Qwen3-8B-Q4_K_M.gguf"
    
    if os.path.exists(model_path):
        print(f"[OK] Model found: {model_path}")
        return True
    else:
        print(f"[ERROR] Model not found: {model_path}")
        print("   Please ensure the model file exists at the specified path")
        print("   or update the path in config.yaml")
        return False


def install_dependencies():
    """Install required Python packages."""
    print("\n[SETUP] Installing dependencies...")
    
    backend_dir = Path(__file__).parent / "backend"
    requirements_file = backend_dir / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"[ERROR] Requirements file not found: {requirements_file}")
        return False
    
    try:
        # Install llama-cpp-python with CUDA support (if available)
        print("\nInstalling llama-cpp-python (this may take a few minutes)...")
        subprocess.run([
            sys.executable, "-m", "pip", "install",
            "llama-cpp-python==0.2.90",
            "--extra-index-url", "https://abetlen.github.io/llama-cpp-python/whl/cpu"
        ], check=True)
        
        # Install other requirements
        print("\nInstalling other dependencies...")
        subprocess.run([
            sys.executable, "-m", "pip", "install",
            "-r", str(requirements_file)
        ], check=True)
        
        print("[OK] Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install dependencies: {e}")
        return False


def create_directories():
    """Create necessary directories."""
    print("\n[SETUP] Creating directories...")
    
    dirs = [
        Path(__file__).parent / "backend",
        Path(__file__).parent / "frontend",
        Path(__file__).parent / "prompts",
    ]
    
    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] {dir_path}")
    
    return True


def main():
    """Main setup function."""
    print("=" * 60)
    print("  Antigravity Local - Setup")
    print("=" * 60)
    print()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        sys.exit(1)
    
    # Check model exists
    if not check_model_exists():
        print("\n[WARNING] Model file not found. Please update config.yaml")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    # Install dependencies
    print("\n" + "=" * 60)
    response = input("Install Python dependencies? (y/n): ")
    if response.lower() == 'y':
        if not install_dependencies():
            sys.exit(1)
    
    print("\n" + "=" * 60)
    print("[SUCCESS] Setup complete!")
    print("\nTo start Antigravity Local:")
    print("  1. Run: run.bat")
    print("  2. Or run: python backend/api.py")
    print("  3. Open browser to: http://localhost:8000")
    print("=" * 60)


if __name__ == "__main__":
    main()
