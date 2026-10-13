# NeuroType: Tempo-Agnostic Keystroke Dynamics Biometrics

[![Recognition](https://img.shields.io/badge/Award-1st%20Place%20(Top%205)-gold.svg)](#achievements)
[![Status](https://img.shields.io/badge/Project-Active%20Prototype-blue.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](#)

NeuroType is an advanced behavioral biometrics authentication engine that verifies user identities based on the rhythm and temporal mechanics of their typing patterns rather than traditional static passwords.

---

## 🏆 Key Achievements
* **1st Place (Top 5 Ranking)** — College AI Community Project Showcase.
* Recognized among the **Top 4 Innovative Engineering Solutions** for behavioral security applications.

---

## 📌 Problem & Concept
Traditional authentication methods rely on knowledge-based factors (passwords, PINs) or static physiological characteristics (fingerprints, facial scans). NeuroType establishes a zero-effort, continuous authentication layer leveraging **keystroke dynamics**:
* **Dwell / Hold Time:** The precise duration a physical key remains pressed.
* **Flight Time / Inter-Key Latency:** The latency and transit interval between consecutive keystrokes.
* **Tempo-Agnostic Classification:** Mitigating False Rejection Rates (FRR) by standardizing rhythm variances during fast and slow typing sessions.

---

## 🛠️ System Architecture

User Typing Input
       │
       ▼
[Custom JS Listeners] ──▶ Raw Event Capture (Key-Rollover & Timing)
       │
       ▼
[Preprocessing Engine] ──▶ Feature Extraction & Dynamic Outlier Capping
       │
       ▼
[Biometric Classifier] ──▶ Identity Verification & Confidence Scoring
       │
       ▼
[Application Interface] ──▶ Real-time Feedback & Verification Status

---

## 📁 Repository Structure

* enrollment_plugin/ — Modular event listener responsible for capturing baseline identity patterns.
* keystroke_plugin/ & free_typing_plugin/ — Dynamic listeners handling raw key-rollover and duplicate key mechanics.
* pages/ — Multi-page dashboard modules for testing, enrollment, and administrative metrics.
* app.py — Core application bootstrap and inference orchestration engine.
* biometric_model.pkl — Serialized pre-trained behavioral classification pipeline.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Pip package manager

### Installation & Run
1. Clone the repository:
   git clone https://github.com/Sohaib-M-M/NeuroType.git
   cd NeuroType

2. Install dependencies:
   pip install -r requirements.txt

3. Launch the application:
   python app.py

---

## 👥 Team & Contributions
* **Sohaib** — Lead Engineering: System Architecture, ML Model Development, Backend & Interface Implementation.
* **Abdulatif Asiri** — Project Pitching, Presentation Delivery & Domain Communication.

---

## 📄 License
This project is developed for academic evaluation and research benchmarking.
