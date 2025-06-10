from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CrewaiYepcodeDemo():
    """CrewaiYepcodeDemo crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self, tools=None):
        self.tools = tools

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    @agent
    def asteroid_data_scientist(self) -> Agent:
        return Agent(
            config=self.agents_config['asteroid_data_scientist'], # type: ignore[index]
            verbose=True,
            tools=self.tools
        )

    @agent
    def impact_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['impact_reporter'], # type: ignore[index]
            verbose=True,
            output_file='asteroid_impact_report.md'
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['research_task'], # type: ignore[index]
    #     )

    @task
    def calculate_impact_task(self) -> Task:
        return Task(
            config=self.tasks_config['calculate_impact_task'], # type: ignore[index]
        )

    @task
    def write_impact_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_impact_report_task'], # type: ignore[index]
            output_file='asteroid_impact_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiYepcodeDemo crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
