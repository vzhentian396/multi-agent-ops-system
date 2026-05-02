
from llm import call_llm


class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def run(self, input_data):
        raise NotImplementedError


class PlannerAgent(Agent):
    def run(self, topic):
        prompt = f"为主题 '{topic}' 制定一个内容运营计划"
        return call_llm(prompt)


class ResearchAgent(Agent):
    def run(self, plan):
        prompt = f"根据以下计划整理相关信息：{plan}"
        return call_llm(prompt)


class ContentAgent(Agent):
    def run(self, research):
        prompt = f"根据以下信息生成内容初稿：{research}"
        return call_llm(prompt)


class OptimizeAgent(Agent):
    def run(self, content):
        prompt = f"优化以下内容，使其更流畅专业：{content}"
        return call_llm(prompt)
