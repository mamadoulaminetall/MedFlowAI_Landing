# 🩺 MedFlow AI — Landing Page

> **L'IA au service des Médecins & Chercheurs**  
> Site officiel · [medflowailanding.streamlit.app](https://medflowailanding.streamlit.app)

---

## 🚀 Aperçu

Site vitrine de **MedFlow AI**, plateforme open source d'outils d'intelligence artificielle conçus pour les cliniciens et chercheurs en médecine. Développée par **Dr. Mamadou Lamine TALL**, PhD Bioinformatique — Aix-Marseille Université 2020.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-10b981?style=flat)
![Status](https://img.shields.io/badge/Status-Live-10b981?style=flat)

---

## 🧬 Outils déployés

| Outil | Description | Accès |
|-------|-------------|-------|
| 🫀 **QoL Cardiac** | Qualité de vie cardiaque · 4 questionnaires · 600 patients | Gratuit |
| 📊 **Scores Cliniques** | 15 scores validés : CHA₂DS₂-VASc, HEART, qSOFA, Glasgow... | Gratuit |
| 💓 **Réinnervation IA** | VFC/HRV post-transplantation · Random Forest AUC=0.961 | Gratuit |
| 🧬 **MYOomics** | RNA-seq · scRNA-seq · ML · Myopathies | Gratuit |
| 📝 **Générateur CR** | Compte-rendu clinique IA → PDF en français | 9€/mois |
| 📚 **Revue Littérature** | PubMed + Claude → synthèse evidence-based | 9€/mois |
| 📈 **Biostatistiques** | Upload CSV → t-test, ANOVA, Kaplan-Meier | 9€/mois |

---

## 🏗️ Structure

```
MedFlowAI_Landing/
├── app.py              # Application Streamlit principale
├── requirements.txt    # Dépendances Python
├── assets/
│   ├── fondateur.jpg       # Photo Dr. ML TALL
│   ├── logo_medflow.png    # Logo MedFlow AI
│   ├── logo_b64.txt        # Logo encodé base64
│   └── photo_b64.txt       # Photo encodée base64
└── README.md
```

---

## ⚙️ Installation locale

```bash
git clone https://github.com/mamadoulaminetall/MedFlowAI_Landing.git
cd MedFlowAI_Landing
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎨 Stack technique

- **Framework** : Streamlit · HTML/CSS glassmorphism
- **Diagramme** : Mermaid.js (roadmap interactive)
- **Design** : Dark theme · `#03080f` · Inter font
- **Assets** : Images encodées base64 (pas de dépendance serveur)
- **Paiement** : Stripe intégré

---

## 📚 Publications scientifiques

**31+ publications** indexées PubMed/Web of Science — génomique microbienne, métagénomique, microbiome, épidémiologie moléculaire.

**Preprints en cours (2026) :**
- Réinnervation Autonome Cardiaque Post-transplantation · Revue PRISMA · N=1 247 patients
- Multi-Omics Profiling in Inherited Muscular Dystrophies · 67 études · N=4 213 échantillons
- QoL Cardiac — Méta-analyse PRISMA · N=600 patients

🔗 [Google Scholar](https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr) · [Thèse 2020](https://theses.fr/2020AIXM0426)

---

## 👤 Auteur

**Dr. Mamadou Lamine TALL**  
PhD Bioinformatique & Génomique — IHU Méditerranée Infection, Aix-Marseille Université  
Fondateur & Développeur — MedFlow AI

📧 mamadoulaminetallgithub@gmail.com  
📍 Montpellier, France  
🔗 [GitHub](https://github.com/mamadoulaminetall) · [Google Scholar](https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr)

---

## 📄 Licence

MIT © 2026 Dr. Mamadou Lamine TALL
