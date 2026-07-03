# 🏹 KARNA - AI Powered Archery Training System

KARNA is an AI-powered archery coaching and performance analysis application developed using **Python**, **Streamlit**, **MediaPipe**, **OpenCV**, and **SQLite**. It helps archers improve their shooting technique through real-time posture analysis, performance tracking, personalized exercise suggestions, diet planning, and practice analytics.

---

## 📌 Features

### 🎯 Real-Time Posture Detection
- Live camera-based posture analysis
- Detects body landmarks using MediaPipe
- Calculates shoulder and elbow angles
- Provides instant posture feedback
- Helps improve shooting form

### 📊 Score Management
- Record practice session scores
- Store number of rounds and total score
- View previous performances
- Track progress over time

### 🥗 Diet Planner
- Personalized nutrition suggestions
- Diet recommendations for archers
- Improve stamina and recovery
- Healthy meal planning

### 💪 Exercise Suggestor
- Exercise recommendations based on posture
- Improve flexibility
- Increase upper body strength
- Enhance shooting stability

### 📝 Daily Practice Records
- Log daily practice sessions
- Record:
  - Number of arrows
  - Practice duration
  - Mistakes made
  - Learnings
- Monitor consistency

### 📈 Performance Dashboard
- View overall statistics
- Analyze score trends
- Track practice history
- Visualize improvement

### 💾 Database Storage
- SQLite database
- Stores:
  - Scores
  - Daily practice records

---

# 🛠️ Tech Stack

- Python
- Streamlit
- MediaPipe
- OpenCV
- NumPy
- SQLite
- Pandas
- Matplotlib

---

# 📂 Project Structure

```
KARNA/
│
├── app.py
├── config.py
├── database.py
├── karna.db
│
├── modules/
│   ├── posture_detection.py
│   ├── scorer.py
│   ├── diet_planner.py
│   ├── exercise_suggestor.py
│   ├── daily_records.py
│   └── dashboard.py
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/your-username/KARNA.git
```

```bash
cd KARNA
```

---

## Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 📊 Modules

## 🏹 Live Detection
Uses MediaPipe pose estimation to analyze the archer's posture and provide live feedback.

## 🎯 Scorer
Stores practice scores and calculates performance statistics.

## 🥗 Diet Planner
Provides nutrition recommendations for better performance and recovery.

## 💪 Exercise Suggestor
Suggests exercises to improve posture, flexibility, and strength.

## 📝 Daily Records
Maintains a training journal including arrows shot, practice time, mistakes, and learnings.

## 📈 Dashboard
Displays historical data and performance analytics.

---

# 🗄️ Database

The project uses SQLite (`karna.db`) for local data storage.

Tables include:

### Scores
- ID
- Rounds
- Score
- Date

### Daily Records
- Date
- Arrows Shot
- Practice Time
- Mistakes
- Learnings

---

# 🎯 Future Improvements

- AI-based shot prediction
- Bow alignment detection
- Arrow trajectory analysis
- Coach dashboard
- Cloud database support
- User authentication
- Multi-user support
- Mobile application
- Video recording and replay
- Progress reports in PDF

---

# 📷 Screenshots
<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/959b4ba2-beb8-4eda-99bf-1cb287ed9fcc" />
<img width="1920" height="1080" alt="Screenshot (132)" src="https://github.com/user-attachments/assets/cdbc6619-fa8f-4b03-b74b-e982d205da58" />
<img width="1920" height="1080" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/cfe6d8ef-e2e7-43ea-bd94-efb163aa58be" />
<img width="1920" height="1080" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/31a096fa-9d89-4afc-bc5b-4e04d4325644" />
<img width="1920" height="1080" alt="Screenshot (135)" src="https://github.com/user-attachments/assets/fcdeb392-f33a-48a4-8408-01fe80187346" />
<img width="1920" height="1080" alt="Screenshot (136)" src="https://github.com/user-attachments/assets/7e9e21d5-2aa2-4b13-9e4b-80588ba14cdf" />






---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```
git checkout -b feature-name
```

3. Commit your changes

```
git commit -m "Added new feature"
```

4. Push to your branch

```
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Atharva Santosh Patil**

AI Developer | Computer Vision Enthusiast | Machine Learning | Python Developer

---

## ⭐ If you like this project, don't forget to Star the repository!
