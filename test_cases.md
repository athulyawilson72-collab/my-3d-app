# Week 2 — Test Cases (Person C)
**Project:** 3D Model Generator  
**Base URL:** http://34.179.225.173:8000  
**Date:** June 2026

---

## 1. Router Accuracy Testing — `/route`

| # | Input Prompt | Expected Path | Result |
|---|---|---|---|
| 1 | "Generate a cube with side 5cm" | parametric | ⏳ |
| 2 | "Make a cylinder radius 3, height 10" | parametric | ⏳ |
| 3 | "Create a futuristic spaceship" | ai | ⏳ |
| 4 | "Design a simple table with 4 legs" | parametric | ⏳ |
| 5 | "Generate a dragon sculpture" | ai | ⏳ |
| 6 | "Make a gear with 20 teeth" | parametric | ⏳ |
| 7 | "Create an abstract art piece" | ai | ⏳ |

---

## 2. Invalid SCAD Generation — `/generate`

| # | Input | Expected Behavior | Result |
|---|---|---|---|
| 1 | Empty string `""` | Error message returned | ⏳ |
| 2 | Random text `"asdfghjkl"` | Error or fallback response | ⏳ |
| 3 | Very long prompt (500+ chars) | Handled without crash | ⏳ |
| 4 | Special characters `"@#$%^&*"` | Error message returned | ⏳ |
| 5 | Valid prompt: `"a cube size 5"` | SCAD code + PNG generated | ⏳ |

---

## 3. Full Integration Testing — generate → refine → download

| # | Step | Action | Expected | Result |
|---|---|---|---|---|
| 1 | Generate | POST /generate `{"prompt": "a cube with side 5cm"}` | SCAD code + PNG | ⏳ |
| 2 | Refine | POST /refine `{"prompt": "make it bigger"}` | Modified model | ⏳ |
| 3 | Download | GET /download/stl | STL file downloaded | ⏳ |

---

## 4. API Documentation Check — `/docs`

| # | Check | Expected | Result |
|---|---|---|---|
| 1 | Open http://34.179.225.173:8000/docs | Swagger UI visible | ⏳ |
| 2 | All endpoints listed | /, /generate, /refine, /route, /download/stl | ⏳ |
| 3 | Request/response schemas visible | JSON schema shown | ⏳ |

---

## Status Legend
- ⏳ Pending (server down)
- ✅ Pass
- ❌ Fail
