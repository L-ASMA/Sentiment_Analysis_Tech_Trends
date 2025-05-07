##  Tech Crowd Sentiment Analysis

This project analyzes large-scale Reddit & Discord discussions using a scalable machine learning pipeline. It integrates real-time data, runs sentiment and topic modeling, and provides interactive visual dashboards.

---

### Features

* Multi-source data collection (Reddit, Discord, NewsAPI)
* Real-time Kafka integration
* Topic modeling (LDA), sentiment analysis (VADER, logistic regression), clustering (K-Means)
* Interactive visualizations (Plotly Dash)
* Automated tests & CI (pytest, GitHub Actions)

---

### Structure

```
/Data processing & analysis/
    *.ipynb, *.py

/Datasets/
    *.csv, *.xlsx

/streaming configurations/
tests/
requirements.txt
README.md
```

---

###  How to Run

```bash
git clone https://github.com/<your-username>/<repo>.git
pip install -r requirements.txt
```

* Add API keys in `.env`
* Start Kafka services
* Run notebooks or scripts
* Launch dashboard:

```bash
python app.py
```

---

### Tests

```bash
pytest tests/
```

---

### Results

* \~85% accuracy (supervised sentiment)
* Clear cluster separation
* Interactive trend visualizations

---

###  License

MIT License
