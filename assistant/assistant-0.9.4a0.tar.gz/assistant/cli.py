import asyncio

from websockets.exceptions import ConnectionClosedOK

from assistant.ptk_shell.shell import AssistantShell


cli = AssistantShell(full_screen=True, mouse_support=True)

async def screen_driver():
	while not cli.exit_screen:
		await asyncio.sleep(0.5)
		cli.redraw_app()

async def interactive():
	try:
		task_prompt = cli.run_async()
		task_drive_screen = screen_driver()
		return await asyncio.gather(task_prompt, task_drive_screen)
		#return await asyncio.gather(task_prompt)
	except ConnectionClosedOK:
		pass
	except KeyboardInterrupt:
		return
	except Exception as e:
		raise e