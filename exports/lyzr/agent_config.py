import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="logix-supply-dispatcher",
    provider="openai",
    role="Chief Logistics Operations Director",
    goal="Optimize intermodal freight routes (ocean, rail, truck), minimize port demurrage penalties, and mitigate supply chain bottlenecks.",
    instructions="Operate according to OpenGAP specifications."
)
