# AI content lab

A sophisticated multi-agent system that leverages the CrewAI framework to automatically generate high-quality, SEO-optimized articles on any given topic through collaborative AI agents.

![Image with a robot](https://github.com/tiagomonteiro0715/ai-content-lab/blob/main/undraw_artificial-intelligence_fuvd.png)

## What this project does?


This system orchestrates five specialized AI agents that work together to create comprehensive, well-researched, and optimized content:

- Research and Fact Checker: Conducts deep research and analysis to identify trends, key insights, and supporting data
- Audience Specialist: Analyzes target audience needs, preferences, and optimizes content for maximum engagement
- Lead Content Writer: Creates compelling, well-structured, and engaging content based on research and strategy
- Senior Editorial Director: Ensures content quality, consistency, and alignment with strategic objectives
- SEO and Content Optimization Specialist: Transforms content into search-engine-optimized, user-friendly material

The system uses advanced AI collaboration to produce articles that would typically require a full editorial team, combining research depth with audience insights, creative writing, editorial excellence, and technical SEO optimization.

## Why these technologies were used?

CrewAI Framework was chosen as the core technology because:

- Agent Orchestration: Provides sophisticated multi-agent coordination and task delegation capabilities
- Memory and Context: Each agent maintains memory across iterations, enabling contextual improvements
- Scalability: Easy to add new agents or modify existing ones without restructuring the entire system
- Collaborative Intelligence: Agents can delegate tasks to each other, creating a natural workflow

- OpenAI GPT-4.1: Selected for its advanced reasoning capabilities and consistent output quality across different specialized roles

### Modular Architecture: The system is designed with clear separation of concerns, making it easy to:

- Modify individual agent behaviors
- Add new content types or formats
- Scale the system for different use cases
- Maintain and debug specific components


## Challenges faced and future features

### Current Challenges Solved:

- Agent Coordination: Ensuring smooth handoffs between agents while maintaining context
- Content Consistency: Maintaining tone and style across multiple AI-generated iterations
- SEO Balance: Optimizing for search engines without compromising content quality
- API Management: Handling OpenAI API calls efficiently across multiple agents

### Future Features Planned:

- Custom Agent Profiles: Allow users to create specialized agents for specific industries
- Content Analytics: Integration with analytics tools to measure content performance
- Custom Output Formats: Support for different content types (newsletters, social media, reports)
- Integration APIs: Connect with popular CMS platforms, publishing and research tools



# Table of Contents

### [ How to Install and Run the Project ](#How_to_install)

### [ How to Use the Project ](#How_to_use)

### [ Credits, Authors and acknowledgment for contributions ](#credits)

---

<a name="how_to_install"></a>

### How to Install and Run the Project


##### Depedencies

###### 1. Create a Virtual Environment (if not already created):
If you haven't already created a virtual environment for your project, you can do so using virtualenv or venv. Here's an example using venv:

```
python -m venv myenv
```


Replace ```myenv``` with the desired name for your virtual environment.

###### 2. Activate the Virtual Environment:
On Windows, activate the virtual environment using:

```
myenv\Scripts\activate
```


On macOS and Linux, use:
```
source myenv/bin/activate
```
Replace ```myenv``` with the name of your virtual environment.

This should display the version of Jupyter Notebook installed within your virtual environment.

###### 3. Install dependencies

crewai is the framework used to create the agents, tasks and run the crew.

We use openai library to simplify the application of the openAI API

```
pip install openai crewai
```

###### 4. Launch your code editor associating it with this virtual environment




---

<a name="How_to_use">
  
### How to Use the Project

#### How to connect an LLM to run the crew of agents?

In the line of code:

```
openai.api_key = "API-KEY-HERE"

```

Change:

```
"API-KEY-HERE"
```

With your API key.

If you seek to use something like claude or an LLM locally, you need to chnage more this part of the code:

```
openai.api_key = "API-KEY-HERE"

OPENAI_API_KEY = openai.api_key

os.environ["OPENAI_API_KEY"] = openai.api_key

os.environ["OPENAI_MODEL_NAME"] = "gpt-4.1-nano-2025-04-14"
```

#### How to write an article on XXXXXXXXXXX topic?

In the part of the code:

```
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
```

You can chanhe the topic that you want the crew of agents to develop here:

```
DEFAULT_TOPIC = "XXXXXXXXXXX"
```



---

<a name="credits">

#### Credits, Authors and acknowledgment for contributions

Tiago Monteiro

- GitHub: @tiagomonteiro0715
- LinkedIn: [Tiago Monteiro](https://www.linkedin.com/in/tiago-monteiro-/)
- Date: August 3, 2025

Acknowledgments

- [CrewAI](https://www.crewai.com/): For providing the multi-agent orchestration capabilities
- [OpenAI](https://openai.com/): For the GPT models that power the individual agents
- [Python Community](https://www.python.org/): For the extensive libraries and tools that make this project possible


# License
This project is open source and available under the MIT License.
