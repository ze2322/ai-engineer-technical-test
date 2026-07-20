from livekit.agents import Agent

from section1_livekit.prompts import SYSTEM_PROMPT
from section1_livekit.llm import llm


class ElectroPiAgent(Agent):

    def __init__(self):

        super().__init__(
            instructions=SYSTEM_PROMPT,
            llm=llm,
        )