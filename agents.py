from llm import call_llm

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def run(self, input_data):
        raise NotImplementedError


class PlannerAgent(Agent):
    def run(self, topic):
        prompt = f"为主题{topic}制定运营计划"
        return call_llm(prompt)


class ResearchAgent(Agent):
    def run(self, plan):
        prompt = f"根据计划整理信息: {plan}"
        return call_llm(prompt)


class ContentAgent(Agent):
    def run(self, research):
        prompt = f"生成内容: {research}"
        return call_llm(prompt)


class OptimizeAgent(Agent):
    def run(self, content):
        prompt = f"优化内容: {content}"
        return call_llm(prompt)


class PublisherAgent(Agent):
    def run(self, content):
        return f"最终发布内容:\n{content}"


class MultiAgentSystem:
    def __init__(self):
        self.planner = PlannerAgent("Planner", "规划")
        self.researcher = ResearchAgent("Researcher", "调研")
        self.writer = ContentAgent("Writer", "写作")
        self.optimizer = OptimizeAgent("Optimizer", "优化")
        self.publisher = PublisherAgent("Publisher", "发布")

    def run(self, topic):
        plan = self.planner.run(topic)
        research = self.researcher.run(plan)
        content = self.writer.run(research)
        optimized = self.optimizer.run(content)
        final = self.publisher.run(optimized)

        return {
            "plan": plan,
            "research": research,
            "content": content,
            "optimized": optimized,
            "final": final
        }
