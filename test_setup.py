#!/usr/bin/env python3
"""
Test script for Creative Visual Coding App
Verifies setup and basic functionality
"""

import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

def test_backend_health():
    """Test backend health endpoint"""
    print("🏥 Testing backend health...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is healthy: {data}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend health check error: {e}")
        return False

def test_frontend_access():
    """Test frontend accessibility"""
    print("🌐 Testing frontend access...")
    try:
        response = requests.get("http://localhost:3000", timeout=10)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend access failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend access error: {e}")
        return False

def test_visual_generation():
    """Test visual generation endpoint"""
    print("🎨 Testing visual generation...")
    try:
        test_input = "A simple animated circle that grows and shrinks"
        payload = {"user_input": test_input}
        
        response = requests.post(
            "http://localhost:8000/generate-visual",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print("✅ Visual generation successful")
                print(f"   Visual ID: {data.get('visual_id')}")
                print(f"   Input: {data.get('user_input')}")
                return True
            else:
                print(f"❌ Visual generation failed: {data.get('error')}")
                return False
        else:
            print(f"❌ Visual generation request failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Visual generation error: {e}")
        return False

def test_visuals_endpoint():
    """Test getting visuals list"""
    print("📋 Testing visuals endpoint...")
    try:
        response = requests.get("http://localhost:8000/visuals", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Visuals endpoint working: {len(data.get('visuals', []))} visuals found")
            return True
        else:
            print(f"❌ Visuals endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Visuals endpoint error: {e}")
        return False

def check_environment():
    """Check environment variables"""
    print("🔧 Checking environment...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        print("✅ OpenAI API key is configured")
        return True
    else:
        print("❌ OpenAI API key not configured properly")
        print("   Please set OPENAI_API_KEY in your .env file")
        return False

def main():
    """Run all tests"""
    print("🧪 Creative Visual Coding App - Setup Test")
    print("=" * 50)
    
    tests = [
        ("Environment", check_environment),
        ("Backend Health", test_backend_health),
        ("Frontend Access", test_frontend_access),
        ("Visuals Endpoint", test_visuals_endpoint),
        ("Visual Generation", test_visual_generation),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your app is ready to use.")
        print("\n🌐 Access your app:")
        print("   Frontend: http://localhost:3000")
        print("   API Docs: http://localhost:8000/docs")
    else:
        print("⚠️  Some tests failed. Please check the setup.")
        
        if not any(name == "Environment" and result for name, result in results):
            print("\n💡 Tips:")
            print("   1. Make sure Docker is running")
            print("   2. Run: docker-compose up --build")
            print("   3. Check that ports 3000 and 8000 are available")
            print("   4. Verify your OpenAI API key in .env file")

if __name__ == "__main__":
    main() 