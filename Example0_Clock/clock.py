from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

from time import strftime

class ClockApp(App):
    sw_seconds = 0
    sw_started = False
    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
    def on_start(self):
        Clock.schedule_interval(self.update_sw, 0.016)
        Clock.schedule_interval(self.update_time, 1)
    def update_sw(self, nap):
    	if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            self.root.ids.stopwatch.text = (
                '%02d:%02d.[size=40]%02d[/size]' %
                (int(minutes), int(seconds),
                int(seconds * 100 % 100))) 
    def start_stop(self):
    	self.sw_started = not self.sw_started
        self.root.ids.start_stop.text = ('Stop' if self.sw_started else 'Start')
    
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.root.ids.stopwatch.text = '00:00.[size=40]00[/size]'
        self.sw_seconds = 0 

if __name__ == '__main__':

    Window.clearcolor = get_color_from_hex('#123456')
    ClockApp().run()
