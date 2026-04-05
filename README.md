<div align="center">
  <h1>🩸 Blood Infection Detection System 🩸</h1>
  <p><strong>AI-Powered Medical Diagnostic Dashboard</strong></p>
  <p>An intelligent, full-stack predictive system for identifying blood infection (sepsis) risks using synthetic clinical data and advanced Machine Learning models.</p>
</div>

<br />

---

## 🚀 How to Run in VS Code (Step-by-Step)

To run this project seamlessly, we highly recommend using **Visual Studio Code (VS Code)**. Because this project is split into a Python backend and a React frontend, you will need to open **two separate terminal windows** inside VS Code.

### ⚙️ Step 1: Start the Backend (Artificial Intelligence API)
1. Open VS Code and open the `Blood-infection` folder.
2. From the top menu, click `Terminal > New Terminal`.
3. In the terminal, navigate directly into the backend folder:
   ```bash
   cd backend
   ```
4. Install all the required Python AI libraries:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   *✅ Success! Keep this terminal running. Your API is now live and waiting for requests at `http://localhost:8000`.*

### 🎨 Step 2: Start the Frontend (React Dashboard)
1. In VS Code, open a **brand new Terminal tab** (click the `+` icon near the top right of your existing terminal window).
2. In this new terminal, navigate into the frontend folder:
   ```bash
   cd frontend
   ```
3. Install the Node.js packages (you only need to do this the very first time):
   ```bash
   npm install
   ```
4. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *✅ Success! Click the local link shown in the terminal (usually `http://localhost:5173/`) to open your beautiful dashboard!*

---

<br />

## 📂 Folder Structure & File Explanations

Understanding the project structure is crucial for customization and learning. Here is exactly why each piece exists:

### 1️⃣ The `backend/` Folder (The Brains 🧠)
This directory acts as the central AI nervous system. It processes incoming data, stores history, and runs prediction math.
- **`main.py`** 🔗: The core web server. We use this file to expose our AI models to the internet via APIs so the React frontend can talk to the Python logic.
- **`ml_model.py`** 🤖: The Machine Learning Engine! We use this to synthetically balance our clinical data (using SMOTE), train our "Random Forest" and "XGBoost" algorithms, and execute the final risk predictions. 
- **`models.py`** 🗄️: The Database Structure. Used to define what a single patient log looks like (Name, Age, WBC Count, etc.) so our SQL database can safely construct tables for it.
- **`check_data.py`** 🔬: A utility script used to inspect the synthetic health data generated during our AI training runs.
- **`test_model.py`** 🧪: A script used purely by developers to validate whether the AI models are working locally without having to launch the whole web server.
- **`requirements.txt`** 📦: The Python Dependency List. We use this to tell Python exactly which external open-source libraries (FastAPI, pandas, scikit-learn, etc.) it must download.
- **`sql_app.db`** 💾: The actual SQLite database file! We use this single file to permanently save all your predictive patient history locally.
- **`models_data/`** 📁: A cached folder holding our compiled `.pkl` AI models. We save the models here securely so the system doesn't have to waste 10 minutes retraining them every single time you restart your PC.

<br />

### 2️⃣ The `frontend/` Folder (The Beauty 🎨)
This directory contains the entire Graphical User Interface built with React.js.
- **`src/App.jsx`** 🖥️: The heart of the visual dashboard! We use this massive file to completely structure the data entry forms, render the historical responsive trend graphs, and fetch updates from the Python API.
- **`src/index.css`** 🖌️: The Master Style Sheet. We use this specifically to map out our gorgeous custom Light & Dark mode colors, enable smart layout scaling for mobile phones, and trigger smooth sliding CSS visual animations!
- **`package.json`** 📦: The JavaScript Dependency List. We use this to document necessary front-end libraries (like `react`, `recharts`, and `axios`) so Node.js knows what to install.
- **`vite.config.js`** ⚡: The Build Tool Configuration. We explicitly use Vite instead of older tools because it watches our code files and updates the web browser almost instantly the second we press "save".

<br />

### 3️⃣ General Project Documentation 📝
- **`PROJECT_GUIDE.txt`**: A plaintext offline manual providing step-by-step startup instructions.
- **`PROJECT_STRUCTURE_AND_QA.txt`**: Extensive technical reading addressing deep theoretical "Whys", such as why we use StandardScaler algorithms, why SQLite was chosen, and how Safe Overrides securely dictate final answers. Excellent for exam/interview prep!

---
<div align="center">
  <h3>✨ Built with Next-Gen Medical ML & Fast Responsive Frameworks ✨</h3>
</div>
