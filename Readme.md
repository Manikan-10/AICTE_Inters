EV Range Prediction — Week 1 Internship Task

This project focuses on **Predicting the Driving Range of Electric Vehicles (EVs)** using machine learning techniques.

### Objective
Replicate the idea of EV cost prediction, but with a **new and unique approach** →  
Predict EV **range (km)** based on features like efficiency, speed, seats etc.

###  Week 1 Deliverables
| Task | Status |
|------|--------|
| Problem Definition |
| Collect EV Dataset |  (Added in `data/`) |
| Exploratory Data Analysis (EDA) | 
| Basic ML Concept Demo |  Linear Regression |
| Try Gen-AI tools |
| Streamlit UI |  Basic UI |

---

###  Dataset Used
Custom EV dataset with columns like:

- Brand, Model
- Range (km) → **Target**
- Efficiency (Wh/km)
- Top speed (km/h)
- Seats
- Body type
- Fast charge rate…

File located in: `data/ev_data.csv`

---

###  ML Model (Week-1 Goal)
- **Regression task**
- Model used: `LinearRegression`
- Next weeks: train advanced models

---

###  Tech Stack
- Python
- Pandas, NumPy
- Scikit-Learn
- Matplotlib, Seaborn
- Streamlit
- OpenAI / Gemini prompts for reports

---

###  How to Run

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
