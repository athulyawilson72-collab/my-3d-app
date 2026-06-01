"""
Week 2 - Automated Test Script
Person C (Athulya) - 3D Model Generator
Base URL: http://34.179.225.173:8000
"""

import requests
import json

BASE_URL = "http://34.179.225.173:8000"

passed = 0
failed = 0

def test(name, result, expected=True):
    global passed, failed
    status = "✅ PASS" if result == expected else "❌ FAIL"
    if result == expected:
        passed += 1
    else:
        failed += 1
    print(f"{status} — {name}")

print("=" * 50)
print("3D Model Generator — Week 2 Tests")
print("=" * 50)

# ─── 1. Health Check ───
print("\n[1] Health Check — GET /")
try:
    r = requests.get(f"{BASE_URL}/", timeout=5)
    test("Server is live", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Server is live ({e})")
    failed += 1

# ─── 2. Router Accuracy Testing ───
print("\n[2] Router Accuracy Testing — POST /route")

router_tests = [
    ("Generate a cube with side 5cm", "parametric"),
    ("Make a cylinder radius 3 height 10", "parametric"),
    ("Create a futuristic spaceship", "ai"),
    ("Design a simple table with 4 legs", "parametric"),
    ("Generate a dragon sculpture", "ai"),
    ("Make a gear with 20 teeth", "parametric"),
    ("Create an abstract art piece", "ai"),
]

for prompt, expected_path in router_tests:
    try:
        r = requests.post(f"{BASE_URL}/route", json={"prompt": prompt}, timeout=10)
        data = r.json()
        actual = data.get("path") or data.get("route") or data.get("type") or str(data)
        test(f'Route: "{prompt[:30]}..." → {expected_path}', expected_path in str(actual).lower())
    except Exception as e:
        print(f"❌ FAIL — Route test failed ({e})")
        failed += 1

# ─── 3. Invalid SCAD Generation ───
print("\n[3] Invalid Input Testing — POST /generate")

invalid_tests = [
    ("Empty string", ""),
    ("Random text", "asdfghjkl"),
    ("Special characters", "@#$%^&*"),
]

for name, prompt in invalid_tests:
    try:
        r = requests.post(f"{BASE_URL}/generate", json={"prompt": prompt}, timeout=10)
        # Should return error, not crash (not 500)
        test(f"Invalid input handled: {name}", r.status_code != 500)
    except Exception as e:
        print(f"❌ FAIL — {name} ({e})")
        failed += 1

# Valid generate
try:
    r = requests.post(f"{BASE_URL}/generate", json={"prompt": "a cube with side 5cm"}, timeout=15)
    test("Valid generate: cube", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Valid generate ({e})")
    failed += 1

# ─── 4. Full Integration: generate → refine → download ───
print("\n[4] Full Integration Testing")

try:
    r = requests.post(f"{BASE_URL}/generate", json={"prompt": "a cube with side 5cm"}, timeout=15)
    test("Step 1: Generate model", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Generate ({e})")
    failed += 1

try:
    r = requests.post(f"{BASE_URL}/refine", json={"prompt": "make it bigger"}, timeout=15)
    test("Step 2: Refine model", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Refine ({e})")
    failed += 1

try:
    r = requests.get(f"{BASE_URL}/download/stl", timeout=10)
    test("Step 3: Download STL", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Download STL ({e})")
    failed += 1

# ─── 5. API Docs Check ───
print("\n[5] API Documentation — GET /docs")
try:
    r = requests.get(f"{BASE_URL}/docs", timeout=5)
    test("Swagger UI accessible", r.status_code == 200)
except Exception as e:
    print(f"❌ FAIL — Docs ({e})")
    failed += 1

# ─── Summary ───
print("\n" + "=" * 50)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 50)
