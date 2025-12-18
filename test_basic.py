"""
Basic test script to verify the implementation
This script tests imports and basic functionality without requiring OLLAMA to be running.
"""

import sys
from pathlib import Path

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from agents import AIAgent, OCRAgent
        print("✓ Agents imported successfully")
    except Exception as e:
        print(f"✗ Failed to import agents: {e}")
        return False
    
    try:
        from utils import load_config, check_ollama_availability, list_available_models
        print("✓ Utils imported successfully")
    except Exception as e:
        print(f"✗ Failed to import utils: {e}")
        return False
    
    return True


def test_agent_initialization():
    """Test agent initialization."""
    print("\nTesting agent initialization...")
    
    try:
        from agents import AIAgent, OCRAgent
        
        # Test AI Agent initialization
        ai_agent = AIAgent(model="llama2", temperature=0.7)
        print("✓ AI Agent initialized successfully")
        
        # Test OCR Agent initialization
        ocr_agent = OCRAgent(model="llama2", language="eng")
        print("✓ OCR Agent initialized successfully")
        
        return True
    except Exception as e:
        print(f"✗ Failed to initialize agents: {e}")
        return False


def test_config():
    """Test configuration utilities."""
    print("\nTesting configuration utilities...")
    
    try:
        from utils import load_config, check_ollama_availability, list_available_models
        
        # Load config
        config = load_config()
        print(f"✓ Configuration loaded: {len(config)} sections")
        
        # Check OLLAMA availability (this may fail if OLLAMA is not running)
        available = check_ollama_availability()
        if available:
            print("✓ OLLAMA service is available")
            
            # List models
            models = list_available_models()
            print(f"✓ Found {len(models)} OLLAMA models")
        else:
            print("⚠ OLLAMA service is not available (this is expected if not running)")
        
        return True
    except Exception as e:
        print(f"✗ Failed config tests: {e}")
        return False


def test_dependencies():
    """Test that required dependencies are installed."""
    print("\nTesting dependencies...")
    
    dependencies = [
        ("langchain", "LangChain"),
        ("langchain_community", "LangChain Community"),
        ("PIL", "Pillow"),
        ("cv2", "OpenCV"),
        ("pytesseract", "PyTesseract"),
        ("dotenv", "python-dotenv"),
        ("requests", "Requests")
    ]
    
    all_ok = True
    for module_name, package_name in dependencies:
        try:
            __import__(module_name)
            print(f"✓ {package_name} is installed")
        except ImportError:
            print(f"✗ {package_name} is NOT installed")
            all_ok = False
    
    return all_ok


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running Basic Tests")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Dependencies", test_dependencies),
        ("Configuration", test_config),
        ("Agent Initialization", test_agent_initialization),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ Test '{test_name}' raised an exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n⚠️ Some tests failed. Please check the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
