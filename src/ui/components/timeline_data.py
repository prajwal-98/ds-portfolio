# src/ui/components/timeline_data.py

def get_career_timeline_data():
    """
    Returns the dictionary required by TimelineJS.
    """
    return {
        "title": {
            "media": {
                "url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop",
                "caption": "Future Goals",
                "credit": "AI & Tech"
            },
            "text": {
                "headline": "Prajwal's Career Journey",
                "text": "<p>From University Graduation to building Enterprise GenAI Systems. A timeline of technical growth and milestones.</p>"
            }
        },
        "events": [
            {
                "start_date": {"year": "2026", "month": "05"},
                "text": {
                    "headline": "Target: Product-Based Tech Company",
                    "text": "<p><strong>Goal:</strong> Transition to a GenAI Engineer or Applied Scientist role.<br><strong>Focus:</strong> Mastering Agentic Workflows, System Design, and Scalable Inference.<br><strong>Prep:</strong> Building end-to-end portfolio projects and contributing to open source.</p>"
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070&auto=format&fit=crop",
                    "caption": "The Next Chapter"
                }
            },
            {
                "start_date": {"year": "2023", "month": "01"},
                "end_date": {"year": "2026", "month": "01"}, # Present
                "text": {
                    "headline": "Data Scientist @ Capgemini",
                    "text": "<p><strong>Client: Unilever</strong><br>Engineered RAG pipelines reducing documentation search time by 40%.<br>Optimized batch inference for sales forecasting using <strong>Databricks & PySpark</strong>.<br>Mentored juniors on Prompt Engineering and Clean Code standards.</p>"
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop",
                    "caption": "Enterprise AI"
                }
            },
            {
                "start_date": {"year": "2022", "month": "06"},
                "text": {
                    "headline": "Graduation & Career Start",
                    "text": "<p>Graduated with Distinction in Computer Science.<br>Completed intensive internship focused on <strong>Data Analysis & Visualization</strong>.<br>Laid the foundation in SQL, Python, and Statistical Modeling.</p>"
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070&auto=format&fit=crop",
                    "caption": "University"
                }
            }
        ]
    }
