"""
Author: https://github.com/tiagomonteiro0715
Date: 2025-08-03
Linkedin: https://www.linkedin.com/in/tiago-monteiro-/

This code is a multi-agent system that uses the crewAI framework to create an article on a given topic.
It uses the following agents:
- Research and Fact Checker
- Audience Specialist
- Lead Content Writer
- Senior Editorial Director
- SEO and Content Optimization Specialist
"""

import warnings
warnings.filterwarnings("ignore")
from crewai import Agent, Task, Crew
import openai
import os
from datetime import datetime


"""
OpenAI API Key
"""

openai.api_key = "API-KEY-HERE"

OPENAI_API_KEY = openai.api_key

os.environ["OPENAI_API_KEY"] = openai.api_key

os.environ["OPENAI_MODEL_NAME"] = "gpt-4.1-nano-2025-04-14"



"""
Agents
"""
research_and_fact_checker = Agent(
    role="Senior Research Analyst",
    goal="Conduct deep research and analysis on {topic} to identify trends, key insights, and supporting data",
    backstory="You are a seasoned research analyst with 15+ years of experience in market research "
    "and trend analysis. You specialize in identifying emerging patterns, key stakeholders, "
    "and data-driven insights across various industries. Your analytical skills help teams "
    "understand complex topics from multiple angles including technical, business, social, "
    "and economic perspectives.",
    allow_delegation=True,
    verbose=True,
    max_iter=3,
    memory=True,
)

audience_analyst = Agent(
    role="Audience Intelligence Specialist",
    goal="Analyze target audience needs, preferences, and optimize content for maximum engagement",
    backstory="You are an audience intelligence expert who understands reader behavior, demographic "
    "preferences, and content consumption patterns. You specialize in creating detailed audience "
    "personas, identifying pain points, and recommending content approaches that resonate "
    "with specific target groups across different platforms and mediums.",
    allow_delegation=False,
    verbose=True,
    max_iter=2,
    memory=True,
)

writer = Agent(
    role="Lead Content Writer",
    goal="Create compelling, well-structured, and engaging content based on research and strategy",
    backstory="You are an award-winning content writer with expertise in translating complex "
    "research into accessible, engaging narratives. You excel at crafting compelling "
    "introductions, developing logical argument flows, and creating content that both "
    "educates and entertains. Your writing adapts seamlessly to different tones, "
    "audiences, and content types.",
    allow_delegation=False,
    verbose=True,
    max_iter=3,
    memory=True,
)


senior_editor = Agent(
    role="Senior Editorial Director",
    goal="Ensure content quality, consistency, and alignment with strategic objectives",
    backstory="You are a senior editorial director with 20+ years of experience in publishing "
    "and content management. You have an eye for narrative flow, structural integrity, "
    "and editorial excellence. You ensure content meets the highest professional standards "
    "while maintaining engagement and achieving strategic objectives.",
    allow_delegation=True,
    verbose=True,
    max_iter=3,
    memory=True,
)

seo_and_humanize_optimizer = Agent(
    role="SEO and Content Optimization Specialist",
    goal="Transform content into search-engine-optimized, user-friendly material that ranks well while maintaining high quality and engagement",
    backstory="You are a seasoned SEO expert with deep expertise in both technical optimization and content quality. "
    "You excel at keyword research, semantic analysis, and content optimization strategies that drive organic traffic. "
    "You understand search engine algorithms, user intent, and content psychology. Your expertise includes "
    "technical SEO (schema markup, structured data, meta optimization), on-page optimization (keyword integration, "
    "heading structure, internal linking), and user experience optimization (readability, mobile-friendliness, "
    "engagement metrics). You stay current with Google's algorithm updates, Core Web Vitals, and emerging "
    "trends like voice search and featured snippets. You balance technical requirements with natural language "
    "flow, ensuring content remains valuable and engaging while achieving optimal search performance.",
    allow_delegation=False,
    verbose=True,
    max_iter=2,
    memory=True,
)


"""
Tasks
"""

research_task = Task(
    description=(
        "1. Conduct comprehensive research on {topic} including:\n"
        "   - Latest trends and developments\n"
        "   - Key players and stakeholders\n"
        "   - Market analysis and statistics\n"
        "   - Technical insights and innovations\n"
        "2. Identify credible sources and data points\n"
        "3. Analyze competitive landscape\n"
        "4. Provide fact-checked information and insights"
    ),
    expected_output="A detailed research report with key findings, "
        "trends, data points, and credible sources for {topic}.",
    agent=research_and_fact_checker,
)

