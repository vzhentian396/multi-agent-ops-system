from agents import PlannerAgent, ResearchAgent, ContentAgent, OptimizeAgent


def run_system(topic):
    planner = PlannerAgent("Planner", "规划")
    research = ResearchAgent("Research", "研究")
    content = ContentAgent("Content", "写作")
    optimize = OptimizeAgent("Optimize", "优化")

    plan = planner.run(topic)
    research_data = research.run(plan)
    draft = content.run(research_data)
    final = optimize.run(draft)

    return final


if __name__ == "__main__":
    result = run_system("AI创业")
    print(result)
