# Mini Project Submission Notes

## Project title
Samsung SmartPick: AI-Inspired Mobile Product Recommendation System

## Problem statement
Customers may find it difficult to choose a smartphone because price, camera, battery, performance, display and storage matter differently to different people. A one-size-fits-all list does not reflect individual preferences.

## Proposed solution
Samsung SmartPick asks the user for a budget and priorities, filters phones that meet the constraints, and ranks the remaining options using a transparent weighted score. It explains why the best match was selected. An optional GenAI feature turns the explanation into natural language.

## User flow
1. Open the app.
2. Choose a maximum budget and main usage.
3. Rate camera, battery, performance and display importance.
4. Select storage and ecosystem preferences.
5. Review the top matches and their scores.
6. Compare matching phones or download the results as CSV.

## Technical flow
User preferences → structured product table → filter by constraints → weighted feature score → rank results → explain recommendation → optional GenAI explanation.

## Concepts demonstrated
- AI and recommendation systems
- Feature selection / feature engineering
- Tabular data and exploratory comparison
- Weighted score (basic applied mathematics)
- Prompting a generative model with bounded facts
- Human-readable explanations and limitations

## Important limitation
The demo catalog and scores are illustrative. The score is a transparent heuristic, not a learned prediction and not evidence of actual customer satisfaction. The app does not collect or store user profiles.

## 60-second presentation script
“Hello everyone. Our project is Samsung SmartPick, a mobile product recommendation system. Choosing a phone can be confusing because everyone has a different budget and different priorities. Our app asks the user about budget, usage, storage and the importance of camera, battery, performance and display. It filters phones that do not meet the constraints, then calculates a weighted score for the remaining options. The app shows the top matches, explains the reason, and allows a comparison to be downloaded as a CSV. We also added an optional Gemini feature to generate a natural-language explanation from the supplied facts. The current catalog is demo data, so our next step would be to replace it with verified product information and evaluate the recommendation quality with real user feedback. Thank you.”

## Likely instructor questions
**Q. Is this a machine-learning model?**  
A. The current version is a content-based recommender using a transparent weighted scoring heuristic. It is AI-inspired, but it is not a trained ML model yet.

**Q. What are the features?**  
A. Price, camera score, battery score, performance score, display score, storage and ecosystem category.

**Q. Why use weights?**  
A. Different users value features differently. Weights let user priorities affect the ranking.

**Q. What is GenAI doing here?**  
A. If configured, Gemini rewrites the recommendation explanation in natural language. It does not choose the products or verify the specs.

**Q. How would you improve it?**  
A. Verify the catalog, add more products, collect opt-in feedback, test ranking quality, and later compare the heuristic with collaborative filtering or a learned ranking model.

**Q. Does the app store personal data?**  
A. No. Preferences are used for the current session only; the prototype does not save a user profile.
