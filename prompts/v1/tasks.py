RESEARCH_TASK = """
You analyse research data and extract key insights for a Linkedin post 
Topic : {topic}
Post Type : {post_type}
Research Data : {research_data}

EXTRACT and return JSON:
{{
    "key_facts":["6-7 compelling statistics and facts and figures"],
    "trending_angles": ["3-5 fresh angles or framing for the topic"],
    "credible_sources":["spources that can be referenced"],
    "hook_opportunity":["potential opening line based on hook research"]
}}
Focus on recent, credible information that supports engaging content creation"""

WRITER_TASK="""Create an engaging linkedin post based on research insights.
Topic: {topic}
Tone: {tone}
Post Type : {post_type}
Research Insights : {research_insights}

Post structure guidelines:
1. Story: Hook, then personal anecdote, then lesson, then call To Action
2. Hot take: contrarian hook, then reasoning, then invite for discussion 
3. Announcement: news, then why it matters, then next steps 
4. Lesson learned: challenge, then what happened, then takeaways 

LinkedIn best practices:
Start with the strong Hook in the first one to two lines
1. keep your writing clear and concise
2. use short paragraphs and plenty of white space
3. share useful insights not just promotions
4. Add a personal story, lesson, or unique point of view
5. End with the clear call To Action, like a question or opinion prompt
6. use three to five relevant hashtags only
7. post consistently so your audience recognizes your voice
8. reply to comments quickly to keep engagement ongoing
9. use visuals like images videos poles or documents when they add value 

RETURN JSON:
{{
    "post_content": "complete linkedin post",
    "hook":"first line extracted",
    "word_count":"number",
    "facts_used":["Research points incorporated"]
}}"""


VALIDATION_TASK="""Validate the linkedin post for accuracy and quality
Post Content : {post_content}
Original Research: {research_insights}
Tone: {tone}

Validation criteria:
- Fact-check all statistics and claims against the provided sources
- Ensure content is original and not copied from source basically, do not plagiarize
- Verify that the  post follows LinkedIn's best practices
- Check for proper formatting
- Confirm engagement elements are appropriate and applied 

Cringe flags to avoid:
- I am humbled to announce
- game changer
- in today's fast-paced world
- I'm excited to share
- let's connect
- tldr 

RETURN JSON:
{{
    "validation_score":"true/false",
    "score":"integer rating from 1 to 10, number only",
    "accuracy_issues":["any factual problems"],
    "quality_issues":["area of improvement"],
    "cringe_flags":["cliche phrases found"],
    "suggestions":["specific improvement"],
    "final_verdict":"ready to post / needs revision"
}}"""