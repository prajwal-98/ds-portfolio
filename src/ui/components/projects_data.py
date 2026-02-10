# src/ui/components/projects_data.py

PROJECTS_DATA = {
    "hero": [
        {
            "title": "End-to-End GenAI Pipeline",
            "tagline": "RAG-based documentation assistant using LangChain and Pinecone.",
            "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1000&auto=format&fit=crop", # Placeholder
            "tech_stack": ["LangChain", "OpenAI API", "Pinecone", "Streamlit"],
            "links": {
                "demo": "#",
                "github": "#"
            },
            "description": "Designed and deployed a Retrieval-Augmented Generation (RAG) system that indexes internal documentation. Reduced search time by 40% for the engineering team."
        },
        {
            "title": "Sales Forecasting Dashboard",
            "tagline": "Automated time-series forecasting with Prophet & PySpark.",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop",
            "tech_stack": ["Python", "Prophet", "Plotly", "Databricks"],
            "links": {
                "demo": "#",
                "github": "#"
            },
            "description": "Built a scalable batch inference pipeline processing 50k+ SKUs weekly. Provides interactive visualizations for demand planners to adjust forecasts."
        }
    ],
    "experiments": [
        {
            "title": "Python Decorators",
            "desc": "Collection of useful utility decorators for logging and timing.",
            "tags": ["Python", "Utils"]
        },
        {
            "title": "SQL Optimizer",
            "desc": "Regex-based script to auto-format and lint messy SQL queries.",
            "tags": ["Automation", "SQL"]
        },
        {
            "title": "Resume Parser",
            "desc": "Simple NLP script to extract skills from PDF resumes.",
            "tags": ["NLP", "Spacy"]
        },
         {
            "title": "Cron Monitor",
            "desc": "A lightweight script to alert on failed cron jobs via Slack.",
            "tags": ["DevOps", "Bot"]
        }
    ]
}