audience_task = Task(
    description=(
        "1. Analyze target audience for {topic} content:\n"
        "   - Demographics and psychographics\n"
        "   - Content consumption preferences\n"
        "   - Pain points and interests\n"
        "   - Platform preferences\n"
        "2. Create detailed audience personas\n"
        "3. Identify content gaps and opportunities\n"
        "4. Recommend content approach and tone"
    ),
    expected_output="Comprehensive audience analysis with personas, "
        "preferences, and content strategy recommendations.",
    agent=audience_analyst,
)

writing_task = Task(
    description=(
        "1. Create compelling content on {topic} based on research and audience analysis:\n"
        "   - Engaging introduction that hooks readers\n"
        "   - Well-structured body with clear sections\n"
        "   - Logical flow and narrative arc\n"
        "   - Strong conclusion with call-to-action\n"
        "2. Ensure content is accessible and engaging\n"
        "3. Incorporate research findings naturally\n"
        "4. Maintain consistent tone and voice"
    ),
    expected_output="A well-written, engaging article in markdown format "
        "with proper structure, flow, and compelling narrative.",
    agent=writer,
)

editing_task = Task(
    description=(
        "1. Review and enhance the written content:\n"
        "   - Improve narrative flow and structure\n"
        "   - Ensure logical progression of ideas\n"
        "   - Enhance readability and engagement\n"
        "   - Maintain editorial standards\n"
        "2. Check for consistency in tone and style\n"
        "3. Ensure content meets strategic objectives"
    ),
    expected_output="A polished, well-structured article with improved "
        "flow, clarity, and editorial excellence.",
    agent=senior_editor,
)

seo_and_humanize_task = Task(
    description=(
        "1. Conduct comprehensive SEO optimization while maintaining content quality:\n"
        "   - Perform keyword research and identify high-value, low-competition keywords\n"
        "   - Integrate primary and secondary keywords naturally throughout the content\n"
        "   - Optimize heading structure (H1, H2, H3) for both SEO and readability\n"
        "   - Create compelling meta titles (50-60 characters) and descriptions (150-160 characters)\n"
        "   - Implement internal linking opportunities and optimize anchor text\n"
        "   - Ensure proper keyword density and avoid keyword stuffing\n"
        "2. Enhance content structure and user experience:\n"
        "   - Optimize content length for search intent and user engagement\n"
        "   - Improve readability with shorter paragraphs, bullet points, and subheadings\n"
        "   - Add schema markup opportunities for rich snippets\n"
        "   - Optimize images with descriptive alt text and file names\n"
        "   - Ensure mobile-friendly content formatting\n"
        "3. Implement technical SEO best practices:\n"
        "   - Optimize URL structure and slug optimization\n"
        "   - Implement structured data where applicable\n"
        "   - Ensure proper semantic HTML structure\n"
        "   - Add social media meta tags for better sharing\n"
    ),
    expected_output="Fully SEO-optimized content with integrated keywords, "
        "proper technical structure, enhanced user experience, and improved "
        "digital discoverability while maintaining high content quality.",
    agent=seo_and_humanize_optimizer,
)


"""
Crew
"""

crew = Crew(
    agents=[
        research_and_fact_checker,
        audience_analyst,
        writer,
        senior_editor,
        seo_and_humanize_optimizer
    ],
    tasks=[
        research_task,
        audience_task,
        writing_task,
        editing_task,
        seo_and_humanize_task
    ],
    verbose=True
)

def run_editorial_crew(topic):
    """
    Run the editorial crew with the specified topic.
    
    Args:
        topic (str): The topic for the article generation
        
    Returns:
        str: The generated content
    """
    try:
        print(f" Starting AI Editorial Crew for topic: '{topic}'")
        print("=" * 60)
        
        result = crew.kickoff(inputs={"topic": topic})
        
        print(" Content generation completed successfully!")
        return result
        
    except Exception as e:
        print(f" Error during content generation: {str(e)}")
        raise


def save_results(result, topic):
    """
    Save the generated results to a markdown file.
    
    Args:
        result: The generated content
        topic (str): The topic used for generation
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ai_article_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# AI Article Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Topic:** {topic}\n\n")
            f.write("## Generated Content\n\n")
            f.write(str(result))
        
        print(f" Results saved to: {filename}")
        return filename
        
    except Exception as e:
        print(f" Error saving results: {str(e)}")
        raise



if __name__ == "__main__":
    DEFAULT_TOPIC = "electronics applied to the automotive industry"
    
    print(" AI Editorial Crew System")
    print("This system uses multiple AI agents to create high-quality, SEO-optimized content.")
    print("Agents: Research, Audience Analysis, Writing, Editing, and SEO Optimization")
    print("=" * 40)
    
    try:
        # Run the editorial crew
        result = run_editorial_crew(DEFAULT_TOPIC)
        
        # Save the results
        filename = save_results(result, DEFAULT_TOPIC)
        
        print("\nProcess completed successfully!")
        print(f"Output file: {filename}")
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        print("Please check your configuration and try again.")