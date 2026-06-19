import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GuessingGameApp(App):
    def build(self):
        # 1. Setup Game Variables
        self.secret_number = random.randint(1, 20)
        self.attempts = 0
        self.max_attempts = 5
        
        # 2. Create a vertical layout box to hold our app elements
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 3. Create Visual Interface Elements
        self.title_label = Label(
            text="🔢 Guess the Number (1-20) 🔢\nAttempts Remaining: 5", 
            font_size='20sp', 
            halign='center'
        )
        
        # Input space where you tap on your phone to type numbers
        self.user_input = TextInput(
            hint_text="Type your guess here", 
            multiline=False, 
            input_filter='int', # Forces phone keyboard to show numbers only
            font_size='24sp',
            size_hint_y=None,
            height=60
        )
        
        # Clickable button
        self.submit_btn = Button(
            text="Submit Guess", 
            background_color=(0, 0.6, 0.8, 1),
            font_size='20sp',
            size_hint_y=None,
            height=60
        )
        # Link the button click event to our check_guess function
        self.submit_btn.bind(on_press=self.check_guess)
        
        # 4. Add the elements to our layout
        layout.add_widget(self.title_label)
        layout.add_widget(self.user_input)
        layout.add_widget(self.submit_btn)
        
        return layout

    def check_guess(self, instance):
        # Safety check: do nothing if input box is empty
        if not self.user_input.text:
            return
            
        guess = int(self.user_input.text)
        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        
        # Game logic processing
        if guess == self.secret_number:
            self.title_label.text = f"🎉 Winner!\nYou guessed it in {self.attempts} tries!"
            self.submit_btn.disabled = True
        elif self.attempts >= self.max_attempts:
            self.title_label.text = f"💀 Game Over! 💀\nThe number was {self.secret_number}."
            self.submit_btn.disabled = True
        elif guess < self.secret_number:
            self.title_label.text = f"📈 Too Low!\nAttempts Remaining: {remaining}"
        elif guess > self.secret_number:
            self.title_label.text = f"📉 Too High!\nAttempts Remaining: {remaining}"
            
        # Clear the input box automatically for the next guess
        self.user_input.text = ""

# Run the mobile application layout
if __name__ == '__main__':
    GuessingGameApp().run()
