from collections import deque
from textual.app import App, ComposeResult
from textual.containers import Vertical, ScrollableContainer
from textual.widgets import Input, Static

class EchoApp(App):
    BINDINGS = [
        ("j", "scroll_down", "Down"),
        ("k", "scroll_up", "Up"),
        ("escape", "focus_output", "Scroll mode"),
        ("i", "focus_input", "Insert mode"),
    ]
    CSS = """
    Screen {
        padding: 2;
    }

    #output_container {
        height: 1fr;
        border: round white;
        padding: 1;
    }

    #history {
        height: 6;
        border: round white;
        padding: 1;
        color: grey;
    }

    #input {
        border: round white;
    }
    """

    def __init__(self):
        super().__init__()
        self.lines: list[str] = []
        self.history = deque(maxlen=10)

    def compose(self) -> ComposeResult:
        yield Vertical(
            ScrollableContainer(
                Static("", id="output"),
                id="output_container",
            ),
            Static("", id="history"),
            Input(
                placeholder="Type what you want here",
                id="input",
            ),
        )

    def on_input_submitted(self, event: Input.Submitted):
        text = event.value.strip()
        if not text:
            return

        self.lines.append(f"> {text}")
        output = self.query_one("#output", Static)
        output.update("\n".join(self.lines))

        container = self.query_one("#output_container", ScrollableContainer)
        container.scroll_end(animate=False)

        self.history.append(text)
        history = self.query_one("#history", Static)
        history.update("\n".join(self.history))

        event.input.value = ""

    def action_scroll_down(self):
        self.query_one("#output_container").scroll_down()

    def action_scroll_up(self):
        self.query_one("#output_container").scroll_up()

    def action_focus_output(self):
        self.query_one("#output_container").focus()

    def action_focus_input(self):
        self.query_one("#input").focus()



if __name__ == "__main__":
    EchoApp().run()
