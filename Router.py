from Agents.MotivateBot import respond as motivator_respond
from Agents.TherapyBot import respond as therapist_respond
from Agents.VentBot import respond as vent_respond

AGENT_MAP = {
    "therapist": therapist_respond,
    "motivator": motivator_respond,
    "vent": vent_respond,
}

def route_input(agent_type: str, user_input: str) -> str:
    if agent_type not in AGENT_MAP:
        return f"Unknown agent type: {agent_type}"
    
    respond_func = AGENT_MAP[agent_type]
    return respond_func(user_input)


if __name__ == "__main__":
    print("🧠 Multi-Agent Chat (type 'exit' to quit)")
    print("Available agents: therapist, motivator, vent")

    current_agent = input("Select your agent: ").strip().lower()

    while current_agent not in AGENT_MAP:
        current_agent = input("Invalid agent. Choose therapist, motivator, or vent: ").strip().lower()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = route_input(current_agent, user_input)
        print(f"{current_agent.capitalize()} AI: {response}")