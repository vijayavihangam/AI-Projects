from crewai import Agent, Task, Crew, LLM

# 1. Connect to your local M5 brain (Ollama)
# No API keys required!
local_model = LLM(
    model="ollama/llama3.2",  # Added the .2 here
    base_url="http://localhost:11434"
)

# 2. Define your Agent
# Think of this as giving the AI a "job description"
assistant = Agent(
    role="Helpful info about CEO LPL Financial",
    goal="Who is CEO of LPL Financial and what is his educational and experience background before he joins at LPL Financial in simple terms.",
    backstory="You are a friendly expert who loves helping people learn new tech.",
    llm=local_model,
    verbose=True # This lets you see the agent's "internal thoughts"
)

# 3. Define the Task
# This is the specific instruction you want it to carry out
simple_task = Task(
    description="Who is CEO of LPL Financial and what is his educational and experience background before he joins at LPL Financial in simple terms in exactly two sentences.",
    expected_output="A two-sentence explanation in plain English.",
    agent=assistant
)

# 4. Create the 'Crew'
# Even with one agent, CrewAI needs a 'Crew' to run the task
crew = Crew(
    agents=[assistant],
    tasks=[simple_task]
)

# 5. Execute
print("### Starting Agent... ###")
result = crew.kickoff()
print("\n\n########################")
print("## RESULT:")
print(result)