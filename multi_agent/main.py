from agents import MultiAgentSystem

if __name__ == "__main__":
    system = MultiAgentSystem()

    topics = [
        "AI行业趋势",
        "自动化运营",
        "内容创业方向"
    ]

    for topic in topics:
        result = system.run(topic)
        print(result["final"])
