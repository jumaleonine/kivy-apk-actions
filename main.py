from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from core import Counter


class CounterApp(App):
    title = "Kivy APK Actions"

    def build(self):
        self.counter = Counter(minimum=0)
        root = BoxLayout(orientation="vertical", padding=24, spacing=16)

        self.label = Label(text="Count: 0", font_size="48sp")
        root.add_widget(self.label)

        row = BoxLayout(size_hint_y=None, height=96, spacing=16)
        row.add_widget(Button(text="-", font_size="32sp", on_press=self.on_minus))
        row.add_widget(Button(text="+", font_size="32sp", on_press=self.on_plus))
        root.add_widget(row)

        root.add_widget(
            Button(text="Reset", size_hint_y=None, height=72, on_press=self.on_reset)
        )
        return root

    def _refresh(self):
        self.label.text = f"Count: {self.counter.value}"

    def on_plus(self, *_):
        self.counter.increment()
        self._refresh()

    def on_minus(self, *_):
        self.counter.decrement()
        self._refresh()

    def on_reset(self, *_):
        self.counter.reset()
        self._refresh()


if __name__ == "__main__":
    CounterApp().run()
