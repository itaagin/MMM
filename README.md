# MMM

## Overview
This project focuses on implementing MMM.

## 🧪 Project Flow

### 🔧 Planning (New Experiment Setup)

The planning pipeline creates, configures, and stores GEO experiment candidates with selected test/control regions.

#### Steps:
1. **Parameter Setup**
   - Load parameters from the `config` file (e.g., game, KPI, geo level, platform).
   - Determine dataset dimensions and default start date based on KPI config.

2. **Data Extraction**
   - Execute a parameterized Presto SQL query to pull data.
   - Filter and format the dataset by geo granularity and time frequency.

3. **Preprocessing**
   - Validate consistent geographic coverage across the time period.
   - Prepare cleaned dataset for market selection.

4. **Test-Control Split Creation**
   - Generate top-`k` market selection splits using `geo_lift_create`.
   - For each `k`, calculate:
     - Test and control weights
     - Aggregate time series
     - Evaluation metrics (e.g., `avg_diff`, `weighted_rmse`)

5. **Visualization & Logging**
   - Generate plots comparing test vs. control:
     - `split`: Side-by-side comparison
     - `diff`: KPI difference over time
   - Save images, metrics, and allocation metadata to MLflow.

---

## Set Up
Open project on your Mac
1. CD to working directory:
```bash
cd /Users/itamar.zach/Desktop/ita/GitHub repo/MMM
```

2. Clone the repository(Github) & open on VS code/pycharm:
  ```
  git clone git@github.com:Playstudios-Data/geo-lift.git
  ```
3. Check the current path:
  ```
  pwd
  ```  
4. Set up a virtual environment, activate it and verify that the venv is on env was created:
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ls -a
  which python
  ```
5. install the dependencies:
  ```
  pip install -r requirements.txt
  ```
6. setup pre-commit hook:
  ```
  pre-commit install
 ```  
---
