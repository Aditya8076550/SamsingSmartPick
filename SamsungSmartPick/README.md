# Samsung SmartPick — Mobile Product Recommendation System

## Selected mini-project
**PJ1: Mobile Product Recommendation System Development Project** from the project overview. It fits the Samsung Mobile context and demonstrates how user preferences can be used to rank products.

## What the app does
- Collects budget, main use, storage needs, ecosystem interest, and importance ratings.
- Filters a small illustrative Samsung Galaxy product dataset.
- Calculates transparent weighted preference scores.
- Shows the top three matches and a comparison table.
- Downloads the comparison as CSV.
- Optionally uses Gemini to generate a natural-language explanation if `GEMINI_API_KEY` is configured.

## Run locally (Windows)
1. Install Python 3.10 or newer.
2. Open Command Prompt in this folder.
3. Create and activate a virtual environment (recommended):
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bat
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bat
   streamlit run app.py
   ```
6. Your browser should open the local Streamlit page.

## Optional Gemini setup
The app works without an API key. To enable the optional GenAI explanation, set an environment variable in the same terminal before launching Streamlit:

```bat
set GEMINI_API_KEY=your_api_key_here
streamlit run app.py
```

Do not commit or share your real API key. Keep it out of GitHub and screenshots.

## Connection to Chapters 1–4
The precise chapter topics should follow the course slides; this prototype uses the concepts visible in the shared course materials:
- **AI / Machine Learning:** use data and a scoring procedure to support a recommendation rather than hard-coding one answer for every user.
- **Generative AI:** optional Gemini-generated explanation uses a prompt containing only the selected product facts and user preferences; the model is asked not to invent specifications.
- **Data Science / EDA:** structured tabular data, feature columns, filtering, sorting and comparison.
- **Math for Data Science:** weighted scoring and normalization; each feature contributes according to its assigned weight.

This is a beginner-friendly **content-based weighted-scoring recommender**, not a trained ML model. Do not claim it was trained on real customer data.

## Data disclaimer
All prices and feature scores in `app.py` are illustrative demo values. They are not live Samsung prices or verified specifications. Replace them with verified data and cite your source before using this as a real buying guide.
