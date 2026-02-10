# src/ui/components/timeline_data.py

def get_career_timeline_data():
    """
    Returns the dictionary required by TimelineJS.
    Strict JSON format to prevent errors.
    """
    return {
        "title": {
            "media": {
                "url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop",
                "caption": "The Journey",
                "credit": "Tech & Growth"
            },
            "text": {
                "headline": "Prajwal's Career Roadmap",
                "text": "<p>From <strong>Student Leader</strong> to <strong>Award-Winning GenAI Scientist</strong>.<br>A timeline of rapid technical growth, mentorship, and enterprise impact.</p>"
            }
        },
        "events": [
            {
                "start_date": {"year": "2025", "month": "01"},
                "end_date": {"year": "2026", "month": "02"},
                "text": {
                    "headline": "Data Scientist @ Capgemini",
                    "text": """
                    <p><strong>Client: Unilever</strong></p>
                    <ul>
                        <li>🏆 <strong>Double Award Winner:</strong> Won 'Best Employee' twice in 1 year.</li>
                        <li>Spearheading critical GenAI projects.</li>
                        <li><em>Stack: Azure OpenAI, PySpark.</em></li>
                    </ul>
                    """
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1965&auto=format&fit=crop",
                    "caption": "Enterprise GenAI"
                }
            },
            {
                "start_date": {"year": "2023", "month": "01"},
                "end_date": {"year": "2024", "month": "12"},
                "text": {
                    "headline": "Jr Data Scientist @ Analytica",
                    "text": """
                    <p>Promoted from Intern.</p>
                    <ul>
                        <li><strong>Key Win:</strong> Trained non-tech staff on <strong>LEAPS</strong> product.</li>
                        <li>Bridged the gap between Data & Business.</li>
                        <li><em>Stack: Python, Mentorship.</em></li>
                    </ul>
                    """
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070&auto=format&fit=crop",
                    "caption": "Mentorship & Product"
                }
            },
            {
                "start_date": {"year": "2022", "month": "01"},
                "end_date": {"year": "2022", "month": "12"},
                "text": {
                    "headline": "Python Intern @ Analytica",
                    "text": "<p>Kickstarted professional career.<br>Built foundational Python scripts for automated reporting and analytics workflows.</p>"
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=2069&auto=format&fit=crop",
                    "caption": "Coding Foundations"
                }
            },
            {
                "start_date": {"year": "2021", "month": "06"},
                "end_date": {"year": "2022", "month": "06"},
                "text": {
                    "headline": "MCA - Ramaiah Institute",
                    "text": """
                    <p>Graduated in Computer Applications.</p>
                    <ul>
                        <li><strong>Leader:</strong> College Rep for Blockchain events.</li>
                        <li>Led technical debates on emerging tech.</li>
                    </ul>
                    """
                },
                "media": {
                    "url": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070&auto=format&fit=crop",
                    "caption": "Academics"
                }
            }
        ]
    }