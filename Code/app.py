from config import app, db, HOST, PORT, DEBUG
from views.login import LoginView
from views.user_registration import UserRegisterationView
from views.event_registration import EventRegisterationView
from views.home import HomeView
from views.about import AboutView
from views.logout import LogoutView
from views.event import EventView

# Routes
app.add_url_rule('/', view_func=HomeView.as_view('home'))
app.add_url_rule('/about', view_func=AboutView.as_view('about'))
app.add_url_rule('/event/<int:id>', view_func=EventView.as_view('event'))
app.add_url_rule('/user_registeration',
                 view_func=UserRegisterationView.as_view('user_registeration'))
app.add_url_rule('/event_registeration',
                 view_func=EventRegisterationView.as_view('event_registeration'))
app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))


if __name__ == "__main__":
    db.create_all()
    app.run(HOST, PORT, DEBUG)
