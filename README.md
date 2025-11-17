# API Testing Project (Python + Requests + PyTest)

This project contains simple automated API tests using Python **Requests** and **PyTest**.
It validates basic CRUD operations (GET, POST, PUT, DELETE) using the public JSONPlaceholder API.

---

## 🔧 Technologies Used
- Python 3.13.7
- Requests library  
- PyTest  

---

## 📁 Test File
- **test_api_ver1.py**

---

## 🧪 Test Scenarios
### 1. GET User
- GET `/users/1`
- Validate status code `200`
- Validate returned user ID

### 2. POST User
- POST `/posts`
- Send JSON body  
- Validate status code `201`
- Validate name in response

### 3. PUT User
- PUT `/posts/1`
- Update data  
- Validate status code `200`

### 4. DELETE User
- DELETE `/posts/1`
- Validate status code `200`

---

## ▶️ How to Run

### Install dependencies
