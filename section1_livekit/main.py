from dotenv import load_dotenv

load_dotenv()

import asyncio

from livekit.agents import (
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
)

from section1_livekit.agent import ElectroPiAgent


async def entrypoint(ctx: JobContext):

    print("Connecting to LiveKit...")

    await ctx.connect()

    print("Connected!")

    session = AgentSession()

    await session.start(
        room=ctx.room,
        agent=ElectroPiAgent(),
    )

    # Disable audio output (no TTS)
    session.output.set_audio_enabled(False)

    print("Agent Started!")

    await session.generate_reply(
        instructions="""
        Introduce yourself briefly.
        """
    )

    print("Waiting for participants...")

    # Keep the worker alive
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":

    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            agent_name="electro-pi-agent",
        )
    )