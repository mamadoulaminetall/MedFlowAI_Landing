"""
MedFlow AI — CV Dr. Mamadou Lamine TALL
Page dédiée /cv
"""
import streamlit as st

st.set_page_config(
    page_title="CV · Dr. Mamadou Lamine TALL",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
[data-testid="stAppViewContainer"] { background: #09090b; }
[data-testid="stSidebar"], [data-testid="collapsedControl"] { display:none; }
[data-testid="stHeader"] { display:none; }
[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
body { font-family: 'Inter', sans-serif; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#09090b;min-height:100vh;padding:60px 5% 80px;font-family:'Inter',sans-serif">

  <!-- top bar -->
  <div style="display:flex;justify-content:space-between;align-items:center;
              margin-bottom:48px;padding-bottom:24px;
              border-bottom:1px solid rgba(16,185,129,0.15)">
    <a href="https://medflowailanding.streamlit.app" style="display:flex;align-items:center;gap:8px;text-decoration:none">
      <span style="font-size:0.75rem;font-weight:700;letter-spacing:2px;
                   text-transform:uppercase;color:#64748b">← MedFlow AI</span>
    </a>
    <span style="font-size:0.65rem;font-weight:700;letter-spacing:2px;
                 text-transform:uppercase;color:#10b981;
                 background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);
                 border-radius:20px;padding:4px 12px">Curriculum Vitæ</span>
  </div>

  <!-- header identité -->
  <div style="text-align:center;margin-bottom:56px">
    <h1 style="font-size:3rem;font-weight:900;color:#f1f5f9;letter-spacing:-1.5px;margin-bottom:8px">
      Mamadou Lamine <span style="background:linear-gradient(135deg,#10b981,#34d399);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent">TALL</span>
    </h1>
    <div style="font-size:1.1rem;color:#94a3b8;margin-bottom:16px;font-weight:500">
      PhD Bioinformatique &amp; Data Science · IA Appliquée à la Recherche Biomédicale
    </div>
    <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin-bottom:20px">
      <span style="color:#64748b;font-size:0.82rem">📍 28 Rue Nicolas Copernic, 34170 Castelnau-le-Lez, France</span>
      <span style="color:#64748b;font-size:0.82rem">📞 +33 7 81 19 85 42</span>
      <span style="color:#64748b;font-size:0.82rem">✉️ laminetall30@gmail.com</span>
    </div>
    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap">
      <a href="https://github.com/mamadoulaminetall" target="_blank"
         style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
                color:#94a3b8;border-radius:8px;padding:6px 14px;font-size:0.76rem;
                font-weight:600;text-decoration:none">GitHub ↗</a>
      <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
         style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
                color:#94a3b8;border-radius:8px;padding:6px 14px;font-size:0.76rem;
                font-weight:600;text-decoration:none">Google Scholar ↗</a>
      <a href="https://theses.fr/2020AIXM0426" target="_blank"
         style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
                color:#94a3b8;border-radius:8px;padding:6px 14px;font-size:0.76rem;
                font-weight:600;text-decoration:none">Thèse ↗</a>
      <a href="https://www.linkedin.com/in/medflow-ia-350531401/" target="_blank"
         style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
                color:#94a3b8;border-radius:8px;padding:6px 14px;font-size:0.76rem;
                font-weight:600;text-decoration:none">LinkedIn ↗</a>
    </div>
  </div>

  <!-- stats résumé -->
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;
              max-width:800px;margin:0 auto 64px;text-align:center">
    <div style="background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);
         border-radius:14px;padding:18px 12px">
      <div style="font-size:2rem;font-weight:900;color:#10b981">29</div>
      <div style="font-size:0.7rem;color:#64748b;margin-top:4px">Publications</div>
    </div>
    <div style="background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.15);
         border-radius:14px;padding:18px 12px">
      <div style="font-size:2rem;font-weight:900;color:#3b82f6">248+</div>
      <div style="font-size:0.7rem;color:#64748b;margin-top:4px">Citations</div>
    </div>
    <div style="background:rgba(139,92,246,0.06);border:1px solid rgba(139,92,246,0.15);
         border-radius:14px;padding:18px 12px">
      <div style="font-size:2rem;font-weight:900;color:#8b5cf6">5 800+</div>
      <div style="font-size:0.7rem;color:#64748b;margin-top:4px">Échantillons analysés</div>
    </div>
    <div style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
         border-radius:14px;padding:18px 12px">
      <div style="font-size:2rem;font-weight:900;color:#f59e0b">10</div>
      <div style="font-size:0.7rem;color:#64748b;margin-top:4px">Outils IA déployés</div>
    </div>
  </div>

  <!-- corps principal 2 colonnes -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;max-width:1200px;margin:0 auto">

    <!-- COLONNE GAUCHE -->
    <div>

      <!-- EXPÉRIENCE -->
      <div style="margin-bottom:48px">
        <div style="font-size:0.65rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
             color:#10b981;margin-bottom:24px;display:flex;align-items:center;gap:8px">
          <div style="width:24px;height:24px;background:rgba(16,185,129,0.12);border-radius:7px;
               display:flex;align-items:center;justify-content:center;font-size:0.8rem">💼</div>
          Expérience professionnelle
        </div>

        <div style="position:relative;padding-left:20px">
          <div style="position:absolute;left:5px;top:8px;bottom:0;width:2px;
                      background:linear-gradient(180deg,#10b981,rgba(16,185,129,0.05))"></div>

          <!-- poste 1 -->
          <div style="position:relative;margin-bottom:22px">
            <div style="position:absolute;left:-20px;top:7px;width:9px;height:9px;border-radius:50%;
                        background:#10b981;box-shadow:0 0 0 3px rgba(16,185,129,0.2)"></div>
            <div style="background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.12);
                 border-radius:12px;padding:14px 16px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px">
                <div style="font-weight:700;color:#e2e8f0;font-size:0.85rem">Head of IT &amp; Lecturer</div>
                <span style="font-size:0.62rem;background:rgba(16,185,129,0.1);color:#10b981;
                      border-radius:20px;padding:2px 8px;white-space:nowrap;margin-left:6px">2023 – Présent</span>
              </div>
              <div style="color:#10b981;font-size:0.76rem;font-weight:600;margin-bottom:6px">
                ERIDAN SCHOOL · Montpellier
              </div>
              <ul style="color:#64748b;font-size:0.74rem;line-height:1.7;padding-left:14px">
                <li>Responsable du département informatique de l'école bilingue internationale</li>
                <li>Enseignement Sciences Numériques, Technologie &amp; Informatique</li>
              </ul>
            </div>
          </div>

          <!-- poste 2 -->
          <div style="position:relative;margin-bottom:22px">
            <div style="position:absolute;left:-20px;top:7px;width:9px;height:9px;border-radius:50%;
                        background:#3b82f6;box-shadow:0 0 0 3px rgba(59,130,246,0.2)"></div>
            <div style="background:rgba(59,130,246,0.04);border:1px solid rgba(59,130,246,0.12);
                 border-radius:12px;padding:14px 16px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px">
                <div style="font-weight:700;color:#e2e8f0;font-size:0.85rem">Research Bioinformatician L4 / Data Manager</div>
                <span style="font-size:0.62rem;background:rgba(59,130,246,0.1);color:#3b82f6;
                      border-radius:20px;padding:2px 8px;white-space:nowrap;margin-left:6px">2023 – 2024</span>
              </div>
              <div style="color:#3b82f6;font-size:0.76rem;font-weight:600;margin-bottom:6px">
                Centre de Recherche · CHU Sainte-Justine · Montréal, Canada
              </div>
              <ul style="color:#64748b;font-size:0.74rem;line-height:1.7;padding-left:14px">
                <li>Préparation des données CNV (*.idat/*.cel) pour la détection de variants</li>
                <li>Annotation génomique et protocole ML DigCNV pour l'optimisation des modèles</li>
                <li>Intégration des données génomiques dans des études cliniques et épidémiologiques</li>
                <li>Rédaction de rapports scientifiques et implémentation de protocoles de validation</li>
              </ul>
            </div>
          </div>

          <!-- poste 3 -->
          <div style="position:relative;margin-bottom:22px">
            <div style="position:absolute;left:-20px;top:7px;width:9px;height:9px;border-radius:50%;
                        background:#8b5cf6;box-shadow:0 0 0 3px rgba(139,92,246,0.2)"></div>
            <div style="background:rgba(139,92,246,0.04);border:1px solid rgba(139,92,246,0.12);
                 border-radius:12px;padding:14px 16px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px">
                <div style="font-weight:700;color:#e2e8f0;font-size:0.85rem">Ingénieur Bioinformatique / Chef de projet Biostatistiques</div>
                <span style="font-size:0.62rem;background:rgba(139,92,246,0.1);color:#8b5cf6;
                      border-radius:20px;padding:2px 8px;white-space:nowrap;margin-left:6px">2021 – 2022</span>
              </div>
              <div style="color:#8b5cf6;font-size:0.76rem;font-weight:600;margin-bottom:6px">
                UCA, Faculté de Médecine / Dépt. DERMG · Nice, France
              </div>
              <ul style="color:#64748b;font-size:0.74rem;line-height:1.7;padding-left:14px">
                <li>Développement de méthodes analytiques et pipelines automatisés pour données NGS</li>
                <li>Modélisation prédictive pour identifier des biomarqueurs diagnostiques/pronostiques</li>
                <li>Analyses différentielles (QC, transcriptomique, génomique), pathway &amp; network analysis</li>
                <li>Conception de BDD et plans d'analyse statistique en collaboration interdisciplinaire</li>
              </ul>
            </div>
          </div>

          <!-- poste 4 -->
          <div style="position:relative;margin-bottom:22px">
            <div style="position:absolute;left:-20px;top:7px;width:9px;height:9px;border-radius:50%;
                        background:#f59e0b;box-shadow:0 0 0 3px rgba(245,158,11,0.2)"></div>
            <div style="background:rgba(245,158,11,0.04);border:1px solid rgba(245,158,11,0.12);
                 border-radius:12px;padding:14px 16px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px">
                <div style="font-weight:700;color:#e2e8f0;font-size:0.85rem">Doctorant — Bioinformatique &amp; Génomique</div>
                <span style="font-size:0.62rem;background:rgba(245,158,11,0.1);color:#f59e0b;
                      border-radius:20px;padding:2px 8px;white-space:nowrap;margin-left:6px">2017 – 2020</span>
              </div>
              <div style="color:#f59e0b;font-size:0.76rem;font-weight:600;margin-bottom:6px">
                IHU Méditerranée Infection · Aix-Marseille Université
              </div>
              <ul style="color:#64748b;font-size:0.74rem;line-height:1.7;padding-left:14px">
                <li>Analyse du mosaïcisme génomique microbien et des transferts horizontaux de gènes</li>
                <li>Phylogénomique, taxonomie microbienne, développement d'outils bioinformatiques</li>
                <li>Traitement de données de séquençage : assemblage, annotation structurale et fonctionnelle</li>
                <li>20+ publications dans des revues internationales à comité de lecture</li>
              </ul>
            </div>
          </div>

          <!-- poste 5 -->
          <div style="position:relative">
            <div style="position:absolute;left:-20px;top:7px;width:9px;height:9px;border-radius:50%;
                        background:#64748b;box-shadow:0 0 0 3px rgba(100,116,139,0.2)"></div>
            <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
                 border-radius:12px;padding:14px 16px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px">
                <div style="font-weight:700;color:#cbd5e1;font-size:0.85rem">Stages cliniques &amp; hospitaliers</div>
                <span style="font-size:0.62rem;background:rgba(100,116,139,0.1);color:#64748b;
                      border-radius:20px;padding:2px 8px;white-space:nowrap;margin-left:6px">2015 – 2016</span>
              </div>
              <div style="color:#64748b;font-size:0.76rem;font-weight:600;margin-bottom:6px">
                CHU FANN · Dakar, Sénégal
              </div>
              <ul style="color:#64748b;font-size:0.74rem;line-height:1.7;padding-left:14px">
                <li>IRM : traitement d'images médicales (FSL/SPM), normalisation, segmentation</li>
                <li>Gestion BDD hospitalières (MySQL, Access), interfaces PHP/HTML, requêtes SQL complexes</li>
              </ul>
            </div>
          </div>

        </div>
      </div><!-- /expérience -->

    </div><!-- /col gauche -->

    <!-- COLONNE DROITE -->
    <div style="display:flex;flex-direction:column;gap:40px">

      <!-- FORMATION -->
      <div>
        <div style="font-size:0.65rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
             color:#3b82f6;margin-bottom:20px;display:flex;align-items:center;gap:8px">
          <div style="width:24px;height:24px;background:rgba(59,130,246,0.12);border-radius:7px;
               display:flex;align-items:center;justify-content:center;font-size:0.8rem">🎓</div>
          Formation
        </div>

        <div style="display:flex;flex-direction:column;gap:10px">

          <div style="background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);
               border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center">
            <div style="min-width:48px;text-align:center;background:rgba(16,185,129,0.1);
                 border-radius:8px;padding:5px 0;font-size:0.7rem;font-weight:800;color:#10b981">2020</div>
            <div>
              <div style="font-weight:700;color:#e2e8f0;font-size:0.82rem">PhD Informatique &amp; Bioinformatique</div>
              <div style="color:#64748b;font-size:0.72rem;margin-top:2px">Aix-Marseille Université · Marseille, France</div>
            </div>
          </div>

          <div style="background:rgba(59,130,246,0.04);border:1px solid rgba(59,130,246,0.1);
               border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center">
            <div style="min-width:48px;text-align:center;background:rgba(59,130,246,0.1);
                 border-radius:8px;padding:5px 0;font-size:0.7rem;font-weight:800;color:#3b82f6">2019</div>
            <div>
              <div style="font-weight:700;color:#e2e8f0;font-size:0.82rem">CESU Biostatistiques &amp; Méthodologie de la Recherche</div>
              <div style="color:#64748b;font-size:0.72rem;margin-top:2px">Faculté de Médecine · Aix-Marseille</div>
            </div>
          </div>

          <div style="background:rgba(139,92,246,0.04);border:1px solid rgba(139,92,246,0.1);
               border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center">
            <div style="min-width:48px;text-align:center;background:rgba(139,92,246,0.1);
                 border-radius:8px;padding:5px 0;font-size:0.7rem;font-weight:800;color:#8b5cf6">2017</div>
            <div>
              <div style="font-weight:700;color:#e2e8f0;font-size:0.82rem">M2 Bioinformatique &amp; Biomathématiques</div>
              <div style="color:#64748b;font-size:0.72rem;margin-top:2px">Université Cheikh Anta Diop · Dakar, Sénégal</div>
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center">
            <div style="min-width:48px;text-align:center;background:rgba(255,255,255,0.05);
                 border-radius:8px;padding:5px 0;font-size:0.7rem;font-weight:800;color:#64748b">2014</div>
            <div>
              <div style="font-weight:700;color:#cbd5e1;font-size:0.82rem">Licence Biologie, Chimie &amp; Géosciences</div>
              <div style="color:#64748b;font-size:0.72rem;margin-top:2px">Université Cheikh Anta Diop · Dakar, Sénégal</div>
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center">
            <div style="min-width:48px;text-align:center;background:rgba(255,255,255,0.05);
                 border-radius:8px;padding:5px 0;font-size:0.7rem;font-weight:800;color:#64748b">2010</div>
            <div>
              <div style="font-weight:700;color:#cbd5e1;font-size:0.82rem">Baccalauréat Scientifique</div>
              <div style="color:#64748b;font-size:0.72rem;margin-top:2px">Lycée Moderne de Rufisque · Dakar, Sénégal</div>
            </div>
          </div>

        </div>
      </div><!-- /formation -->

      <!-- COMPÉTENCES -->
      <div>
        <div style="font-size:0.65rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
             color:#8b5cf6;margin-bottom:20px;display:flex;align-items:center;gap:8px">
          <div style="width:24px;height:24px;background:rgba(139,92,246,0.12);border-radius:7px;
               display:flex;align-items:center;justify-content:center;font-size:0.8rem">⚙️</div>
          Compétences techniques
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px">

          <div>
            <div style="font-size:0.62rem;color:#10b981;font-weight:700;letter-spacing:1px;
                 text-transform:uppercase;margin-bottom:8px">Langages</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
              <span style="background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);
                    color:#10b981;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Python</span>
              <span style="background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.2);
                    color:#3b82f6;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">R</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Perl</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Shell/Bash</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">PHP / JS</span>
            </div>
          </div>

          <div>
            <div style="font-size:0.62rem;color:#3b82f6;font-weight:700;letter-spacing:1px;
                 text-transform:uppercase;margin-bottom:8px">Machine Learning</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
              <span style="background:rgba(139,92,246,0.08);border:1px solid rgba(139,92,246,0.2);
                    color:#8b5cf6;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Scikit-learn</span>
              <span style="background:rgba(139,92,246,0.06);border:1px solid rgba(139,92,246,0.15);
                    color:#a78bfa;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Classification</span>
              <span style="background:rgba(139,92,246,0.06);border:1px solid rgba(139,92,246,0.15);
                    color:#a78bfa;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Clustering</span>
              <span style="background:rgba(139,92,246,0.06);border:1px solid rgba(139,92,246,0.15);
                    color:#a78bfa;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">PCA</span>
            </div>
          </div>

          <div>
            <div style="font-size:0.62rem;color:#f59e0b;font-weight:700;letter-spacing:1px;
                 text-transform:uppercase;margin-bottom:8px">Bioinformatique</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
              <span style="background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.2);
                    color:#f59e0b;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">GATK</span>
              <span style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
                    color:#fbbf24;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Samtools</span>
              <span style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
                    color:#fbbf24;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Bowtie2</span>
              <span style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
                    color:#fbbf24;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Prokka</span>
              <span style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
                    color:#fbbf24;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Snakemake</span>
              <span style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.15);
                    color:#fbbf24;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Nextflow</span>
            </div>
          </div>

          <div>
            <div style="font-size:0.62rem;color:#64748b;font-weight:700;letter-spacing:1px;
                 text-transform:uppercase;margin-bottom:8px">Cloud &amp; DevOps</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">GCP</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">AWS</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Docker</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">CI/CD</span>
              <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    color:#94a3b8;border-radius:20px;padding:3px 10px;font-size:0.7rem;font-weight:600">Git/GitLab</span>
            </div>
          </div>

        </div>

        <!-- langues -->
        <div style="display:flex;gap:10px;margin-top:8px">
          <div style="flex:1;background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.12);
               border-radius:12px;padding:12px;text-align:center">
            <div style="font-size:1.3rem;margin-bottom:4px">🇫🇷</div>
            <div style="font-weight:700;color:#e2e8f0;font-size:0.78rem">Français</div>
            <div style="color:#10b981;font-size:0.65rem;margin-top:2px">Natif</div>
          </div>
          <div style="flex:1;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.12);
               border-radius:12px;padding:12px;text-align:center">
            <div style="font-size:1.3rem;margin-bottom:4px">🇬🇧</div>
            <div style="font-weight:700;color:#e2e8f0;font-size:0.78rem">English</div>
            <div style="color:#3b82f6;font-size:0.65rem;margin-top:2px">Professionnel</div>
          </div>
        </div>

      </div><!-- /compétences -->

      <!-- PUBLICATIONS résumé -->
      <div>
        <div style="font-size:0.65rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
             color:#f59e0b;margin-bottom:16px;display:flex;align-items:center;gap:8px">
          <div style="width:24px;height:24px;background:rgba(245,158,11,0.12);border-radius:7px;
               display:flex;align-items:center;justify-content:center;font-size:0.8rem">📄</div>
          Sélection de publications
        </div>

        <div style="display:flex;flex-direction:column;gap:8px">

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:10px;padding:12px 14px">
            <div style="color:#cbd5e1;font-size:0.76rem;font-weight:600;margin-bottom:3px">
              Epidemiology and genomic characterisation of influenza — Marseille
            </div>
            <div style="color:#64748b;font-size:0.7rem">Travel Med Infect Dis · 2022 · PMID 34921995</div>
          </div>

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:10px;padding:12px 14px">
            <div style="color:#cbd5e1;font-size:0.76rem;font-weight:600;margin-bottom:3px">
              Spatiotemporal Dynamic of the RTS,S/AS01 Malaria Vaccine Target Antigens in Senegal
            </div>
            <div style="color:#64748b;font-size:0.7rem">Am J Trop Med Hyg · 2021 · PMID 34634772</div>
          </div>

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:10px;padding:12px 14px">
            <div style="color:#cbd5e1;font-size:0.76rem;font-weight:600;margin-bottom:3px">
              Detection of horizontal sequence transfer in microorganisms in the genomic era
            </div>
            <div style="color:#64748b;font-size:0.7rem">bioRxiv · 2022 · ML Tall et al.</div>
          </div>

          <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
               border-radius:10px;padding:12px 14px">
            <div style="color:#cbd5e1;font-size:0.76rem;font-weight:600;margin-bottom:3px">
              Optimization and standardization of the culturomics technique for human microbiome
            </div>
            <div style="color:#64748b;font-size:0.7rem">Sci Rep · 2020 · PMID 32541790</div>
          </div>

          <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
             style="text-align:center;background:rgba(245,158,11,0.06);
                    border:1px solid rgba(245,158,11,0.2);color:#f59e0b;
                    border-radius:10px;padding:10px;font-size:0.74rem;font-weight:700;
                    text-decoration:none;display:block;margin-top:4px">
            Voir les 29 publications complètes · Google Scholar ↗
          </a>
        </div>
      </div><!-- /publications -->

    </div><!-- /col droite -->
  </div><!-- /grille -->

  <!-- footer -->
  <div style="text-align:center;margin-top:64px;padding-top:32px;
              border-top:1px solid rgba(255,255,255,0.06)">
    <a href="https://medflowailanding.streamlit.app" style="color:#10b981;font-size:0.8rem;font-weight:600;text-decoration:none">
      ← Retour sur MedFlow AI
    </a>
  </div>

</div>
""", unsafe_allow_html=True)
