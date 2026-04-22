# 🧬 V_OmegaFold: The Universal Map for Modular Folding and De Novo Design

![Status](https://img.shields.io/badge/Status-In_Silico_Prototype-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Framework](https://img.shields.io/badge/Theory-Structural_Columns-purple)

🌍 *Scroll down for the Spanish version / Desplázate hacia abajo para la versión en español.*

---

## 🇬🇧 English Version

### 📌 Overview
**V_OmegaFold** is not a treatment for a specific disease; it is a **computational engine and a universal theoretical framework** designed to address any pathology at the molecular level. This repository contains the architectural blueprint for designing *De Novo* proteins (proteins that do not exist in nature) by controlling their 3D geometry through a modular folding approach.

This project demonstrates how to use protein language models on local consumer hardware to reverse-engineer untreatable diseases, shifting the paradigm from passive prediction to **active creation**.

### 🧠 The Foundational Discovery: The Hemoglobin 121 Anomaly
The architecture of V_OmegaFold was born from observing and experimenting with the Hemoglobin structure, specifically isolating the behavior at **residue 121**.

During *in silico* stress tests, we managed to "pause" the thermodynamic collapse. This allowed us to observe a fundamental biological truth that changes protein design: **Proteins do not fold sequentially (from beginning to end) like a string.**

#### The "Structural Columns" Theory
Based on the 121 anomaly, V_OmegaFold establishes that folding is **modular**. The structure relies on specific physical "Columns" or anchors. If we correctly program and position these columns in the 1D sequence, thermodynamics forces the rest of the amino acids to collapse predictably around them. 
**Result:** By owning the physical columns, we can dictate the exact final shape of any protein, forging "keys" and "wedges" at will.

### 🎯 Proof of Concept (Addressed Diseases)
Using this map of modular columns, the V_OmegaFold engine has been tested against the active sites of multiple critical diseases:
* **Alzheimer's:** Neutralization of amyloid plaque aggregation.
* **Huntington's Disease:** Stabilization of polyglutamine tracts in the mutated HTT protein.
* **COVID-19:** Steric inhibition of the main protease (Mpro) and blocking of the Spike protein's Receptor Binding Domain (RBD).
* **Type 2 Diabetes (Baseline Pipeline):** Design of a suicidal peptide warhead (`EDDYFLVPR`) to seal the Cysteine 215 residue of the **PTP1B** enzyme, reversing insulin resistance from its root.

### 🚀 Installation & Usage (Local Environment)
We recommend running this in an isolated `venv`. *Note: Physical collapse execution requires downloading model weights (~8.44 GB).*

```bash
git clone [https://github.com/CRTK0/V_OmegaFold.git](https://github.com/CRTK0/V_OmegaFold.git)
cd V_OmegaFold
pip install -r requirements.txt
python src/01_esmfold_local.py
```
Disclaimer: This project is a computational simulation (in silico). Generated sequences and models have not been subjected to in vitro or in vivo testing. For open-source research purposes only.

##############################################################
##############################################################
🇪🇸 Versión en Español
📌 Visión General
V_OmegaFold no es un tratamiento para una enfermedad específica; es un motor computacional y un marco teórico universal para curar cualquier patología a nivel molecular. Este repositorio contiene el plano arquitectónico para diseñar proteínas De Novo (que no existen en la naturaleza) controlando su geometría tridimensional mediante un enfoque de plegamiento modular.

Este proyecto demuestra cómo utilizar modelos de lenguaje de proteínas en hardware local de consumo para aplicar ingeniería inversa a enfermedades intratables, pasando de la predicción pasiva a la creación activa.

🧠 El Descubrimiento Fundacional: La Anomalía de la Hemoglobina 121
La arquitectura de V_OmegaFold nació de la observación y experimentación con la estructura de la Hemoglobina, específicamente aislando el comportamiento en el residuo 121.

Durante estas pruebas de estrés in silico, logramos "pausar" el colapso termodinámico. Esto nos permitió observar una verdad biológica fundamental: Las proteínas no se pliegan de forma secuencial (de principio a fin) como una cuerda.

La Teoría de las "Columnas Estructurales"
A partir de la anomalía 121, V_OmegaFold establece que el plegamiento es modular. La estructura depende de "Columnas" o anclajes físicos específicos. Si programamos y posicionamos estas columnas correctamente en la secuencia 1D, el resto de los aminoácidos se ven obligados por la termodinámica a colapsar de forma predecible alrededor de ellas.
Resultado: Al poseer las columnas físicas, podemos dictar la forma final exacta de cualquier proteína, forjando "llaves" y "cuñas" a voluntad.

🎯 Pruebas de Concepto (Enfermedades Abordadas)
Utilizando este mapa de columnas modulares, el motor V_OmegaFold ha sido puesto a prueba contra los sitios activos de múltiples enfermedades críticas:

Alzheimer: Neutralización de la agregación de placas amiloides.

Enfermedad de Huntington: Estabilización de los tractos de poliglutamina en la proteína HTT mutada.

COVID-19: Inhibición estérica de la proteasa principal (Mpro) y bloqueo del dominio de unión al receptor (RBD) de la proteína Spike.

Diabetes Tipo 2 (Pipeline de Referencia): Diseño de una "ojiva" peptídica suicida (EDDYFLVPR) para sellar el residuo Cisteína 215 de la enzima PTP1B, revirtiendo la resistencia a la insulina desde la raíz.

🚀 Instalación y Uso (Entorno Local)
Se recomienda ejecutar en un entorno virtual aislado (venv). Nota: La ejecución del colapso físico requiere la descarga inicial de los pesos del modelo (~8.44 GB).
```bash
git clone [https://github.com/CRTK0/V_OmegaFold.git](https://github.com/CRTK0/V_OmegaFold.git)
cd V_OmegaFold
pip install -r requirements.txt
python src/01_esmfold_local.py
```
⚠️ Descargo de Responsabilidad (Disclaimer)
Este proyecto es una simulación computacional (in silico). Las secuencias, teorías de plegamiento modular y modelos generados no han sido sometidos a ensayos in vitro o in vivo. Este código representa un ejercicio de investigación bioinformática extrema y su propósito es estrictamente académico, open-source y de demostración de capacidades computacionales.
