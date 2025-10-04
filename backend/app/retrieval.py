import random, datetime

# Mock retrieval function; replace with FAISS + embeddings in production
def retrieve_sources(claim: str):
    if "carrot" in claim.lower():
        return [
            {
                "id": "S1",
                "title": "Small clinical trial on beta-carotene (2016)",
                "url": "https://example.edu/vision-trial-2016",
                "date": "2016-04-12",
                "snippet": "No significant improvement in night vision.",
                "reliability": 0.75
            },
            {
                "id": "S2",
                "title": "Historical nutrition claims (encyclopedia)",
                "url": "https://encyclo.org/carrot-myths",
                "date": "1945-10-01",
                "snippet": "Origin of the myth in WWII propaganda.",
                "reliability": 0.60
            }
        ]
    else:
        return [
            {
                "id": "S1",
                "title": "Preprint observational study (2021)",
                "url": "https://preprint.org/x-y-2021",
                "date": "2021-07-22",
                "snippet": "Observational correlation found.",
                "reliability": 0.5
            },
            {
                "id": "S2",
                "title": "Review article (2022)",
                "url": "https://journals.org/review-x-2022",
                "date": "2022-03-15",
                "snippet": "Evidence mixed and limited.",
                "reliability": 0.8
            }
        ]
