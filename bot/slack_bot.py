from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import langgraph_flow

app = App(token="xoxb-your-token")

@app.command("/dev-report")
def handle_dev_report(ack, respond):
    ack()
    result = langgraph_flow.run_flow()
    respond(result)

if __name__ == "__main__":
    SocketModeHandler(app, "xapp-your-token").start()